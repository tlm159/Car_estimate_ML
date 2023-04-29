# Projet de prédiction de prix de voiture

Ce projet vise à créer un modèle capable de prédire le prix d'une voiture à partir de ses caractéristiques. Pour ce faire, nous avons utilisé un jeu de données de voitures d'occasion provenant du site web Kaggle.

## Dossier de projet

- `column_infos`: Dossier contenant les informations sur les colonnes du dataset.
- `data`: Dossier contenant les données en format csv des different étapes de traitement.
- `fastapi`: Dossier contenant le code pour l'API FastAPI.
- `models`: Dossier contenant le modèle entraîné avec pickle.
- `notebook`: Dossier contenant les notebooks utilisés pour la préparation des données ,l'analyse des données et l'entraînement du modèle.
- `streamlit`: Dossier contenant le code pour l'application Streamlit.

## Installation
- Cloner ce repository avec la commande `git clone git@github.com:DonzerHD/Car_estimate_ML.git`
- Installer les dépendances avec la commande `pip install -r requirements.txt`

## Notebooks
- `preparation_donnees.ipynb`: Notebook pour la préparation des données.
- `analyse_donnees.ipynb`: Notebook pour l'analyse des données.
- `entrainement_modele.ipynb`: Notebook pour l'entraînement du modèle.
- `utils.py`: Fichier contenant les fonctions utilisées dans les notebooks.
- `Analyse_model_rdstate.txt`: Fichier contenant les résultats de l'analyse du modèle avec différentes valeurs de random_state et variables.

### Préparation des données
Les données ont été préparées en effectuant les étapes suivantes :
-   Lecture du fichier csv contenant les données brutes
-   Renommage des colonnes pour les rendre plus claires et cohérentes
-   Conversion des unités de mesure en système métrique et traduction des noms de colonnes en français
-   Séparation de la colonne "marque_modele" en deux colonnes distinctes : "marque" et "modele"
-   Suppression des lignes contenant des valeurs manquantes
-   Vérification de l'absence de doublons
-   Nettoyage des noms de marque pour une meilleure uniformité
-   Nettoyage des noms de modèle pour une meilleure uniformité
-   Sauvegarde des données nettoyées dans un nouveau fichier csv.

### Analyse des données
Les données ont été analysées en effectuant les étapes suivantes :

- Suppression de la colonne car_ID, qui n'était pas nécessaire.
- Calcul de la matrice de corrélation entre les variables pour identifier les relations entre elles.
- Création d'une heatmap pour visualiser la matrice de corrélation.
- Visualisation des relations entre le prix et les différents types de carburant à l'aide d'un boxplot.
- Analyse de la répartition des valeurs de chaque colonne catégorielle.
- Effectuation du test ANOVA pour chaque variable catégorielle afin de déterminer si elle a un impact significatif sur le prix. ANOVA est un test statistique utilisé pour déterminer si une variable indépendante a un impact significatif sur une variable dépendante. Pour en savoir plus sur cette méthode, vous pouvez cliquer [ici](https://www.tibco.com/fr/reference-center/what-is-analysis-of-variance-anova#:~:text=Analyse%20de%20la%20variance%20(ANOVA)%20est%20une%20formule%20statistique%20utilis%C3%A9e,les%20moyennes%20de%20diff%C3%A9rents%20groupes.).
- ⚠️ Il est important de noter que pour l'analyse ANOVA, il est recommandé d'utiliser des colonnes dont les valeurs sont bien réparties pour obtenir des résultats significatifs. ⚠️
- Pour les autres variables pour lesquelles le test ANOVA n'a pas été effectué, j'ai déterminé moi-même celles qui ont un impact significatif sur le prix afin de les inclure dans le modèle.
- Sélection des colonnes nécessaires pour la création du modèle et enregistrement dans un fichier CSV.
- L'analyse des données a permis d'identifier les variables les plus pertinentes pour la prédiction du prix des voitures. Les résultats de l'analyse ont été utilisés pour créer le modèle de prédiction de prix de voiture.

### Entraînement du modèle
Voici les étapes pour entraîner un modèle de prédiction de prix de voitures d'occasion:
- Préparation des données : ajout de nouvelles caractéristiques et division des données en caractéristiques et cible.
- Identification des colonnes numériques et catégorielles.
- Création d'un préprocesseur pour combiner les transformateurs de variables numériques et catégorielles.
- Utilisation d'une GridSearchCV pour trouver les meilleurs hyperparamètres pour un modèle de forêt aléatoire.
- Évaluation du meilleur modèle sélectionné sur un ensemble de test.
- L'utilisation de la métrique RMSE pour évaluer le modèle est plus adaptée aux problèmes de régression, car elle donne une idée de la magnitude de l'erreur. Par exemple, une erreur de prédiction de 5 000 dollars est plus importante sur une voiture qui coûte 20 000 dollars que sur une voiture qui coûte 200 000 dollars.
- Visualisation de la courbe d'apprentissage .
- Le modèle de forêt aléatoire avec les meilleurs paramètres a donné les résultats suivants : **RMSE de 2234.98**, **R2 de 0.93** et **MAE de 1537.89**. Ces indicateurs de performance indiquent que le modèle est assez précis pour prédire le prix des voitures d'occasion en se basant sur leurs caractéristiques.
- Enregistrement du modèle entraîné dans un fichier pickle pour une  l'utiliser dans l'API FastAPI et l'application Streamlit.

## API FastAPI
- Se placer dans le dossier `fastapi`
- Lancer l'API avec la commande `uvicorn app:app --reload`
- Le dossier se compose de 2 fichiers:
    - `app.py`: Fichier contenant le code de l'API.
    - `schemas.py`: Fichier contenant la classe de schéma de données pour l'API.
- Utiliser le logiciel Postman pour tester l'API .
- Pour tester l'API, envoyer une requête POST sur l'adresse `http://127.0.0.1:8000/predict`
- Dans Postman, sélectionner `raw` et `JSON` dans l'onglet `Body`
- Envoyer le body suivant en exemple :
```
{
    "type_vehicule": "berline",
    "roues_motrices": "propulsion",
    "modele": "X4",
    "marque": "BMW",
    "empattement": 262.9,
    "longueur_voiture": 480.1,
    "largeur_voiture": 169.9,
    "poids_vehicule": 1465.102160,
    "taille_moteur": 209,
    "taux_alésage": 91.9,
    "chevaux": 182,
    "consommation_ville": 14.7,
    "consommation_autoroute": 10.69
}
```
- Le résultat de la requête est un JSON contenant le prix prédit.

## Streamlit
- Se placer dans le dossier `streamlit`
- Lancer l'application avec la commande `streamlit run app.py`
- Le dossier se compose de 3 fichiers:
    - `app.py`: Fichier contenant le code de l'application.
    - `components.py`: Fichier contenant les fonctions pour les composants de l'application.
    - `utils.py`: Fichier contenant les fonctions utilitaires pour l'application.
- Se rendre sur l'adresse `http://localhost:8501/` pour accéder à l'application.
- Vous pouvez sélectionner les caractéristiques de la voiture à prédire à l'aide des widgets.

## Conclusion
En conclusion, ce projet de prédiction de prix de voitures d'occasion a permis de mettre en pratique les étapes de préparation de données, d'analyse de données et de création de modèle. Les résultats de l'analyse de données ont été utilisés pour entraîner un modèle de prédiction de prix de voiture avec une précision raisonnable. Ce projet peut servir de base pour des projets similaires et a permis de comprendre l'importance de chaque étape dans le processus de création de modèle de prédiction.

## Licence
Ce projet est sous licence ``MIT`` - voir le fichier [LICENSE](LICENSE) pour plus d'informations.

## Auteurs
* **Thomas.l59** _alias_ [@DonzerHD](https://github.com/DonzerHD)
