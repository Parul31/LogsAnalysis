import psycopg2

DBNAME = "news"

def question1():
    """question1 is What are the most popular three articles of all time? """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title,count(path) as views from articles,log where articles.slug=substring(log.path,10) group by articles.title order by views desc")
    result = c.fetchall()
    print(result)
    db.close()
question1()
