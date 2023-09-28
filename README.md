# Student Data Analysis

This repository is dedicated to managing, cleaning, and analyzing a dataset ('stud.csv') consisting of student data. The dataset includes the following columns: `StudentID`, `Age`, `email`, `hrsStudy`, and `FinalGrade`. 

The primary goal is to preprocess this data, identify and handle outliers and missing values, and perform exploratory data analysis.

## Contents

- **`stud.csv`**: Original dataset containing student information.
- **`cleaned_data.csv`**: Data after cleaning and preprocessing.
- **`mySolution.ipynb`**: Detailed Jupyter Notebook of the data cleaning and processing steps.
- **`final.py`**: Python script of the data processing steps from the notebook, providing a cleaner, non-notebook alternative.

## Original Data (`stud.csv`)

The dataset contains records for 50 students with the following fields:
- **StudentID**: Unique identifier for each student.
- **Age**: Age of the student.
- **email**: Email address of the student, following the format `s[StudentID]@oslomet.no`.
- **hrsStudy**: Number of hours the student studies.
- **FinalGrade**: Final grade achieved by the student.

### Issues Noted in Original Data

- Abnormal ages (e.g., 333 and 220).
- Missing values in `hrsStudy` and `FinalGrade`.
- Implausible grade values like 673.
- Mixed data types due to non-numeric or missing values.

## Data Cleaning

The data cleaning process involved:
1. Replacing empty strings with NaN.
2. Converting the `Age` and `hrsStudy` columns to numeric data types.
3. Removing outliers from the `FinalGrade` column based on Z-scores.
4. Converting numeric grades to letter grades.

### Observations from Cleaned Data

- The cleaned dataset (`cleaned_data.csv`) has 48 records, indicating the removal of some problematic rows during the cleaning process.
- The Int32 data type was used for fields like `Age` and `hrsStudy` to accommodate missing values.
- Int32 can handle both integer values and missing values simultaneously. This provides a clearer representation of the data, as ages and study hours are naturally integers, while still allowing for the existence of missing or null values in the dataset.

**Note**: After outlier removal, some anomalies still exist in fields like Age and FinalGrade. I will remove these as well through at a later time.

## Script (`mySolution.ipynb` & `final.py`)

Both the Jupyter Notebook and the Python script go through the following steps:
1. Data Initialization.
2. Display of Data Information.
3. Replacement of Empty Strings with NaN.
4. Display of Missing Values.
5. Conversion of Data Types for `Age` and `hrsStudy`.
6. Display of the FinalGrade Bar Plot.
7. Removal of Outliers Based on Z-scores.
8. Saving of Cleaned Data.
9. Display of Information for Cleaned Data.
10. Conversion of Numeric Grades to Letter Grades and Visualization of the Distribution.

For a detailed understanding and view of the process, including visualizations, please refer to `mySolution.ipynb`. For a straightforward script, refer to `final.py`.
