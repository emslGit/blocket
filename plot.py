import json
import matplotlib.pyplot as plt


def plot_shit(file, max_mileage=34999):
    data = []
    with open(file, 'r') as f:
        for ad in json.load(f)['ads']:
            params = list(filter(lambda x: x['id'] == 'level_2', ad['parameterGroups'][1]['parameters']))
            data.append({
                'subject': ad['subject'],
                'id': ad['adId'],
                'url': ad['shareUrl'],
                'location': ad['location'][0]['name'],
                'price': ad['price']['value'],
                'year': ad['parameterGroups'][0]['parameters'][3]['value'],
                'mileage': int(ad['parameterGroups'][0]['parameters'][2]['value'].replace(' ', '').split('-')[1]),
                'model': params[0]['value'] if params else 'Unknown'
            })

    by_mileage = sorted(filter(lambda ad: ad['mileage'] <= max_mileage, data), key=lambda ad: ad['mileage'])

    by_mileage_320 = list(filter(lambda ad: ad['model'] == '320', by_mileage))
    by_mileage_320_x = list(map(lambda ad: ad['mileage'], by_mileage_320))
    by_mileage_320_y = list(map(lambda ad: ad['price'], by_mileage_320))

    by_mileage_323 = list(filter(lambda ad: ad['model'] == '323', by_mileage))
    by_mileage_323_x = list(map(lambda ad: ad['mileage'], by_mileage_323))
    by_mileage_323_y = list(map(lambda ad: ad['price'], by_mileage_323))

    by_mileage_325 = list(filter(lambda ad: ad['model'] == '325', by_mileage))
    by_mileage_325_x = list(map(lambda ad: ad['mileage'], by_mileage_325))
    by_mileage_325_y = list(map(lambda ad: ad['price'], by_mileage_325))

    by_mileage_328 = list(filter(lambda ad: ad['model'] == '328', by_mileage))
    by_mileage_328_x = list(map(lambda ad: ad['mileage'], by_mileage_328))
    by_mileage_328_y = list(map(lambda ad: ad['price'], by_mileage_328))

    by_mileage_330 = list(filter(lambda ad: ad['model'] == '330', by_mileage))
    by_mileage_330_x = list(map(lambda ad: ad['mileage'], by_mileage_330))
    by_mileage_330_y = list(map(lambda ad: ad['price'], by_mileage_330))
    # print(json.dumps(by_mileage_320, indent=2))

    plt.figure(figsize=(8, 5))
    plt.scatter(
        by_mileage_320_x,
        by_mileage_320_y,
        color=['tab:red'] * len(by_mileage_320), alpha=0.65, s=200, edgecolors='none', label='320'
    )
    plt.scatter(
        by_mileage_323_x,
        by_mileage_323_y,
        color=['green'] * len(by_mileage_323), alpha=0.85, s=200, edgecolors='none', label='323'
    )
    plt.scatter(
        by_mileage_325_x,
        by_mileage_325_y,
        color=['tab:orange'] * len(by_mileage_325), alpha=0.55, s=200, edgecolors='none', label='325'
    )
    plt.scatter(
        by_mileage_328_x,
        by_mileage_328_y,
        color=['blue'] * len(by_mileage_328), alpha=0.75, s=200, edgecolors='none', label='328'
    )
    plt.scatter(
        by_mileage_330_x,
        by_mileage_330_y,
        color=['black'] * len(by_mileage_330), alpha=0.85, s=200, edgecolors='none', label='330'
    )
    plt.xticks(rotation=-45, ha="left", fontsize=8)
    plt.yticks(fontsize=8)
    plt.legend(['320i', '323i', '325i', '328i', '330ci'], loc='best')
    plt.xlabel('Miltal')
    plt.ylabel('SEK')
    plt.grid(c='black', alpha=0.1)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(500))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(5000))
    plt.ylim(0)
    plt.show()
