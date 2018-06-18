import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


email_template_html = """
Olá! <br>
Nós somos da equipe Licitando. Nossa missão é oferecer auxílio para que sua empresa participe de novos negócios. De quebra, os órgãos públicos compram produtos a um preço justo :)
<br>
Nós selecionamos oportunidades que podem se encaixar no perfil da sua empresa. Clique no link abaixo:
<br>
<a href='https://2414abd3.ngrok.io/?q=lapis'>Quero conhecer novos negócios</a>
<br>
Obrigado pelo apoio e bons negócios!
<br>
<em>Atenciosamente, <br>
Equipe Licitando.
</em>
"""

email_template_text = """
Olá! \n
Nós somos da equipe Licitando. Nossa missão é oferecer auxílio para que sua empresa participe de novos negócios. De quebra, os órgãos públicos compram produtos a um preço justo :)
\n
Nós selecionamos oportunidades que podem se encaixar no perfil da sua empresa. Clique no link abaixo:
\n
Quero conhecer novos negócios
\n
Obrigado pelo apoio e bons negócios!
\n
Atenciosamente, \n
Equipe Licitando.
</em>
"""


# def send_email(user, pwd, recipient, subject, body):
#     import smtplib
#
#     FROM = user
#     TO = recipient if isinstance(recipient, list) else [recipient]
#     SUBJECT = subject
#     TEXT = body
#
#     # Prepare actual message
#     message = """From: %s\nTo: %s\nSubject: %s\n\n%s
#     """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.ehlo()
#         server.starttls()
#         server.login(user, pwd)
#         server.sendmail(FROM, TO, message)
#         server.close()
#
#         print('successfully sent the mail')
#     except:
#         print("failed to send mail")


def send_email(user, pwd, recipient, subject):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    msg = MIMEMultipart('alternative')
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)

        part2 = MIMEText(email_template_html, 'html')
        msg.attach(part2)

        msg['Subject'] = subject
        server.sendmail(FROM, TO, msg.as_string())

        print('successfully sent the mail')
    except:
        print("failed to send mail")


if __name__ == '__main__':
    send_email(
        'vedolinproducoes',
        EMAIL_HOST_PASSWORD,
        'henriquesamchou@gmail.com',
        'Plataforma Licitando - Oportunidades',
    )