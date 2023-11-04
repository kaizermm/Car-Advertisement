# Car-Advertisement
## Introduction
The objective of this report is to analyze the impact of age, mileage, condition, and cylinder on the price of vehicles using data collected over the past few years. By examining these factors, we aim to gain insights into how each variable influences the pricing of vehicles.
## DataSets
Data columns in vehicle_us.csv
|Column            |Description         |Column type | 
 |:---------------|:------------------------|:-------------|
 | price     | price of a vehicle| integer      |
 | model_year   | year model of a vehicle  | float     |
 | model   | model of a car | objective   |
 | condition    | condition of a car | object   |
 |  cylinders     | Number of cylinders of a vehicle|  float    |
 |  fuel   |  fuel type | objective     |
 |   odometer    | instrument for measuring the distance | float  |
 |  transmission   | type of transmission |  object    |
 |  type   |  type of vehicle | object    |
 |  pain_color   | color of the vehicle | object  |
 | is_4wd      | Does the vehicle have 4-wheel drive? (1 for yes, 0 for no) |  float    |
 | date_posted    |  date post the ad | object     |
 | date_listed      | number of day have posted the vehicle ad  | float  |


## This project includes the following files:

- The project's final Jupyter notebook (EDA.ipynb) in notebooks;
- app.py to build the app
- vehicles_us.csv
- .gitignore file
- .streamlit

### Table of content

1. Introduction
  
2. General Information

3. First Impressions
 
4. Data Preprocessing
  
5. Exploratory Data Analysis

6. Unveiling Top Car Types
  
7. Unraveling Price Factors
  
8. General Conclusions: Insights and Takeaways

### App link
https://ke-23.onrender.com/

### Instruction for running on the local machine
1. To download a GitHub repository and run it using Streamlit, follow these steps:

2. Fork the repository: Go to the GitHub repository you want to download and click on the "Fork" button in the top right corner. This will create a copy of the repository in your GitHub account.

3. Navigate to the desired directory: Open the command prompt and use the cd command to navigate to the directory where you want to download the repository. For example, if you want to download it to your Documents folder, you can use the command cd Documents to navigate there.

4. Clone the repository: In the command prompt, use the git clone command followed by the repository URL. This will download the repository to your local machine.

5. Navigate to the repository directory: Use the cd command to navigate into the downloaded repository directory. For example, if the repository name is my-repo, you can use the command cd my-repo to enter the directory.

6. Run the Streamlit app: In the command prompt, use the streamlit run command followed by the name of the Python file that contains your Streamlit app. Typically, this file is named app.py. 
