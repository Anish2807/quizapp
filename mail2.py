import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("anish4726@gmail.com","7631457585")
"""
message = "Hello Sir"

s.sendmail("anish4726@gmail.com","anishlnct12@gmail.com",message)

s.quit()
"""
