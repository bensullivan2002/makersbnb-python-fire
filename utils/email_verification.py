import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import urlencode


def send_confirmation_email(user_email):
    smtp_server = 'localhost'
    smtp_port = 1025
    smtp_username = 'Ben@gmail.com'
    smtp_password = 'Password123!'

    sender_email = 'no-reply@makersbnb.com'
    receiver_email = user_email
    subject = 'Confirmation E-mail'
    confirmation_link = 'https://makersbnb.com/confirm?' + urlencode({'email': user_email})
    body = (f'Thank you for signing up with MakersBnB!\n\n Please click on the following link to complete your '
            f'registration: {confirmation_link}')

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Confirmation Email has been sent. Please check your inbox.")
    except Exception as e:
        print("Error sending confirmation email:", e)
