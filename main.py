from scrape import get_url, parse_site
from plot import plot_shit


OUTPUT = './json_data.json'
CATEGORY = '/fordon/bilar?'
PARAMS = {
    'cb': 3,        # for sale
    'cg': 1020,     # not sure about this one
    'mye': 2018,    # maximum year 2018
    'cxpf': 7,      # 7 => power 160hp
    'fu': 1,        # 1 => fuel petrol
    'gb': 1,        # 1 => gearbox manual
    'me': 31,       # 31 => max mileage 24999 (note: also change input to plot_shit)
    'pe': 8,        # 11 => price 100k
    'cxdw': 0,      # 0 => twd
    'q': 'bmw',
    'sort': 'price'
}


if __name__ == '__main__':
    URL = get_url(CATEGORY, PARAMS)
    print(URL)
    parse_site(URL)
    plot_shit(OUTPUT, 24999)
