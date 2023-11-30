import streamlit as st

st.header('Significant visualizations 💪')

for i in range(5):
    st.write(" ")

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\jinan\Projet_Python_SPAM\spambase.data", sep = ',', header= None )

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


 
k = 15
corr = df.corr()
cols = corr.abs().nlargest(k, 'spam')['spam'].index

cm = np.corrcoef(df[cols].values.T)


fig, ax = plt.subplots(figsize=(12, 10))
heatmap = sns.heatmap(cm, yticklabels=cols.values, xticklabels=cols.values,
                      cmap=sns.diverging_palette(250, 10, as_cmap=True),
                      annot=True, square=True, annot_kws={"fontsize": 8})


ax.set(title=f"Top {k} Variables most correlated with 'spam' ")

st.pyplot(fig)

st.write("Correlation with Spam: Several features show moderate to strong correlation with the 'spam' variable, such as 'word_freq_your' (0.38) and 'word_freq_000' (0.33). These features are likely to be important predictors in a spam prediction model.")
st.write("These features are likely to be important predictors in a spam prediction model.")


for i in range(5):
    st.write(" ")

from PIL import Image 

image1 = Image.open("wordcloud_spam.png")
st.image(image1)
st.write("This word cloud visually represents the most frequent terms in spam. The larger a word appears in the cloud, the higher its frequency in the analyzed data. Words like 'you,' 'your,' 'free,' and 'our' are highlighted, indicating that they are particularly common in spam. This visualization is helpful for quickly identifying key terms that could be used to filter or flag unwanted emails")

for i in range(5):
    st.write(" ")

image2 = Image.open("wordcloud_no_spam.png")
st.image(image2)
st.write("The terms like 'you,' 'will,' and 'your' are common, but there are also specific references such as 'hp' and 'george,' which could indicate proper nouns or technical terms related to a specific company or person. This clearly shows that these emails are legitimate (non-spam).")

for i in range(5):
    st.write(" ")


spam_df = df[df['spam'] == 1]
non_spam_df = df[df['spam'] == 0]

spam_word_frequency = spam_df.iloc[:, :48].mean(axis=0)
non_spam_word_frequency = non_spam_df.iloc[:, :48].mean(axis=0)

column_names = df.columns[:48]

# Bar plot avec Streamlit
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(range(len(spam_word_frequency)), spam_word_frequency, alpha=0.9, label='Spam')
ax.bar(range(len(non_spam_word_frequency)), non_spam_word_frequency, alpha=0.9, label='Non Spam')
ax.set_ylabel("Average frequency")
ax.set_title("Comparison of word usage frequency for Spam and Non-Spam")
ax.set_xticks(range(len(column_names)))
ax.set_xticklabels(column_names, rotation='vertical')
ax.legend()

# Afficher le graphique avec Streamlit
st.pyplot(fig)

st.write("Some words, such as 'money,' 'business,' 'credit,' 'remove,' and 'receive,' associated with urgency or financial appeal, appear to be much more frequent in spam emails than in non-spam emails. ")
st.write("Conversely, other words may be more common in non-spam emails, such as 'george,' 'hpl,' '847,' suggesting a more everyday language in regular communications. ")
st.write("The height of the bars indicates the relative frequency of each word, with certain words being significantly more frequent in one category or the other, which could help differentiate spam from legitimate emails.")

for i in range(5):
    st.write(" ")


char_columns = ['char_freq_;', 'char_freq_(', 'char_freq_[', 'char_freq_!', 'char_freq_$', 'char_freq_hash']

# Bar plot 
fig, ax = plt.subplots(figsize=(10, 6))
df.groupby('spam')[char_columns].mean().T.plot(kind='bar', color=['purple', 'yellow'], ax=ax)
ax.set_title('Distribution of Specific Characters in Spam and No-Spam Emails')
ax.set_xlabel('Specific Characters')
ax.set_ylabel('Average Frequency')

l = ['No Spam', 'Spam']
ax.legend(labels=l, title='Category')

st.pyplot(fig)

text = """
The visualization shows a significant difference in the frequency of specific characters, namely '!' and '$' , between spam and non-spam emails, with a much higher frequency in spam. This suggests that these characters could be important indicators for distinguishing spam.

=> The high frequency of '!' in spam emails is indicative of attempts to grab attention or convey a sense of urgency, two tactics often employed in unwanted emails to prompt recipients to act quickly.

=> The prevalence of the '$' character, marked in spam emails, is consistent with common techniques used in spam to draw attention to potential financial gains or easy money opportunities.

Other characters have relatively similar frequencies between the two categories, suggesting that they may be less discriminatory."""
st.write(text)



for i in range(5):
    st.write(" ")


image3 = Image.open("visu_capital_run.png")
st.image(image3)


t = """
capital_run_length_average: Non-spam emails tend to have shorter sequences of capital letters on average than spam.

capital_run_length_average_longest: There is a less pronounced difference between spam and non-spam for the longest sequence of capital letters, although spams tend to have longer sequences.

capital_run_length_average_total: The total length of capital letter sequences is significantly higher in spam emails compared to non-spam, suggesting that excessive use of capital letters is a common feature of spams.

This bar plot can be useful for identifying features to use in a spam detection model. It indicates that the use of capital letters is more frequent and intensive in spams than in legitimate emails.
"""

st.write(t)
    