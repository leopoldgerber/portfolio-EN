#!/usr/bin/env python
# coding: utf-8

# In[13]:


#================ LIBRARIES ================

import mysql.connector
from mysql.connector import Error
#from config import database_config # host, port, user, password

from datetime import date

import pandas as pd
import requests
from xml.etree import ElementTree

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

#================ FUNCTION TO CONNECT TO THE SQL SERVER ================

def mysql_conncetion(host_name, port_name, user_name, user_password, database_name = None):
    database_connection = None
    try:
        database_connection = mysql.connector.connect(
            host = host_name,
            port = port_name,
            user = user_name,
            password = user_password,
            database = database_name
        )
        print("================ CONNECTED")
    except Error as db_connection_error:
        print(db_connection_error)
    return database_connection

#================ SQL SERVER CONNECTION - CONFIG CHECK ================

#connection = mysql_conncetion(database_config["mysql"]["host"],
#                              database_config["mysql"]["port"],
#                              database_config["mysql"]["user"],
#                              database_config["mysql"]["password"])
connection = mysql_conncetion("***.***.host.***.***", **port**, "**user**", "password")

print('================ report_name - START')

#================ report_name - PARAGRAPH 1 ================

try:    
    cursor = connection.cursor(dictionary = True)
    try_sql_query = '''
    SELECT
      a.company
      , (a.PROFIT_YEAR + IF(b.balance_operation IS NULL, 0, b.balance_operation)) AS balance
    FROM
    (
    SELECT
    '******** Ltd.' AS company,
     ROUND(SUM(IF(trades.CMD IN (0, 1), (PROFIT + trades.COMMISSION + trades.SWAPS), 0)) +  (SELECT
      h.amount
    FROM
       trades_db.hedge_report_name AS h
                      WHERE
                        h.company = '******** Ltd.' ), 2) AS PROFIT_YEAR

    FROM
     trades_db.USERS AS users
     INNER JOIN trades_db.MT4_TRADES AS trades ON users.LOGIN = trades.LOGIN
    WHERE
      users.GROUP REGEXP 'FTM-'
      AND trades.CMD IN (0, 1)
      AND users.USER_COLOR NOT IN (11920639)
      AND trades.CLOSE_TIME > (SELECT
                        h.slice_date
                      FROM
                        trades_db.hedge_report_name AS h
                      WHERE
                        h.company = '******** Ltd.'
                        )
      AND trades.CLOSE_TIME < (SELECT
                        DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                      FROM
                        (
                          SELECT
                            rs.id AS id
                          FROM
                            trades_db.report_settings AS rs
                        ) AS last_report
                        LEFT JOIN trades_db.report_settings AS rs ON last_report.id = rs.id
                        ORDER BY 
                        	rs.id DESC
								LIMIT
									1,1)
    UNION ALL

    SELECT
      h.company,
      h.amount
    FROM
       trades_db.hedge_report_name AS h
    WHERE
      h.company != '******** Ltd.' ) AS a
     LEFT JOIN (
       SELECT
      s.S4
      , IF(SUM(s.X1) IS NULL, 0, SUM(s.X1)) + IF(SUM(s.X2) IS NULL, 0, SUM(s.X2)) - IF(SUM(s.X3) IS NULL, 0, SUM(s.X3)) AS balance_operation
    FROM
      trades_db.report_supplement_f7004 AS s
    WHERE
      CAST(CONCAT((s.D1), ' ',(s.T1)) AS DATETIME) > (SELECT
                        h.slice_date
                      FROM
                        trades_db.hedge_report_name AS h
                      WHERE
                        h.company = '******** Ltd.'
                        )
      AND CAST(CONCAT((s.D1), ' ',(s.T1)) AS DATETIME) < (SELECT
                        DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                      FROM
                        (
                          SELECT
                            rs.id AS id
                          FROM
                            trades_db.report_settings AS rs
                        ) AS last_report
                        LEFT JOIN trades_db.report_settings AS rs ON last_report.id = rs.id
                        ORDER BY 
                        	rs.id DESC
								LIMIT
									1,1)
    GROUP BY
      s.S4
     ) AS b ON b.S4 = a.company
    '''
    cursor.execute(try_sql_query)
    query_result = cursor.fetchall()
    
    report_name_1 = pd.DataFrame(query_result)
    
except Error as error:
    print(error)
    
print('================ report_name - PARAGRAPH 1')
    
    
#================ report_name - PARAGRAPH 2 TO 4 ================

try:    
    cursor = connection.cursor(dictionary = True)
    try_sql_query = '''
    SELECT
    DATE(DATE_FORMAT((trades.CLOSE_TIME), '%Y.%m.01')) AS MONTH,
    DATE_FORMAT((DATE_SUB(trades.CLOSE_TIME, INTERVAL - 

    (SELECT
      rs.time_zone_difference
    FROM
      (
        SELECT
          MAX(rs.id) AS id
        FROM
          trades_db.report_settings AS rs
      ) AS last_report
      LEFT JOIN trades_db.report_settings AS rs ON last_report.id = rs.id) 

      HOUR)), '%u') AS WEEK, /*Интервал можно брать из trades_db.report_settings, поле time_zone_difference*/
    ROUND(SUM(IF(trades.CMD IN (0, 1), (PROFIT + trades.COMMISSION + trades.SWAPS), 0)), 2) AS 'Торговый результат клиентов',
    ROUND(SUM(IF(trades.CMD IN (6) AND trades.COMMENT REGEXP 'SO Deposit to zero', (PROFIT + trades.COMMISSION + trades.SWAPS), 0)), 2) AS 'SO Deposit to zero',
    ROUND(SUM(IF(trades.CMD IN (6) AND trades.COMMENT REGEXP 'Bonus In', (PROFIT + trades.COMMISSION + trades.SWAPS), 0)), 2) AS 'Bonus'
    FROM
    trades_db.USERS AS users
    INNER JOIN trades_db.MT4_TRADES AS trades ON users.LOGIN = trades.LOGIN
    WHERE
    users.GROUP REGEXP 'FTM-'
    AND users.GROUP NOT REGEXP 'tst'
    AND users.USER_COLOR NOT IN (11920639)
    AND (trades.CMD IN (0, 1) OR (trades.CMD = 6 AND trades.COMMENT REGEXP 'SO Deposit to zero|Bonus In'))
    AND trades.CLOSE_TIME >= 
      (SELECT
                        DATE_ADD(rs.start_date, INTERVAL -rs.time_zone_difference HOUR)
                      FROM
                        (
                          SELECT
                            rs.id AS id
                          FROM
                            trades_db.report_settings AS rs
                        ) AS last_report
                        LEFT JOIN trades_db.report_settings AS rs ON last_report.id = rs.id
                        ORDER BY 
                        	rs.id DESC
								LIMIT
									1,1)
    /*Границы можно брать из trades_db.report_settings, поле start_date, с учетом поля time_zone_difference */
      AND trades.CLOSE_TIME < (SELECT
                        DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                      FROM
                        (
                          SELECT
                            rs.id AS id
                          FROM
                            trades_db.report_settings AS rs
                        ) AS last_report
                        LEFT JOIN trades_db.report_settings AS rs ON last_report.id = rs.id
                        ORDER BY 
                        	rs.id DESC
								LIMIT
									1,1)
    /*Границы можно брать из trades_db.report_settings, поле end_date, с учетом поля time_zone_difference */
    '''
    cursor.execute(try_sql_query)
    query_result = cursor.fetchall()
    
    report_name_2_4 = pd.DataFrame(query_result)
    #report_name_2_4['Торговый результат клиентов'] = report_name_2_4['Торговый результат клиентов'].astype(int)
    
except Error as error:
    print(error)

print('================ report_name - PARAGRAPH 2 TO 4')    

#================ report_name - PARAGRAPH 5 ================

try:    
    cursor = connection.cursor(dictionary = True)
    try_sql_query = '''
    SELECT
    users.rez
    , SUM(BALANCE - COALESCE(change_balance, 0)) AS balance
    FROM
    (
    SELECT
    users.*,
    SUM(PROFIT + trades.COMMISSION + trades.SWAPS) AS change_balance
    FROM
    (
    SELECT
    SUM(IF(va.custom_country REGEXP 'BELARUS', users.BALANCE, 0)) AS BALANCE_BY,
    SUM(IF(va.custom_country NOT REGEXP 'BELARUS', users.BALANCE, 0)) AS BALANCE_NO_BY,
    SUM(users.BALANCE) AS BALANCE,
    IF(va.custom_country REGEXP 'BELARUS', 'BY', 'NO_BY') AS rez,
    users.login
    FROM
    trades_db.USERS AS users
    LEFT JOIN crm.vtiger_account_view_wopd AS va ON users.ID = va.accountid
    WHERE
    users.GROUP REGEXP 'FTM-'
    AND users.GROUP NOT REGEXP 'tst'
    AND users.USER_COLOR NOT IN (11920639)
    GROUP BY users.login
    ) AS users
    LEFT JOIN trades_db.MT4_TRADES AS trades ON users.LOGIN = trades.LOGIN AND trades.CLOSE_TIME > (SELECT
                        DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                      FROM
                        (
                          SELECT
                            rs.id AS id
                          FROM
                            trades_db.report_settings AS rs
                        ) AS last_report
                        LEFT JOIN trades_db.report_settings AS rs ON last_report.id = rs.id
                        ORDER BY 
                        	rs.id DESC
								LIMIT
									1,1)
    /*Границы можно брать из trades_db.report_settings, поле end_date - 12 часов, с учетом поля time_zone_difference */
    GROUP BY users.LOGIN
    ) AS users
     GROUP BY rez

    '''
    cursor.execute(try_sql_query)
    query_result = cursor.fetchall()
    
    report_name_5 = pd.DataFrame(query_result)
    
except Error as error:
    print(error)
    
print('================ report_name - PARAGRAPH 5')

#================ report_name - PARAGRAPH 6 ================

try:    
    cursor = connection.cursor(dictionary = True)
    try_sql_query = '''
    SELECT 
      t_all.full_symbol
    #  , t_all.symbol
    #  , group_concat(round(t_all.amount, 2)) AS all_amount
      , abs(SUM(t_all.amount)) AS sum_amount
      , ROUND((SUM(volume_minus) + SUM(volume_plus))/100, 2) AS volume
      , t_all.currency
    FROM
    (SELECT
      SUBSTRING_INDEX(SUBSTRING_INDEX(tr.SYMBOL,'.',1), '_', 1) AS full_symbol
      , tr.SYMBOL
      , ss.symbol_group
      , sum(tr.VOLUME) AS volume_sum
      , SUM(if(tr.cmd = 1, -tr.volume, 0)) AS volume_minus
      , SUM(if(tr.cmd = 0, tr.volume, 0)) AS volume_plus
      , t0.bid
      , t0.ask
      , cs.contract_size
      , (SUM(if(tr.cmd = 1, -tr.volume, 0)) * cs.contract_size * if(ss.symbol_group = 1 , 1, t0.bid)) / if(ss.symbol_group = 4,20,if(ss.symbol_group IS NULL, 20, 100)) AS volume_minus_bid
      , (SUM(if(tr.cmd = 0, tr.volume, 0)) * cs.contract_size * if(ss.symbol_group = 1, 1, t0.ask)) / if(ss.symbol_group = 4,20,if(ss.symbol_group IS NULL, 20, 100)) AS volume_plus_ask
      , ((SUM(if(tr.cmd = 1, -tr.volume, 0)) * cs.contract_size * if(ss.symbol_group = 1, 1, t0.bid)) / if(ss.symbol_group = 4,20,if(ss.symbol_group IS NULL, 20, 100))
        + (SUM(if(tr.cmd = 0, tr.volume, 0)) * cs.contract_size * if(ss.symbol_group = 1, 1, t0.ask)) / if(ss.symbol_group = 4,20,if(ss.symbol_group IS NULL, 20, 100))) / 100 AS amount
      , cs.currency
    FROM
      trades_db.USERS AS us
      LEFT JOIN trades_db.MT4_TRADES AS tr ON us.login = tr.login
      LEFT JOIN db_config.sprecification_symbols AS ss ON ss.symbol = tr.symbol
      LEFT JOIN (
          SELECT
            tcfr.symbol
            , tcfr.date_time AS last_date_tcfr
            , tcfr.ask
            , tcfr.bid
          FROM
            trades_db.ticks_collected_ftm_reporting AS tcfr
            INNER JOIN (
            SELECT 
              tcfr.symbol
              , max(tcfr.date_time) AS max_date
            FROM 
              trades_db.ticks_collected_ftm_reporting AS tcfr
            WHERE 
              tcfr.ask != 0
              AND tcfr.bid != 0
            GROUP BY
              tcfr.symbol
            ) AS t0 ON tcfr.symbol = t0.symbol AND t0.max_date = tcfr.date_time
            ) AS t0 ON t0.symbol = tr.symbol
      LEFT JOIN(
          SELECT
            cs.symbol
            , cs.slice_date
            , cs.contract_size
            , cs.currency
          FROM 
            db_config.con_symbol AS cs
            INNER JOIN (
            SELECT 
              cs.symbol
              , max(cs.slice_date) AS max_date
            FROM 
              db_config.con_symbol AS cs
            GROUP BY
              cs.symbol) AS t0 ON cs.symbol = t0.symbol AND cs.slice_date = t0.max_date
          GROUP BY 
            cs.symbol 
          ) AS cs ON cs.symbol = tr.symbol
    WHERE
    #  tr.SYMBOL REGEXP 'XAUUSD'
      tr.cmd IN (0,1)
      AND (tr.CLOSE_TIME BETWEEN (SELECT
                        DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                      FROM
                        (
                          SELECT
                            rs.id AS id
                          FROM
                            trades_db.report_settings AS rs
                        ) AS last_report
                        LEFT JOIN trades_db.report_settings AS rs ON last_report.id = rs.id
                        ORDER BY 
                        	rs.id DESC
								LIMIT
									1,1) AND NOW())
        AND tr.OPEN_TIME <= (SELECT
                        DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                      FROM
                        (
                          SELECT
                            rs.id AS id
                          FROM
                            trades_db.report_settings AS rs
                        ) AS last_report
                        LEFT JOIN trades_db.report_settings AS rs ON last_report.id = rs.id
                        ORDER BY 
                        	rs.id DESC
								LIMIT
									1,1)
      AND us.GROUP REGEXP 'ftm'
      AND us.GROUP NOT REGEXP 'tst'
    GROUP BY
      tr.SYMBOL

    UNION ALL

    SELECT
      SUBSTRING_INDEX(SUBSTRING_INDEX(tr.SYMBOL,'.',1), '_', 1) AS full_symbol
      , tr.SYMBOL
      , ss.symbol_group
      , sum(tr.VOLUME) AS volume_sum
      , SUM(if(tr.cmd = 1, -tr.volume, 0)) AS volume_minus
      , SUM(if(tr.cmd = 0, tr.volume, 0)) AS volume_plus
      , t0.bid
      , t0.ask
      , cs.contract_size
      , (SUM(if(tr.cmd = 1, -tr.volume, 0)) * cs.contract_size * if(ss.symbol_group = 1 , 1, t0.bid)) / if(ss.symbol_group = 4,20,if(ss.symbol_group IS NULL, 20, 100)) AS volume_minus_bid
      , (SUM(if(tr.cmd = 0, tr.volume, 0)) * cs.contract_size * if(ss.symbol_group = 1, 1, t0.ask)) / if(ss.symbol_group = 4,20,if(ss.symbol_group IS NULL, 20, 100)) AS volume_plus_ask
      , ((SUM(if(tr.cmd = 1, -tr.volume, 0)) * cs.contract_size * if(ss.symbol_group = 1, 1, t0.bid)) /if(ss.symbol_group = 4,20,if(ss.symbol_group IS NULL, 20, 100)) 
        + (SUM(if(tr.cmd = 0, tr.volume, 0)) * cs.contract_size * if(ss.symbol_group = 1, 1, t0.ask)) / if(ss.symbol_group = 4,20,if(ss.symbol_group IS NULL, 20, 100))) / 100 AS amount
      , cs.currency
    FROM
      trades_db.USERS AS us
      LEFT JOIN trades_db.MT4_TRADES AS tr ON us.login = tr.login
      LEFT JOIN db_config.sprecification_symbols AS ss ON ss.symbol = tr.symbol
      LEFT JOIN (
          SELECT
            tcfr.symbol
            , tcfr.date_time AS last_date_tcfr
            , tcfr.ask
            , tcfr.bid
          FROM
            trades_db.ticks_collected_ftm_reporting AS tcfr
            INNER JOIN (
            SELECT 
              tcfr.symbol
              , max(tcfr.date_time) AS max_date
            FROM 
              trades_db.ticks_collected_ftm_reporting AS tcfr
            WHERE 
              tcfr.ask != 0
              AND tcfr.bid != 0
            GROUP BY
              tcfr.symbol
            ) AS t0 ON tcfr.symbol = t0.symbol AND t0.max_date = tcfr.date_time
            ) AS t0 ON t0.symbol = tr.symbol
      LEFT JOIN(
          SELECT
            cs.symbol
            , cs.slice_date
            , cs.contract_size
            , cs.currency
          FROM 
            db_config.con_symbol AS cs
            INNER JOIN (
            SELECT 
              cs.symbol
              , max(cs.slice_date) AS max_date
            FROM 
              db_config.con_symbol AS cs
            GROUP BY
              cs.symbol) AS t0 ON cs.symbol = t0.symbol AND cs.slice_date = t0.max_date
          GROUP BY 
            cs.symbol 
          ) AS cs ON cs.symbol = tr.symbol
    WHERE
    #  tr.SYMBOL REGEXP 'XAUUSD'
      tr.cmd IN (0,1)
      AND tr.CLOSE_TIME = '1970-01-01'
        AND tr.OPEN_TIME <= (SELECT
                        DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                      FROM
                        (
                          SELECT
                            rs.id AS id
                          FROM
                            trades_db.report_settings AS rs
                        ) AS last_report
                        LEFT JOIN trades_db.report_settings AS rs ON last_report.id = rs.id
                        ORDER BY 
                        	rs.id DESC
								LIMIT
									1,1)
      AND us.GROUP NOT REGEXP 'tst'
    GROUP BY
      tr.SYMBOL) AS t_all
    GROUP BY
      t_all.full_symbol
    HAVING
      volume != 0.00
    '''
    cursor.execute(try_sql_query)
    query_result = cursor.fetchall()       
    
    connection.commit()
    
    report_name_6 = pd.DataFrame(query_result)
    
    
    cursor.close()
    connection.close()
    
except Error as error:
    print(error)
    
print('================ report_name - PARAGRAPH 6')
    
#================ CONNECT TO NBRB ================

response = requests.get("https://www.national_bank.com/api/currencies", verify=False)
json = response.json()

dataset = pd.DataFrame.from_dict(pd.json_normalize(json), orient = 'columns')


#================ PREPARE DATA ================

#Create unique symbols from report_name_6
currency = set()

for symbol in report_name_6['currency']: 
    currency.add(symbol)

#Create temporary dictionary
temp = []

for symbol in currency:
    temp.append(requests.get(
        "https://www.national_bank.com/api/rates/" + symbol + "?parammode=2", verify=False).json())

#Prepare dataset   
data = pd.DataFrame(temp).rename(columns={'Cur_Abbreviation':'currency'})

data.columns = data.columns.str.lower()

df = data.drop(['cur_id', 'date', 'cur_name'], axis = 1)

#Merge 
report_name_6 = report_name_6.merge(df, on = ['currency'])

#Create converted tables
report_name_6['BYN'] = round(report_name_6.sum_amount * (report_name_6.cur_officialrate / report_name_6.cur_scale), 2)

report_name_6['USD'] = round(report_name_6.BYN / list(dict(
    requests.get("https://www.national_bank.com/api/usd?parammode=2", verify=False).json()).values())[-1], 2)

report_name_6.full_symbol = report_name_6.full_symbol.apply(lambda x : str(x).replace('#',''))


#================ DATAFRAMES TO EXCEL ================

def dataframes_to_excel(df_list, sheets, file_name, spaces): 
    writer = pd.ExcelWriter(file_name,engine='xlsxwriter')  
    data = report_name_6.to_excel(writer, sheet_name = 'Лист 1', index = False)
    row = 0 
    for dataframe in df_list: 
        dataframe.to_excel(writer,sheet_name=sheets,startrow=row , startcol=0, index = False)    
        row = row + len(dataframe.index) + spaces + 1 
        writer.sheets['Лист 1'].set_column(0,7,13)
        writer.sheets['Лист 2'].set_column(0,4,28)
    writer.save() 
    
dataframes = [report_name_1, report_name_2_4, report_name_5]  

dataframes_to_excel(dataframes, 'Лист 2', 'C:/Users/*****/report_name_' + str(date.today()) +'.xlsx', 1)

print('================ report_name - FINISH')


# In[ ]:




