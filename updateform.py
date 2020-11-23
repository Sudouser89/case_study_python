#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb
from datetime import datetime
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>Update Screen</h1>")
print("<form action='/cgi-bin/updateform.py'  method='post'>")
print("ssn: <input type='text' name='ssn'>")
print("<input type='submit'>")
print("</form>")

form=cgi.FieldStorage()
ssn=form.getvalue('ssn')
tlist=[]

f=open("custdata.txt","r")
for line in f:
    for w in line.split():
        if str(w)==str(ssn):
            h=line
            for s in h.split():
                tlist.append(s)
            print("<h2>Data Found for "+str(ssn)+"</h2>")
            print("<form action='/cgi-bin/updateform.py'  method='post'>")
            print("data: <textarea hidden name='data'  rows='2' cols='60'>"+line+"</textarea></br>")
            print("ssn: <input readonly type='text' name='ssns'  value="+tlist[0]+"></br>")
            print("customer id: <input readonly type='text' name='cid' value="+tlist[1]+"></br>")
            print("Name: <input type='text' name='name' value="+tlist[2]+"></br>")
            print("Age: <input type='text' name='age' value="+tlist[3]+"></br>")
            print("Address line 1: <input type='text' name='ad1' value="+tlist[4]+"></br>")
            print("Address line 2: <input type='text' name='ad2' value="+tlist[5]+"></br>")
            print("city: <input type='text' name='city' value="+tlist[6]+"></br>")
            print("state: <input type='text' name='state' value="+tlist[7]+"></br>")
            print("<input type='submit' name='submit'>")
            print("</form>")

if form.getvalue('name'):
    print("<h2>Customer update initiated successfully</h2>")
    h=form.getvalue('data')
    ssns=form.getvalue('ssns')
    cid=form.getvalue('cid')
    name=form.getvalue('name')
    age=form.getvalue('age')
    ad1=form.getvalue('ad1')
    ad2=form.getvalue('ad2')
    city=form.getvalue('city')
    state=form.getvalue('state')
    g=open("custdata.txt","a")
    g.write(ssns)
    g.write(" ")
    g.write(cid)
    g.write(" ")
    g.write(name)
    g.write(" ")
    g.write(age)
    g.write(" ")
    g.write(ad1)
    g.write(" ")
    g.write(ad2)
    g.write(" ")
    g.write(city)
    g.write(" ")
    g.write(state)
    g.write(" ")
    g.write("\n")
    with open("custdata.txt", "r+") as ff:
        d = ff.readlines()
        ff.seek(0)
        for i in d:
            if i.strip() != h.strip():
                ff.write(i)
        ff.truncate()
    kk=open("customerstat.txt","a")
    kk.write(ssns)
    kk.write(",")
    kk.write(cid)
    kk.write(",")
    kk.write("Active")
    kk.write(",")
    kk.write("Customer-updation-successful")
    kk.write(",")
    now = datetime.now()
    kk.write(str(now.strftime("%d/%m/%Y-%H:%M:%S")))
    kk.write(",")
    kk.write("\n")
    kk.close()
print("</body></html>")
        