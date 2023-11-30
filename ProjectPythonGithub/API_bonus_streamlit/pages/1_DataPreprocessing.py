import streamlit as st
import pandas as pd
from PIL import Image 

st.header('Let’s do a little cleaning together ... 🧼🫧')

st.text('There is the link to our dataset : https://archive.ics.uci.edu/dataset/94/spambase')

data = pd.read_csv(r"C:\Users\jinan\Projet_Python_SPAM\spambase.data", sep = ',', header= None )
data.head()

df = data.copy()
df.columns  = ["word_freq_make", "word_freq_address", "word_freq_all", "word_freq_3d",
                      "word_freq_our", "word_freq_over", "word_freq_remove", "word_freq_internet",
                      "word_freq_order", "word_freq_mail", "word_freq_receive", "word_freq_will",
                      "word_freq_people", "word_freq_report", "word_freq_addresses", "word_freq_free",
                      "word_freq_business", "word_freq_email", "word_freq_you", "word_freq_credit",
                      "word_freq_your", "word_freq_font", "word_freq_000", "word_freq_money", "word_freq_hp",
                      "word_freq_hpl", "word_freq_george", "word_freq_650", "word_freq_lab", "word_freq_labs",
                      "word_freq_telnet", "word_freq_857", "word_freq_data", "word_freq_415", "word_freq_85", "word_freq_technology", "word_freq_1999", "word_freq_parts", "word_freq_pm", "word_freq_direct",
                      "word_freq_cs", "word_freq_meeting", "word_freq_original", "word_freq_project", "word_freq_re",
                      "word_freq_edu", "word_freq_table", "word_freq_conference", "char_freq_;", "char_freq_(",
                      "char_freq_[", "char_freq_!", "char_freq_$", "char_freq_hash", "capital_run_length_average",
                      "capital_run_length_longest", "capital_run_length_total", "spam"]


st.markdown('Here is our dataframe :')

st.write(df)

# Texte avec couleur et formatage Markdown
info_text = """
For information, we consider during our study that the target column is spam. 
A spam is assigned to 1 while a non-spam is assigned to 0.
"""

st.markdown(f"<p style='color: red;'>{info_text}</p>", unsafe_allow_html=True)

st.write('There is no missing values in this dataset :')
st.write(df.isnull().sum())

st.write('Descriptive statistics of columns : ➗〽️✖️')
st.write(df.describe())

st.markdown(f"<p style='color: green;'>Normalization :</p>", unsafe_allow_html=True)

st.text('Why make a normalization?')

st.write('Before normalization : ')
imageb = Image.open("df_before_normalization.png")
st.image(imageb)
st.write('After normalization with MinMaxScaling : 😍')
imagea = Image.open("df_after_normalization.png")
st.image(imagea)
