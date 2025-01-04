from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import load_products, save_products
import logging

# Configure Edge WebDriver
def setup_driver():
    service = Service("../drivers/msedgedriver.exe")
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Edge(service=service, options=options)
    return driver

def scrape_price(driver, url):
    """Scrape the price of a product from a given URL."""
    driver.get(url)
    try:
        # Example for Amazon (adjust selectors for other sites)
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "priceblock_ourprice"))
        )
        price = price_element.text.replace("$", "").replace(",", "")
        return float(price)
    except Exception as e:
        logging.error(f"Error scraping price from {url}: {e}")
        return None