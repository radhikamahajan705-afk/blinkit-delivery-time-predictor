# Blinkit-Delivery-Time-Predictor
Machine learning model to predict quick-commerce delivery time using distance, traffic, and weather features. Includes SHAP explainability and a Streamlit web app for real-time predictions.

🛵 Blinkit Delivery Time Predictor

An end-to-end machine learning project that predicts quick-commerce delivery time and explains why — built and adapted for a Blinkit-style dark-store delivery context.

Show Image Show Image Show Image

📌 Overview

Quick-commerce platforms like Blinkit promise delivery within minutes — which means predicting delivery time accurately isn't just a modeling exercise, it directly affects customer trust and SLA commitments.

This project builds a regression model that predicts delivery time from order-level features (distance, traffic, weather, rider experience), flags likely SLA breaches, and explains individual predictions using SHAP — then wraps it all in a live, interactive web app.

✨ Features
🎯 Delivery time prediction in minutes, based on real-world order conditions
⚠️ SLA breach flag — predicts whether an order is likely to miss the delivery-time promise
🔍 SHAP explainability — shows exactly which factors pushed a prediction up or down
📊 Feature importance analysis — reveals what actually drives delivery time (spoiler: distance dominates)
🌐 Interactive Streamlit app — enter order details and get a live prediction
🗂️ Dataset

Trained on a food-delivery dataset (1,000 orders) with the following fields: distance, weather, traffic level, time of day, vehicle type, preparation time, and courier experience. Reframed for a quick-commerce context by treating restaurant-to-customer distance as dark-store-to-customer distance.

🛠️ Tech Stack
Category	Tools
Data processing	pandas, numpy
Modeling	scikit-learn (Random Forest, tuned via GridSearchCV), XGBoost
Explainability	SHAP
Deployment	Streamlit Cloud
Development	Google Colab

🔄 Project Workflow
Data cleaning — handled missing values using mode (categorical) and median (numerical) imputation
Feature engineering — created a Distance × Preparation Time interaction feature and a data-driven SLA breach flag
Modeling — compared Random Forest vs Gradient Boosting; tuned hyperparameters via GridSearchCV, reducing the train-test R² overfitting gap from 0.19 to 0.08
Explainability — used SHAP to understand feature-level impact on individual predictions, not just global importance
Deployment — packaged the trained model into a Streamlit app for real-time, interactive use

📈 Key Finding

Distance and its interaction with preparation time account for ~90% of the model's predictive power — weather, traffic, and vehicle type have comparatively minor impact in this dataset. This suggests that for quick-commerce platforms, dark-store placement matters more than route-condition optimization.

🚀 Try It Live

🔗 [Live App Link — add after deployment]

💻 Run Locally
bash
git clone https://github.com/your-username/blinkit-delivery-time-predictor.git
cd blinkit-delivery-time-predictor
pip install -r requirements.txt
streamlit run app.py

📁 Repository Structure
├── app.py                  # Streamlit app (UI + prediction logic)
├── requirements.txt        # Python dependencies
├── delivery_model.pkl      # Trained Random Forest model
├── model_columns.pkl       # Feature column order for inference
└── README.md

🔮 Future Improvements
Add real-time traffic/weather API integration
Deploy via FastAPI + Docker for production-grade serving
Add model monitoring for data drift detection
Expand dataset with real dark-store geolocation data

Author: Radhika Mahajan — built as a self-learning project to explore end-to-end ML workflows, from data cleaning to deployment.
