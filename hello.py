#!/usr/bin/env python3
import json
import os
import cgi
import cgitb
cgitb.enable()

# print('Content-Type: application/json')
# print()
# print(json.dumps(dict(os.environ), indent=2))

# print('Content-Type: text/html')
# print()
# print("""
# <!doctype html>

# <html>
# <body>
# <h1> HELLO </h1>)
# <ul>
# """)

# print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']} </p>")
# print(f"<p> BROWSER={os.environ['HTTP_USER_AGENT']} </p>")
# print("<ul>")
# for parameter in os.environ["QUERY_STRING"].split('&'):
#     name, value = parameter.split("=")
#     print(f"<li><em>{name}</em> = {value}</li>")

# print("</ul>")
# print("""
# </ul>
# </body>
# </html>
# """)

print('Content-Type: text/html')
print()
print("""
<!doctype html>

<html>
<body>
""")
print("""

    <h1> Welcome! </h1>

    <form method="POST">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>

""")

# Getting form cgi values
# From Nosklo https://stackoverflow.com/users/17160/nosklo
# From StackOvefflow
# From https://stackoverflow.com/a/464977
form = cgi.FieldStorage()  # can handle POST too

username = form.getvalue('user')
password = form.getvalue('password')

print(f"<h2> username={username}")
print(f"<h2> password={password}")

print("""
</body>
</html>
""")
