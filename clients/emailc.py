import email
import imaplib
import re
from datetime import datetime

from config import SMTP_SERVER, EMAIL_PWD, EMAIL, PATTERN_TEXT
from entity.EmailDto import EmailDto


def connect():
    imap = imaplib.IMAP4_SSL(SMTP_SERVER)
    imap.login(EMAIL, EMAIL_PWD)
    imap.select("BCC")
    return imap


def close(imap: imaplib.IMAP4):
    imap.close()
    imap.logout()


def get_all_unseen_mail(imap: imaplib.IMAP4):
    _, data = imap.uid('search', "ALL")  # UNSEEN
    ids = data[0].split()
    return [get_mail_by_id(imap, id) for id in ids]


def get_mail_by_id(imap: imaplib.IMAP4, id: int):
    _, data = imap.uid('fetch', id, '(RFC822)')

    email_message = email.message_from_string(data[0][1].decode('utf-8'))
    date_message = re.sub(r" \(\w+\)", '', email_message['Date'])
    body_message = str(email_message.get_payload(decode=True).decode('utf-8'))

    match = re.compile(PATTERN_TEXT).match(body_message)
    return (
        EmailDto()
        .with_id(id)
        .with_email_time(datetime.strptime(date_message, "%a, %d %b %Y %H:%M:%S %z"))
        .with_trn_time(datetime.strptime(f"{match.group('trn_date')} {match.group('trn_time')}", "%d.%m.%y %H.%M.%S"))
        .with_trn_amount(match.group("trn_amount"))
        .with_trn_currency(match.group("trn_currency"))
        .with_balance(match.group("balance"))
        .with_balance_currency(match.group("balance_currency"))
        .with_merchant(match.group("merchant"))
    )


def get_balance(imap: imaplib.IMAP4):
    pass
