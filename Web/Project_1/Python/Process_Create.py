#!/usr/local/bin/python3

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

with open("Data/"+title, "w") as new_file :
    new_file.write(description)

#Redirection
print("location: Python.py?id="+title)
print()
