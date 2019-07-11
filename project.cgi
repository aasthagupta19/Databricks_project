#!/usr/bin/python3
import   cgi,subprocess,os
import  cgitb
cgitb.enable()

print("Content-type:text/html")
print("")

#  get  html page code and data
web=cgi.FieldStorage()
#get the value of first name	
data=web.getvalue('x')
os.system("ansible-playbook web.yml")

print('''
<html>
<body>
<a href="13.233.142.8:4200"> click </a> 
</body>
</html>
''')

