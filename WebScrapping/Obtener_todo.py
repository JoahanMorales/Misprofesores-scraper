import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")  
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)

driver = webdriver.Chrome(options=options, service=chrome_service)

escuela = "IPN-ESCOM_1694"
URL = "https://www.misprofesores.com/escuelas/" + escuela  
driver.get(URL)

time.sleep(3)

dataSet = driver.execute_script("return window.dataSet;")



file_path = "dataset_"+escuela+".json"
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(dataSet, file, ensure_ascii=False, indent=4)

print(f"Archivo '"+file_path+"' guardado en la carpeta actual.")

driver.quit()
