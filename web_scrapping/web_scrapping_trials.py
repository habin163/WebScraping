from selenium import webdriver
import time
import requests
from Pillow import Image
from io import BytesIO
baseUrl = ""

driver = webdriver.Firefox()
driver.get(baseUrl)

driver.execute_script("window.scrollBy(0,1000);")
time.sleep(5)
image_elements = driver.find_element_by_css_selector("#gridMulti img")

for image in image_elements:
    image_href = image.get_attribute('src')
    image_object = requests.get(image_href)
    image = Image.open(BytesIO(image_object.content))
    image.save("./images/image" + str(i) + "." + image.format, image.format)
    i += 1