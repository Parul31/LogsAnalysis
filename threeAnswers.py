#!/usr/bin/env python

import psycopg2

DBNAME = "news"


def get_result(query):
    """to get the query results."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# question1 is What are the most popular three articles of all time?
def get_top_articles():
    query_for_ques1 = "select title,count(path) as views "
    "from articles,log where articles.slug=substring(log.path,10) "
    "group by articles.title order by views desc limit 3"
    results_for_ques1 = get_result(query_for_ques1)
    print("\nWhat are the most popular three articles of all time?")
    for result in results_for_ques1:
        print("{:^10} --{:^10}views".format(result[0], result[1]))


# question2 is Who are the most popular article authors of all time?
def get_top_authors():
    query_for_ques2 = "select name,view from authors,ques2 "
    "where authors.id=ques2.author order by view desc"
    results_for_ques2 = get_result(query_for_ques2)
    print("\nWho are the most popular article authors of all time?")
    for result in results_for_ques2:
        print("{:^10} --{:^10}views".format(result[0], result[1]))


# question3 is On which days did more than 1% of requests lead to errors?
def get_error_percentage():
    query_for_ques3 = "select t1.day,t1.percentage "
    "from (select day,round((status_404*100)/status_all::decimal,1) "
    "as percentage from ques3) t1 where t1.percentage>1"
    results_for_ques3 = get_result(query_for_ques3)
    print("\nOn which days did more than 1% of requests lead to errors?")
    for result in results_for_ques3:
        print("{:^10} --{:^10}%".format(result[0], result[1]))

if __name__ == "__main__":
    get_top_articles()
    get_top_authors()
    get_error_percentage()
