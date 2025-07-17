# Détection de Churn - Données Télécom

## 🎯 Objectif
Prédire si un client risque de résilier son abonnement.

## 🗂️ Données
Source : IBM Telco dataset (7043 clients, 21 variables)

## 🔍 Méthodologie
- EDA : visualisation des profils de churners
- Prétraitement : encodage, imputation, scaling
- Modélisation : Logistic Regression, Random Forest, XGBoost, KNN, SVC
- Évaluation : accuracy, recall, precision, F1-score, ROC-AUC, confusion matrix
- Interprétabilité : SHAP, feature importance

## 📊 Résultats
- Meilleur modèle : XGBoost
- Accuracy = 0.80
- Recall = 0.53
- F1 = 0.58
- ROC-AUC = 0.84
- Variables importantes : Contract, PaymentMethod, InternetService
- https://churnpython-rvye97ruvtvqtgwowbdmtz.streamlit.app/

## 🧠 Pistes d’amélioration
- Améliorer les résulats en Recall en utilisant un rééchantillonnage (SMOTE, Tomek ?)
- Fixer un seuil de prédiction different pour répondre à nos besoins. (p=0.5 actuellement)
