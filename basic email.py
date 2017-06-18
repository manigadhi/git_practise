"""
We are adding the email config
"""
import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("gadhimani430@gmail.com", "9535895336")
msg = "i love u veena"
server.sendmail("gadhimani430@gmail.com", "manivna@gmail.com", "i love u veena")
server.quit()
