import requests
from bs4 import BeautifulSoup
import smtplib


url = 'https://www.amazon.in/Samsung-Galaxy-Smartphone-Silver-Storage/dp/B0DSKNHX1T/ref=sr_1_4?dib=eyJ2IjoiMSJ9.TnXF_RGJpd3TbN40AampmFNzchw8IaU0Jj-aomhOgolnFOJoLDYiauy1PvzevI9ZLl4R56BuXZ2TCLj-OdDtPElws_k4HETnLM3qZY5c4DFihLEMLZifZqnU9e35MjnwyxiyjgeIyVe0OVGI-bBbY_3GPdVmSLaJtfuK54mwywGeYBL3i8D2HBoSGYeqCCI7XKELoq8SAngRnCeXpluJBI6V5LQXt08YbrKU5McVjkY.B_xCVOTw24M2D-i287996_0yKT3RN-rVSOWg9w0ttrM&dib_tag=se&keywords=25&qid=1794743382&sr=8-4'
response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

price_element = soup.find(class_="a-price-whole")
product_title_element = soup.find(id="productTitle")

if price_element and product_title_element:
    price_text = price_element.get_text(strip=True)
    product_title = product_title_element.get_text(strip=True)
    current_price = int(price_text.replace(",", "").replace(".", ""))
    message = f"""Subject: Amazon Price Alert

    Product: {product_title}

    Current Price: Rs {current_price:,}

    Product Link:{url}
    """
    print(f"Current price: ₹{current_price:,}")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(from_accounnt, PASSWORD)
        connection.sendmail(from_accounnt, to_account, msg=message.encode("utf-8"))
        print("Price alert email sent successfully.")
else:
    print("Price not found.")

