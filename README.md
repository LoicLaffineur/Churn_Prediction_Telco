# Réduisez le taus de désabonnement de vos clients avec l'analyse prédictive.

## 🎯 Problématique client 
Dans le secteur du télécoms, acquérir des clients est une tâche bien plus couteuse que la fidélisation d'un client déjà existant. C'est pourquoi, identifier les clients susceptibles de se désabonner (ci-après churn) permet d'agir en amont et de réduire les pertes de revenus.

## Notre solution : 

Nous avons développer un modèle prédictif capable d'identifier les clients a risque de désabonnement avec : 
- 80% d'accuracy et 53% de recall (capacité à détécter les vrais clients a risques)
- Une analyse des variables clés : type de contrat, méthode de paiement, services internet souscrits,... .
- Des recommandations actionnables : cibles les clients avec des offres personnalisées à leur profils (sur le plan business), ajouter les seuils de prédiction pour optimiser la détection en fonction des besoins (sur le plan technique).
- Une application StreamLit utilisable pour de futurs profil et améliorable en ajoutant diverses informations (SHAP, ...)

## Technologies utilisées  : 
Python, Pandas, Scikit-learn, XGBoost, Logistic Regression, Random Forest, SVM, Matplotlib, Seaborn, SHAP

## Résultats attendus pour l'entreprise : 
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
