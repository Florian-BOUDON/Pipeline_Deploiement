# Loading folder
import os
import pandas as pd

# Loadind data
path = "C:/Users/fbbou/PycharmProjects/Pipeline_Deploiement"
os.chdir(path)

df = pd.read_excel("segmentation.xlsx", sheet_name="segmentation")

# Data description
df.info()
df_desc = pd.DataFrame(df.describe(include="all"))

# Target description
print(df.objet.value_counts())

# Split data
from sklearn.model_selection import train_test_split
df_train, df_test = train_test_split(df, test_size=300, random_state=0, stratify=df.objet)

# Shape description
print(df_train.shape, df_test.shape)

# Selection, Standardization, Perceptron
from sklearn.feature_selection import SelectKBest, f_classif, VarianceThreshold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron

# Pipeline
from sklearn.pipeline import Pipeline
model = Pipeline([("selFirst", VarianceThreshold()),
                  ("selSecond", SelectKBest(score_func=f_classif, k=5)),
                  ("std", StandardScaler()),
                  ("clf", Perceptron(random_state=0))
                  ])

# Learning
model.fit(df_train.iloc[:, :-1], df_train.objet)

# Output description

# Variances computing
model.named_steps["selFirst"].variances_

# Coefficients of perceptron
model.named_steps["clf"].coef_

# Prediction of data test
pred = model.predict(df_test.iloc[:, :-1])

# Metric and Score
from sklearn import metrics
metrics.accuracy_score(df_test.objet, pred)

# Numbers of features to select
parameters = [{"selSecond__k": [1, 2, 5, 10, 15]}]

# Cross-validation
from sklearn.model_selection import StratifiedKFold
CvStrat = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)

# Best result of parameters
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(model, param_grid=parameters, cv=CvStrat, refit=True)

# Computing
grid.fit(df_train.iloc[:, :-1], df_train.objet)

# Shown the result
grid.cv_results_

# Transform result on df
pd.DataFrame(grid.cv_results_)[["params", "mean_test_score"]]

# Best model
pred_Best = grid.best_estimator_.predict(df_train.iloc[:, :-1])
metrics.accuracy_score(df_train.objet,pred_Best )

# Library to save and saving
import pickle
f = open("pipeline.sav", "wb")
pickle.dump(grid.best_estimator_, f)

# Close the  file
f.close()
