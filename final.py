#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv('stud.csv')

df.info()

df = df.replace(r'^\s*$', np.nan, regex=True)

missing_values = df.isna().sum()
print("Missing Values:")
print(missing_values)

print(df)

df['Age'] = pd.to_numeric(df['Age'], errors='coerce', downcast='integer')
df['hrsStudy'] = pd.to_numeric(df['hrsStudy'], errors='coerce', downcast='integer')
df['Age'] = df['Age'].astype('Int32')
df['hrsStudy'] = df['hrsStudy'].astype('Int32')

df["FinalGrade"].plot.bar()

z_scores = (df['FinalGrade'] - df['FinalGrade'].mean()) / df['FinalGrade'].std()
abs_z_scores = np.abs(z_scores)
threshold = 3
filtered_entries = (abs_z_scores < threshold)
df_clean = df[filtered_entries]

df_clean.to_csv('cleaned_data.csv', index=False)

df_clean["FinalGrade"].plot.bar()

print("\nDataFrame after removing outliers:")
print(df_clean)

print("\nData Types:")
print(df_clean.dtypes)

df_clean.info()

def grade_to_letter(grade):
    if grade > 90:
        return 'A'
    elif grade > 80:
        return 'B'
    elif grade > 70:
        return 'C'
    elif grade > 60:
        return 'D'
    elif grade > 50:
        return 'E'
    else:
        return 'F'

df_clean['LetterGrade'] = df_clean['FinalGrade'].apply(grade_to_letter)

print(df_clean[['FinalGrade', 'LetterGrade']])

grade_counts = df_clean['LetterGrade'].value_counts().sort_index()
grade_counts.plot(kind='bar', color='skyblue')

