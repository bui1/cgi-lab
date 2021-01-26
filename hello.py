#!/usr/bin/env python3
import sys
from secret import username, password
from templates import login_page, secret_page
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
print("Set-Cookie: is_logged_in=false")
print()
print("""
<!doctype html>

<html>
<body>
""")

print(login_page())


print("""
</body>
</html>
""")
