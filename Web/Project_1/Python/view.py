import os, html_sanitizer
def get_list():
    sanitizer=html_sanitizer.Sanitizer()
    files=os.listdir("Data")
    liststr=""
    for item in files :
        item=sanitizer.sanitize(item)
        liststr=liststr+"<li><a href='Python.py?id={name}'>{name}</a></li>".format(name=item)
    return liststr
