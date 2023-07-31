# Création d'un pipeline

Ce projet vise à présenter un exemple de classification multiclasse en utilisant le **perceptron multiclasse** de scikit-learn. Nous montrerons comment gérer les hyper-paramètres en utilisant GridSearch, et comment structurer l'ensemble du flux de travail avec l'objet pipeline de scikit-learn pour une sauvegarde et un chargement simple des modèles à l'aide de fichiers **pickle**.

## Description du projet
Notre objectif est de créer un classificateur multiclasse capable de prédire des étiquettes pour plusieurs catégories différentes. Nous utiliserons l'algorithme Perceptron Multiclasse de scikit-learn pour accomplir cette tâche.

### Prérequis
Nous utiliserons les bibliothèques suivantes pour les deux scripts :

Python 3.x      
scikit-learn    
numpy     
pandas      
pickle
os

### Structure des fichiers

├── data=Segmentation.xlsx     
├── deploiementr.py     
├── modelisation.py      
├── pipeline.sav     
└── README.md       

Le dossier "data" contient le fichier d'entraînement et de test au format excel.  
modelisation.py est le script Python pour entraîner le modèle et effectuer la recherche sur la grille des hyper-paramètres.       
deploiementr.py est le script Python pour charger le modèle entraîné et faire des prédictions sur de nouvelles données.       
README.md est le fichier que vous lisez actuellement, fournissant une description détaillée du projet.     

## Étapes du Projet
Préparation des Données : avant d'entraîner le modèle, nous allons pré-traiter les données en les chargeant à partir des fichiers excel et les diviser en ensembles d'entraînement et de test.

### Création du pipeline
Nous allons créer un pipeline scikit-learn qui comprendra les étapes suivantes :
- Le pré-traitement des données.
- L'instanciation du modèle Perceptron Multiclasse.
- La gestion des hyper-paramètres avec GridSearch pour trouver les meilleurs paramètres du modèle.
- Entraînement du modèle : utilisation de l'ensemble d'entraînement et ajuster les hyper-paramètres à l'aide de GridSearch pour obtenir le modèle optimal.
- Évaluation du modèle : une fois le modèle entraîné, nous évaluerons ses performances en utilisant l'ensemble de test.
- Sauvegarde du modèle : enfin, nous sauvegarderons le modèle entraîné à l'aide de Pickle pour une utilisation future.


### Conclusion
Ce projet a présenté un exemple de classification multiclasse en utilisant le perceptron multiclasse de scikit-learn avec la gestion des hyper-paramètres via GridSearch.          
En utilisant l'objet Pipeline de scikit-learn et la sauvegarde des modèles avec Pickle, nous avons créé un flux de travail complet pour l'entraînement et la prédiction de modèles de machine learning.






