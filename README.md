# Création d'un Pipeline

Ce projet vise à présenter un exemple de classification multiclasse en utilisant le **Perceptron Multiclasse** de scikit-learn. Nous montrerons comment gérer les hyper-paramètres en utilisant GridSearch, et comment structurer l'ensemble du flux de travail avec l'objet Pipeline de scikit-learn pour une sauvegarde et un chargement simples des modèles à l'aide de fichiers **Pickle**.

## Description du Projet
Notre objectif est de créer un classificateur multiclasse capable de prédire des étiquettes pour plusieurs catégories différentes. Nous utiliserons l'algorithme Perceptron Multiclasse de scikit-learn pour accomplir cette tâche.

### Prérequis
Avant de commencer, assurez-vous d'avoir les bibliothèques suivantes installées :

Python 3.x
scikit-learn
numpy
pandas

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
Préparation des Données : Avant d'entraîner le modèle, nous allons prétraiter les données en les chargeant à partir des fichiers excel et les diviser en ensembles d'entraînement et de test.

### Création du Pipeline
Nous allons créer un Pipeline scikit-learn qui comprendra les étapes suivantes :
- Le prétraitement des données
- L'instanciation du modèle Perceptron Multiclasse.
- La gestion des hyper-paramètres avec GridSearch pour trouver les meilleurs paramètres du modèle.
- Entraînement du Modèle : Nous allons entraîner le modèle en utilisant l'ensemble d'entraînement et ajuster les hyper-paramètres à l'aide de GridSearch pour obtenir le modèle optimal.
- Évaluation du Modèle : Une fois le modèle entraîné, nous évaluerons ses performances en utilisant l'ensemble de test.
- Sauvegarde du Modèle : Enfin, nous sauvegarderons le modèle entraîné à l'aide de Pickle pour une utilisation future.


### Conclusion
Ce projet a présenté un exemple de classification multiclasse en utilisant le Perceptron Multiclasse de scikit-learn avec la gestion des hyper-paramètres via GridSearch.          
En utilisant l'objet Pipeline de scikit-learn et la sauvegarde des modèles avec Pickle, nous avons créé un flux de travail complet pour l'entraînement et la prédiction de modèles de machine learning.






