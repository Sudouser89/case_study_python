#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1>Customer details Screen</h1>")
print("<form action='/cgi-bin/custsearch.py'  method='post'>")
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
            print("<table style='border: 1px solid black'>")
            print("<tr>")
            print("<th style='border: 1px solid black'>SSN</th>")
            print("<th style='border: 1px solid black'>Customer ID</th>")
            print("<th style='border: 1px solid black'>Name</th>")
            print("<th style='border: 1px solid black'>Age</th>")
            print("<th style='border: 1px solid black'>Address 1</th>")
            print("<th style='border: 1px solid black'>Address 2</th>")
            print("<th style='border: 1px solid black'>City</th>")
            print("<th style='border: 1px solid black'>State</th>")
            print("</tr>")
            print("<tr>")
            print("<td style='border: 1px solid black'>"+tlist[0]+"</td>")
            print("<td style='border: 1px solid black'>"+tlist[1]+"</td>")
            print("<td style='border: 1px solid black'>"+tlist[2]+"</td>")
            print("<td style='border: 1px solid black'>"+tlist[3]+"</td>")
            print("<td style='border: 1px solid black'>"+tlist[4]+"</td>")
            print("<td style='border: 1px solid black'>"+tlist[5]+"</td>")
            print("<td style='border: 1px solid black'>"+tlist[6]+"</td>")
            print("<td style='border: 1px solid black'>"+tlist[7]+"</td>")
            print("</tr>")
            print("</table>")
            tlist=[]
print("</body></html>")