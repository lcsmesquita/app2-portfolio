import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "lucas.mesquita1110@gmail.com"
password = "noypxcjzddhpmkro"

receiver = "lucas.mesquita1110@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: First e-mail automation
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)