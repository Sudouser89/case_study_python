#!C:\Users\Pavan\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
print("Content-type: text/html\r\n\r\n") 
form = cgi.FieldStorage()
# Get data from fields
nm=form.getvalue('name')
cp=form.getvalue('cp')
def admindata():
    if nm=="admin" and cp=="admin":
        redirectURL = "http://localhost/adminhome.html"
        print("<html>")
        print("<head>")
        print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'"/>') 
        print("</head>")
        print("</html>")
    else:
        print("<html>")
        print("<body>")
        print("<h1>wrong uname or pwd</h1>")
        print("</body>")
        print("</html>")
def cashdata():
    if nm=="cash" and cp=="cash":
        redirectURL = "http://localhost/cashhome.html"
        print("<html>")
        print("<head>")
        print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'"/>') 
        print("</head>")
        print("</html>")
    else:
        print("<html>")
        print("<body>")
        print("<h1>wrong uname or pwd</h1>")
        print("</body>")
        print("</html>")

if __name__== "__main__":
  admindata()
  cashdata()