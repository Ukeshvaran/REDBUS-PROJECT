import pandas as pd

df=pd.read_csv("C:/Users/ukesh/OneDrive/Desktop/redbus.csv")
df['Fare'] = df['Fare'].str.replace('INR', '', regex=False) 
df['Fare'] = df['Fare'].str.replace(',', '', regex=False)   
df['Fare'] = df['Fare'].fillna(0)
df['Fare'] = pd.to_numeric(df['Fare'], errors='coerce') 
df['Fare'] = df['Fare'].fillna(0)

print(df['Fare'].head())


df["Ratings"]=df["Ratings"].str.replace("New","")
df["Ratings"]=df["Ratings"].str.strip()
df["Ratings"]=df["Ratings"].str.split().str[0]
df["Ratings"] = pd.to_numeric(df["Ratings"], errors='coerce')
df["Ratings"].fillna(0,inplace=True)



df.to_csv('ukesh.csv')



final_df=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/ukesh.csv')
final_df.head()