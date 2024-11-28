import smtplib
from email.mime.text import MIMEText

def send_email():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'jffilho500@gmail.com'  # Substitua pelo seu endereço de e-mail
    smtp_password = ''  # Substitua pela sua senha de e-mail

    sender_email = 'jffilho500@gmail.com'  # Substitua pelo seu endereço de e-mail
    receiver_email = 'jffilho618@gmail.com'  # Substitua pelo endereço de e-mail do destinatário

    # Criação da mensagem de e-mail
    msg = MIMEText('Este é um e-mail de teste.')
    msg['Subject'] = 'Teste de E-mail'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Envio do e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    send_email()
