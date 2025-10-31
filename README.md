# 🛒 Amazon Price Tracker Bot --- Day 47 of Python Bootcamp 🚀

Welcome to **Day 47** of my Python Bootcamp journey! 🎯
Today, I built a **web-scraping price tracker** that watches a product
on Amazon and sends me an **email alert** 📩 when the price drops below
a chosen value (in this case, **\$100**) 💸.

---

## 📌 Project Overview

This Python script:

✅ Visits an Amazon product page  
✅ Scrapes the **current product price** using BeautifulSoup  
✅ Converts the scraped price into a numeric value  
✅ Checks if the price is below \$100\  
✅ Sends an **email alert automatically** if the condition is met 👇  
>/ "Hey! The price dropped --- go buy it!" 🛍️

Perfect for saving money and learning web automation! 😉

---

## 🧠 What I Learned

- 🌐 **Web scraping** with `requests` + `BeautifulSoup`
- 🕵️ Extracting HTML elements & parsing price values
- ✉️ Sending emails using `smtplib`
- 🔐 Securing credentials using **Environment Variables**
- 🧮 Converting scraped text to numeric price
- 📊 Automating price monitoring logic

---

## 📂 Code Summary

The script performs:

Step Action

---

1️⃣ Import libraries  
2️⃣ Fetch product URL  
3️⃣ Scrape price info  
4️⃣ Convert price to float  
5️⃣ Compare price vs target  
6️⃣ If lower → send email notification

---

## 🛠️ Technologies Used

- Python 🐍
- Requests 🌐
- BeautifulSoup 🥣
- smtplib ✉️
- OS module 🔐 (for environment variables)

---

## 🖥️ Example Alert Message

> **Subject:** Amazon Price Alert!  
> Good news! Your tracked item is now under \$100 🎉  
> 👉 Product Link: _(product URL)_

---

## 🏁 Final Thoughts

This project helped me combine:

✨ Automation  
✨ Web scraping  
✨ Real-world email alerts

and it reminded me how useful Python can be outside the browser!
