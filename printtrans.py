#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>Print Screen</h1>")
print("<form action='/cgi-bin/printtrans.py'  method='post'>")
print("ssn: <input type='text' name='ssn'>")
print("Number of transactions: <input type='number' name='tn'>")
print("<input type='submit'>")
print("</form>")

form=cgi.FieldStorage()
ssn=form.getvalue('ssn')
tn=form.getvalue('tn')
tlist=[]

fd=open("statement.txt","r")
o=fd.readlines()
x=len(o)
f=open("statement.txt","r")
for line in f:
    for w in line.split(","):
        if str(w)==str(ssn):
            h=line
            for s in h.split(","):
                tlist.append(s)
            if int(tn)<x:
                with open("trans.txt","a") as t:
                    t.write(line)
        
if form.getvalue('tn'):
    print("<a href='http://localhost/cgi-bin/trans.txt' download>download</a>")
print("</body></html>")