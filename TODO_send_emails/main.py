# main.py
# python-mini-projects @Mitesh

import smtplib
from email.message import EmailMessage

recipents = ["XXXX@gmail.com"]

def email():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    user_email = input("Enter your email [gmail-only]: ")
    user_pass = input("Enter your password: ")
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(user_email,user_pass)
    print("Logged In")


    subject = "Automated Email From Python"
    body = "Utlilzed a Python Script to Automate Sending an Email to a list of Recipents."

    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject

    for recipent in recipents:
        s.send_message(user_email,recipent,message)
        print(f"Sent Email to {recipent}")
    

    s.quit()
    print("Done - Logging Out")


def testemail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    user_email = input("Enter your email [gmail-only]: ")
    user_pass = input("Enter your password: ")
    # Identify yourself to an ESMTP server using EHLO
    s.ehlo()

    # Secure the SMTP connection
    s.starttls()

    # Login to the server (if required)
    s.login(user_email,user_pass)


    # Send an email
    from_address = user_email
    to_address = user_email
    message = """\
    Subject: Test Email

    This is a test email message.
    """

    s.sendmail(from_address, to_address, message)

    # Quit the SMTP session
    s.quit()

if __name__ == "__main__":
    testemail()



