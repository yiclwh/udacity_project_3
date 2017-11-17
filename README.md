# Log Analysis

## Introduction

This project is submitted for Udacity Full-Stack Web Developer Project 3 - **Log Analysis**


## Contents

* Porject files
  * `loganalysis.py`
  * `README.md`

* Views
  * `topauthors`
    ```SQL
    create view topauthors as 
    select articles.author, count(log.path) as clickcount 
    FROM articles left join log on 
    log.path like concat('%',articles.slug,'%') 
    group by articles.author order by clickcount desc
    ```

## How To Run The Application

* Using the Terminal:

  * Type `python loganalysis.py`

* Using the Python IDLE:

  * Select Run from the IDLE menu,

  * Click `Run Module` from the dropdown list