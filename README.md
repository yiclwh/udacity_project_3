# Log Analysis

## Introduction

This project is submitted for Udacity Full-Stack Web Developer Project 3 - **Log Analysis**.

The python 3 code work with mock PostgreSQL database that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.


## Contents

* Requirements
  * Python3
  * PostgreSQL
  * psycopg2

* Porject files
  * `loganalysis.py`
  * `README.md`

* SQL views
  * `topauthors`
    ```SQL
    create view topauthors as 
    select articles.author, count(log.path) as clickcount 
    FROM articles left join log on 
    log.path like concat('%',articles.slug,'%') 
    group by articles.author order by clickcount desc
    ```

## How To Run The Application

* Load *newsdata.sql* using command `psql -d news -f newsdata.sql`
  * The sql file could also be found [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

* Excute python script *loganalysis.py*
  * Using the Terminal:

    * Type `python3 loganalysis.py` or `./logsanalysis.py`

  * Using the Python IDLE:

    * Select Run from the IDLE menu,

    * Click `Run Module` from the dropdown list