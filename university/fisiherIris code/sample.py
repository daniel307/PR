import pandas as pd
import numpy as np
import seaborn as sns


iris_data = pd.read_csv('assets/iris.csv')
iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

#you can specific the number to show here
iris_data.head(10)


iris_data.shape


iris_data['species'].unique()
print(iris_data.groupby('species').size())


iris_data.min()
iris_data.max()
iris_data.mean()
iris_data.median()
iris_data.std()



summary = iris_data.describe()
summary = summary.transpose()
summary.head()

