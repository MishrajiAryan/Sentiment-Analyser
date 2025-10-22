import streamlit as st
import pandas as pd
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer

# Load model
@st.cache_resource
def load_model():
    model = DistilBertForSequenceClassification.from_pretrained('./sentiment_model')
    tokenizer = DistilBertTokenizer.from_pretrained('./sentiment_model')
    model.eval()
    return model, tokenizer

model, tokenizer = load_model()

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        pred = torch.argmax(probs).item()
    
    sentiment_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
    return sentiment_map[pred], probs[0][pred].item() * 100

# UI
st.title("Sentiment Analyzer")

tab1, tab2 = st.tabs(["Single Review", "Batch Analysis"])

with tab1:
    text = st.text_area("Enter review:", height=150)
    if st.button("Analyze"):
        if text:
            sentiment, conf = predict_sentiment(text)
            st.success(f"**{sentiment}** ({conf:.1f}% confident)")

with tab2:
    uploaded = st.file_uploader("Upload CSV with reviews", type=['csv'])
    if uploaded:
        df = pd.read_csv(uploaded)
        col = st.selectbox("Select review column:", df.columns)
        
        if st.button("Analyze All"):
            results = []
            progress = st.progress(0)
            for i, review in enumerate(df[col]):
                sent, conf = predict_sentiment(str(review))
                results.append({'Review': review, 'Sentiment': sent, 'Confidence': f"{conf:.1f}%"})
                progress.progress((i + 1) / len(df))
            
            result_df = pd.DataFrame(results)
            st.dataframe(result_df)
            st.download_button("Download Results", result_df.to_csv(index=False), "results.csv")
