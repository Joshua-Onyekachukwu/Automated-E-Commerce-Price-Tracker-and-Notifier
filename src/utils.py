import json
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    filename="../logs/tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def load_products(file_path="data/products.json"):
    """Load product data from a JSON file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning("Products file not found. Creating a new one.")
        return []

def save_products(products, file_path="data/products.json"):
    """Save product data to a JSON file."""
    Path(file_path).parent.mkdir(exist_ok=True, parents=True)
    with open(file_path, "w") as file:
        json.dump(products, file, indent=4)
    logging.info("Products saved successfully.")