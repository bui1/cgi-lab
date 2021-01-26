#!/usr/bin/env python3
import sys
from secret import username, password
from templates import login_page, secret_page
import json
import os
import cgi
import cgitb
cgitb.enable()

# Getting form cgi values
# From Nosklo https://stackoverflow.com/users/17160/nosklo
# From StackOverflow
# From https://stackoverflow.com/a/464977
form = cgi.FieldStorage()  # can handle POST too

input_username = form.getvalue('username')
input_password = form.getvalue('password')


if (input_username == username and input_password == password):
    print("Set-Cookie: is_logged_in=true")


print("Content-Type: text/html\n")
print()
for parameter in os.environ["HTTP_COOKIE"].split(';'):
    name, value = parameter.split("=")
    if value == "true":
        print("""<!doctype html>
            <html>
            <body>
            """)
        print(secret_page(input_username, input_password))
        print("""
                </body>
                </html>
                """)
