import requests
import streamlit as st
from utils.entity_anonymizer import nlp

url: str = '0.0.0.0'
port: str = '8000'

def get_x_anomymize(text: str):
    global url, port
    full_url = f'http://{url}:{port}/x_anonymize/'
    json = {
        "name": "Text",
        "text": text
    }
    response = requests.post(full_url, json=json)
    return response.json()

def get_ent_pos(text: str):
    global url, port
    full_url = f'http://{url}:{port}/ent_pos/'
    json = {
        "name": "Text",
        "text": text
    }
    response = requests.post(full_url, json=json)
    return response.json()


st.title('Text Anonymizer')

# create a batch input widget
with st.form(key='form'):
    text = st.text_area(
        label = 'Enter text here',
        height = 40,
        )
    pos_or_x = st.selectbox(
        label='Get Entity Positions or Replace Entity with X\'s',
        options=('Get Entity Positions', 'X Anonymize Entities',),
        index=1,
    )
    submit_button = st.form_submit_button(
        label='Anonymize Text'
    )

# run if text is entered and submitted
if text:
    doc = nlp(text)
    st.caption('Texts and Entities')
    if (pos_or_x == 'Get Entity Positions'):
        # entity_pos = get_entity_positions(text)
        entity_pos = get_ent_pos(text)
        st.write(entity_pos)
    elif (pos_or_x == 'X Anonymize Entities'):
        anonymized_text = get_x_anomymize(text)
        st.write(anonymized_text)
