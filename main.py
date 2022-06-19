# importanto
import os 
import time
import smtplib
from email.message import EmailMessage

# importanto variavel 
from conta import senha 
from conta import mail 

# Configuração de email e senha
EMAIL_ADDRESS = mail
EMAIL_PASSWORD = senha

# Criando e-mail

msg = EmailMessage()

# Titulo do email
msg ['Subject'] = 'Mensagem de titulo'
msg ['From'] = ''
msg['To'] = ''
msg.set_content('Mensagem dentro do email')

 # Enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',443) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)

