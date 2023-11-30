import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.header(f"Algo used : SVC, RandomForestClassifier, LogisticRegression, XGBoost 👩‍💻🐍")

st.markdown('During our study, we use the scikit-learn library to try several algorithms, change the hyper parameters, do a grid search etc...')

st.markdown(f"Comparison of algorithms used :")

import streamlit as st
import pandas as pd

# Données
models = ['XgBoost', 'SVC', 'RandomForestClassifier', 'Logistic Regression']
accuracy = [0.9609, 0.9349, 0.9587, 0.9207]

# Création d'un DataFrame
data = {'Model': models, 'Accuracy': accuracy}
df = pd.DataFrame(data)

# Bar plot avec Streamlit
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(models, accuracy, color='skyblue')

# Ajout des étiquettes
for bar, acc in zip(bars, accuracy):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.01, round(acc, 4), ha='center', va='bottom')

# Titres et étiquettes
ax.set_xlabel('Model')
ax.set_ylabel('Accuracy')
ax.set_title('Model Accuracy Comparison')
ax.set_ylim(0.7, 1.0)

# Afficher le graphique avec Streamlit
st.pyplot(fig)

st.write("This chart suggests that XGBoost and RandomForestClassifier are the most performing models for this data, with an accuracy exceeding 95%. The SVC also demonstrates good performance, albeit slightly lower, and logistic regression has the lowest accuracy, although still above 92%.")
for i in range(5):
    st.write(" ")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Données
models = ['XgBoost', 'SVC', 'RandomForestClassifier', 'Logistic Regression']
auc = [0.9878, 0.9791, 0.9866, 0.9702]

# Bar plot avec Streamlit
fig, ax = plt.subplots(figsize=(9, 7))
bars = ax.bar(models, auc, color='lightcoral')

# Ajout des étiquettes
for bar, auc_value in zip(bars, auc):
    if bar.get_height() < 0.99:
        ax.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 0.01, f'{auc_value:.4f}', ha='center', color='black')
    else:
        ax.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() - 0.04, f'{auc_value:.4f}', ha='center', color='black')

# Titres et étiquettes
ax.set_xlabel('Model')
ax.set_ylabel('AUC')
ax.set_ylim(0.7, 1.0)
ax.set_title('Model AUC Comparison', pad=20)
ax.spines['top'].set_visible(False)

# Afficher le graphique avec Streamlit
st.pyplot(fig)

st.write("All models exhibit high AUC scores, indicating that they are all quite effective at correctly classifying positive and negative instances. XGBoost and RandomForestClassifier slightly outperform the others.")

