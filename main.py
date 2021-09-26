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
    'fu': 2,        # 2 => diesel
    'cxdw': 0,      # 0 => twd
    'cbl1': 1,      # 0 => 1-series
    'q': 'bmw',
    'sort': 'date'
}
BMW_335 = {
    'cg': 1020,     # not sure about this one
    'mys': 2011,    # min year
    'mye': 2015,    # max year
    'cxpf': 8,      # 7 => power 180hp
    # 'pe': 18,       # 16 => price 170k
    'ps': 1,        # 1 => min price 5k
    'fu': 1,        # 1 => petrol
    'cxdw': 0,      # 0 => twd
    'me': 26,       # 26 => max mileage 15999
    'q': '335',
    'sort': 'date'
}
BMW_330 = {
    'cg': 1020,     # not sure about this one
    'mys': 2005,    # min year
    'mye': 2012,    # max year
    'cxpf': 8,      # 7 => power 180hp
    'pe': 18,       # 16 => price 170k
    'ps': 1,        # 1 => min price 5k
    'fu': 1,        # 1 => petrol
    'cxdw': 0,      # 0 => twd
    'me': 26,       # 26 => max mileage 15999
    'q': '330',
    'sort': 'date'
}
C63_AMG = {
    'cg': 1020,     # not sure about this one
    'mys': 2007,    # min year
    'mye': 2018,    # max year
    'cxpf': 16,     # 16 => power 400hp
    'me': 26,       # 26 => max mileage 15999
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
AYGO = {
    'cg': 1020,     # not sure about this one
    'mys': 2015,    # min year
    'me': 21,       # 31 => max mileage 10999
    'ps': 1,        # 1 => min price 5k
    'pe': 8,        # 8 => price 70k
    'q': 'aygo',
    'sort': 'date'
}
C1 = {
    'cg': 1020,     # not sure about this one
    'mys': 2015,    # min year
    'me': 21,       # 31 => max mileage 10999
    'ps': 1,        # 1 => min price 5k
    'pe': 8,        # 8 => price 70k
    'q': 'c1',
    'sort': 'date'
}
PEUGEOT_108 = {
    'cg': 1020,     # not sure about this one
    'mys': 2015,    # min year
    'me': 21,       # 31 => max mileage 10999
    'ps': 1,        # 1 => min price 5k
    'pe': 8,        # 8 => price 70k
    'q': '108',
    'sort': 'date'
}
PEUGEOT_107 = {
    'cg': 1020,     # not sure about this one
    'mys': 2005,    # min year
    'mye': 2014,    # min year
    'me': 21,       # 31 => max mileage 10999
    'ps': 1,        # 1 => min price 5k
    'pe': 8,        # 8 => price 70k
    'q': '107',
    'sort': 'date'
}

if __name__ == '__main__':
    # small_cars = [get_url(CATEGORY, AYGO), get_url(CATEGORY, C1), get_url(CATEGORY, PEUGEOT_108)]
    # models = ["Aygo", "C1", "108"]

    fast_cars = [get_url(CATEGORY, BMW_335)]
    models = ["335"]

    parse_site(fast_cars)
    plot_shit(OUTPUT, models)
