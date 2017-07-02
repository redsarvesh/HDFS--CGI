#!/usr/bin/python

import  cgi,cgitb,os,time,commands,sys
cgitb.enable()
print  "content-type:text/html"
print  ""
x=cgi.FieldStorage()
nn_ip=x.getvalue("nnip")
directory=x.getvalue("dirname")

datanodes=x.getlist('my_list')

################################################################# NAMENODE ##########################################################################


commands.getoutput("sudo -i touch /var/www/cgi-bin/hdfs-site.xml")
commands.getoutput("sudo -i chmod 777 /var/www/cgi-bin/hdfs-site.xml")

file1=open("/var/www/cgi-bin/hdfs-site.xml","w")
s="<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\""+"text/xsl\""+" href="+"\"configuration.xsl\""+"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>"+"/"+directory+"</value>\n</property>\n</configuration>"
file1.write(s)
file1.close()

commands.getoutput("sudo -i touch /var/www/cgi-bin/core-site.xml")
commands.getoutput("sudo -i chmod 777 /var/www/cgi-bin/core-site.xml")


file2=open("/var/www/cgi-bin/core-site.xml","w")
s="<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\""+"text/xsl\""+" href="+"\"configuration.xsl\""+"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://ipaddr:10001</value>\n</property>\n</configuration>"
file2.write(s)
file2.close()

namenode=nn_ip


commands.getoutput("sudo -i sshpass -p 'q' scp /var/www/cgi-bin/hdfs-site.xml root@"+namenode+":/etc/hadoop/")

commands.getoutput("sudo -i sshpass -p 'q' scp /var/www/cgi-bin/core-site.xml root@"+namenode+":/etc/hadoop/")

		

	
commands.getoutput("sudo -i sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+namenode+" "+'\'sed -i \"s/ipaddr/'+namenode+"/"+"\" /etc/hadoop/core-site.xml\'")

################################################################ DATANODE #########################################################################
s=1


for dn_ip in datanodes:

	commands.getoutput("sudo -i sshpass -p 'q' scp /var/www/cgi-bin/core-site.xml root@"+dn_ip+":/etc/hadoop/")

	commands.getoutput("sudo -i sshpass -p 'q' scp /var/www/cgi-bin/hdfs-site.xml root@"+dn_ip+":/etc/hadoop/")

	
	
	
	commands.getoutput("sudo -i sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+dn_ip+" "+'\'sed -i \"s/ipaddr/'+namenode+"/"+"\" /etc/hadoop/core-site.xml\'")
	
	commands.getoutput("sudo -i sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+dn_ip+" "+'\'sed -i \"s/'+directory+'/'+"number"+str(s)+"/"+"\" /etc/hadoop/hdfs-site.xml\'")

	commands.getoutput("sudo -i sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+dn_ip+" "+'\'sed -i \"s/dfs.name.dir/dfs.data.dir/'+"\""+" /etc/hadoop/hdfs-site.xml\'")
	

	s=s+1

time.sleep(2)
print "done"
print " cooooool :-) "
time.sleep(5)
print  "<meta http-equiv='refresh' content='2;url=http://192.168.122.1/hadoopproject/second.html'/>"

