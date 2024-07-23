import smtplib, ssl


def send_email(user_message):
    host = 'smtp.gmail.com'
    port =  465

    username = 'REPLACE WITH YOURS'
    password = 'REPLACE WITH YOURS'
    asd

    receiver_email = 'REPLACE WITH YOURS'
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, user_message)
