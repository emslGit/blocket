import json
import requests
from bs4 import BeautifulSoup


def get_url(category, query_params):
    url = "https://www.blocket.se/annonser/" + category
    for param, val in query_params.items():
        url = url + param + '=' + str(val) + '&'
    return url.rstrip('&')


def parse_site(url):
    print(url)
    json_data = parse_page(url)
    pages = json_data['totalPageCount']

    for page in range(pages - 1):
        json_data['ads'] += parse_page(url, page + 1)['ads']

    if not json_data['ads']:
        print("No ads found.")
        exit(0)

    with open('./json_data.json', 'w') as f:
        f.write(json.dumps(json_data, indent=2, sort_keys=True))

    return json_data['ads'][0]['adId']


def check_latest(url):
    json_data = parse_page(url)
    return json_data['ads'][0]['adId']


def parse_page(url, page=None):
    paginated_url = url + ('&page=' + str(page)) if page else url
    page = requests.get(paginated_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    split_top = str(soup).split('type="application/json">')[1]
    split_bot = split_top.split('</script>', 1)

    return json.loads(split_bot[0])['props']['pageProps']['initialReduxState']['classified']['searchResults']
