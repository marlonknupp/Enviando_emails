import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


clientes = pd.read_excel('./clientes.xlsx')

for index, cliente in clientes.iterrows():
    msg = MIMEMultipart()
    msg['Subject'] = 'email de marlon_knupp :)'
    msg['From'] = 'marlonjcc23@gmail.com'
    msg ['to'] = cliente ['email']
    message = f'Fala,{cliente['nome']}. voce esta recebendo um email de um projeto pessoal de marlon_knupp!'
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    server.login('marlonjcc23@gmail.com','vhbw njqk hnzf gtwo')   # email / Senha
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

##
    
    