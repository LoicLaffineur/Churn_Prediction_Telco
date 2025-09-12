# Réduisez le taux de désabonnement de vos clients avec l'analyse prédictive.

## 🎯 Problématique client 
Dans le secteur du télécoms, acquérir des clients est une tâche bien plus couteuse que la fidélisation d'un client déjà existant. C'est pourquoi, identifier les clients susceptibles de se désabonner (ci-après churn) permet d'agir en amont et de réduire les pertes de revenus.

## 💡 Notre solution : 

Nous avons développer un modèle prédictif capable d'identifier les clients a risque de désabonnement avec : 
- 80% d'accuracy et 53% de recall (capacité à détécter les vrais clients a risques)
- Une analyse des variables clés : type de contrat, méthode de paiement, services internet souscrits,... .
- Des recommandations actionnables : cibles les clients avec des offres personnalisées à leur profils (sur le plan business), ajouter les seuils de prédiction pour optimiser la détection en fonction des besoins (sur le plan technique).
- Une application StreamLit utilisable pour de futurs profil et améliorable en ajoutant diverses informations (SHAP, ...)

## 🛠️ Technologies utilisées  : 
Python, Pandas, Scikit-learn, XGBoost, Logistic Regression, Random Forest, SVM, Matplotlib, Seaborn, SHAP

## 🚀 Résultats attendus pour l'entreprise : 
- Réduction des coûts : Moins de perte = économies sur les campagnes d'acquisition.
- Amélioration de l'expérience client : Des offres proactives et adaptées pour les clients à risque.
- Prise de décision data-driven

----------------------------------------------------------------------------------

## 🗂️ Données
Source : IBM Telco dataset (7043 clients, 21 variables)

## 🔍 Méthodologie : 
- EDA : visualisation des profils de churners
- Prétraitement : encodage, imputation, scaling
- Modélisation : Logistic Regression, Random Forest, XGBoost, KNN, SVC
- Évaluation : accuracy, recall, precision, F1-score, Precision-Recall curve, confusion matrix
- Interprétabilité : SHAP, feature importance

## 📊 Résultats

#### Résulats finaux : 

<img width="619" height="628" alt="pr_churn" src="https://github.com/user-attachments/assets/7daf1994-0bb5-4933-ae0b-626b7ede9d88" />

<img width="485" height="401" alt="res_fin_churn" src="https://github.com/user-attachments/assets/13d3dfdd-f2eb-4f74-ac2e-eb8ff104079e" />

#### Meilleur modèle : **Régression Logistique avec seuil de décision à 0.29**
- Accuracy = 0.76
- Recall = **0.81**
- Precision = 0.52
- F1 = 0.64
- Variables importantes : Insulin, Glucose, Age

#### Matrice de confusion finale : 

<img width="507" height="455" alt="cm_rl" src="https://github.com/user-attachments/assets/b52e5083-3deb-46a2-b6c5-f312312ef4e4" />

#### SHAP : 

<img width="884" height="497" alt="shap" src="https://github.com/user-attachments/assets/b0310bce-93ba-4c4d-9713-2635d6f6dd11" />




- [https://churnpython-rvye97ruvtvqtgwowbdmtz.streamlit.app/](https://laffineur-telco-churn.streamlit.app/)
