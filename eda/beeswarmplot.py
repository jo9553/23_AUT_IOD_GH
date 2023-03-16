from sklearn import datasets

iris = datasets.load_iris()

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.DataFrame(iris.data)
df.loc[0:50,"species"] = "setosa"
df.loc[50:100,"species"] = "versicolor"
df.loc[100:150,"species"] = "virginica"
df.columns= ["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)", "species"]

print(df)
# Create bee swarm plot with Seaborn's default settings
sns.set()
sns.swarmplot(x='species', y='petal length (cm)', data=df, hue="species")

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()

