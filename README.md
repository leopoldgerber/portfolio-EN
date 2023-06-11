# Leopold Gerber - Data Analyst | Data Scientist Portfolio
## About
Hello, I'm Leopold Gerber - but you can call me Leo - and I am a Data Analyst/Data Scientist.

As a data analyst, I've faced many tasks, ranging from generating queries for uploading target groups and automating reports, to creating scripts for competitor analysis and models that calculate the risks of domestic currency conversion.

My portfolio includes work projects and competition projects. 
I created this repository to showcase my hard skills and track my progress in Data Analytics / Data Science.

</br>

# Content Table
- [1 - Marketing Web Scraping](#1---marketing-web-scraping) (Scraping, EDA, Power BI)
- [2 - Car Price Predict](#2---car-price-predict) (EDA, Feature Engineering, Machine Learning)
- [3 - Report Automation](#3---report-automation) (MySQL, Python)
- [4 - Sales Management](#4---sales-management) (SQL, EDA, Plotly Dash)
- [5 - Recommendation System](#5---recommendation-system) (EDA, Feature Engineering, Machine Learning, Python)

</br>

# Portfolio Projects
## 1 - Marketing Web Scraping 
<code>[Script](1%20-%20Marketing%20Web%20Scraping/Marketing%20Web%20Scraping.py)</code>
<code>[Dashboard](1%20-%20Marketing%20Web%20Scraping/Marketing%20Web%20Scraping%20Power%20BI%20Demo.pbix)</code>

### - Description - 
Parser script that collects data from Semrush platform without using API (banned at no additional cost). Prescribed script running chrome driver, authorization on the site and parsing all necessary reports (total number of single reports ~ 22 000), internal loops for entered months, fixing domains and month with empty reports, data processing and feature engineering (countries, companies and dates), collecting all reports by category (total number of collected reports - 5). Creation of dashboard for visualization of received data.

### - Results - 
Automated collection of reports.  Visualized data - Dashboards. Thanks to parsing of historical data we managed to save on platform fees (monthly expenses for plan + tax and Traffic Analytics API + tax).

### - Skills -
data parser, data cleaning, feature engineering, data visualization

### - Technology -
Python, Pandas, Numpy, Selenium, Power BI

</br>

[Scroll up](#content-table)

</br>

## 2 - Car Price Predict
<code>[Notebook](2%20-%20Project%20Car%20Price%20Predict/Project%20Car%20Price%20Predict.ipynb)</code>

### - Description - 
The poject contains three datasets: a natural dataset that has been filled since 2014, a parsed dataset from 2019 and a test dataset from 2021. The total number of records is 254265. All three datasets have different values within the attributes/columns (according to the test dataset the columns count ~ 27). The project includes the following steps: import necessary libraries, defining the main functions, data loading, data cleaning and preprocessing, filling missing values, EDA (exploratory data analysis), analyzing the statistical significance (One-Way Anova), hypothesis testing (F-critical, T-critical and p-value - three methods included), measuring statistical factors, finding outliers, feature engineering, data visualization, testing five ML models with MAPE. Participation in the kaggle competition.

### - Skills - 
data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.

### - Technology - 
Python, Pandas, Numpy, Scipy Stats, Seaborn, Matplotlib, Statsmodels, Sklearn, CatBoost, RandomForestRegressor, ExtraTreesRegressor, XGBRegressor, StackingRegressor.

### - Results -
A predictive model has been created, the speed of processing requests has increased - resulting in increased profits.

</br>

[Scroll up](#content-table)

</br>

## 3 - Report Automation
<code>[V7001 (Py)](3%20-%20Report%20Automation%20Script/V7001.py)</code>
<code>[V7002 (Py)](3%20-%20Report%20Automation%20Script/V7002.py)</code>
<code>[V7003 (Py)](3%20-%20Report%20Automation%20Script/V7003.py)</code>
<code>[V7004 (Py)](3%20-%20Report%20Automation%20Script/V7004.py)</code>
<code>[V7001 (SQL)](3%20-%20Report%20Automation%20Script/v7001_sql.sql)</code>
<code>[V7003 (SQL)](3%20-%20Report%20Automation%20Script/v7003_sql.sql)</code>

### - Description - 
A family of scripts for automating reports on closed and open trades, deposits and withdrawals, and hedge fund information for a national bank. A bot for sending reports to everyone assigned.

### - Skills - 
SQL Query, report automation.

### - Technology - 
Python, Pandas, Numpy, mysql.connector, openpyxl, MySQL.

### - Results -
Creation of a script to automate reporting.

</br>

[Scroll up](#content-table)

</br>

### 4 - Sales Management
<code>[Notebook](4%20-%20Sales%20Management/Sales%20Management.ipynb)</code>
<code>[PlotlyDash (Files)](4%20-%20Sales%20Management/Plotly%20Dash/index.py)</code>
<code>[Power BI](4%20-%20Sales%20Management/Sales%20Management%20Dashboard.pbix)</code>

### - Description - 
The project includes 4 datasets with the total number of rows 78 354 (customers, sales, products, calendar). Datasets contain information about online purchases, customers and product. Thanks to this we can find out the age of the target audience, the demand for products by customer, the local demand for product and much more. Two types of data visualization (dashboards) were created for convenience: in Power BI and HerokuApp.

### - Skills - 
data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.

### - Technology - 
SQL (SSMS, clearing tables), Python (data preprocessing, data preparation for the dashboard, pandas, numpy, seaborn, itertools, matplotlib, dash, plotly.express), Jupyter Lab (creating the plotly dash app)
Power BI (Creating an interactive dashboard), Heroku (Upload the Plotly Dash App)

### - Results - 
Knowing the key selling locations of products and their category, it is possible to properly place the products in warehouses. This optimizes logistics (products are not wasted in warehouses), reduces the cost of transporting products here and there, and the advantage over competitors (speed of delivery increases).

### - EDA (short) -
- The data has been processed and cleared of unnecessary columns
- The percentage of missing information was also checked.
- Empty values have been partially restored. But some of the empty values had to be removed due to the lack of information on the prodcuts. Attempts were made to search for the same product by name, product id and categories.
- Some of the empty values in the product value column were restored by finding the average value found using the general category and subcategory of similar products.
- Datasets were combined with each other through special id keys
- The analysis revealed the age of the target audience.
- Cities with the highest demand are identified.
- Identified products with the maximum demand for the general indicators and in each subcategory separately.
- Create an interactive dashboard as an app and in Power BI

</br>

[Scroll up](#content-table)

</br>

### 5 - Recommendation System
<code>[Notebook 1: Analysis & Preprocessing](5%20-%20Recommendation%20System/1%20-%20Analysis%20&%20Preprocessing.ipynb)</code> <code>[Notebook 2: ML Models](5%20-%20Recommendation%20System/2%20-%20ML%20Models.ipynb)</code>

### - Description - 
The goal of the task is to increase profits (by 20%) by selling additional products on the online store platform. The available files include a dataset with historical events on the platform, hashed product property data and a category tree. To solve the problem the data were analyzed, processed and prepared for ML models. Six models were involved in the experiments.

### - Skills - 
data cleaning, data analysis, descriptive statistics, data visualization, feature engineering, machine learning, web-service, docker container

### - Technology - 
Python (data preprocessing, data preparation, feature engineering, ML models testing, pandas, numpy, matplotlib), Flask (web-service), Docker (containerization)

### - Results - 
Using technical metrics (MAP@K and RMSE), a model was selected for recommendations, and a cold start strategy was created. The model was wrapped in a web service and containerized. The map metric showed a result of 33%. The task is completed.

</br>

[Scroll up](#content-table)
