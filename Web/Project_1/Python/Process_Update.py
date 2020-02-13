#!/usr/local/bin/python3

import cgi,os
form = cgi.FieldStorage()
pageId=form["pageId"].value
title = form["title"].value
description = form['description'].value

with open("Data/"+pageId, "w") as new_file :
    new_file.write(description)

os.rename('Data/'+pageId, 'Data/'+title)
#Redirection
print("location: Python.py?id="+title)
print()
