#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb
from itertools import islice
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>Customer Status Screen</h1>")

kk=open("customerstat.txt","r")
l=kk.read()
kkk=open("customerstat.txt","r")
ux=kkk.readlines()
uy=[]
u=[]
for i in range(len(ux)):
    uy.append(5)
for x in l.split(','):
    u.append(x.strip())
inputt = iter(u) 
output = [list(islice(inputt, elem)) 
          for elem in uy]
print("<table style='border: 1px solid black; width:580px'>")
print("<tr>")
print("<th>SSN</th>")
print("<th>CID</th>")
print("<th>Status</th>")
print("<th>Message</th>")
print("<th>Last Updated</th>")
print("</tr>")
print("</table>")
for i in range(len(ux)):
    print(str(output[i])+"</br>")
print("</body></html>")
     
