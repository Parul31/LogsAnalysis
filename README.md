# LogsAnalysis
The task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. 
This reporting tool is a Python program(threeAnswers.py) using the psycopg2 module to connect to the database. 
Here are the questions the reporting tool answer:

1. What are the most popular three articles of all time? 

2. Who are the most popular article authors of all time? 

3. On which days did more than 1% of requests lead to errors?

To run this program you need vagrant and news database. 
Run following commands- 

1. vagrant up

2. vagrant ssh

3. psql news

4. To import newsdata.sql file in news database use psql -d news -f newsdata.sql command.

5. create following views-

create view ques2 as select articles.author,count(path) as view from log,articles where articles.slug=substring(path,10) group by articles.author;

create view ques3 as select to_char(t1.day,'FMMonth FMDD,YYYY') as day,t1.status_all,coalesce(t2.status_404,0) as status_404 from (select date(time) as day,count(status) as
status_all from log group by day order by day) t1 left join (select date(time) as day,count(status) as status_404 from log where status='404 NOT FOUND' group by day order by day) t2 on t1.day
=t2.day;

6. python threeAnswers.py

The output of the program is provided in output.txt
