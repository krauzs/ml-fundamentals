import pandas as pd 

df = pd.read_csv("titanic.csv")
df = df.drop(columns=['Cabin'])
df['Age'] = df['Age'].fillna(df['Age'].median())
df = df.dropna(subset=['Embarked'])

print(df.groupby("Sex")["Survived"].mean()) 
print(df.groupby("Pclass")["Survived"].mean())
# From this we can see that sex is the stronger signal with a larger gap and that being in a higher class has a higher survival rate
# The model should weigh on sex before pclass 

print(df["Sex"].value_counts())
print(df["Embarked"].value_counts())

df = pd.get_dummies(df, columns=['Sex', 'Embarked'],drop_first=True ,dtype=int)
print(df.head())