
📧 Email/SMS Spam Classifier

A simple web app built using Streamlit to detect whether a given email or SMS message is SPAM or NOT SPAM using a trained ML model.

-------------------------------
🚀 Features:
- Detects spam in real-time
- Text preprocessing with stemming and stopword removal
- TF-IDF based vectorization
- User-friendly Streamlit interface

🛠️ How to Use:
1. Install dependencies:

2. Download NLTK stopwords:
    import nltk
    nltk.download('stopwords')

3. Run the app:
    streamlit run app.py

🧠 Model:
- Trained using TF-IDF + classifier (e.g., Logistic Regression)
- Files required:
    - model (1).pkl (ML model)
    - vectorizer.pkl (TF-IDF vectorizer)


