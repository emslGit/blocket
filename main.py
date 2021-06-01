import threading
import matplotlib.pyplot as plt
import smtplib
import winsound
from time import sleep
from scrape import get_url, parse_site, check_latest
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
    'cbl1': 2,      # 2 => 3-series
    'q': 'bmw',
    'sort': 'date'
}
URL = get_url(CATEGORY, PARAMS)


def hoot():
    winsound.Beep(250, 100)
    winsound.Beep(250, 100)


if __name__ == '__main__':
    latest = parse_site(URL)

    def loop():
        global latest
        while True:
            laterest = check_latest(URL)
            if latest != laterest:
                print('New objects...')
                hoot()
                latest = parse_site(URL)
            sleep(5)

    t1 = threading.Thread(target=loop)
    t1.start()

    plot_shit(OUTPUT, 24999)
    t1.join()
