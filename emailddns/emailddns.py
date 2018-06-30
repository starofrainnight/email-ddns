# -*- coding: utf-8 -*-

"""Main module."""

import email
import ipgetter
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.header import Header
from .exceptions import NoEMailError, EMailFetchError


def send_update_email(host, port, account, password):
    server = smtplib.SMTP_SSL(host, port)
    server.login(account, password)
    try:
        myip = ipgetter.myip()

        # Send to my self
        message = MIMEText(myip, 'plain', 'utf-8')
        message['From'] = Header("SELF <%s>" % account, 'utf-8')
        message['To'] = Header("SELF <%s>" % account, 'utf-8')
        message['Subject'] = Header("[EMAIL-DDNS:UPDATE]", 'utf-8')

        server.sendmail(account, [account], message.as_string())
    finally:
        server.quit()


def fetch_update_email(host, port, account, password):
    if port <= 0:
        port = imaplib.IMAP4_SSL_PORT

    conn = imaplib.IMAP4_SSL(host, port)
    conn.login(account, password)
    try:
        conn.select()
        typ, msg_nums = conn.search('utf-8', '(FROM "SELF")')
        nums = msg_nums[0].split()
        if len(nums) <= 0:
            raise NoEMailError("There does not have E-Mails!")

        num = nums[-1]  # Latest email
        typ, data = conn.fetch(num, '(RFC822)')
        if typ != 'OK':
            raise EMailFetchError("Failed to get email index: %s" % num)

        msg = email.message_from_string(data[0][1].decode())
        ip = msg.get_payload(decode=True).decode()
        return ip
    finally:
        conn.close()
        conn.logout()


def clear_update_emails(host, port, account, password):
    """Clear all update emails except latest one
    """

    if port <= 0:
        port = imaplib.IMAP4_SSL_PORT

    conn = imaplib.IMAP4_SSL(host, port)
    conn.login(account, password)
    try:
        conn.select()
        typ, msg_nums = conn.search('utf-8', '(FROM "SELF")')
        nums = msg_nums[0].split()
        if len(nums) <= 0:
            return

        # Remove all related e-mails except latest one
        nums = nums[:-1]
        for num in nums:
            conn.store(num, '+FLAGS', '\\Deleted')
        conn.expunge()
    finally:
        conn.close()
        conn.logout()
