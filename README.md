# Blinkit-Delivery-Time-Predictor
Machine learning model to predict quick-commerce delivery time using distance, traffic, and weather features. Includes SHAP explainability and a Streamlit web app for real-time predictions.

Blinkit Delivery Time Predictor

An end-to-end machine learning project that predicts quick-commerce delivery time using order distance, weather, traffic, and rider experience data — adapted for a Blinkit-style dark-store delivery context.

What this project does
Predicts delivery time (in minutes) for an order based on real-time conditions
Flags whether an order is likely to breach a 30-minute SLA promise
Explains why the model made a prediction using SHAP
Provides a live Streamlit web app for interactive predictions
Tech stack
Data processing: pandas, numpy
Modeling: scikit-learn (Random Forest, tuned via GridSearchCV), XGBoost
Explainability: SHAP
Deployment: Streamlit Cloud
Notebook: Google Colab
Project workflow
Data cleaning — handled missing values using mode (categorical) and median (numerical) imputation
Feature engineering — created a Distance x Preparation Time interaction feature and an SLA breach flag
Modeling — compared Random Forest vs Gradient Boosting, then tuned hyperparameters to reduce overfitting (train-test R² gap reduced from 0.19 to 0.08)
Explainability — used SHAP to understand feature-level impact on individual predictions
Deployment — packaged the trained model into a Streamlit app for real-time use
Key finding

Distance and its interaction with preparation time account for ~90% of the model's predictive power — weather, traffic, and vehicle type have comparatively minor impact in this dataset.

Try it live

[Add your Streamlit app link here after deployment]

Run locally
bash
pip install -r requirements.txt
streamlit run app.py
