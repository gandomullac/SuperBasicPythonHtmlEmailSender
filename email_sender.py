import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import time

# Load environment variables from the .env file
load_dotenv()

# SMTP server configuration
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))
smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')

# Email configuration
subject = os.getenv('SUBJECT')
mailing_list_file = os.getenv('MAILING_LIST_FILE')
html_email_file = os.getenv('HTML_EMAIL_FILE')
from_address = os.getenv('FROM_ADDRESS')

# Read data from the Excel file
df = pd.read_excel(mailing_list_file, engine='openpyxl')

# Iterate through each row of the DataFrame
for index, row in df.iterrows():
    to_address = row['Address']
    name = row['Name']

    # Read HTML content from the email and replace $NAME
    with open(html_email_file, 'r', encoding='utf-8') as file:
        html_content = file.read().replace('$NAME', name)

    # Create the email message
    message = MIMEMultipart('alternative')
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = subject

    # Attach the HTML content to the email
    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_address, to_address, message.as_string())
            print(f'Email successfully sent to {to_address}!')
    except Exception as e:
        print(f'Error sending email to {to_address}: {e}')

    # Wait for 2 seconds before sending the next email
    time.sleep(2)
