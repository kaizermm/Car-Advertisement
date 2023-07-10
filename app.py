{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Unveiling the Driving Factors: Exploring the Influences on Car Prices"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As an analyst at Crankshaft List, delving into the world of car sales is an exhilarating experience. Each day, our platform witnesses a surge of free vehicle advertisements, painting a vivid picture of the market's dynamics.Through a comprehensive analysis of our vast vehicles ads database, we aim to shed light on the pivotal factors that wield the greatest influence when it comes to selling a car."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Table of content"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style='color:blue'>\n",
    "\n",
    "1.Introduction\n",
    "  \n",
    "\n",
    "2.General Information\n",
    "\n",
    "\n",
    "3.First Impressions\n",
    " \n",
    "4.Data Preprocessing\n",
    "  \n",
    "5.Exploratory Data Analysis\n",
    "\n",
    "6.Unveiling Top Car Types\n",
    "  \n",
    " 7.Unraveling Price Factors\n",
    "  \n",
    "8.General Conclusions: Insights and Takeaways\n",
    "\n",
    "9.Conclusion and Project Completion Checklist"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Introduction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Welcome to the fascinating world of car sales analysis! In this analysis, we will delve into car sales data and embark on a journey to uncover the factors that play a pivotal role in influencing car prices.\n",
    "\n",
    "Car sales are a dynamic and ever-evolving market, with hundreds of transactions taking place every day. Understanding the intricate web of variables that contribute to price fluctuations is crucial for both buyers and sellers in making informed decisions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### General information"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\lelou\\anaconda3\\lib\\site-packages (1.24.1)\n",
      "Requirement already satisfied: pillow<10,>=6.2.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (9.2.0)\n",
      "Requirement already satisfied: watchdog in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (4.23.4)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: pandas<3,>=0.25 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (1.4.4)\n",
      "Requirement already satisfied: packaging<24,>=14.1 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: rich<14,>=10.11.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (13.4.2)\n",
      "Requirement already satisfied: pydeck<1,>=0.1.dev5 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (0.8.1b0)\n",
      "Requirement already satisfied: tenacity<9,>=8.0.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (8.0.1)\n",
      "Requirement already satisfied: requests<3,>=2.4 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (2.28.1)\n",
      "Requirement already satisfied: validators<1,>=0.2 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (0.20.0)\n",
      "Requirement already satisfied: toml<2 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: importlib-metadata<7,>=1.4 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (4.11.3)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (5.3.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.0.1 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (4.3.0)\n",
      "Requirement already satisfied: numpy<2,>=1 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (1.21.5)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: pympler<2,>=0.9 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: tzlocal<5,>=1.1 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (4.3.1)\n",
      "Requirement already satisfied: pyarrow>=4.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (12.0.1)\n",
      "Requirement already satisfied: python-dateutil<3,>=2 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from streamlit) (3.1.31)\n",
      "Requirement already satisfied: toolz in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.11.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.16.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.5)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3->streamlit) (4.0.10)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from importlib-metadata<7,>=1.4->streamlit) (3.8.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from packaging<24,>=14.1->streamlit) (3.0.9)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from pandas<3,>=0.25->streamlit) (2022.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from python-dateutil<3,>=2->streamlit) (1.16.0)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from requests<3,>=2.4->streamlit) (1.26.11)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from requests<3,>=2.4->streamlit) (3.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from requests<3,>=2.4->streamlit) (2022.9.14)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from requests<3,>=2.4->streamlit) (2.0.4)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from rich<14,>=10.11.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from rich<14,>=10.11.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: pytz-deprecation-shim in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from tzlocal<5,>=1.1->streamlit) (0.1.0.post0)\n",
      "Requirement already satisfied: tzdata in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from tzlocal<5,>=1.1->streamlit) (2023.3)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from validators<1,>=0.2->streamlit) (5.1.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3->streamlit) (5.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\lelou\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.11.0->streamlit) (0.1.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install streamlit\n",
    "# Loading all the libraries\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "import streamlit as st\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    vehicle_ad_data=pd.read_csv('/Users/lelou/Car-Advertisement/vehicles_us.csv')\n",
    "except:\n",
    "    vehicle_ad_data=pd.read_csv('https://code.s3.yandex.net/datasets/vehicles_us.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 51525 entries, 0 to 51524\n",
      "Data columns (total 13 columns):\n",
      " #   Column        Non-Null Count  Dtype  \n",
      "---  ------        --------------  -----  \n",
      " 0   price         51525 non-null  int64  \n",
      " 1   model_year    47906 non-null  float64\n",
      " 2   model         51525 non-null  object \n",
      " 3   condition     51525 non-null  object \n",
      " 4   cylinders     46265 non-null  float64\n",
      " 5   fuel          51525 non-null  object \n",
      " 6   odometer      43633 non-null  float64\n",
      " 7   transmission  51525 non-null  object \n",
      " 8   type          51525 non-null  object \n",
      " 9   paint_color   42258 non-null  object \n",
      " 10  is_4wd        25572 non-null  float64\n",
      " 11  date_posted   51525 non-null  object \n",
      " 12  days_listed   51525 non-null  int64  \n",
      "dtypes: float64(4), int64(2), object(7)\n",
      "memory usage: 5.1+ MB\n"
     ]
    }
   ],
   "source": [
    "vehicle_ad_data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "The \"vehicle_us\" dataset consists of 51,525 entries with 13 columns, providing information about vehicles available for sale. It includes details like price, model year, model, condition, cylinders, fuel, odometer, transmission, type, paint color, is_4wd, date posted, and days listed. The dataset contains a mix of numeric and categorical data, with some columns having missing values. Overall, analyzing this dataset can offer insights into the used vehicle market and factors affecting pricing and desirability."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### First Impressions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "      <th>model_year</th>\n",
       "      <th>model</th>\n",
       "      <th>condition</th>\n",
       "      <th>cylinders</th>\n",
       "      <th>fuel</th>\n",
       "      <th>odometer</th>\n",
       "      <th>transmission</th>\n",
       "      <th>type</th>\n",
       "      <th>paint_color</th>\n",
       "      <th>is_4wd</th>\n",
       "      <th>date_posted</th>\n",
       "      <th>days_listed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>9400</td>\n",
       "      <td>2011.0</td>\n",
       "      <td>bmw x5</td>\n",
       "      <td>good</td>\n",
       "      <td>6.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>145000.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>SUV</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2018-06-23</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>ford f-150</td>\n",
       "      <td>good</td>\n",
       "      <td>6.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>88705.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>white</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2018-10-19</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5500</td>\n",
       "      <td>2013.0</td>\n",
       "      <td>hyundai sonata</td>\n",
       "      <td>like new</td>\n",
       "      <td>4.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>110000.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>red</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2019-02-07</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1500</td>\n",
       "      <td>2003.0</td>\n",
       "      <td>ford f-150</td>\n",
       "      <td>fair</td>\n",
       "      <td>8.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>NaN</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2019-03-22</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>14900</td>\n",
       "      <td>2017.0</td>\n",
       "      <td>chrysler 200</td>\n",
       "      <td>excellent</td>\n",
       "      <td>4.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>80903.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>black</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2019-04-02</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>14990</td>\n",
       "      <td>2014.0</td>\n",
       "      <td>chrysler 300</td>\n",
       "      <td>excellent</td>\n",
       "      <td>6.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>57954.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>black</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2018-06-20</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>12990</td>\n",
       "      <td>2015.0</td>\n",
       "      <td>toyota camry</td>\n",
       "      <td>excellent</td>\n",
       "      <td>4.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>79212.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>white</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-12-27</td>\n",
       "      <td>73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>15990</td>\n",
       "      <td>2013.0</td>\n",
       "      <td>honda pilot</td>\n",
       "      <td>excellent</td>\n",
       "      <td>6.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>109473.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>SUV</td>\n",
       "      <td>black</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2019-01-07</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>11500</td>\n",
       "      <td>2012.0</td>\n",
       "      <td>kia sorento</td>\n",
       "      <td>excellent</td>\n",
       "      <td>4.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>104174.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>SUV</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2018-07-16</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>9200</td>\n",
       "      <td>2008.0</td>\n",
       "      <td>honda pilot</td>\n",
       "      <td>excellent</td>\n",
       "      <td>NaN</td>\n",
       "      <td>gas</td>\n",
       "      <td>147191.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>SUV</td>\n",
       "      <td>blue</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2019-02-15</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>19500</td>\n",
       "      <td>2011.0</td>\n",
       "      <td>chevrolet silverado 1500</td>\n",
       "      <td>excellent</td>\n",
       "      <td>8.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>128413.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>black</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2018-09-17</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>8990</td>\n",
       "      <td>2012.0</td>\n",
       "      <td>honda accord</td>\n",
       "      <td>excellent</td>\n",
       "      <td>4.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>111142.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>grey</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2019-03-28</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>18990</td>\n",
       "      <td>2012.0</td>\n",
       "      <td>ram 1500</td>\n",
       "      <td>excellent</td>\n",
       "      <td>8.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>140742.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2019-04-02</td>\n",
       "      <td>37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>16500</td>\n",
       "      <td>2018.0</td>\n",
       "      <td>hyundai sonata</td>\n",
       "      <td>excellent</td>\n",
       "      <td>4.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>22104.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>silver</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2019-01-14</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>12990</td>\n",
       "      <td>2009.0</td>\n",
       "      <td>gmc yukon</td>\n",
       "      <td>excellent</td>\n",
       "      <td>8.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>132285.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>SUV</td>\n",
       "      <td>black</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2019-01-31</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>17990</td>\n",
       "      <td>2013.0</td>\n",
       "      <td>ram 1500</td>\n",
       "      <td>excellent</td>\n",
       "      <td>8.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>NaN</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>red</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2018-05-15</td>\n",
       "      <td>111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>14990</td>\n",
       "      <td>2010.0</td>\n",
       "      <td>ram 1500</td>\n",
       "      <td>excellent</td>\n",
       "      <td>8.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>130725.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>red</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2018-12-30</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>13990</td>\n",
       "      <td>2014.0</td>\n",
       "      <td>jeep cherokee</td>\n",
       "      <td>excellent</td>\n",
       "      <td>6.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>100669.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>SUV</td>\n",
       "      <td>red</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2018-08-16</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>12500</td>\n",
       "      <td>2013.0</td>\n",
       "      <td>chevrolet traverse</td>\n",
       "      <td>excellent</td>\n",
       "      <td>6.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>128325.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>SUV</td>\n",
       "      <td>white</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2019-04-09</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>13990</td>\n",
       "      <td>2018.0</td>\n",
       "      <td>hyundai elantra</td>\n",
       "      <td>excellent</td>\n",
       "      <td>4.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>31932.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>red</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-08-25</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    price  model_year                     model  condition  cylinders fuel  \\\n",
       "0    9400      2011.0                    bmw x5       good        6.0  gas   \n",
       "1   25500         NaN                ford f-150       good        6.0  gas   \n",
       "2    5500      2013.0            hyundai sonata   like new        4.0  gas   \n",
       "3    1500      2003.0                ford f-150       fair        8.0  gas   \n",
       "4   14900      2017.0              chrysler 200  excellent        4.0  gas   \n",
       "5   14990      2014.0              chrysler 300  excellent        6.0  gas   \n",
       "6   12990      2015.0              toyota camry  excellent        4.0  gas   \n",
       "7   15990      2013.0               honda pilot  excellent        6.0  gas   \n",
       "8   11500      2012.0               kia sorento  excellent        4.0  gas   \n",
       "9    9200      2008.0               honda pilot  excellent        NaN  gas   \n",
       "10  19500      2011.0  chevrolet silverado 1500  excellent        8.0  gas   \n",
       "11   8990      2012.0              honda accord  excellent        4.0  gas   \n",
       "12  18990      2012.0                  ram 1500  excellent        8.0  gas   \n",
       "13  16500      2018.0            hyundai sonata  excellent        4.0  gas   \n",
       "14  12990      2009.0                 gmc yukon  excellent        8.0  gas   \n",
       "15  17990      2013.0                  ram 1500  excellent        8.0  gas   \n",
       "16  14990      2010.0                  ram 1500  excellent        8.0  gas   \n",
       "17  13990      2014.0             jeep cherokee  excellent        6.0  gas   \n",
       "18  12500      2013.0        chevrolet traverse  excellent        6.0  gas   \n",
       "19  13990      2018.0           hyundai elantra  excellent        4.0  gas   \n",
       "\n",
       "    odometer transmission    type paint_color  is_4wd date_posted  days_listed  \n",
       "0   145000.0    automatic     SUV         NaN     1.0  2018-06-23           19  \n",
       "1    88705.0    automatic  pickup       white     1.0  2018-10-19           50  \n",
       "2   110000.0    automatic   sedan         red     NaN  2019-02-07           79  \n",
       "3        NaN    automatic  pickup         NaN     NaN  2019-03-22            9  \n",
       "4    80903.0    automatic   sedan       black     NaN  2019-04-02           28  \n",
       "5    57954.0    automatic   sedan       black     1.0  2018-06-20           15  \n",
       "6    79212.0    automatic   sedan       white     NaN  2018-12-27           73  \n",
       "7   109473.0    automatic     SUV       black     1.0  2019-01-07           68  \n",
       "8   104174.0    automatic     SUV         NaN     1.0  2018-07-16           19  \n",
       "9   147191.0    automatic     SUV        blue     1.0  2019-02-15           17  \n",
       "10  128413.0    automatic  pickup       black     1.0  2018-09-17           38  \n",
       "11  111142.0    automatic   sedan        grey     NaN  2019-03-28           29  \n",
       "12  140742.0    automatic  pickup         NaN     1.0  2019-04-02           37  \n",
       "13   22104.0    automatic   sedan      silver     NaN  2019-01-14           29  \n",
       "14  132285.0    automatic     SUV       black     1.0  2019-01-31           24  \n",
       "15       NaN    automatic  pickup         red     1.0  2018-05-15          111  \n",
       "16  130725.0    automatic  pickup         red     1.0  2018-12-30           13  \n",
       "17  100669.0    automatic     SUV         red     1.0  2018-08-16           25  \n",
       "18  128325.0    automatic     SUV       white     1.0  2019-04-09           13  \n",
       "19   31932.0    automatic   sedan         red     NaN  2018-08-25           27  "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#look at a sample of data for first 20 rows\n",
    "vehicle_ad_data.head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>unique</th>\n",
       "      <th>top</th>\n",
       "      <th>freq</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>model</th>\n",
       "      <td>51525</td>\n",
       "      <td>100</td>\n",
       "      <td>ford f-150</td>\n",
       "      <td>2796</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>condition</th>\n",
       "      <td>51525</td>\n",
       "      <td>6</td>\n",
       "      <td>excellent</td>\n",
       "      <td>24773</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fuel</th>\n",
       "      <td>51525</td>\n",
       "      <td>5</td>\n",
       "      <td>gas</td>\n",
       "      <td>47288</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>transmission</th>\n",
       "      <td>51525</td>\n",
       "      <td>3</td>\n",
       "      <td>automatic</td>\n",
       "      <td>46902</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>type</th>\n",
       "      <td>51525</td>\n",
       "      <td>13</td>\n",
       "      <td>SUV</td>\n",
       "      <td>12405</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>paint_color</th>\n",
       "      <td>42258</td>\n",
       "      <td>12</td>\n",
       "      <td>white</td>\n",
       "      <td>10029</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date_posted</th>\n",
       "      <td>51525</td>\n",
       "      <td>354</td>\n",
       "      <td>2019-03-17</td>\n",
       "      <td>186</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              count unique         top   freq\n",
       "model         51525    100  ford f-150   2796\n",
       "condition     51525      6   excellent  24773\n",
       "fuel          51525      5         gas  47288\n",
       "transmission  51525      3   automatic  46902\n",
       "type          51525     13         SUV  12405\n",
       "paint_color   42258     12       white  10029\n",
       "date_posted   51525    354  2019-03-17    186"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# A summary statistics table for categorical columns in a DataFrame\n",
    "vehicle_ad_data.describe(include='object').T"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The dataset contains information on 51,525 vehicles. The most popular vehicle model is the \"Ford F-150\" with 2,796 occurrences. A significant number of vehicles are listed as being in \"excellent\" condition (24,773 entries). The majority of vehicles run on \"gas\" fuel (47,288 entries) and have \"automatic\" transmission (46,902 entries). The most frequently listed vehicle type is \"SUV\" (12,405 entries). The most common paint color is \"white\" (10,029 entries), and the vehicles were posted on 354 different dates, with the most frequent date being \"2019-03-17\" (186 occurrences)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Preprocessing"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Processing missing value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total number of row : 51525\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "price               0\n",
       "model_year       3619\n",
       "model               0\n",
       "condition           0\n",
       "cylinders        5260\n",
       "fuel                0\n",
       "odometer         7892\n",
       "transmission        0\n",
       "type                0\n",
       "paint_color      9267\n",
       "is_4wd          25953\n",
       "date_posted         0\n",
       "days_listed         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#count number of null in the dataset\n",
    "print('total number of row :',len(vehicle_ad_data))\n",
    "vehicle_ad_data.isna().sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "price            0.000000\n",
       "model_year       7.023775\n",
       "model            0.000000\n",
       "condition        0.000000\n",
       "cylinders       10.208637\n",
       "fuel             0.000000\n",
       "odometer        15.316836\n",
       "transmission     0.000000\n",
       "type             0.000000\n",
       "paint_color     17.985444\n",
       "is_4wd          50.369723\n",
       "date_posted      0.000000\n",
       "days_listed      0.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Propotion of missing value compare to the whole percentage in percent\n",
    "propor_miss_percent = (vehicle_ad_data.isnull().sum() / len(vehicle_ad_data)) * 100\n",
    "propor_miss_percent"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style='color:blue'>\n",
    "The dataset analysis reveals intriguing insights:\n",
    "\n",
    "-Missing values are present across multiple columns, except for the \"price\" column which is complete.\n",
    "\n",
    "-The \"model_year\" column has 3,619 missing values, creating uncertainty about the manufacturing year of certain vehicles.\n",
    "\n",
    "-The \"cylinders\" column shows 5,260 missing values, suggesting a lack of cylinder information.\n",
    "\n",
    "-The \"odometer\" column has 7,892 missing values, indicating a lack of distance traveled data.\n",
    "\n",
    "-The \"paint_color\" column has 9,267 missing values, leaving color information unknown.\n",
    "\n",
    "-Surprisingly, the \"is_4wd\" column has 25,953 missing values, with almost half of the available values being 1. These missing values could potentially be interpreted as 0.\n",
    "\n",
    "-Possible reasons for missing values include intentional omission, data entry errors, incomplete information from sellers, and even incorrect measurements or equipment errors.\n",
    "\n",
    "-Anomalies like unusually low prices raise concerns about data quality.\n",
    "Effective data cleaning and imputation techniques are crucial to ensure accurate and comprehensive analysis."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step to fill in missing data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "      <th>model_year</th>\n",
       "      <th>model</th>\n",
       "      <th>condition</th>\n",
       "      <th>cylinders</th>\n",
       "      <th>fuel</th>\n",
       "      <th>odometer</th>\n",
       "      <th>transmission</th>\n",
       "      <th>type</th>\n",
       "      <th>paint_color</th>\n",
       "      <th>is_4wd</th>\n",
       "      <th>date_posted</th>\n",
       "      <th>days_listed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>9400</td>\n",
       "      <td>2011.0</td>\n",
       "      <td>bmw x5</td>\n",
       "      <td>good</td>\n",
       "      <td>6.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>145000.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>SUV</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>2018-06-23</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>ford f-150</td>\n",
       "      <td>good</td>\n",
       "      <td>6.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>88705.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>white</td>\n",
       "      <td>1</td>\n",
       "      <td>2018-10-19</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5500</td>\n",
       "      <td>2013.0</td>\n",
       "      <td>hyundai sonata</td>\n",
       "      <td>like new</td>\n",
       "      <td>4.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>110000.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>red</td>\n",
       "      <td>0</td>\n",
       "      <td>2019-02-07</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1500</td>\n",
       "      <td>2003.0</td>\n",
       "      <td>ford f-150</td>\n",
       "      <td>fair</td>\n",
       "      <td>8.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>NaN</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>2019-03-22</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>14900</td>\n",
       "      <td>2017.0</td>\n",
       "      <td>chrysler 200</td>\n",
       "      <td>excellent</td>\n",
       "      <td>4.0</td>\n",
       "      <td>gas</td>\n",
       "      <td>80903.0</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>black</td>\n",
       "      <td>0</td>\n",
       "      <td>2019-04-02</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   price  model_year           model  condition  cylinders fuel  odometer  \\\n",
       "0   9400      2011.0          bmw x5       good        6.0  gas  145000.0   \n",
       "1  25500         NaN      ford f-150       good        6.0  gas   88705.0   \n",
       "2   5500      2013.0  hyundai sonata   like new        4.0  gas  110000.0   \n",
       "3   1500      2003.0      ford f-150       fair        8.0  gas       NaN   \n",
       "4  14900      2017.0    chrysler 200  excellent        4.0  gas   80903.0   \n",
       "\n",
       "  transmission    type paint_color  is_4wd date_posted  days_listed  \n",
       "0    automatic     SUV         NaN       1  2018-06-23           19  \n",
       "1    automatic  pickup       white       1  2018-10-19           50  \n",
       "2    automatic   sedan         red       0  2019-02-07           79  \n",
       "3    automatic  pickup         NaN       0  2019-03-22            9  \n",
       "4    automatic   sedan       black       0  2019-04-02           28  "
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Fill the NaNs in is_4wd column with zeros since the column contains either 1 or 0\n",
    "vehicle_ad_data['is_4wd'].fillna(value= 0.0, inplace=True)\n",
    "vehicle_ad_data['is_4wd'] = vehicle_ad_data['is_4wd'].astype(int)\n",
    "vehicle_ad_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 6.  4.  8. nan  5. 10.  3. 12.]\n"
     ]
    }
   ],
   "source": [
    "#Fill missing value in model_year column with the median of cars of the same model\n",
    "vehicle_ad_data['model_year'].fillna(\n",
    "    vehicle_ad_data.groupby(['model'])['model_year'].transform(np.median), inplace=True\n",
    ")\n",
    "unique_cylinders = vehicle_ad_data['cylinders'].unique()\n",
    "print(unique_cylinders)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "By using the median to fill in missing 'model_year' values, we are choosing a value that is representative of the central tendency of the data. It provides a reasonable estimate for the missing values without being skewed by extreme values which is 'model_year' min value is 1908 and max value 2019 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fill missing values in 'cylinders' based on car model\n",
    "vehicle_ad_data['cylinders'].fillna(\n",
    "    vehicle_ad_data.groupby(['model'])['cylinders'].transform('median'), inplace=True\n",
    ")\n",
    "\n",
    "# Filter out incorrect values with 4 characters\n",
    "vehicle_ad_data = vehicle_ad_data[vehicle_ad_data['cylinders'].astype(str).str.len() < 4]\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The cylinders column represents discrete values, and using the meadian could be appropriate as there no outliers or extreme values that might heavily influence the mean as both mean value of 'cylinders' is 6 which is in reasonable range compare to the min value 3 and max value 12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Filled last missing odometer values of same listing with the mean value \n",
    "vehicle_ad_data['odometer'].fillna((vehicle_ad_data['odometer'].mean()), inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "# change the missing values from 'paint_color' with the most occuring color from mode\n",
    "vehicle_ad_data['paint_color'] = vehicle_ad_data.groupby('model')['paint_color'].transform(lambda x: x.fillna(x.mode().iloc[0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "      <th>model_year</th>\n",
       "      <th>cylinders</th>\n",
       "      <th>odometer</th>\n",
       "      <th>is_4wd</th>\n",
       "      <th>days_listed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>50974.000000</td>\n",
       "      <td>50974.000000</td>\n",
       "      <td>50974.000000</td>\n",
       "      <td>50974.000000</td>\n",
       "      <td>50974.000000</td>\n",
       "      <td>50974.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>12184.917958</td>\n",
       "      <td>2009.763007</td>\n",
       "      <td>6.079060</td>\n",
       "      <td>115980.344653</td>\n",
       "      <td>0.493075</td>\n",
       "      <td>39.549869</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>10029.128146</td>\n",
       "      <td>6.094470</td>\n",
       "      <td>1.616071</td>\n",
       "      <td>59735.258143</td>\n",
       "      <td>0.499957</td>\n",
       "      <td>28.197912</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1908.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>5000.000000</td>\n",
       "      <td>2007.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>80000.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>19.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>9000.000000</td>\n",
       "      <td>2011.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>115980.344653</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>33.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>16838.000000</td>\n",
       "      <td>2014.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>147000.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>53.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>375000.000000</td>\n",
       "      <td>2019.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>990000.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>271.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               price    model_year     cylinders       odometer        is_4wd  \\\n",
       "count   50974.000000  50974.000000  50974.000000   50974.000000  50974.000000   \n",
       "mean    12184.917958   2009.763007      6.079060  115980.344653      0.493075   \n",
       "std     10029.128146      6.094470      1.616071   59735.258143      0.499957   \n",
       "min         1.000000   1908.000000      3.000000       0.000000      0.000000   \n",
       "25%      5000.000000   2007.000000      4.000000   80000.000000      0.000000   \n",
       "50%      9000.000000   2011.000000      6.000000  115980.344653      0.000000   \n",
       "75%     16838.000000   2014.000000      8.000000  147000.000000      1.000000   \n",
       "max    375000.000000   2019.000000      8.000000  990000.000000      1.000000   \n",
       "\n",
       "        days_listed  \n",
       "count  50974.000000  \n",
       "mean      39.549869  \n",
       "std       28.197912  \n",
       "min        0.000000  \n",
       "25%       19.000000  \n",
       "50%       33.000000  \n",
       "75%       53.000000  \n",
       "max      271.000000  "
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vehicle_ad_data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "price           0\n",
      "model_year      0\n",
      "model           0\n",
      "condition       0\n",
      "cylinders       0\n",
      "fuel            0\n",
      "odometer        0\n",
      "transmission    0\n",
      "type            0\n",
      "paint_color     0\n",
      "is_4wd          0\n",
      "date_posted     0\n",
      "days_listed     0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Make sure the table contains no more missing columns\n",
    "missing_counts = vehicle_ad_data.isna().sum()\n",
    "# Display the count of missing values in each column\n",
    "print( missing_counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Process Duplicates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "# counting clear dublicates\n",
    "print(vehicle_ad_data.duplicated().sum()) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The result indicates that there are no obvious duplicates present in the dataset. However, it is possible that there are implicit duplicates where the model names are written differently. Such errors can impact the accuracy of the results obtained from the analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['bmw x5', 'ford f-150', 'hyundai sonata', 'chrysler 200',\n",
       "       'chrysler 300', 'toyota camry', 'honda pilot', 'kia sorento',\n",
       "       'chevrolet silverado 1500', 'honda accord', 'ram 1500',\n",
       "       'gmc yukon', 'jeep cherokee', 'chevrolet traverse',\n",
       "       'hyundai elantra', 'chevrolet tahoe', 'toyota rav4',\n",
       "       'chevrolet silverado', 'jeep wrangler', 'chevrolet malibu',\n",
       "       'ford fusion se', 'chevrolet impala', 'chevrolet corvette',\n",
       "       'jeep liberty', 'toyota camry le', 'nissan altima',\n",
       "       'subaru outback', 'toyota highlander', 'dodge charger',\n",
       "       'toyota tacoma', 'chevrolet equinox', 'nissan rogue',\n",
       "       'mercedes-benz benze sprinter 2500', 'honda cr-v',\n",
       "       'jeep grand cherokee', 'toyota 4runner', 'ford focus',\n",
       "       'honda civic', 'kia soul', 'chevrolet colorado',\n",
       "       'ford f150 supercrew cab xlt', 'chevrolet camaro lt coupe 2d',\n",
       "       'chevrolet cruze', 'ford mustang', 'chevrolet silverado 3500hd',\n",
       "       'nissan frontier crew cab sv', 'subaru impreza',\n",
       "       'jeep grand cherokee laredo', 'nissan versa', 'ford f-250 sd',\n",
       "       'chevrolet silverado 1500 crew', 'ford f250 super duty',\n",
       "       'chevrolet camaro', 'ford mustang gt coupe 2d', 'subaru forester',\n",
       "       'ford explorer', 'ford f-350 sd', 'ford edge', 'nissan maxima',\n",
       "       'ford f-250', 'nissan sentra', 'ford f150', 'chevrolet suburban',\n",
       "       'ford expedition', 'dodge grand caravan', 'ford taurus',\n",
       "       'acura tl', 'ford f350 super duty', 'ford ranger', 'gmc sierra',\n",
       "       'hyundai santa fe', 'ford escape', 'gmc sierra 2500hd',\n",
       "       'honda civic lx', 'gmc sierra 1500', 'honda odyssey',\n",
       "       'cadillac escalade', 'volkswagen jetta', 'toyota corolla',\n",
       "       'chrysler town & country', 'volkswagen passat', 'toyota prius',\n",
       "       'buick enclave', 'ford fusion', 'toyota tundra', 'ram 3500',\n",
       "       'ram 2500', 'nissan frontier', 'chevrolet silverado 2500hd',\n",
       "       'jeep wrangler unlimited', 'ford f-250 super duty', 'gmc acadia',\n",
       "       'toyota sienna', 'ford focus se', 'ford f250', 'dodge dakota',\n",
       "       'ford f350', 'chevrolet trailblazer', 'ford econoline',\n",
       "       'nissan murano'], dtype=object)"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#viewing unique model name\n",
    "vehicle_ad_data['model'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on the 'model' column, we found duplicates for the Ford F-150, Ford F-250 SD, and Ford F-350 SD. The model names ['ford f-150', 'ford f-250 sd', 'ford f-350 sd'] correspond to ['ford f150', 'ford f-250 super duty', 'ford f350 super duty'].\n",
    "To get rid of them, declare the function `replace_wrong_models()` with two parameters: \n",
    "* `wrong_models=` — the list of duplicates\n",
    "* `correct_models=` — the string with the correct value\n",
    "\n",
    "The function should correct the names in the `'model'` column from the `vehicle_ad_data` table.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "# function replace implicit duplicates\n",
    "def replace_wrong_models(wrong_models, correct_models):\n",
    "    # Replace the wrong model names with the correct model names\n",
    "    vehicle_ad_data['model'] = vehicle_ad_data['model'].replace(wrong_models, correct_models)\n",
    "    # Print the updated 'model' column\n",
    "    print(vehicle_ad_data['model'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0                bmw x5\n",
      "1            ford f-150\n",
      "2        hyundai sonata\n",
      "3            ford f-150\n",
      "4          chrysler 200\n",
      "              ...      \n",
      "51520     nissan maxima\n",
      "51521       honda civic\n",
      "51522    hyundai sonata\n",
      "51523    toyota corolla\n",
      "51524     nissan altima\n",
      "Name: model, Length: 50974, dtype: object\n"
     ]
    }
   ],
   "source": [
    "#list of wrong model\n",
    "wrong_models=['ford f150', 'ford f-250 super duty', 'ford f350 super duty']\n",
    "#list of correct model\n",
    "correct_models=['ford f-150', 'ford f-250 sd', 'ford f-350 sd']\n",
    "#call of the function to replace wrong models\n",
    "replace_wrong_models(wrong_models, correct_models)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Last but not least, we prefer to have a unique combinations of 'price', 'model_year', 'model', and 'odometer' values which will eliminate  duplicate data. As duplicate data can be a sign of data quality issues, such as data entry errors or data duplication during merging or importing processes. Identifying and removing duplicates improves the overall quality of the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 40499 entries, 0 to 51524\n",
      "Data columns (total 13 columns):\n",
      " #   Column        Non-Null Count  Dtype  \n",
      "---  ------        --------------  -----  \n",
      " 0   price         40499 non-null  int64  \n",
      " 1   model_year    40499 non-null  float64\n",
      " 2   model         40499 non-null  object \n",
      " 3   condition     40499 non-null  object \n",
      " 4   cylinders     40499 non-null  float64\n",
      " 5   fuel          40499 non-null  object \n",
      " 6   odometer      40499 non-null  float64\n",
      " 7   transmission  40499 non-null  object \n",
      " 8   type          40499 non-null  object \n",
      " 9   paint_color   40499 non-null  object \n",
      " 10  is_4wd        40499 non-null  int32  \n",
      " 11  date_posted   40499 non-null  object \n",
      " 12  days_listed   40499 non-null  int64  \n",
      "dtypes: float64(3), int32(1), int64(2), object(7)\n",
      "memory usage: 4.2+ MB\n"
     ]
    }
   ],
   "source": [
    "#Drop duplicates\n",
    "vehicle_ad_data = vehicle_ad_data.drop_duplicates(subset=['model','price', 'model_year', 'model', 'odometer'])\n",
    "vehicle_ad_data.info()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Data replacement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "price             int64\n",
       "model_year      float64\n",
       "model            object\n",
       "condition        object\n",
       "cylinders       float64\n",
       "fuel             object\n",
       "odometer        float64\n",
       "transmission     object\n",
       "type             object\n",
       "paint_color      object\n",
       "is_4wd            int32\n",
       "date_posted      object\n",
       "days_listed       int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#check data type\n",
    "vehicle_ad_data.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "model_year: The model_year column is currently represented as a float64 data type. To plot a histogram or scatterplot based on the model year, it is generally more appropriate to convert it to an integer data type. This allows for better visualization and interpretation of the data, as model years are typically represented as whole numbers.\n",
    "\n",
    "cylinders: The cylinders column is currently represented as a float64 data type. However, since the number of cylinders in a vehicle is typically a discrete value, it is often more appropriate to convert it to an integer data type for plotting purposes. This ensures that the data is displayed accurately without decimal places.\n",
    "\n",
    "odometer: The odometer column is currently represented as a float64 data type, which indicates a continuous numerical value. To plot a histogram or scatterplot based on the odometer reading, it is common to keep it as a numerical value rather than converting it to a different data type.\n",
    "\n",
    "date_posted: The date_posted column is currently represented as an object data type, which typically indicates a string or generic object. To plot data over time or analyze temporal patterns, it is advisable to convert this column to a datetime data type. This allows for easier manipulation, sorting, and visualization of the dates."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Replaceing data type for model_year category to int\n",
    "vehicle_ad_data['model_year'] = vehicle_ad_data['model_year'].astype(int)\n",
    "#Replaceing data type for cylinders category to int\n",
    "vehicle_ad_data['cylinders'] = vehicle_ad_data['cylinders'].astype(int)\n",
    "#Replaceing data type for odometer category to int\n",
    "vehicle_ad_data['odometer'] = vehicle_ad_data['odometer'].astype(int)\n",
    "#Replacing data type for date_posted into datetime type\n",
    "vehicle_ad_data['date_posted']=pd.to_datetime(vehicle_ad_data['date_posted'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "price                    int64\n",
       "model_year               int32\n",
       "model                   object\n",
       "condition               object\n",
       "cylinders                int32\n",
       "fuel                    object\n",
       "odometer                 int32\n",
       "transmission            object\n",
       "type                    object\n",
       "paint_color             object\n",
       "is_4wd                   int32\n",
       "date_posted     datetime64[ns]\n",
       "days_listed              int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check for data type again\n",
    "#Checking data types\n",
    "vehicle_ad_data.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Make Calculation and Enrich the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 4 1 3 0 5]\n"
     ]
    }
   ],
   "source": [
    "#  Change the condition values with something that can be manipulated more easily\n",
    "vehicle_ad_data.loc[:, 'condition'] = vehicle_ad_data['condition'].replace(\n",
    "    to_replace=['new', 'like new', 'excellent', 'good', 'fair', 'salvage'],\n",
    "    value=[5, 4, 3, 2, 1, 0]\n",
    ")\n",
    "\n",
    "# Check unique values in the 'condition' column\n",
    "unique_conditions = vehicle_ad_data['condition'].unique()\n",
    "print(unique_conditions)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  8,   7,  17,   3,   5,   4,  12,   2,  11,   6,   9,   1,  10,\n",
       "        16,  15,  14,  18,  13,  54,  25,  19,  20,  27,  23,  39,  21,\n",
       "        24,  45,  22,  26,  34,  43,  32,  44,  30,  29,  47,  53,  50,\n",
       "        31,  41,  55,  40,  51,  28,  33,  56,  38,  57,  35,  46,  42,\n",
       "        52,  64,  48,  49,  37,  36,  66,  58,  72,  59,  60, 111,  83,\n",
       "        70,  61,  90], dtype=int64)"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#add the age of the car\n",
    "# first isolate 'year' from 'date_posted' column\n",
    "vehicle_ad_data['year_posted'] = vehicle_ad_data['date_posted'].dt.year\n",
    "# create a function that calculate car age\n",
    "def calculate_car_age(row):\n",
    "    return ((row['year_posted'] - row['model_year'])+1)\n",
    "\n",
    "vehicle_ad_data['Car_Age'] = vehicle_ad_data.apply(calculate_car_age, axis=1)\n",
    "\n",
    "vehicle_ad_data['Car_Age'].unique()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mileage is a crucial factor that can significantly impact the price of a car. Generally, higher mileage tends to lower the price. To calculate the car's mileage, we utilize the following function:\n",
    "\n",
    "vehicle_data['Car_mileage'] = vehicle_data['odometer'] / (vehicle_data['year_posted'] - vehicle_data['model_year'])\n",
    "\n",
    "In this function, we include a \"+1\" to the equation row['year_posted'] - row['model_year']. This addition ensures that we avoid infinite values for 'Car_mileage'. Without this adjustment, if there are 'Car_age' values of 0, the equation would result in division by zero, which is undefined."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 40499 entries, 0 to 51524\n",
      "Data columns (total 16 columns):\n",
      " #   Column        Non-Null Count  Dtype         \n",
      "---  ------        --------------  -----         \n",
      " 0   price         40499 non-null  int64         \n",
      " 1   model_year    40499 non-null  int32         \n",
      " 2   model         40499 non-null  object        \n",
      " 3   condition     40499 non-null  int64         \n",
      " 4   cylinders     40499 non-null  int32         \n",
      " 5   fuel          40499 non-null  object        \n",
      " 6   odometer      40499 non-null  int32         \n",
      " 7   transmission  40499 non-null  object        \n",
      " 8   type          40499 non-null  object        \n",
      " 9   paint_color   40499 non-null  object        \n",
      " 10  is_4wd        40499 non-null  int32         \n",
      " 11  date_posted   40499 non-null  datetime64[ns]\n",
      " 12  days_listed   40499 non-null  int64         \n",
      " 13  year_posted   40499 non-null  int64         \n",
      " 14  Car_Age       40499 non-null  int64         \n",
      " 15  Car_mileage   40499 non-null  float64       \n",
      "dtypes: datetime64[ns](1), float64(1), int32(4), int64(5), object(5)\n",
      "memory usage: 4.6+ MB\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([6, 4, 8, 5, 3])"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Add 'Car_mileage' and handle non-finite values\n",
    "vehicle_ad_data['Car_mileage'] = vehicle_ad_data['odometer'] / ((vehicle_ad_data['year_posted'] - vehicle_ad_data['model_year'])+1)\n",
    "vehicle_ad_data['Car_mileage'].replace([np.inf, -np.inf], np.nan, inplace=True)\n",
    "\n",
    "# Round 'Car_mileage' to remove decimal places\n",
    "vehicle_ad_data['Car_mileage'] = vehicle_ad_data['Car_mileage'].round()\n",
    "\n",
    "# Check the data type of 'Car_mileage'\n",
    "vehicle_ad_data['Car_mileage'].dtypes\n",
    "#Verify new columns\n",
    "vehicle_ad_data.head()\n",
    "vehicle_ad_data.info()\n",
    "vehicle_ad_data['cylinders'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exploratory data analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After informing your boss about completing the data cleaning process, your manager promptly provides you with specific parameters to prioritize. These parameters include: \n",
    "\n",
    "-price \n",
    "\n",
    "-Car_Age \n",
    "\n",
    "-Car_mileage \n",
    "\n",
    "-cylinders\n",
    "\n",
    "-Conditions\n",
    " \n",
    "To ensure a focused analysis, your manager suggests eliminating any outliers from the dataset. Additionally, your manager advises narrowing the analysis to only the two or three most frequently advertised types of vehicles on the website. By narrowing the focus to these specific types, you can obtain valuable insights and make informed decisions based on the most prevalent and relevant vehicles in your dataset. This targeted approach will enable you to extract meaningful patterns and trends from the data, leading to more accurate and actionable conclusions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Header\n",
    "st.header(\"Data Distribution\")\n",
    "\n",
    "# Histogram for Price\n",
    "st.subheader(\"Price Distribution\")\n",
    "fig_price = px.histogram(vehicle_ad_data, x='price')\n",
    "st.plotly_chart(fig_price)\n",
    "\n",
    "# Histogram for Car Age\n",
    "st.subheader(\"Car Age Distribution\")\n",
    "fig_car_age = px.histogram(vehicle_ad_data, x='Car_Age')\n",
    "st.plotly_chart(fig_car_age)\n",
    "\n",
    "# Histogram for Car Mileage\n",
    "st.subheader(\"Car Mileage Distribution\")\n",
    "fig_car_mileage = px.histogram(vehicle_ad_data, x='Car_mileage')\n",
    "st.plotly_chart(fig_car_mileage)\n",
    "\n",
    "# Scatter Plot for Price and Car Age\n",
    "st.subheader(\"Scatter Plot: Price vs Car Age\")\n",
    "fig_scatter = px.scatter(vehicle_ad_data, x='Car_Age', y='price')\n",
    "st.plotly_chart(fig_scatter)\n",
    "\n",
    "# Checkbox to toggle between histograms and scatter plot\n",
    "show_scatter = st.checkbox(\"Show Scatter Plot\")\n",
    "\n",
    "if show_scatter:\n",
    "    st.plotly_chart(fig_scatter)\n",
    "else:\n",
    "    st.plotly_chart(fig_price)\n",
    "    st.plotly_chart(fig_car_age)\n",
    "    st.plotly_chart(fig_car_mileage)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The last two variables:condition,cylinders are categorical, meaning they have a limited number of distinct values. Therefore, there is no need to make any changes to their data range. However, the first three variables, price, Car_Age, and Car_mileage, follow a Poisson distribution. This distribution reveals an interesting pattern in the data. Initially, the counts are relatively small, but they rapidly increase until reaching a peak in the first tenth area. Afterward, the counts gradually diminish.\n",
    "\n",
    "To further analyze these variables, we can create boxplot distributions for price, Car_Age, and Car_mileage. The boxplot provides visual insights into the distribution of these variables, including measures of central tendency, dispersion, and potential outliers. By examining the boxplots, we can gain a better understanding of the overall range and distribution of these variables in our dataset.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Header\n",
    "st.header(\"Boxplots\")\n",
    "# Boxplot for Price\n",
    "st.subheader(\"Price Boxplot\")\n",
    "fig_price = px.box(vehicle_ad_data, x='price')\n",
    "st.plotly_chart(fig_price)\n",
    "\n",
    "# Boxplot for Car Age\n",
    "st.subheader(\"Car Age Boxplot\")\n",
    "fig_car_age = px.box(vehicle_ad_data, x='Car_Age')\n",
    "st.plotly_chart(fig_car_age)\n",
    "\n",
    "# Boxplot for Car Mileage\n",
    "st.subheader(\"Car Mileage Boxplot\")\n",
    "fig_car_mileage = px.box(vehicle_ad_data, x='Car_mileage')\n",
    "st.plotly_chart(fig_car_mileage)\n",
    "\n",
    "# Checkbox to toggle between boxplots\n",
    "show_car_age = st.checkbox(\"Show Car Age Boxplot\")\n",
    "show_car_mileage = st.checkbox(\"Show Car Mileage Boxplot\")\n",
    "\n",
    "if show_car_age:\n",
    "    st.plotly_chart(fig_car_age)\n",
    "\n",
    "if show_car_mileage:\n",
    "    st.plotly_chart(fig_car_mileage)\n",
    "\n",
    "# Default: Show Price Boxplot\n",
    "st.plotly_chart(fig_price)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Car_mileage has a lot of outliers to be removed.Let removed them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_outlier(dataframe, col):\n",
    "    # Calculate the quantiles\n",
    "    lower_quantile = dataframe[col].quantile(0.05)\n",
    "    upper_quantile = dataframe[col].quantile(0.95)\n",
    "    \n",
    "    # Create new column\n",
    "    new_col = col + '_clean'\n",
    "    dataframe[new_col] = dataframe[col].copy()\n",
    "    \n",
    "    # Remove outliers\n",
    "    dataframe.loc[(dataframe[new_col] > upper_quantile) | (dataframe[new_col] < lower_quantile), col] = None\n",
    "    \n",
    "    return dataframe\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "      <th>model_year</th>\n",
       "      <th>model</th>\n",
       "      <th>condition</th>\n",
       "      <th>cylinders</th>\n",
       "      <th>fuel</th>\n",
       "      <th>odometer</th>\n",
       "      <th>transmission</th>\n",
       "      <th>type</th>\n",
       "      <th>paint_color</th>\n",
       "      <th>is_4wd</th>\n",
       "      <th>date_posted</th>\n",
       "      <th>days_listed</th>\n",
       "      <th>year_posted</th>\n",
       "      <th>Car_Age</th>\n",
       "      <th>Car_mileage</th>\n",
       "      <th>price_clean</th>\n",
       "      <th>Car_mileage_clean</th>\n",
       "      <th>Car_Age_clean</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>9400.0</td>\n",
       "      <td>2011</td>\n",
       "      <td>bmw x5</td>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>gas</td>\n",
       "      <td>145000</td>\n",
       "      <td>automatic</td>\n",
       "      <td>SUV</td>\n",
       "      <td>black</td>\n",
       "      <td>1</td>\n",
       "      <td>2018-06-23</td>\n",
       "      <td>19</td>\n",
       "      <td>2018</td>\n",
       "      <td>8.0</td>\n",
       "      <td>18125.0</td>\n",
       "      <td>9400</td>\n",
       "      <td>18125.0</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25500.0</td>\n",
       "      <td>2011</td>\n",
       "      <td>ford f-150</td>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>gas</td>\n",
       "      <td>88705</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>white</td>\n",
       "      <td>1</td>\n",
       "      <td>2018-10-19</td>\n",
       "      <td>50</td>\n",
       "      <td>2018</td>\n",
       "      <td>8.0</td>\n",
       "      <td>11088.0</td>\n",
       "      <td>25500</td>\n",
       "      <td>11088.0</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5500.0</td>\n",
       "      <td>2013</td>\n",
       "      <td>hyundai sonata</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>gas</td>\n",
       "      <td>110000</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>red</td>\n",
       "      <td>0</td>\n",
       "      <td>2019-02-07</td>\n",
       "      <td>79</td>\n",
       "      <td>2019</td>\n",
       "      <td>7.0</td>\n",
       "      <td>15714.0</td>\n",
       "      <td>5500</td>\n",
       "      <td>15714.0</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2003</td>\n",
       "      <td>ford f-150</td>\n",
       "      <td>1</td>\n",
       "      <td>8</td>\n",
       "      <td>gas</td>\n",
       "      <td>115980</td>\n",
       "      <td>automatic</td>\n",
       "      <td>pickup</td>\n",
       "      <td>white</td>\n",
       "      <td>0</td>\n",
       "      <td>2019-03-22</td>\n",
       "      <td>9</td>\n",
       "      <td>2019</td>\n",
       "      <td>17.0</td>\n",
       "      <td>6822.0</td>\n",
       "      <td>1500</td>\n",
       "      <td>6822.0</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>14900.0</td>\n",
       "      <td>2017</td>\n",
       "      <td>chrysler 200</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>gas</td>\n",
       "      <td>80903</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>black</td>\n",
       "      <td>0</td>\n",
       "      <td>2019-04-02</td>\n",
       "      <td>28</td>\n",
       "      <td>2019</td>\n",
       "      <td>3.0</td>\n",
       "      <td>26968.0</td>\n",
       "      <td>14900</td>\n",
       "      <td>26968.0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51520</th>\n",
       "      <td>9249.0</td>\n",
       "      <td>2013</td>\n",
       "      <td>nissan maxima</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>gas</td>\n",
       "      <td>88136</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>black</td>\n",
       "      <td>0</td>\n",
       "      <td>2018-10-03</td>\n",
       "      <td>37</td>\n",
       "      <td>2018</td>\n",
       "      <td>6.0</td>\n",
       "      <td>14689.0</td>\n",
       "      <td>9249</td>\n",
       "      <td>14689.0</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51521</th>\n",
       "      <td>2700.0</td>\n",
       "      <td>2002</td>\n",
       "      <td>honda civic</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>gas</td>\n",
       "      <td>181500</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>white</td>\n",
       "      <td>0</td>\n",
       "      <td>2018-11-14</td>\n",
       "      <td>22</td>\n",
       "      <td>2018</td>\n",
       "      <td>17.0</td>\n",
       "      <td>10676.0</td>\n",
       "      <td>2700</td>\n",
       "      <td>10676.0</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51522</th>\n",
       "      <td>3950.0</td>\n",
       "      <td>2009</td>\n",
       "      <td>hyundai sonata</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>gas</td>\n",
       "      <td>128000</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>blue</td>\n",
       "      <td>0</td>\n",
       "      <td>2018-11-15</td>\n",
       "      <td>32</td>\n",
       "      <td>2018</td>\n",
       "      <td>10.0</td>\n",
       "      <td>12800.0</td>\n",
       "      <td>3950</td>\n",
       "      <td>12800.0</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51523</th>\n",
       "      <td>7455.0</td>\n",
       "      <td>2013</td>\n",
       "      <td>toyota corolla</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>gas</td>\n",
       "      <td>139573</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>black</td>\n",
       "      <td>0</td>\n",
       "      <td>2018-07-02</td>\n",
       "      <td>71</td>\n",
       "      <td>2018</td>\n",
       "      <td>6.0</td>\n",
       "      <td>23262.0</td>\n",
       "      <td>7455</td>\n",
       "      <td>23262.0</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51524</th>\n",
       "      <td>6300.0</td>\n",
       "      <td>2014</td>\n",
       "      <td>nissan altima</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>gas</td>\n",
       "      <td>115980</td>\n",
       "      <td>automatic</td>\n",
       "      <td>sedan</td>\n",
       "      <td>grey</td>\n",
       "      <td>0</td>\n",
       "      <td>2018-06-05</td>\n",
       "      <td>10</td>\n",
       "      <td>2018</td>\n",
       "      <td>5.0</td>\n",
       "      <td>23196.0</td>\n",
       "      <td>6300</td>\n",
       "      <td>23196.0</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>40499 rows × 19 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         price  model_year           model  condition  cylinders fuel  \\\n",
       "0       9400.0        2011          bmw x5          2          6  gas   \n",
       "1      25500.0        2011      ford f-150          2          6  gas   \n",
       "2       5500.0        2013  hyundai sonata          4          4  gas   \n",
       "3          NaN        2003      ford f-150          1          8  gas   \n",
       "4      14900.0        2017    chrysler 200          3          4  gas   \n",
       "...        ...         ...             ...        ...        ...  ...   \n",
       "51520   9249.0        2013   nissan maxima          4          6  gas   \n",
       "51521   2700.0        2002     honda civic          0          4  gas   \n",
       "51522   3950.0        2009  hyundai sonata          3          4  gas   \n",
       "51523   7455.0        2013  toyota corolla          2          4  gas   \n",
       "51524   6300.0        2014   nissan altima          2          4  gas   \n",
       "\n",
       "       odometer transmission    type paint_color  is_4wd date_posted  \\\n",
       "0        145000    automatic     SUV       black       1  2018-06-23   \n",
       "1         88705    automatic  pickup       white       1  2018-10-19   \n",
       "2        110000    automatic   sedan         red       0  2019-02-07   \n",
       "3        115980    automatic  pickup       white       0  2019-03-22   \n",
       "4         80903    automatic   sedan       black       0  2019-04-02   \n",
       "...         ...          ...     ...         ...     ...         ...   \n",
       "51520     88136    automatic   sedan       black       0  2018-10-03   \n",
       "51521    181500    automatic   sedan       white       0  2018-11-14   \n",
       "51522    128000    automatic   sedan        blue       0  2018-11-15   \n",
       "51523    139573    automatic   sedan       black       0  2018-07-02   \n",
       "51524    115980    automatic   sedan        grey       0  2018-06-05   \n",
       "\n",
       "       days_listed  year_posted  Car_Age  Car_mileage  price_clean  \\\n",
       "0               19         2018      8.0      18125.0         9400   \n",
       "1               50         2018      8.0      11088.0        25500   \n",
       "2               79         2019      7.0      15714.0         5500   \n",
       "3                9         2019     17.0       6822.0         1500   \n",
       "4               28         2019      3.0      26968.0        14900   \n",
       "...            ...          ...      ...          ...          ...   \n",
       "51520           37         2018      6.0      14689.0         9249   \n",
       "51521           22         2018     17.0      10676.0         2700   \n",
       "51522           32         2018     10.0      12800.0         3950   \n",
       "51523           71         2018      6.0      23262.0         7455   \n",
       "51524           10         2018      5.0      23196.0         6300   \n",
       "\n",
       "       Car_mileage_clean  Car_Age_clean  \n",
       "0                18125.0              8  \n",
       "1                11088.0              8  \n",
       "2                15714.0              7  \n",
       "3                 6822.0             17  \n",
       "4                26968.0              3  \n",
       "...                  ...            ...  \n",
       "51520            14689.0              6  \n",
       "51521            10676.0             17  \n",
       "51522            12800.0             10  \n",
       "51523            23262.0              6  \n",
       "51524            23196.0              5  \n",
       "\n",
       "[40499 rows x 19 columns]"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#call the clean_outlier function\n",
    "clean_outlier(vehicle_ad_data, 'price')\n",
    "clean_outlier(vehicle_ad_data, 'Car_mileage')\n",
    "clean_outlier(vehicle_ad_data, 'Car_Age')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Header\n",
    "st.header(\"Histograms\")\n",
    "\n",
    "#Histogram for Price\n",
    "st.subheader(\"Price Histogram\")\n",
    "fig_price = px.histogram(vehicle_ad_data, x='price_clean')\n",
    "st.plotly_chart(fig_price)\n",
    "\n",
    "# Histogram for Car Age\n",
    "st.subheader(\"Car Age Histogram\")\n",
    "fig_car_age = px.histogram(vehicle_ad_data, x='Car_Age_clean')\n",
    "st.plotly_chart(fig_car_age)\n",
    "\n",
    "# Histogram for Car Mileage\n",
    "st.subheader(\"Car Mileage Histogram\")\n",
    "fig_car_mileage = px.histogram(vehicle_ad_data, x='Car_mileage_clean')\n",
    "st.plotly_chart(fig_car_mileage)\n",
    "\n",
    "# Checkbox to toggle between histograms\n",
    "show_car_age = st.checkbox(\"Show Car Age Histogram\")\n",
    "show_car_mileage = st.checkbox(\"Show Car Mileage Histogram\")\n",
    "\n",
    "if show_car_age:\n",
    "    st.plotly_chart(fig_car_age)\n",
    "\n",
    "if show_car_mileage:\n",
    "    st.plotly_chart(fig_car_mileage)\n",
    "\n",
    "# Default: Show Price Histogram\n",
    "st.plotly_chart(fig_price)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After removing the outliers, our data distribution appears to be more refined and cleaner."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Unraveling the Top Car Prices"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First, let's examine the type of vehicle that has the highest average price."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "st.header(\"Average Price per Vehicle Type\")\n",
    "type_grouped = vehicle_ad_data.pivot_table(index='type', values='price', aggfunc='mean')\n",
    "show_histogram = st.checkbox(\"Show Histogram\")\n",
    "\n",
    "# Define fig_bar outside the if-else statement\n",
    "fig_bar = px.bar(type_grouped, x=type_grouped.index, y='price')\n",
    "\n",
    "if show_histogram:\n",
    "    # Histogram for price\n",
    "    st.subheader(\"Histogram: Price Distribution\")\n",
    "    fig_hist = px.histogram(vehicle_ad_data, x='price')\n",
    "    st.plotly_chart(fig_hist)\n",
    "else:\n",
    "    st.plotly_chart(fig_bar)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "Based on the given information, we can draw the following analytic conclusions:\n",
    "\n",
    "Bus and mini-vans are the next most expensive types of vehicles. This can be attributed to their larger size and popularity among consumers.\n",
    "\n",
    "The average prices of the first 10 car types after SUVs are quite similar, with only small differences between them. This suggests that these car types offer similar features and specifications, resulting in comparable average prices.\n",
    "\n",
    "Other car types, such as buses, coupes, hatchbacks, off-road vehicles, pickups, sedans, trucks, vans, and wagons, fall within a similar price range, with some variations based on their specific features and market demand\n",
    "\n",
    "Next, we will create a plot and identify the two types with the greatest number of ads in order to identify which type is the most popular."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "st.header(\"Number of Ads per Vehicle Type\")\n",
    "type_grouped = vehicle_ad_data.groupby('type').agg(count=('price', 'count'), mean=('price', 'mean'))\n",
    "\n",
    "\n",
    "st.subheader(\"Bar Graph: Number of Ads per Vehicle Type\")\n",
    "fig_bar = px.bar(type_grouped, x=type_grouped.index, y='count')\n",
    "st.plotly_chart(fig_bar)\n",
    "\n",
    "\n",
    "show_average_price = st.checkbox(\"Show Average Price\")\n",
    "\n",
    "if show_average_price:\n",
    "    # Bar graph for average price per vehicle type\n",
    "    st.subheader(\"Bar Graph: Average Price per Vehicle Type\")\n",
    "    fig_price = px.bar(type_grouped, x=type_grouped.index, y='mean')\n",
    "    st.plotly_chart(fig_price)\n",
    "else:\n",
    "    st.plotly_chart(fig_bar)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on the table, we can draw the following analytical conclusions:\n",
    "\n",
    "From the provided table, we can observe the number of ads for each vehicle type. The top two types with the highest number of ads are \"sedan\" with 10,228 ads and \"SUV\" with 10,065 ads. These two types seem to be the most popular choices among advertisers.\n",
    "\n",
    "Following sedan and SUV, we have \"truck\" with 8,971 ads and \"pickup\" with 5,483 ads, indicating a significant presence in the market.\n",
    "\n",
    "Other vehicle types such as \"coupe,\" \"mini-van,\" \"wagon,\" \"hatchback,\" \"van,\" \"convertible,\" \"other,\" \"offroad,\" and \"bus\" have relatively lower numbers of ads, ranging from 5 to 1,594. These types may have a comparatively smaller market share or may be less frequently advertised."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Unraveling Price Factors"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the bar plot above, we observe that 'SUV' and 'Sedan' are the two most popular types of vehicles in the given data set. To further analyze these vehicle types, we can subset our data frame to focus specifically on these two categories. By narrowing our analysis, we can gain more insights into the characteristics, pricing trends, and other relevant factors related to SUVs and sedans."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type_grouped = vehicle_ad_data.pivot_table(index='type', values='price', aggfunc='mean')\n",
    "\n",
    "#Header\n",
    "st.header(\"Average Price per Vehicle Type\")\n",
    "\n",
    "#Bar graph for average price per vehicle type\n",
    "fig_bar = px.bar(type_grouped, x=type_grouped.index, y='price')\n",
    "st.plotly_chart(fig_bar)\n",
    "\n",
    "#Subset data for SUV and sedan\n",
    "popular_vehicle = vehicle_ad_data[vehicle_ad_data['type'].isin(['SUV', 'sedan'])]\n",
    "\n",
    "#Scatter plot for SUV and sedan with link between price and condition\n",
    "fig_scatter = px.scatter(popular_vehicle, x='condition', y='price')\n",
    "st.plotly_chart(fig_scatter)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on the scatter plot, we observe a distinct relationship between the Price and Condition variables. The data points indicate that vehicles in the 'excellent' condition (labeled as 3) tend to have the highest prices, followed by vehicles in 'good' condition (labeled as 2), and then those in 'fair' condition (labeled as 1). This trend aligns with the distribution of the number of ads, where the majority of vehicles fall into these three condition categories. Therefore, it can be concluded that vehicles in excellent condition not only command higher prices but are also more popular among buyers."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will analyze the relationship between Mileage comparable to price of the vehicle."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "#scatter plot between price and age\n",
    "st.header(\"Relationship between Price and Age of a Vehicle\")\n",
    "show_scatter = st.checkbox(\"Show Scatter Plot\")\n",
    "\n",
    "if show_scatter:\n",
    "# Scatter plot for price and age\n",
    "    st.subheader(\"Scatter Plot: Price vs Age\")\n",
    "    fig_scatter = px.scatter(vehicle_ad_data, x='Car_Age_clean', y='price')\n",
    "    st.plotly_chart(fig_scatter)\n",
    "else:\n",
    "# Histogram for price\n",
    "    st.subheader(\"Histogram: Price Distribution\")\n",
    "    fig_hist = px.histogram(vehicle_ad_data, x='price')\n",
    "    st.plotly_chart(fig_hist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on the graph, we can draw the conclusion that there is a higher concentration of data points for newer cars, indicating that most customers prefer vehicles with an age ranging from 0 to 20 years. As the car age increases beyond 20 years, the distribution of data points becomes less dense, suggesting a decrease in customer preference for older vehicles. This trend aligns with the general expectation that newer cars are more desirable due to factors such as updated features, improved technology, and reduced wear and tear.\n",
    "Next, we will analyze how mileage affect the price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "st.header(\"Relationship between Price and Mileage of a Vehicle\")\n",
    "show_scatter = st.checkbox(\"Show Scatter Plot\")\n",
    "\n",
    "if show_scatter:\n",
    "# Scatter plot for mileage and price\n",
    "    st.subheader(\"Scatter Plot: Mileage vs Price\")\n",
    "    fig_scatter = px.scatter(vehicle_ad_data, x='Car_mileage_clean', y='price_clean')\n",
    "    st.plotly_chart(fig_scatter)\n",
    "else:\n",
    "# Histogram for price\n",
    "    st.subheader(\"Histogram: Price Distribution\")\n",
    "    fig_hist = px.histogram(vehicle_ad_data, x='price_clean')\n",
    "    st.plotly_chart(fig_hist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The scatter plot reveals an interesting pattern between car mileage and value. As mileage increases, there is a noticeable decrease in the distribution of data points for both SUVs and sedans. This suggests that higher mileage tends to be associated with lower car values in these vehicle types.\n",
    "\n",
    "Furthermore, the scatter plot highlights that the majority of data points are concentrated within the range of 0 to 25,000 in terms of car mileage. This indicates that vehicles with lower mileage tend to have a higher distribution, implying that they are more commonly advertised and sought after by potential buyers."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The data distribution of sedans and SUVs reveals that the most popular choices among consumers are vehicles with 4, 6, and 8 cylinders. These cylinder configurations seem to dominate the market, indicating a higher demand for vehicles with these engine types.\n",
    "\n",
    "One of the main reasons for this is that they offer a good balance between power and fuel efficiency. They provide sufficient power for everyday driving needs while still maintaining reasonable fuel economy.\n",
    "\n",
    "On the other hand, there is relatively low distribution for sedans and SUVs with 3 and 5 cylinders. This suggests that vehicles with these cylinder configurations are less common or less preferred among buyers in the dataset."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
