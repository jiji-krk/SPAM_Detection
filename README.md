# Python_for_DataAnalysis
Camila_KRIKA_Jinane_Krika

# Spam Detection and Analysis

# Overview
This repository contains the code and analysis for a comprehensive study on spam email detection. The project covers various aspects, including data pre-processing, data visualization, modeling, and a Streamlit-based interface for practical use.

# Project Structure

**Jupyter Notebook** : projet_final.ipynb

•	Data Pre-processing: Utilized Min-Max Scaling for normalization.

•	Data Visualization: Explored and decoded email content, identifying common features of spam and non-spam emails. Key findings include specific keywords, prevalent special characters, and distinguishing traits.

•	Modeling: Followed a structured approach, involving library importation, data splitting, hyperparameter tuning using grid search, model creation and training, evaluation metrics calculation, ROC curve, confusion matrix analysis, and learning curve plotting.

•	Comparative Analysis: Assessed model performance using various metrics such as accuracy, AUC, and more.

**Streamlit Interface** : API.py
An interactive tool built with Streamlit, allowing users to input a sentence and analyze whether it is likely to be spam or not. The tool leverages the findings from the comprehensive analysis in the Jupyter Notebook.

**PowerPoint Presentation:** `Final Project PYTHON FOR DATA ANALYSIS - power point.pptx`
A visual presentation summarizing key insights, findings, and the overall project.

# How to Use the Streamlit Interface
1.	Ensure you have Streamlit installed (pip install streamlit).
2.	run the streamlit application using the command "streamlit run API.py"
3.	Input a sentence into the provided text area.
4.	Click the "Predict" button to see if the sentence is predicted as spam or non-spam.

# Conclusion
This project provides a deep dive into spam email detection, from data exploration to the creation of a user-friendly tool. The insights gained from the analysis and the implementation of the Streamlit interface make it a valuable resource for both understanding spam characteristics and practical applications.
Feel free to explore the Jupyter Notebook for an in-depth analysis, and interact with the Streamlit interface for real-time spam detection.

