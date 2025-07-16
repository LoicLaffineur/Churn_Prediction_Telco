# Churn_Python

TO DO.

https://churnpython-rvye97ruvtvqtgwowbdmtz.streamlit.app/


# Détection de Churn - Données Télécom

## 🎯 Objectif
Prédire si un client risque de résilier son abonnement.

## 🗂️ Données
Source : IBM Telco dataset (7043 clients, 21 variables)

## 🔍 Méthodologie
- EDA : visualisation des profils de churners
- Prétraitement : encodage, imputation, scaling
- Modélisation : Logistic Regression, Random Forest, XGBoost
- Évaluation : accuracy, recall, precision, F1-score, ROC-AUC
- Interprétabilité : SHAP

## 📊 Résultats
- Meilleur modèle : XGBoost
- F1-score : 0.84
- Variables importantes : tenure, contrat, service Internet

## 🧠 Pistes d’amélioration
- Intégrer le coût de churn
- Ajouter des données externes
