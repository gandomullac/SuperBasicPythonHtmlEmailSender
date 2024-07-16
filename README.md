## Email Sender Script

This repository contains a small but functional Python script designed to send personalized HTML emails to a list of recipients. It is a handy alternative to using third-party solutions and is tailored for specific use cases where customizability and control are essential.

## Features

- **Personalized Emails:** Each recipient gets a personalized email with their name dynamically inserted into the HTML content.
- **Excel Mailing List:** Uses an Excel file to manage the mailing list, making it easy to update and manage recipients.
- **Environment Configuration:** Uses environment variables to manage SMTP server settings and email content configuration, enhancing security and flexibility.
- **HTML Email Support:** Supports sending richly formatted HTML emails.

## Prerequisites
- Python 3.x
- Required Python libraries: pandas, openpyxl, smtplib, email, python-dotenv
- SMTP server credentials
- Mailing list in Excel format
- HTML email template

## Installation
1. Clone the repository:
```sh
git clone https://github.com/yourusername/email-sender-script.git
cd email-sender-script
```

2. Install the required Python libraries:

```sh
pip install pandas openpyxl python-dotenv
```

3. Create a .env file in the project directory and populate it with your SMTP server details and email settings (there is a handy `.env.example` file you can use):

```env
SMTP_SERVER=smtp.yourserver.com
SMTP_PORT=587
SMTP_USERNAME=yourusername
SMTP_PASSWORD=yourpassword
SUBJECT=Your Email Subject
MAILING_LIST_FILE=path/to/mailing_list.xlsx
HTML_EMAIL_FILE=path/to/email_template.html
FROM_ADDRESS=your.email@domain.com
```

4. Ensure you have the mailing list Excel file and HTML email template file in the specified paths.

## Usage
Run the script using Python:

```sh
python email_sender.py
```

The script will read the mailing list from the Excel file, personalize the HTML content for each recipient, and send the emails via the specified SMTP server. It waits for 2 seconds between sending each email to avoid overwhelming the server.

## Disclaimer
I advise to test the script before sending out lots of emails. This is meant for a very small amount of transactional emails (like, company invitation to dinner (this was the original goal)), I discourage using such a tool to send out marketing emails: there are services out there that do just that.

Note: Providers like Google may require an app password to use their SMTP servers. Ensure you have configured the necessary app passwords or other required authentication methods for your email provider.

## License
This project is open source and available under the MIT License.

## Contributions
Contributions, issues, and feature requests are welcome, unexpected, but definitely welcome! Feel free to check the issues page if you have any questions or suggestions.