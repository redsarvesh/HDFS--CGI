#!/usr/bin/python

import  cgi,cgitb,os,time,commands,sys
cgitb.enable()
print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
#  here  setup  choice  will store 

choice=x.getvalue('choose')


if    choice   ==   'hdfs'  :
	print  "<meta http-equiv='refresh' content='1;url=http://192.168.122.1/hadoopproject/third.html' />"




	



