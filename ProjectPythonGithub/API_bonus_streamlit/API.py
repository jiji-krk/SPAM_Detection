import streamlit as st
from PIL import Image 

title = 'Email Analysis for Spam Detection 📧'

st.header(title)

for i in range(5):
    st.write(" ")

# Charger l'image depuis un fichier local
image_path = "image_spam.png"
image_path = Image.open(image_path)
image = st.image(image_path)


for i in range(5):
    st.write(" ")
    

introduction = '''

In the current globalized era, email has emerged as an essential means of communication. However, this surge in email usage has also been accompanied by a rapid proliferation of unwanted emails: SPAM.
Spam can pose a potential threat to the security of computer systems or be a time-consuming issue for businesses. "On average, an employee spends more than 3 hours per week reading and sorting through emails."

Source: https://www.nowteam.net/dangers-spam-entreprise

'''

st.write(introduction)


#streamlit run API.py