import streamlit as st
from transformers import pipeline

st.title('Text Classifiction app')
st.write('This app uses sentiment analyser library to clasify the sentiment of your texts as postive or negative. The web app is built using [Streamlit](https://docs.streamlit.io/en/stable/getting_started.html).')

st.write('*Note: it will take up to 30 seconds to run the app.*')

form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')

if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label}')
    else:
        st.error(f'{label}')

