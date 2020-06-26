import json
import matplotlib.pyplot as plt

map_img = plt.imread('map.png')

save_path = '/Users/brad/Library/Application Support/Steam/userdata/97203856/361280/remote/turmoil_campaign_save.json'

with open(save_path, 'r') as f:
    save_data = json.load(f)

fig, ax = plt.subplots(figsize=(10, 8))

ax.imshow(map_img, extent=(15, 1180, 150, 1110))

for region, data in save_data['estates'].items():
    color = 'g'
    if data['played']:
        color = 'r'

    print(region)
    print(data)

    ax.scatter(data['i'], 1200 - data['j'], s=10, c=color)
    ax.text(data['i'] + 5, 1200 - data['j'] + 5, '%d' % (data['oil'] / 1000), fontsize=10)

plt.show()
