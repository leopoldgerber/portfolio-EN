# Leopold Gerber - Data Analyst | Data Scientist Portfolio
## About
Hello, I'm Leopold Gerber - but you can call me Leo - and I am a Junior Data Analyst.

As an analyst, I've encountered all kinds of tasks, from unloading target groups and automating reports, all the way to full-fledged scripting, taking cost savings into account for the company. 

In addition to working cases, in my portfolio you can find competitive projects on Kaggle, as well as training projects from data analysis courses.
I created this repository to showcase my hard skills and track my progress in Data Analytics / Data Science.

# Content Table
- [1 - Marketing Web Scraping](#marketing-web-scraping) (Scraping, EDA, Power BI)
- [2 - Car Price Predict](#2-car-price-predict) (EDA, Feature Engineering, Machine Learning)
- [3 - Report Automation](#report-automation) (MySQL, Python)
- [4 - Sales Management](#sales-management) (SQL, EDA, Plotly Dash)

# Portfolio Projects
### 1- Marketing Web Scraping 
<code>[Script](1%20-%20Marketing%20Web%20Scraping/Marketing%20Web%20Scraping.py)</code>
<code>[Dashboard](1%20-%20Marketing%20Web%20Scraping/Marketing%20Web%20Scraping%20Power%20BI%20Demo.pbix)</code>
<br>
<ins>**Description:**</ins> Parser script that collects data from Semrush platform without using API (banned at no additional cost). Prescribed script running chrome driver, authorization on the site and parsing all necessary reports (total number of single reports ~ 22 000), internal loops for entered months, fixing domains and month with empty reports, data processing and feature engineering (countries, companies and dates), collecting all reports by category (total number of collected reports - 5). 
Creation of dashboard for visualization of received data.
<br>
<ins>**Skills:**</ins> data parser, data cleaning, feature engineering, data visualization.
<br>
<ins>**Technology:**</ins> Python, Pandas, Numpy, Selenium, Power BI.
<br>
<ins>**Results:**</ins> Automated collection of reports.  Visualized data - Dashboards. Thanks to parsing of historical data we managed to save on platform fees (monthly expenses for plan + tax and Traffic Analytics API + tax).

### 2 - Car Price Predict
<code>[Notebook](Project%20Car%20Price%20Predict.ipynb)</code>
<br>
<ins>**Description:**</ins> The poject contains three datasets: a natural dataset that has been filled since 2014, a parsed dataset from 2019 and a test dataset from 2021. The total number of records is 254265. All three datasets have different values within the attributes/columns (according to the test dataset the columns count ~ 27). The project includes the following steps: import necessary libraries, defining the main functions, data loading, data cleaning and preprocessing, filling missing values, EDA (exploratory data analysis), analyzing the statistical significance (One-Way Anova), hypothesis testing (F-critical, T-critical and p-value - three methods included), measuring statistical factors, finding outliers, feature engineering, data visualization, testing five ML models with MAPE. Participation in the kaggle competition.
<br>
<ins>**Skills:**</ins> data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.
<br>
<ins>**Technology:**</ins> Python, Pandas, Numpy, Scipy Stats, Seaborn, Matplotlib, Statsmodels, Sklearn, CatBoost, RandomForestRegressor, ExtraTreesRegressor, XGBRegressor, StackingRegressor.
<br>
<ins>**Results:**</ins> A predictive model has been created, the speed of processing requests has increased - resulting in increased profits.

### 3 - Report Automation
<code>[Script](Report%20Automation%20Script.py)</code>
<br>
<ins>**Description:**</ins> The National Bank issued a new decree on the reporting of trading operations of operating brokers in the country. To avoid manually assembling reports every weekend, I was instructed to collect the main queries according to the criteria satisfactory to the bank. It was also necessary to write a script, combining all query results into a single dataset, which would recalculate trade operations according to the national currency rate with the help of parsing and output a ready excel report. At the same time to set up a cheat sheet which bypassed the use of python path through cmd (company policy) - the solution was to run the compiler through a .bat file with the script I had written.
<br>
<ins>**Skills:**</ins> SQL Query, report automation.
<br>
<ins>**Technology:**</ins> Python, Pandas, Numpy, mysql.connector, openpyxl, MySQL.
<br>
<ins>**Results:**</ins> Creation of a script to automate reporting.


### 4 - Sales Management
<code>[Notebook](Sales%20Management.ipynb)</code>
<code>[PlotlyDash (Files)](PlotlyDash)</code>
<code>[Power BI](Sales%20Management%20Dashboard.pbix)</code>
<br>
<ins>**Description:**</ins> The project includes 4 datasets with the total number of rows 78 354 (customers, sales, products, calendar). Datasets contain information about online purchases, customers and product. Thanks to this we can find out the age of the target audience, the demand for products by customer, the local demand for product and much more. Two types of data visualization (dashboards) were created for convenience: in Power BI and HerokuApp.
<br>
<ins>**Skills:**</ins> data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.
<br>
<ins>**Technology:**</ins> SQL (SSMS, clearing tables), Python (data preprocessing, data preparation for the dashboard, pandas, numpy, seaborn, itertools, matplotlib, dash, plotly.express), Jupyter Lab (creating the plotly dash app)
Power BI (Creating an interactive dashboard), Heroku (Upload the Plotly Dash App)
<br>
<ins>**Results:**</ins> Knowing the key selling locations of products and their category, it is possible to properly place the products in warehouses. This optimizes logistics (products are not wasted in warehouses), reduces the cost of transporting products here and there, and the advantage over competitors (speed of delivery increases).
</br>
<ins>**EDA (short):**</ins>
</br>
- The data has been processed and cleared of unnecessary columns
- The percentage of missing information was also checked.
- Empty values have been partially restored. But some of the empty values had to be removed due to the lack of information on the prodcuts. Attempts were made to search for the same product by name, product id and categories.
- Some of the empty values in the product value column were restored by finding the average value found using the general category and subcategory of similar products.
- Datasets were combined with each other through special id keys
- The analysis revealed the age of the target audience.
- Cities with the highest demand are identified.
- Identified products with the maximum demand for the general indicators and in each subcategory separately.
- Create an interactive dashboard as an app and in Power BI
