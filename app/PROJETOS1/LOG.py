import subprocess
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def send_email(image_path):
    # Configurações do servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'jffilho500@gmail.com'
    smtp_password = 'xsujddrvujadbsti'
    sender_email = 'jffilho500@gmail.com'
    receiver_email = 'jffilho618@gmail.com'

    # Criação da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Intruso detectado'

    # Adiciona texto à mensagem
    body = MIMEText('Uma tentativa de login incorreta foi detectada.')
    msg.attach(body)

    # Adiciona imagem à mensagem
    with open(image_path, 'rb') as f:
        img = MIMEImage(f.read())
        msg.attach(img)

    # Envia e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def capture_photo(photo_path):
    # Comando para capturar uma foto com fswebcam
    command = f'fswebcam -r 1280x720 {photo_path}'

    # Executa o comando usando subprocess
    subprocess.run(command, shell=True)

import subprocess
import re

# Variável global para controlar o envio de email


def monitor_auth_log():
    email_sent=False

    tail_process = subprocess.Popen(['tail', '-F', '/var/log/auth.log'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Started monitoring...")
    
    try:
        while True:
            line = tail_process.stdout.readline().decode().strip()
            if 'authentication failure' in line and not email_sent:
                # Extrai o usuário do registro de autenticação
                x = re.search(r'authentication failure.*user=([\w-]+)', line)
                print("Line:", line)
                print("Match object:", x)
                if x:
                    for i in range(3):
                        username = x.group(1)
                        # Captura uma foto
                        photo_path = '/home/bomb4/Documentos/PROJETOS/fotos/photo.jpg'
                        capture_photo(photo_path)
                        # Envia a foto por e-mail
                        send_email(photo_path)
                    email_sent = True  # Marca que o email foi enviado
                     # Sai do loop após enviar o email
    except KeyboardInterrupt:
        print("Stopping monitoring...")

if __name__ == "__main__":
    monitor_auth_log()
