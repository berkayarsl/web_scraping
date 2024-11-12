from selenium import webdriver
from selenium.webdriver.common.by import By
import time
times = 2

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options)
driver.get("https://books.toscrape.com/")
time.sleep(times)


category_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Travel') or contains(text(),'Nonfiction')]")
category_urls = [element.get_attribute("href") for element in category_elements]
print(category_urls)

driver.get(category_urls[0])
time.sleep(times)

book_elements_xpath = "//div[@class = 'image_container']//a"
books_elements = driver.find_elements(By.XPATH,book_elements_xpath)
book_urls = [element.get_attribute("href") for element in books_elements]
print(book_urls)
pagination =3
url = category_urls[0]
book_urls = []
for i in range (1,pagination):
    update_url =    url if i ==1 else url.replace("index",f"page-{i}")
    driver.get(update_url)
    book_elements = driver.find_elements(By.XPATH,book_elements_xpath)
    if not book_elements:
        break
    temp_urls = [element.get_attribute("href") for element in book_elements]
    book_urls.extend(temp_urls)

print(book_urls)
print(len(book_urls))

driver.get(book_urls[0])
time.sleep(times)

content_div = driver.find_elements(By.XPATH,"//div[@class = 'content']")
inner_html = content_div[0].get_attribute("innerHTML")






