import argparse
import requests
import random
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import json
import csv

if __name__ == '__main__':

    # create a User Agent list
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1",
    ]

    random.shuffle(user_agent_list)
    user_agent = user_agent_list[0]

    # get command line arguments
    parser = argparse.ArgumentParser(
                        prog='ebay-dl',
                        description='Download information from ebay and convert to JSON',
                        )
    parser.add_argument('search_term', )
    parser.add_argument('--num_pages', default=10)
    parser.add_argument('--csv', action='store_true')
    args = parser.parse_args()
    print('args.search_term=', args.search_term)

    # list of all items found in all ebay webpages
    items = []

    with sync_playwright() as p:
        context = p.firefox.launch_persistent_context(
            user_data_dir='./userdata',
            headless=False,
            viewport={'width': 1280, 'height': 800},
            )
        page = context.new_page()

        page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            });
            """)

        for page_number in range(1, int(args.num_pages)+1):
        # build the url
            url = 'https://www.ebay.com/sch/i.html?_nkw='
            url += args.search_term
            url += '&_sacat=0&_from=R40&_pgn='
            url += str(page_number)
            url += '&rt=nc'
            print('url=', url)

            page.goto(url)
            page.wait_for_timeout(5000)

            for _ in range(5):
                page.mouse.wheel(0, 2000)
                page.wait_for_timeout(1000)
                page.mouse.wheel(0, 1500)
                page.wait_for_timeout(1000)
            html = page.content()

            if 'Pardon Our Interruption' in html:
                print('BLOCKED')
                break
            
            soup = BeautifulSoup(html, 'html.parser')

            tags_items = soup.select('.su-card-container__content')

            print('len(tags_items)=', len(tags_items))

            for tag_item in tags_items:
                tag_name = tag_item.select_one('.s-card__title')
                if not tag_name:
                    continue

                title = tag_name.get_text(strip=True).replace('Opens in a new window or tab', '').strip()

                if not title or 'shop on ebay' in title.lower():
                    continue

                price = None
                cents = None
                tags_price = tag_item.select('.su-styled-text.primary.bold.large-1.s-card__price')
                for tag in tags_price:
                    text = tag.get_text(strip=True)
                    text = text.replace(',', '')
                    text = text.split(' to ')[0]
                    new_price = ''
                    for t in text:
                        if t.isdigit() or t == '.':
                            new_price += t
                    if new_price:
                        price = float(new_price)
                        cents = int(price * 100)
                        break
                
                free_returns = any(
                    'free returns' in t.get_text(strip=True).lower()
                    for t in tag_item.select('.su-styled-text.secondary.large')
                )

                items_sold = None
                tags_itemssold = tag_item.select('.su-styled-text.primary.bold.large')
                for tag in tags_itemssold:
                    text = tag.get_text(strip=True).lower()

                    if 'sold' in text:
                        items_sold = text
                        break
                
                status = None
                tags_status = tag_item.select('.su-styled-text.secondary.default')
                for tag in tags_status:
                    status = tag.get_text(strip=True)

                shipping = None
                tags_shipping = tag_item.select('.su-styled-text.secondary.large')
                for tag in tags_shipping:
                    text = tag.get_text(strip=True).lower()
                    if 'free delivery' in text:
                        shipping = 0
                        break
                    cost = ''
                    for t in text:
                        if t.isdigit() or t == '.':
                            cost += t
                    if cost:
                        cost = float(cost)
                        shipping = int(cost * 100)
                        break


                items.append({
                    'name': title,
                    'price': cents,
                    'status': status,
                    'shipping': shipping,
                    'free_returns': free_returns,
                    'items_sold': items_sold,
                })

                print('name=', title)
                print('price=', cents)
                print('status=', status)
                print('shipping=', shipping)
                print('free returns=', free_returns)
                print('items_sold=', items_sold)
        
            print('items=', items)
            print('len(items)=', len(items))
            time.sleep(2)
        context.close()

    if args.csv:
        filename = args.search_term+'.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'name',
                'price',
                'status',
                'shipping',
                'free_returns',
                'items_sold',
            ])

            writer.writeheader()
            writer.writerows(items)
    else:
        filename = args.search_term+'.json'
        with open(filename, 'w', encoding='ascii') as f:
            f.write(json.dumps(items))