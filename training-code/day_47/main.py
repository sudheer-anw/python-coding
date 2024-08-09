import requests
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

# URL of the product you want to monitor
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# User-Agent header to simulate a request from a web browser
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Email credentials and settings
sender_email = "your_email@example.com"
sender_password = "your_password"
recipient_email = "recipient_email@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def get_request(url, headers, retries=5, backoff_factor=1):
    for i in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {i + 1} failed: {e}")
            if i < retries - 1:
                time.sleep(backoff_factor * (2 ** i))  # Exponential backoff
            else:
                raise
    return None

def extract_price(html):
    soup = BeautifulSoup(html, 'html.parser')
    price_element = soup.find("span", {"id": "priceblock_ourprice"}) or \
                    soup.find("span", {"id": "priceblock_dealprice"}) or \
                    soup.find("span", {"class": "a-price-whole"}) or \
                    soup.find("span", {"class": "a-price a-text-price"})
    
    if price_element:
        price = price_element.get_text().strip()
        return price
    else:
        with open("amazon_page.html", "w", encoding='utf-8') as f:
            f.write(html)
        print("Price element not found. HTML saved to amazon_page.html for debugging.")
    return None

# Main execution block
previous_price = None
try:
    while True:
        response = get_request(url, header)
        if response:
            print("Request succeeded.")
            current_price = extract_price(response.text)
            if current_price:
                print(f"Current price: {current_price}")
                if previous_price and current_price != previous_price:
                    send_email("Price Update", f"The price has changed from {previous_price} to {current_price}.")
                previous_price = current_price
            else:
                print("Failed to extract price.")
        else:
            print("Failed to retrieve data.")
        time.sleep(60)  # Wait for 1 minute before checking again
except requests.exceptions.RequestException as e:
    print(f"Failed to retrieve data: {e}")
except KeyboardInterrupt:
    print("Script terminated by user.")
