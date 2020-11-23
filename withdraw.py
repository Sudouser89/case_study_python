#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb, random
from datetime import datetime
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>Withdraw Screen</h1>")
print("<form action='/cgi-bin/withdraw.py'  method='post'>")
print("ssn: <input type='text' name='ssn'>")
print("<input type='submit'>")
print("</form>")

form=cgi.FieldStorage()
ssn=form.getvalue('ssn')
tlist=[]
    
f=open("actdata.txt","r")
for line in f:
    for w in line.split():
        if str(w)==str(ssn):
            h=line
            for s in h.split():
                tlist.append(s)
            print("<h2>Data Found for "+str(ssn)+"</h2>")
            print("<form action='/cgi-bin/withdraw.py'  method='post'>")
            print("<textarea hidden name='data'  rows='2' cols='40'>"+line+"</textarea></br>")
            print("SSN: <input readonly type='text' name='ssn' value="+tlist[0]+"></br>")
            print("Customer id: <input readonly type='text' name='cid' value="+tlist[1]+"></br>")
            print("Account id: <input readonly type='text' name='aid' value="+tlist[2]+"></br>")
            print("Account type: <input readonly type='text' name='atype' value="+tlist[3]+"></br>")
            print("Balance: <input readonly type='text' name='balance' value="+tlist[4]+"></br>")
            print("Withdraw Amount: <input type='number' name='withdraw'></br>")
            print("<input type='submit' name='submit'>")
            print("</form>")

if form.getvalue('withdraw'):
    print("<h2>Amount withdrawn successfully</h2>")
    h=form.getvalue('data')
    ssn=form.getvalue('ssn')
    cid=form.getvalue('cid')
    aid=form.getvalue('aid')
    atype=form.getvalue('atype')
    balance=form.getvalue('balance')
    withdraw=form.getvalue('withdraw')
    g=open("actdata.txt","a")
    g.write(ssn)
    g.write(" ")
    g.write(cid)
    g.write(" ")
    g.write(aid)
    g.write(" ")
    g.write(atype)
    g.write(" ")
    g.write(str(int(balance)-int(withdraw)))
    g.write("\n")
    with open("actdata.txt", "r+") as ff:
        d = ff.readlines()
        ff.seek(0)
        for i in d:
            if i.strip() != h.strip():
                ff.write(i)
        ff.truncate()
    kkk=open("statement.txt","a")
    kkk.write(ssn)
    kkk.write(",")
    kkk.write(str(int(random.uniform(111111111,999999999))))
    kkk.write(",")
    kkk.write("Withdraw")
    kkk.write(",")
    now = datetime.now()
    kkk.write(str(now.strftime("%d/%m/%Y-%H:%M:%S")))
    kkk.write(",")
    kkk.write(withdraw)
    kkk.write(",")    
    kkk.write("\n")
    kkk.close()
print("</body></html>")