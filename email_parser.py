import csv
import glob
import os
import re
from email import policy
from email.parser import BytesParser
from typing import Union

EMAIL_FOLDER  = "emails" 
ATTACHMENT_FOLDER = "attachments"

def get_clean_email(email: str) -> Union[str,None]:
    """Get a clean email address from the email header"""
    match  = re.findall(r'[\w\.-]+@[\w\.-]+', email)
    return match[0] if match else None

def parse_email(email_file: str) -> dict:
    """Parse an email file and return a dictionary containing the email metadata"""
    with open(email_file, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
        save_attachment_file(msg)
        attachment = ', '.join(
            [part.get_filename() for part in msg.iter_attachments()]
        )
        email_metadata =  {
            'to': get_clean_email(msg['to']),
            'from': get_clean_email(msg['from']),
            'subject': msg['subject'],
            'body': msg.get_body(preferencelist=('html')).get_content(),
            'time': msg['date'],
            'attachments': attachment
        }
        return email_metadata

def get_email_files() -> list:
    """Get all email files from the email folder"""
    return glob.glob(os.path.join(EMAIL_FOLDER, '**/*.eml'), recursive=True)


def save_attachment_file(msg: BytesParser)-> None:
    """Save an attachment file from an email message"""
    for part in msg.iter_attachments():
        filename = part.get_filename()
        if filename:
            with open(os.path.join(ATTACHMENT_FOLDER, filename), 'wb') as fp:
                fp.write(part.get_content())

def render_data_to_csv(data: list) -> None:
    """Render the data into a CSV file"""
    with open("data.csv", "w", newline="") as csv_file:
        fieldnames = ['to', 'from', 'subject','body', 'time', 'attachments']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for email_data in data:
            writer.writerow(email_data)


if __name__ == "__main__":
    email_files = get_email_files()
    parsed_emails = [parse_email(email_file) for email_file in email_files]
    render_data_to_csv(parsed_emails)

