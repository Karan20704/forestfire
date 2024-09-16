# Forest Fire Dataset Analysis and Prediction

This project analyzes the Forest Fire dataset with data from two regions: Bejaia and Sidi Abbes. The goal is to perform exploratory data analysis (EDA), split the data into training and test sets, scale the data, and use Ridge Regression to predict the Fire Weather Index (FWI). Additionally, a web application is provided for making FWI predictions.

## Project Steps

1. **Data Preparation**
2. **Exploratory Data Analysis (EDA)**
3. **Data Splitting**
4. **Data Scaling**
5. **Prediction Model**
6. **Web Application**

<details>
<summary>Data Preparation and EDA</summary>

### Dataset Overview
The dataset used in this project is the Algerian Forest Fires Dataset, which contains data from two regions: Bejaia and Sidi Abbes. The dataset includes various meteorological and fire-related features.

### Steps for Data Preparation

1. **Loading the Data**: The dataset is loaded and initial exploration is performed.
2. **Handling Missing Values**: Missing values are identified and handled appropriately.
3. **Data Cleaning**: The dataset is cleaned by removing any unnecessary or duplicate data.
4. **Feature Engineering**: New features are created to enhance the dataset for better model performance.

### Exploratory Data Analysis (EDA)
EDA is performed to understand the dataset better. Visualizations such as histograms, pie charts, and heatmaps are created to analyze the distribution of data and correlations between features.

</details>

<details>
<summary>Data Splitting</summary>

The cleaned dataset is split into training and test sets. The target variable is FWI, and the features are the meteorological and fire-related parameters.

</details>

<details>
<summary>Data Scaling</summary>

`StandardScaler` from scikit-learn is used to scale the features for better model performance.

</details>

<details>
<summary>Prediction Model</summary>

Ridge Regression is used as the prediction model. The model is trained on the training data and evaluated on the test data. The performance metrics include Mean Absolute Error (MAE) and R² score.

</details>

<details>
<summary>Web Application</summary>

A web application is developed using Flask to provide a user interface for making FWI predictions. The user can input the feature values, and the application returns the predicted FWI.

### Running the Web Application

1. Navigate to the `webapp` directory.
2. Run the Flask application:
   ```bash
   python app.py
