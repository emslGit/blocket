from scrape import get_url, parse_site
from plot import plot_shit


OUTPUT = './json_data.json'
CATEGORY = 'hela_sverige/fordon/bilar?'
CATEGORY_GBG = 'goteborg/fordon/bilar?r=15&ag=1&'

BMW_1_SERIES = {
    'cg': 1020,     # not sure about this one
    'mye': 2018,    # max year
    'cxpf': 5,      # 6 => power 140hp
    'me': 31,       # 31 => max mileage 24999
    'pe': 16,       # 16 => price 150k
    'ps': 1,        # 1 => min price 5k
    'cxdw': 0,      # 0 => twd
    'cbl1': 1,      # 0 => 1-series
    'q': 'bmw',
    'sort': 'date'
}
BMW_3_SERIES = {
    'cg': 1020,     # not sure about this one
    'mys': 2007,    # min year
    'mye': 2018,    # max year
    'cxpf': 8,      # 7 => power 180hp
    'me': 27,       # 27 => max mileage 16999
    'pe': 16,       # 16 => price 150k
    'ps': 21,       # 1 => min price 5k
    'cxdw': 0,      # 0 => twd
    'cbl1': 2,      # 2 => 3-series
    'q': 'bmw',
    'sort': 'date'
}
C63_AMG = {
    'cg': 1020,     # not sure about this one
    'mys': 2007,    # min year
    'mye': 2018,    # max year
    'cxpf': 16,     # 16 => power 400hp
    'me': 26,       # 31 => max mileage 15999
    'ps': 1,        # 1 => min price 5k
    'q': 'c63',
    'sort': 'date'
}
VOLVO_V70 = {
    'cg': 1020,     # not sure about this one
    'mys': 2014,    # min year
    'ms': 31,       # 31 => min mileage 20000
    'ps': 1,        # 1 => min price 5k
    'pe': 9,        # 9 => price 80k
    'q': 'volvo',
    'sort': 'date'
}
SMALL = {
    'cg': 1020,     # not sure about this one
    'mys': 2010,    # min year
    'me': 21,       # 31 => max mileage 10999
    'ps': 1,        # 1 => min price 5k
    'pe': 9,        # 9 => price 80k
    'q': 'c1',
    'sort': 'date'
}

URL = get_url(CATEGORY, BMW_3_SERIES)

if __name__ == '__main__':
    latest = parse_site(URL)
    plot_shit(OUTPUT)
