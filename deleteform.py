#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb
from datetime import datetime
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>Delete Screen</h1>")
print("<form action='/cgi-bin/deleteform.py'  method='post'>")
print("ssn: <input type='text' name='ssn'>")
print("<input type='submit'>")
print("</form>")

form=cgi.FieldStorage()
ssn=form.getvalue('ssn')

f=open("custdata.txt","r")
for line in f:
    for w in line.split():
        if str(w)==str(ssn):
            print("<h2>Data Found for "+str(ssn)+"</h2>")
            print("<form action='/cgi-bin/deleteform.py'  method='post'>")
            print("data: <textarea readonly name='data'  rows='2' cols='60'>"+line+"</textarea></br>")
            print("<input type='submit' name='Delete' value='Delete'>")
            print("</form>")

if form.getvalue('data'):
    print("<h2>Customer deletion initiated successfully</h2>")
    h=form.getvalue('data')
    u=[]
    for i in h.split():
        u.append(i)
    ssn=u[0]
    cid=u[1]
    with open("custdata.txt", "r+") as ff:
        d = ff.readlines()
        ff.seek(0)
        for i in d:
            if i.strip() != h.strip():
                ff.write(i)
        ff.truncate()
    kk=open("customerstat.txt","a")
    kk.write(ssn)
    kk.write(",")
    kk.write(cid)
    kk.write(",")
    kk.write("Active")
    kk.write(",")
    kk.write("Customer-deletion-successful")
    kk.write(",")
    now = datetime.now()
    kk.write(str(now.strftime("%d/%m/%Y-%H:%M:%S")))
    kk.write(",")
    kk.write("\n")
    kk.close()
print("</body></html>")