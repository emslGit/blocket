import json
import matplotlib.pyplot as plt


def scatter_by_mileage(models, data, max_mileage=24999):
    by_mileage = sorted(filter(lambda ad: ad['mileage'] <= max_mileage, data), key=lambda ad: ad['mileage'])
    by_mileage_x = list()
    by_mileage_y = list()

    for model in models:
        filtered = list(filter(lambda ad: ad['model'] == model, by_mileage))
        by_mileage_x += [list(map(lambda ad: ad['mileage'], filtered))]
        by_mileage_y += [list(map(lambda ad: ad['price'], filtered))]

    settings = {
        'colors': ['tab:red', 'green', 'tab:orange', 'blue', 'black', 'tab:blue', 'purple'],
        'alpha': [0.65, 0.85, 0.55, 0.75, 0.85, 0.85, 0.75]
    }

    plt.figure('Model By Mileage', figsize=(8, 6))
    for i in range(len(by_mileage_x)):
        plt.scatter(
            by_mileage_x[i],
            by_mileage_y[i],
            color=[settings['colors'][i]] * len(by_mileage_x[i]),
            alpha=settings['alpha'][i],
            s=150,
            marker="o",
            edgecolors='none'
        )
    plt.legend(models, loc='best')
    plt.xticks(rotation=-45, ha="left", fontsize=8)
    plt.yticks(fontsize=8)
    plt.xlabel('Miltal')
    plt.ylabel('SEK')
    plt.grid(c='black', alpha=0.1)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(500))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(5000))
    plt.ylim(0)
    plt.show()


def plot_shit(file):
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
                'fuel': ad['parameterGroups'][0]['parameters'][0]['value'],
                'mileage': int(ad['parameterGroups'][0]['parameters'][2]['value'].replace(' ', '').split('-')[1]),
                'model': params[0]['value'] if params else 'Unknown'
            })

    scatter_by_mileage(['320', '323', '325', '328', '330'], data)
    # scatter_by_mileage(['116', '118', '120', '123', '125', '130'], data)
