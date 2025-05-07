from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time
#pip install selenium webdriver-manager openpyxl

# Setup headless Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the page
url = "https://irshad.az/mehsullar?q=iphone"
driver.get(url)
time.sleep(5)  # Wait for JavaScript to load

# Parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Create Excel file
wb = Workbook()
ws = wb.active
ws.title = "Irshad Apple"
ws.append(["name", "details","value"])

# Scrape products
phone = soup.find_all("div", class_="product__flex__left-right")
phones = soup.find_all("div", class_="product__flex-right")

# Minimum ortaq say qədər dövr
count = min(len(phone), len(phones))

for i in range(count):
    
    name_tag =phone[i].find("a", class_="product__name")
    details_tag =phone[i].find("dl", class_="product__details")
    value_tag =phones[i].find("p", class_="new-price")    

    name = name_tag.get_text(strip=True) if name_tag else ""
    details = details_tag.get_text(strip=True) if details_tag else ""  
    value = value_tag.get_text(strip=True) if value_tag else ""
        
    if name and details and value:
     ws.append([name, details, value])     
wb.save("irshad_apple_products.xlsx")
print("Done: irshad_apple_products.xlsx")