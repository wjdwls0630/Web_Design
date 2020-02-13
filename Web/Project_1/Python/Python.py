#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi, view,html_sanitizer
sanitizer=html_sanitizer.Sanitizer()
form = cgi.FieldStorage()
if 'id' in form:
    title=pageId = form["id"].value
    title=sanitizer.sanitize(title)
    with open('Data/'+pageId, 'r') as file :
        description=file.read()
        description=sanitizer.sanitize(description)
    update_link="<a href='Update.py?id={pageId}'>Update</a>".format(pageId=pageId)
    delete_action="""
    <form action="Process_Delete.py" method="post">
    <input type="hidden" name="pageId" value={pageId}>
    <input type='submit' value='Delete'>
    </form>
    """.format(pageId=pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link=""
    delete_action=""
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
  <a href="Create.py">Create</a>
  {update_link}
  {delete}
  <h2>{title}</h2>
  <p>{description}</p>

</body>
</html>
'''.format(title=pageId, liststr=view.get_list(),update_link=update_link,delete=delete_action,description=description))
