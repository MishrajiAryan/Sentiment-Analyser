# Sentiment-Analyser

A machine learning project for analyzing sentiment in Amazon product reviews, optimized to work efficiently even on older hardware and designed for straightforward use.

## Demo
A repo is hosted on Hugging Face Spacce to demonstrate this project and can be accessed using below link. Please note due to docker contraints, uploading file is not working for now.

**Demo:** [Demo for Product Sentiment Analyser](https://huggingface.co/spaces/mishrajiaryan/product_sentiment_analysis)
### Demo Video

https://github.com/user-attachments/assets/d6cd0f62-8a8d-4e15-92e4-7442e2d1e34d

## Project Overview

This repository includes the code and notebooks to perform sentiment analysis on Amazon product reviews. The process—from data loading and model training to evaluation and prediction—is cleanly documented and works seamlessly in both Jupyter and Google Colab.

- **Colab Notebook:** [Sentiment Analysis Colab Demo](https://colab.research.google.com/drive/1hk_MxyMzxs1bBtyk7s8xYMEwex-inF-s?usp=sharing)
- **Dataset Used:** [Amazon Product Reviews (Kaggle)](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews)
- **Contact for Model/Help:** mishraji.aaryan@gmail.com

## Limitations

- **99k Reviews Only:** Due to resource limitations, the provided model was trained on approximately 99,000 reviews.
- **English Language Only:** Currently supports sentiment prediction only for reviews in English.

## How to Use (Tutorial)

**Step 1:** Download or clone the repository (make sure you have the `trial_run` folder).

**Step 2:** Obtain or generate the `sentiment_model` folder:
- You can **generate it by running the notebook (Jupyter/Colab)** as demonstrated in the Colab link above, or
- Place a copy of the pre-trained `sentiment_model` (contact for access, or from your own notebook run) inside the `trial_run` folder.

**Step 3:** Set up your Python environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

**Step 4:** Run the Web Application:
```bash
python run.py
```
A browser window will automatically open where you can test product review sentiment analysis from the UI.

**Tested On:**  
Runs smoothly on a 6-year-old CPU-only laptop with 8GB RAM. No GPU required!


## License

This code is provided for educational and non-commercial use.  
For questions, model requests, or collaborations: [mishraji.aaryan@gmail.com](mailto:mishraji.aaryan@gmail.com)

---

**Made with ❤️ by Aryan Mishra**
