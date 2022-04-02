import smtplib

username = 'allowcookies2022@gmail.com'
password = 'ACookies'


def send_mail(text='Email_body', subject='Hello word', from_email='', to_emails=[]):
    assert isinstance(to_emails, list)
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, 'Hi kids!')
    server.quit()
