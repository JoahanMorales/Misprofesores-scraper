import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)

driver = webdriver.Chrome(options=options, service=chrome_service)

URL = "https://www.misprofesores.com/escuelas/IPN-UPIICSA_1164"
driver.get(URL)

time.sleep(3)

html_content = driver.page_source

file_path = r"C:\Users\chump\OneDrive\Escritorio\Escritorio\WebScrapping\pagina.html"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"Archivo HTML guardado en: {file_path}")

driver.quit()
