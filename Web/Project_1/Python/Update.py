#!/usr/local/bin/python3
print("Content-Type: text/html\n")
import cgi, view, html_sanitizer
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    with open('Data/'+pageId, 'r') as file :
        description=file.read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
<button class="button button2" onclick="location.href='Python.html'">Go Back</button>
  <h1><a href="Python.py">WEB</a></h1>
  <ol>
    {liststr}
  </ol>
  <p><a href="Create.py">Create</a></p>
  <form action="Process_Update.py" method="post">
  <fieldset style = "width:300px; height:500px;">
  <legend>Information You Create</legend>
  <input type="hidden" name="pageId" value="{form_default_title}"
  Title : <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
  Description : <p><textarea rows="4"style="overflow:visible;" name="description"
  placeholder="description">{form_default_description}</textarea></p>
  <input type = "submit" value = "submit"/>
  <input type = "reset" value = "reset"/><br><br>
  </fieldset>
</body>
</html>
'''.format(title=pageId,
           liststr=view.get_list(),
           description=description,
           form_default_title=pageId,
           form_default_description=description))
