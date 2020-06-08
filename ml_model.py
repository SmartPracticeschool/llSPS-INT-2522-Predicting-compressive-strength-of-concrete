# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# reading the dataset
df = pd.read_excel('Concrete_Data.xls')

# renaming columns
df_new = df.rename(columns={'Cement (component 1)(kg in a m^3 mixture)': 'Cement',
                           'Blast Furnace Slag (component 2)(kg in a m^3 mixture)':'Blast Furnace Slag',
                           'Fly Ash (component 3)(kg in a m^3 mixture)':'Fly Ash',
                           'Water  (component 4)(kg in a m^3 mixture)':'Water',
                           'Superplasticizer (component 5)(kg in a m^3 mixture)':'Superplasticizer',
                           'Coarse Aggregate  (component 6)(kg in a m^3 mixture)':'Coarse Aggregate',
                           'Fine Aggregate (component 7)(kg in a m^3 mixture)':'Fine Aggregate',
                           'Age (day)': 'Age',
                           'Concrete compressive strength(MPa, megapascals) ':'Concrete compressive strength'})      


# Converting to NumPy Arrays
X = df_new.iloc[:,0:8].values
y = df_new.iloc[:,8:9].values

# Splitting train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# creating Random Forest Regression model
from sklearn.ensemble import RandomForestRegressor
forest = RandomForestRegressor(n_estimators=50, random_state=42)

# fitting the model with training data
forest.fit(X_train, y_train)

# saving model with training data
pickle.dump(forest, open('ml_model.pkl','wb'))

# loading model to compare the results
ml_model = pickle.load(open('ml_model.pkl','rb'))
