import schedule
import time
from scraper import setup_driver, scrape_price
from notifications import send_email, send_desktop_notification
from utils import load_products, save_products
import logging

def check_prices():
    """Check prices for all tracked products."""
    driver = setup_driver()
    products = load_products()

    for product in products:
        url = product["url"]
        threshold = product["threshold"]
        product_name = url.split("/")[-1]  # Extract product name from URL

        price = scrape_price(driver, url)
        if price and price < threshold:
            send_email(product_name, price, threshold)
            send_desktop_notification(product_name, price, threshold)

    driver.quit()

# Schedule price checks every hour
schedule.every().hour.do(check_prices)

if __name__ == "__main__":
    logging.info("Starting price tracker scheduler.")
    while True:
        schedule.run_pending()
        time.sleep(1)