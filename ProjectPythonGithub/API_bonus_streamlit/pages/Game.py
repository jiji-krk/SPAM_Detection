from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import re

st.header("Prediction of emails : Spam or Non-Spam ⬇️")

image = Image.open("chatbot_is_spam.png")
st.image(image)

for i in range(5):
    st.write(" ")

model = RandomForestClassifier(random_state=42)

#load dataset
df = pd.read_csv(r"C:\Users\jinan\Projet_Python_SPAM\spambase.data", sep=',', header=None)
df.columns = ["word_freq_make", "word_freq_address", "word_freq_all", "word_freq_3d",
              "word_freq_our", "word_freq_over", "word_freq_remove", "word_freq_internet",
              "word_freq_order", "word_freq_mail", "word_freq_receive", "word_freq_will",
              "word_freq_people", "word_freq_report", "word_freq_addresses", "word_freq_free",
              "word_freq_business", "word_freq_email", "word_freq_you", "word_freq_credit",
              "word_freq_your", "word_freq_font", "word_freq_000", "word_freq_money", "word_freq_hp",
              "word_freq_hpl", "word_freq_george", "word_freq_650", "word_freq_lab", "word_freq_labs",
              "word_freq_telnet", "word_freq_857", "word_freq_data", "word_freq_415", "word_freq_85",
              "word_freq_technology", "word_freq_1999", "word_freq_parts", "word_freq_pm", "word_freq_direct",
              "word_freq_cs", "word_freq_meeting", "word_freq_original", "word_freq_project", "word_freq_re",
              "word_freq_edu", "word_freq_table", "word_freq_conference", "char_freq_;", "char_freq_(",
              "char_freq_[", "char_freq_!", "char_freq_$", "char_freq_hash", "capital_run_length_average",
              "capital_run_length_longest", "capital_run_length_total", "spam"]

# Based on our study 
important_features = ["word_freq_business", "word_freq_money", "word_freq_you",
                      "char_freq_!", "char_freq_$"]

# importantes columns 
X = df[important_features]

#scaling 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# test, training 
y = df["spam"]
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# fit
model.fit(X_train, y_train)

#UI
text_input = st.text_area("Please enter the email text")

#Compte le nombre de fois que chaque colonne (mot, caractère, etc.) apparaît dans le texte et stocke ces fréquences dans une liste.
def extract_features(text):
    features = [text.count("business"), text.count("money"), text.count("you"),
                len(re.findall(r'!', text)), len(re.findall(r'\$', text))]
    return features

# Prediction
if st.button("Predict"):
    if text_input:
        user_inputs = extract_features(text_input)
        user_scaled = scaler.transform([user_inputs])
        prediction = model.predict(user_scaled)[0]

        if prediction == 1:
            st.write("The email is predicted as spam")
        else:
            st.write("The email is predicted as ham / non spam")
    else:
        st.warning("Veuillez saisir le texte de l'e-mail avant de prédire.")
