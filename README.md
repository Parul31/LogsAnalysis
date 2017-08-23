# LogsAnalysis
The task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. 
This reporting tool is a Python program(threeAnswers.py) using the psycopg2 module to connect to the database. 
Here are the questions the reporting tool answer:

1. What are the most popular three articles of all time? 

2. Who are the most popular article authors of all time? 

3. On which days did more than 1% of requests lead to errors?

To run this program you need vagrant and news database.
run following commands- 

vagrant up

vagrant ssh

psql news

create following views-

create view ques2 as select articles.author,count(path) as view from log.articles where articles.slug=substring(path,10) group by articles.author;

create view ques3 as select t1.day,t1.status_all,coalesce(t2.status_404,0) as status_404 from (select to_char(time,'MonthDD,YYYY') as day,count(status) as status_all from log group by
day order by day) t1 left join (select to_char(time,'MonthDD,YYYY') as day,count(status) as status_404 from log where status='404 NOT FOUND' group by day order by day) t2 on t1.day=t2.day;

run the code by- python threeAnswers.py