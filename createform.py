#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb, random
from datetime import datetime
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>Customer creation initiated successfully</h1>")
print("</body></html>")  
form = cgi.FieldStorage()

class create:
    def __init__(self,ssn,name,age,ad1,ad2,city,state):
        self.ssn=ssn
        self.name=name
        self.age=age
        self.ad1=ad1
        self.ad2=ad2
        self.city=ssn
        self.state=state
    def custinp(self,ssn,name,age,ad1,ad2,city,state):
        f=open("custdata.txt","a")
        f.write(ssn)
        f.write(" ")
        cid=str(int(random.uniform(111111111,999999999)))
        f.write(cid)
        f.write(" ")
        f.write(name)
        f.write(" ")
        f.write(age)
        f.write(" ")
        f.write(ad1)
        f.write(" ")
        f.write(ad2)
        f.write(" ")
        f.write(city)
        f.write(" ")
        f.write(state)
        f.write("\n")
        f.close()
        kk=open("customerstat.txt","a")
        kk.write(ssn)
        kk.write(",")
        kk.write(cid)
        kk.write(",")
        kk.write("Active")
        kk.write(",")
        kk.write("Customer-creation-successful")
        kk.write(",")
        now = datetime.now()
        kk.write(str(now.strftime("%d/%m/%Y-%H:%M:%S")))
        kk.write(",")
        kk.write("\n")
        kk.close()

if __name__=='__main__':
    ssn=form.getvalue('ssn')
    name=form.getvalue('name')
    age=form.getvalue('age')
    ad1=form.getvalue('ad1')
    ad2=form.getvalue('ad2')
    city=form.getvalue('city')
    state=form.getvalue('state')
    s=create(ssn,name,age,ad1,ad2,city,state)
    s.custinp(ssn,name,age,ad1,ad2,city,state)
