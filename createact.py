#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb, random
from datetime import datetime
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>Create Account Screen</h1>")
print("<form action='/cgi-bin/createact.py'  method='post'>")
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
            print("<form action='/cgi-bin/createact.py'  method='post'>")
            print("SSN: <input readonly type='text' name='ssn' value="+tlist[0]+"></br>")
            print("Customer id: <input readonly type='text' name='cid' value="+tlist[1]+"></br>")
            print("<label>Account type:</label>")
            print("<select id='act' name='act'>")
            print("<option value='savings'>Savings</option>")
            print("<option value='current'>Current</option>")
            print("</select></br>")
            print("Deposit Amount: <input type='number' name='deposit'></br>")
            print("<input type='submit' name='submit'>")
            print("</form>")

if form.getvalue('deposit'):
    print("<h2>Account creation initiated successfully</h2>")
    g=open("actdata.txt","a")
    g.write(form.getvalue('ssn'))
    g.write(" ")
    g.write(form.getvalue('cid'))
    g.write(" ")
    g.write(str(int(random.uniform(111111111,999999999))))
    g.write(" ")
    g.write(form.getvalue('act'))
    g.write(" ")
    g.write(form.getvalue('deposit'))
    g.write("\n")
    kk=open("actstat.txt","a")
    kk.write(form.getvalue('cid'))
    kk.write(",")
    kk.write(form.getvalue('act'))
    kk.write(",")
    kk.write("Active")
    kk.write(",")
    kk.write("Account-creation-successful")
    kk.write(",")
    now = datetime.now()
    kk.write(str(now.strftime("%d/%m/%Y-%H:%M:%S")))
    kk.write(",")
    kk.write("\n")
    kk.close()
print("</body></html>")
