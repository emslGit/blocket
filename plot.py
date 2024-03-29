import json
import matplotlib.pyplot as plt
import unidecode

SETTINGS = {
    'colors': ['tab:red', 'green', 'tab:orange', 'blue', 'black', 'tab:blue', 'purple', 'yellow', 'brown'],
    'alpha': [0.65, 0.85, 0.55, 0.75, 0.85, 0.85, 0.75, 0.75, 0.75]
}


def scatter_by_mileage(models, data, min_price=5000, min_mileage=4999, max_mileage=50000):
    by_mileage = sorted(filter(lambda ad: max_mileage >= ad['mileage'] >= min_mileage, data), key=lambda ad: ad['mileage'])
    by_mileage_x = list()
    by_mileage_y = list()

    for model in models:
        filtered = list(filter(lambda ad: ad['model'] == model, by_mileage))
        by_mileage_x += [list(map(lambda ad: ad['mileage'], filtered))]
        by_mileage_y += [list(map(lambda ad: ad['price'], filtered))]

    plt.figure('Model By Mileage', figsize=(8, 6))
    for i in range(len(by_mileage_x)):
        plt.scatter(
            by_mileage_x[i],
            by_mileage_y[i],
            color=[SETTINGS['colors'][i]] * len(by_mileage_x[i]),
            alpha=SETTINGS['alpha'][i],
            s=150,
            marker="o",
            edgecolors='none'
        )
    plt.legend(models, loc='lower left')
    plt.xticks(rotation=-45, ha="left", fontsize=8)
    plt.yticks(fontsize=8)
    plt.xlabel('Miltal')
    plt.ylabel('SEK')
    plt.grid(c='black', alpha=0.1)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(500))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(max(min_price, 0)))
    plt.ylim(0)
    plt.show()


def plot_shit(file, allowed=[]):
    data = []
    models = []
    i = 0
    with open(file, 'r') as f:
        for ad in json.load(f):

            level_1, level_2 = None, None
            if len(ad['parameterGroups']) > 1:
                level_1 = list(filter(lambda x: x['id'] == 'level_1', ad['parameterGroups'][1]['parameters']))
                level_2 = list(filter(lambda x: x['id'] == 'level_2', ad['parameterGroups'][1]['parameters']))

            level_1 = level_1[0]['value'] if level_1 else 'Unknown'
            level_2 = level_2[0]['value'] if level_2 else 'Unknown'

            model = level_1 + '/' + level_2

            if model not in models:
                models.append(model)

            mileage = ad['parameterGroups'][0]['parameters'][2]['value'].split('-')
            mileage = unidecode.unidecode(mileage[max(len(mileage) - 1, 0)])\
                .replace('Mer an ', '')\
                .replace(' ', '')

            data.append({
                'subject': unidecode.unidecode(ad['subject']),
                'id': ad['adId'],
                'url': ad['shareUrl'],
                'location': unidecode.unidecode(ad['location'][0]['name']),
                'price': ad['price']['value'],
                'year': ad['parameterGroups'][0]['parameters'][3]['value'],
                'fuel': ad['parameterGroups'][0]['parameters'][0]['value'],
                'mileage': int(mileage),
                'model': model
            })
            i += 1

    print(models)
    print('Ads: {}/{}'.format(i, len(data)))

    if len(allowed) > len(SETTINGS['colors']) or (not len(allowed) and len(models) > len(SETTINGS['colors'])):
        raise Exception("Too many models! Try specifying desired models.")

    if len(allowed):
        scatter_by_mileage(list(filter(lambda x: any(m in x for m in allowed), models)), data)
    else:
        scatter_by_mileage(models, data)
