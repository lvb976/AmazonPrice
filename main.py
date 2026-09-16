import requests
import os
import smtplib
from bs4 import BeautifulSoup
responce=requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","Accept-Language": "en-US,en;q=0.9"})
soup=BeautifulSoup(responce.text,"html.parser")
url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
price_class=soup.select_one(".a-price-whole")
print(price_class)
price=float(price_class.get_text().replace(",",""))
print(price)
password=os.environ.get("PASSWORD")
my_email="lvb976@gmail.com"
# to_email="venkatabalajilanka@gmail.com"
# if price<7400:
#     with smtplib.SMTP("smtp.gmail.com",587) as connection:
#         connection.starttls()
#         connection.login(user=my_email,password=password)
#         connection.sendmail(from_addr=my_email,to_addrs=to_email,msg=f"Subject:Am@zon Price Alert!\n\nInstant Pot Duo Evo Plus 9-in-1 Electric Pressure Cooker,Sterilizer,Slow Cooker,Rice Cooker,Grain Marker,Sous Vide,and Warmer,6 Quart,10 programs is now below $90 \n{url}")
#
