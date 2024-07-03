#Iporting the neccesary package
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.set(color_codes=True)

# Load the dataset
df = pd.read_csv("/content/data.csv")

# Display the first 5 rows
print(df.head(5))

# Display the last 5 rows
print(df.tail(5))

# Display the data types of columns
print(df.dtypes)

# Drop the specified columns
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
print(df.head(5))

# Rename columns
df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels":
                        "Drive mode", "highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price"})
print(df.head(5))

# Display the shape of the dataframe
print(df.shape)

# Find duplicated rows
duplicated_rows_df = df[df.duplicated()]
print("Number of duplicated rows:", duplicated_rows_df.shape[0])

# Drop duplicates
df = df.drop_duplicates()
print(df.head(5))

# Count the non-NA/null entries for each column
print(df.count())

# Check for null values
print(df.isnull().sum())

# Drop rows with null values
df = df.dropna()
print(df.count())

# Check again for null values
print(df.isnull().sum())

# Plot boxplots
sns.boxplot(x=df['Price'])
plt.show()

sns.boxplot(x=df['HP'])
plt.show()

sns.boxplot(x=df['Cylinders'])
plt.show()

# Calculate IQR for numeric columns
numeric_cols = ['HP', 'Cylinders', 'MPG-H', 'MPG-C', 'Price']
Q1 = df[numeric_cols].quantile(0.25)
Q3 = df[numeric_cols].quantile(0.75)
IQR = Q3 - Q1
print(IQR)

# Filter out the outliers
df = df[~((df[numeric_cols] < (Q1 - 1.5 * IQR)) | (df[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df.shape)

# Plot the number of cars by make
df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10, 5))
plt.title("Number of cars by make")
plt.ylabel("Number of cars")
plt.xlabel("Make")
plt.show()

# Plot the correlation heatmap for numeric columns only
plt.figure(figsize=(10, 5))
numeric_df = df[numeric_cols]  # Selecting only numeric columns
c = numeric_df.corr()
sns.heatmap(c, cmap="BrBG", annot=True)
plt.show()

print(c)

# Scatter plot of HP vs. Price
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')  # Corrected this line
ax.set_ylabel('Price')  # Corrected this line
plt.show()
