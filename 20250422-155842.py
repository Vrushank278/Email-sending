from smtplib import SMTP
print("  ")
print("email handling using python")
print('---------------------------')

#take from user input

to = input("Enter email id: ")
message = input("Enter a message to send: ")

# login in smtp for google

obj = SMTP('smtp.gmail.com', 587)

#587 is required to send mail

#starting for code
obj.starttls()

#enter user id and passskey for login
obj.login("visuthakor58@gmail.com", "enuwzowfdgekohtp")

#to send massage to mail id you will enter
obj.sendmail("visuthakor58@gmail.com",to, message)

#to exit from smtp
obj.quit()

print("mail send successfully")
