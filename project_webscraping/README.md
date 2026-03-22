# eBay Scraper

My ebay-dl.py file extracts information from ebay about a given item, including names of the item sold, prices, status, shipping, free returns, and items sold. The outputs are stored in a JSON and csv file.

## How to Run:

Step 1: Install dependencies:
```
import argparse
import requests
import random
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import json
import csv
```

Step 2: Install the browser used by Playwright in the terminal:
```
playwright install
```

Step 3: Run the scraper from the terminal using the following format:
```
python3 ebay-dl.py <search_term> --num_pages <number_of_pages>
```

Step 4: Generate a CSV file: Use the --csv flag:
```
python3 ebay-dl.py <search_term> --num_pages <number_of_pages> --csv
```

## Course Project
[Course Project repository](https://github.com/mikeizbicki/cmc-csci040/tree/2026spring/project_02_webscraping)
