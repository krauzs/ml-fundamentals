import pandas as pd 
from sklearn.model_selection import train_test_split

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
print(df.columns)
y = df["Survived"]
X = df.drop(columns=['Survived','PassengerId','Name','Ticket'])
print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape)
print(X_test.shape)