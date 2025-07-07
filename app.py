import streamlit as st
import pickle
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
ps = PorterStemmer()

import re

def transform_text(text):
    text = text.lower()
    text = re.findall(r'\b\w+\b', text)

    y = []
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(ps.stem(i))

    return " ".join(y)

# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model (1).pkl', 'rb'))
#UI
st.title('Email/SMS Spam Classifier')

user_input = st.text_input('Enter the Received SMS/Email Message')

if st.button('Predict'):
    transformed_text = transform_text(user_input)
    vector_input = tfidf.transform([transformed_text])
    result = model.predict(vector_input)

    if result == 1:
        st.header('SPAM')
    else:
        st.header('NOT SPAM')
