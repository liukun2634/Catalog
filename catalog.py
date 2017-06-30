#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Author: Kun Liu
# @Date: 2017-07-05 19:21:22
# @Last modified by: Kun Liu
# @Last modified date: 2017-07-10 20:31:22

import psycopg2

"""
    This file can connect to database for selecting 
    the most popular articles, authors and 
    the date with over 1% requests error.
"""

DBNAME = "news"

# connect to database
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# open the out.txt for output the answer
with open('out.txt', 'w') as f:
   
    #select the most popular there articles 
    c.execute("select title, count(*) as reviews "
              "from articles,log "
              "where '/article/'||articles.slug=log.path "
              "group by title "
              "order by reviews desc;")
    popular_article = c.fetchall()
    f.write('Most popular three artiles are: \n')
    for i in range(0, 3):
        f.write('     '+str(i+1)+'. "'+popular_article[i][0]
                + '"'+'--'+str(popular_article[i][1])+' reviews\n')
 
    #select the most popular authors sorted by list
    # c.execute("drop view if exists popular_article")
    c.execute("create view popular_article as "
              "select title, count(*) as reviews, author "
              "from articles, log "
              "where ('/article/')||slug=path "
              "group by title,author "
              "order by reviews desc;")
    c.execute("select name, sum(reviews) as views "
              "from authors join popular_article "
              "on author=id "
              "group by name "
              "order by views desc;")
    popular_author = c.fetchall()
    f.write('\n\nMost popular authors are : \n')
    for i in range(0, len(popular_author)):
        f.write('     '+str(i+1)+'. "'+popular_author[i][0]
                + '"'+'--'+str(popular_author[i][1])+' reviews\n')

    #select the date more than 1% requests lead to errors
    # c.execute("drop view if exists error_date")
    # c.execute("drop view if exists total_date")
    c.execute("create view error_date as "
              "select time::date, count(*) as error_nums "
              "from log where status<>'200 OK' "
              "group by time::date;")
    c.execute("create view total_date as"
              " select time::date, count(*) as total_nums "
              "from log "
              "group by time::date;")
    c.execute("select error_date.time, "
              "round(error_nums::numeric/total_nums::numeric,4) "
              "as result from total_date "
              "join error_date on total_date.time=error_date.time "
              "where round(error_nums::numeric/total_nums::numeric,4)>0.01;")
    error_date = c.fetchall()
    f.write('\n\nThis day had more than 1% requests lead to errors: \n')
    f.write('     '+str(error_date[0][0])+'--' +
            str(round(error_date[0][1]*100, 2))+'% errors')

#close database
db.close()
