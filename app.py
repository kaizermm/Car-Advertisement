
# Loading all the libraries
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
#read the file
encoding="unicode_escape"
vehicle_ad_data=pd.read_csv('vehicles_us.csv',encoding= 'unicode_escape')
# Fill the NaNs in is_4wd column with zeros since the column contains either 1 or 0
vehicle_ad_data['is_4wd'].fillna(value= 0.0, inplace=True)
vehicle_ad_data['is_4wd'] = vehicle_ad_data['is_4wd'].astype(int)
vehicle_ad_data.head()
#Fill missing value in model_year column with the median of cars of the same model
vehicle_ad_data['model_year'].fillna(
    vehicle_ad_data.groupby(['model'])['model_year'].transform(np.median), inplace=True
)
unique_cylinders = vehicle_ad_data['cylinders'].unique()
print(unique_cylinders)
# Fill missing values in 'cylinders' based on car model
vehicle_ad_data['cylinders'].fillna(
    vehicle_ad_data.groupby(['model'])['cylinders'].transform('median'), inplace=True
)

# Filter out incorrect values with 4 characters
vehicle_ad_data = vehicle_ad_data[vehicle_ad_data['cylinders'].astype(str).str.len() < 4]
#Filled last missing odometer values of same listing with the mean value 
vehicle_ad_data['odometer'].fillna((vehicle_ad_data['odometer'].mean()), inplace=True)
# change the missing values from 'paint_color' with the most occuring color from mode
vehicle_ad_data['paint_color'] = vehicle_ad_data.groupby('model')['paint_color'].transform(lambda x: x.fillna(x.mode().iloc[0]))
# function replace implicit duplicates
def replace_wrong_models(wrong_models, correct_models):
    # Replace the wrong model names with the correct model names
    vehicle_ad_data['model'] = vehicle_ad_data['model'].replace(wrong_models, correct_models)
    # Print the updated 'model' column
    print(vehicle_ad_data['model'])
#list of wrong model
wrong_models=['ford f150', 'ford f-250 super duty', 'ford f350 super duty']
#list of correct model
correct_models=['ford f-150', 'ford f-250 sd', 'ford f-350 sd']
#call of the function to replace wrong models
replace_wrong_models(wrong_models, correct_models)
#Drop duplicates to have unique combination of data
vehicle_ad_data = vehicle_ad_data.drop_duplicates(subset=['model','price', 'model_year', 'model', 'odometer'])
#Replaceing data type for model_year category to int
vehicle_ad_data['model_year'] = vehicle_ad_data['model_year'].astype(int)
#Replaceing data type for cylinders category to int
vehicle_ad_data['cylinders'] = vehicle_ad_data['cylinders'].astype(int)
#Replaceing data type for odometer category to int
vehicle_ad_data['odometer'] = vehicle_ad_data['odometer'].astype(int)
#Replacing data type for date_posted into datetime type
vehicle_ad_data['date_posted']=pd.to_datetime(vehicle_ad_data['date_posted'])
#  Change the condition values with something that can be manipulated more easily
vehicle_ad_data.loc[:, 'condition'] = vehicle_ad_data['condition'].replace(
    to_replace=['new', 'like new', 'excellent', 'good', 'fair', 'salvage'],
    value=[5, 4, 3, 2, 1, 0]
)
#add the age of the car
# first isolate 'year' from 'date_posted' column
vehicle_ad_data['year_posted'] = vehicle_ad_data['date_posted'].dt.year
# create a function that calculate car age
def calculate_car_age(row):
    return ((row['year_posted'] - row['model_year'])+1)

vehicle_ad_data['Car_Age'] = vehicle_ad_data.apply(calculate_car_age, axis=1)
    # Add 'Car_mileage' and handle non-finite values
vehicle_ad_data['Car_mileage'] = vehicle_ad_data['odometer'] / ((vehicle_ad_data['year_posted'] - vehicle_ad_data['model_year'])+1)
vehicle_ad_data['Car_mileage'].replace([np.inf, -np.inf], np.nan, inplace=True)

# Round 'Car_mileage' to remove decimal places
vehicle_ad_data['Car_mileage'] = vehicle_ad_data['Car_mileage'].round()

#header
st.header('data distribution')
#histogram for price
st.subheader('price distribution')
fig_price=px.histogram(vehicle_ad_data,x='Car_Age')
st.plotly_chart(fig_price)

# Histogram for Car Age
st.subheader("Car Age Distribution")
fig_car_age = px.histogram(vehicle_ad_data, x='Car_Age')
st.plotly_chart(fig_car_age)


# Histogram for Car Mileage
st.subheader("Car Mileage Distribution")
fig_car_mileage = px.histogram(vehicle_ad_data, x='Car_mileage')
st.plotly_chart(fig_car_mileage)


# Scatter Plot for Price and Car Age
st.subheader("Scatter Plot: Price vs Car Age")
fig_scatter = px.scatter(vehicle_ad_data, x='Car_Age', y='price')
st.plotly_chart(fig_scatter)


# Checkbox to toggle between histograms and scatter plot
show_scatter = st.checkbox("Show Scatter Plot")


if show_scatter:
    st.plotly_chart(fig_scatter)
else:
    st.plotly_chart(fig_price)
    st.plotly_chart(fig_car_age)
    st.plotly_chart(fig_car_mileage)


# Header
st.header("Boxplots")
# Boxplot for Price
st.subheader("Price Boxplot")
fig_price = px.box(vehicle_ad_data, x='price')
st.plotly_chart(fig_price)


# Boxplot for Car Age
st.subheader("Car Age Boxplot")
fig_car_age = px.box(vehicle_ad_data, x='Car_Age')
st.plotly_chart(fig_car_age)


# Boxplot for Car Mileage
st.subheader("Car Mileage Boxplot")
fig_car_mileage = px.box(vehicle_ad_data, x='Car_mileage')
st.plotly_chart(fig_car_mileage)


# Checkbox to toggle between boxplots
show_car_age = st.checkbox("Show Car Age Boxplot")
show_car_mileage = st.checkbox("Show Car Mileage Boxplot")


if show_car_age:
    st.plotly_chart(fig_car_age)


if show_car_mileage:
    st.plotly_chart(fig_car_mileage)


# Default: Show Price Boxplot
st.plotly_chart(fig_price)


def clean_outlier(dataframe, col):
    # Calculate the quantiles
    lower_quantile = dataframe[col].quantile(0.05)
    upper_quantile = dataframe[col].quantile(0.95)
   
    # Create new column
    new_col = col + '_clean'
    dataframe[new_col] = dataframe[col].copy()
   
    # Remove outliers
    dataframe.loc[(dataframe[new_col] > upper_quantile) | (dataframe[new_col] < lower_quantile), col] = None
    return dataframe

#call the clean_outlier function
clean_outlier(vehicle_ad_data, 'price')
clean_outlier(vehicle_ad_data, 'Car_mileage')
clean_outlier(vehicle_ad_data, 'Car_Age')

#Header
st.header("Histograms")

#Histogram for Price
st.subheader("Price Histogram")
fig_price = px.histogram(vehicle_ad_data, x='price_clean')
st.plotly_chart(fig_price)

# Histogram for Car Age
st.subheader("Car Age Histogram")
fig_car_age = px.histogram(vehicle_ad_data, x='Car_Age_clean')
st.plotly_chart(fig_car_age)

# Histogram for Car Mileage
st.subheader("Car Mileage Histogram")
fig_car_mileage = px.histogram(vehicle_ad_data, x='Car_mileage_clean')
st.plotly_chart(fig_car_mileage)

# Checkbox to toggle between histograms
show_car_age = st.checkbox("Show Car Age Histogram")
show_car_mileage = st.checkbox("Show Car Mileage Histogram")

if show_car_age:
    st.plotly_chart(fig_car_age)

if show_car_mileage:
    st.plotly_chart(fig_car_mileage)

# Default: Show Price Histogram
st.plotly_chart(fig_price)

#unraveling top car price
st.header("Average Price per Vehicle Type")
type_grouped = vehicle_ad_data.pivot_table(index='type', values='price', aggfunc='mean')
show_histogram = st.checkbox("Show Histogram")

# Define fig_bar outside the if-else statement
fig_bar = px.bar(type_grouped, x=type_grouped.index, y='price')

if show_histogram:
    # Histogram for price
    st.subheader("Histogram: Price Distribution")
    fig_hist = px.histogram(vehicle_ad_data, x='price')
    st.plotly_chart(fig_hist)
else:
    st.plotly_chart(fig_bar)

#plot and identify the two types with the greatest number of ads in order to identify which type is the most popular
st.header("Number of Ads per Vehicle Type")
type_grouped = vehicle_ad_data.groupby('type').agg(count=('price', 'count'), mean=('price', 'mean'))


st.subheader("Bar Graph: Number of Ads per Vehicle Type")
fig_bar = px.bar(type_grouped, x=type_grouped.index, y='count')
st.plotly_chart(fig_bar)


show_average_price = st.checkbox("Show Average Price")

if show_average_price:
    # Bar graph for average price per vehicle type
    st.subheader("Bar Graph: Average Price per Vehicle Type")
    fig_price = px.bar(type_grouped, x=type_grouped.index, y='mean')
    st.plotly_chart(fig_price)
else:
    st.plotly_chart(fig_bar)

#price factor
type_grouped = vehicle_ad_data.pivot_table(index='type', values='price', aggfunc='mean')

#Header
st.header("Average Price per Vehicle Type")

#Bar graph for average price per vehicle type
fig_bar = px.bar(type_grouped, x=type_grouped.index, y='price')
st.plotly_chart(fig_bar)

#Subset data for SUV and sedan
popular_vehicle = vehicle_ad_data[vehicle_ad_data['type'].isin(['SUV', 'sedan'])]

#Scatter plot for SUV and sedan with link between price and condition
fig_scatter = px.scatter(popular_vehicle, x='condition', y='price')
st.plotly_chart(fig_scatter)

#scatter plot between price and age
st.header("Relationship between Price and Age of a Vehicle")
show_scatter = st.checkbox("Show Scatter Plot")

if show_scatter:
# Scatter plot for price and age
    st.subheader("Scatter Plot: Price vs Age")
    fig_scatter = px.scatter(vehicle_ad_data, x='Car_Age_clean', y='price')
    st.plotly_chart(fig_scatter)
else:
# Histogram for price
    st.subheader("Histogram: Price Distribution")
    fig_hist = px.histogram(vehicle_ad_data, x='price')
    st.plotly_chart(fig_hist)

st.header("Relationship between Price and Mileage of a Vehicle")
show_scatter = st.checkbox("Show Scatter Plot")

st.header("Relationship between Price and Mileage of a Vehicle")
show_scatter = st.checkbox("Show Scatter Plot")

if show_scatter:
# Scatter plot for mileage and price
    st.subheader("Scatter Plot: Mileage vs Price")
    fig_scatter = px.scatter(vehicle_ad_data, x='Car_mileage_clean', y='price_clean')
    st.plotly_chart(fig_scatter)
else:
# Histogram for price
    st.subheader("Histogram: Price Distribution")
    fig_hist = px.histogram(vehicle_ad_data, x='price_clean')
    st.plotly_chart(fig_hist)
