![The Daily Bugle](assets/images/Spider-Man-Daily-Bugle.jpg)

# The Daily Bugle Logs Analysis

## Requirements

The Daily Bugle Logs Analysis is command line application using `Python 2.7` and `psycopg2` library.

1. Create new virtual environment for this project
  + `virtualenv TheDailyBugle`
  + activate the virtual environment `source TheDailyBugle/bin/activate`
  + go to **logs analysis** directory and run `pip install -r requirements.txt`
2. you should already have PostgresSQL installed in your machine and having a database
called `news` there. import unzipped of [newsdata.sql.zip](news_data/newsdata.sql.zip) to news database using
`psql -d news -f newsdata.sql` after that can use following commands to make sure import was successful
  + `\dt` to lists the tables that are available in the database
  + `\d TableName` shows the database schema for that particular table.
3. make sure you can connect to your PostgresSQL
  + in your command line interface enter `python`
  + enter following to make sure you can connect to the database
  ```
  >>> import psycopg2
  >>> connection = psycopg2.connect(dbname="news")
  ```
4. go to the project directory and run `python log_analyzer.py`
5. you see the answers to each question defined at `What is Logs Analysis` section

You should see result like following

```
###################### TOP 3 ARTICLES ######################
Most Popular article is
 'Candidate is jerk, alleges rival' -- 338647 Views
############################################################
Second most Popular article is
 'Bears love berries, alleges bear' -- 253801 Views
############################################################
Third most Popular article is
 'Bad things gone, say good people' -- 170098 Views

###################### TOP AUTHORS ######################
############################################################
Ursula La Multa -- 507594 Views
############################################################
Rudolf von Treppenwitz -- 423457 Views
############################################################
Anonymous Contributor -- 170098 Views
############################################################
Markoff Chaney -- 84557 Views

################## Days Error went over 1% ##################
Jul 17, 2016 -- 2.26
##################
```

## What is Logs Analysis

Logs Analysis connect to **The Daily Bugle** database and show us following information:

  + Most popular three articles of all time
  + The most popular article authors of all time (a sorted list with the most popular author at the top.)
  + On which days did more than 1% of requests lead to errors


## Author

+ **SEYEDAMIR TADRISI** [AMIR](mailto:amirtds@gmail.com)
