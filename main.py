#Imports
import requests
from bs4 import BeautifulSoup
import smtplib
import os

#Url and headers
url = "https://www.amazon.ca/Instant-Electric-Pressure-Sterilizer-Stainless/dp/B00FLYWNYQ/ref=sr_1_1?crid=1ZJFGOE6CDVIW&dib=eyJ2IjoiMSJ9.y4LLAMvRXyF-GJBFF44YpgoQFm3qlOqvoway1SDbaoV2dPjBL7Ke0ur9UOqGNDVb6Ef6Sur5iS1dsFQj9AR6k3zfrzrMP43ZZ86apRbHNjwwm4f65kU_GKyMmGoAizzPhlNIXZEU3iHPLtFA2ff6HrC6rTQIV1JjcLpYDN52cstqfLXk2xA8ls4k_criG-MdBPsHWIfxqbggAcmwZLBY3pu91RN1bkvF6apXkLlF2oUphRn23r0SHg5_4yn-vOGSyJeJKRnRyM7PYm-TAggnN_P8ndTJpATnH9-TO1lmU_E.08QcYus6CARBUYbmQW_p9es3-Nn7sHBw4SFvlEW04pA&dib_tag=se&keywords=instant+pot+duo&qid=1761722414&sprefix=%2Caps%2C88&sr=8-1"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}
#Request
response = requests.get(url,headers= headers)

#Email and Password
my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_EMAIL_PASSWORD")
address = os.getenv("TO_EMAIL")

#Scraping the Website
soup = BeautifulSoup(response.content,"html.parser")

#Getting Exact Price
whole = soup.find("span",class_="a-price-whole").get_text(strip=True)
fraction = soup.find("span", class_="a-price-fraction").get_text(strip=True)
price = float(f"{whole}{fraction}")

#Condition and Sending Mail
if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=address,
            msg=f"Subject:Amazon Price Alert!\n\nInstant Pot Duo Evo Plus 9-in-1 Electric Pressure Cooker, Sterilizer, Slow Cooker, Rice Cooker, Grain Maker, Steamer, Saute, Yogurt Maker, Sous Vide, Bake, and Warmer, 6 Quart, 10 Programs is now under $100 \n {url}")
