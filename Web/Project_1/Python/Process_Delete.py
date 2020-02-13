#!/usr/local/bin/python3

import cgi ,os
form = cgi.FieldStorage()
pageId = form["pageId"].value


os.remove("Data/"+pageId)


#Redirection
print("location: Python.py")
print()
