import re
import smtplib, ssl
from email.message import EmailMessage

def check_emails (text):
  emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
  if emails == []:
    return "No email"
  else:
    return "emails"

def send_email (body):
  port = 465  # For SSL

  password="G#fT@tKLzO"

  msg = EmailMessage()
  msg.set_content('The following is their message with contact info.' + body)

  msg['Subject'] = 'Please follow up with customer'
  msg['From'] = "support@quadbase.com"
  msg['To'] = "support@quadbase.com"

# Send the message via our own SMTP server.
  server = smtplib.SMTP_SSL("box5109.bluehost.com", port)
  server.login("aes+quadbase.com", password)
  server.send_message(msg)
  server.quit()