import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("bincybiju50@gmail.com","nauwxdeywobzojxo")
msg="Gowww...irangi podi pichakkari"
try:
    s.sendmail("bincybiju50@gmail.com","ksgowri3@gmail.com",msg)
    print("Mail sent successfully")
except:
    print("Mail not sent,Wrong email address of reciever")
s.quit()