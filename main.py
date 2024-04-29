import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("resources/Dataset.csv")


# 1. Remove duplicates
df = df.drop_duplicates()


# 2. Replace missing values in "livelihood score" column with 0
df['Livelihood_Score'] = df['Livelihood_Score'].fillna(0)


# 3. Remove unwanted special characters from "oblast" column values.
df['Oblast'] = df['Oblast'].str.replace(r"[^a-zA-Z]+", "", regex=True)


# 4. Order from highest to lowest.
df = df.sort_values(by='Livelihood_Score', ascending=False)


# 5. Set conditional equation to a new column and call it "Severity".
# If score is >75 then High, if >49 & <76 then Medium, if <50 then Low
conditions = [
    (df['Livelihood_Score'] > 75),
    (df['Livelihood_Score'] > 49) & (df['Livelihood_Score'] < 76),
    (df['Livelihood_Score'] < 50)
]
values = ['High', 'Medium', 'Low']
df['Severity'] = np.select(conditions, values, default='Unknown')


# Write df to file
df.to_csv("resources/cleaned_dataset.csv", index=False)


# 6. Visualize the scores by oblast using bar chart or scatter plot
plt.figure(figsize=(12, 6))
plt.bar(df['Oblast'], df['Livelihood_Score'], color='skyblue')
plt.xlabel('Oblast')
plt.ylabel('Livelihood Score')
plt.title('Livelihood Score by Oblast')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
