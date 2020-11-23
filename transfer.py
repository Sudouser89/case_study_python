#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb, random
from datetime import datetime
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>Transfer Screen</h1>")
print("<form action='/cgi-bin/transfer.py'  method='post'>")
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
            print("<form action='/cgi-bin/transfer.py'  method='post'>")
            print("<textarea hidden name='data'  rows='2' cols='40'>"+line+"</textarea></br>")
            print("SSN: <input readonly type='text' name='ssn' value="+tlist[0]+"></br>")
            print("Source account id: <input readonly type='text' name='aid' value="+tlist[2]+"></br>")
            print("Target SSN: <input type='text' name='target'></br>")
            print("Source Balance: <input readonly type='text' name='balance' value="+tlist[4]+"></br>")
            print("Transfer Amount: <input type='number' name='transfer'></br>")
            print("<input type='submit' name='submit'>")
            print("</form>")

if form.getvalue('transfer'):
    print("<h2>Amount transfer completed successfully</h2>")
    h=form.getvalue('data')
    u=[]
    for i in h.split():
        u.append(i)
    cid=u[1]
    aid=u[2]
    atype=u[3]
    ssn=form.getvalue('ssn')
    tssn=form.getvalue('target')
    sbalance=form.getvalue('balance')
    transfer=form.getvalue('transfer')
    g=open("actdata.txt","a")
    g.write(ssn)
    g.write(" ")
    g.write(cid)
    g.write(" ")
    g.write(aid)
    g.write(" ")
    g.write(atype)
    g.write(" ")
    g.write(str(int(sbalance)-int(transfer)))
    g.write("\n")
    with open("actdata.txt", "r+") as ff:
        d = ff.readlines()
        ff.seek(0)
        for i in d:
            if i.strip() != h.strip():
                ff.write(i)
        ff.truncate()
    fg=open("actdata.txt","r")
    kk=[]
    for line in fg:
        for wk in line.split():
            if str(wk)==tssn:
                g=line
                for t in g.split():
                    kk.append(t)
                tcid=kk[1]
                taid=kk[2]
                tatype=kk[3]
                tbalance=kk[4]
                gt=open("actdata.txt","a")
                gt.write(tssn)
                gt.write(" ")
                gt.write(tcid)
                gt.write(" ")
                gt.write(taid)
                gt.write(" ")
                gt.write(tatype)
                gt.write(" ")
                gt.write(str(int(tbalance)+int(transfer)))
                gt.write("\n")
                with open("actdata.txt", "r+") as fff:
                    dt = fff.readlines()
                    fff.seek(0)
                    for j in dt:
                        if j.strip() != g.strip():
                            fff.write(j)
                    fff.truncate()
    kkk=open("statement.txt","a")
    kkk.write(ssn)
    kkk.write(",")
    kkk.write(str(int(random.uniform(111111111,999999999))))
    kkk.write(",")
    kkk.write("Transfer")
    kkk.write(",")
    now = datetime.now()
    kkk.write(str(now.strftime("%d/%m/%Y-%H:%M:%S")))
    kkk.write(",")
    kkk.write(transfer)
    kkk.write(",")    
    kkk.write("\n")
    kkk.close()
print("</body></html>")