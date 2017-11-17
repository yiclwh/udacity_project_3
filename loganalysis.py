#!/usr/bin/python3
import psycopg2

#Function definition
def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")

def print_result(data):
    for pair in data:
        print('  {} -- {} views'.format(pair[0], pair[1]))

# main implementation
print('\n1. What are the most popular three articles of all time?\n')
conn, cursor = connect("news")
cursor.execute(
    "SELECT articles.title, count(log.path) as clickcount "
    "FROM articles left join log "
    "on log.path like concat('%',articles.slug,'%') "
    "group by articles.title order by clickcount desc limit 3;"
    )
print_result(cursor.fetchall())

print('\n2. Who are the most popular article authors of all time?\n')
cursor.execute(
    "select authors.name, clickcount "
    "FROM authors, topauthors "
    "where authors.id = topauthors.author order by clickcount desc;"
    )
print_result(cursor.fetchall())

print('\n3. On which days did more than 1% of requests lead to errors?\n')
cursor.execute(
    "select round(100.0*count_log.error_count/count_log.total_count, 2) "
    "as error_percent, time "
    "from (select sum(case when status like '4%' "
    "or status like '5%' then 1 else 0 end) as error_count, "
    "count(time::timestamp::date) as total_count, time::timestamp::date "
    "from log group by time::timestamp::date) as count_log "
    "where round(100.0*count_log.error_count/count_log.total_count, 1) >= 1"
    )
data = cursor.fetchall()
for pair in data:
    print('  {} -- {}% errors\n'.format(pair[1], pair[0]))

conn.close()
