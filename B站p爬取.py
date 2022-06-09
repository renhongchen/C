import re
import os
import ffmpeg
from lxml import etree
import requests
def main():
    url = input('url:')
    r = requests.get(url)
    html = etree.HTML(str(r.text))
    data = html.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
    name = html.xpath('//h1/@title')[0]
    url1 = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"',data)[0]
    url2 = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"',data)[0]
    print(name)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        'Referer':'https://www.bilibili.com/'
    }
    response_30280 = requests.get(url1,headers=headers)
    response_30064 = requests.get(url2,headers=headers)
    dtat_30280 = response_30280.content
    data_30064 = response_30064.content
    with open('lemon_30280.mp4','wb') as f:
        f.write(dtat_30280)
    with open('不谓侠.mp3','wb') as f:
        f.write(data_30064)
    name = str(name) + '.mp4'
    os.system(f'D:\FFmpeg\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg -i "lemon_30280.mp4" -i "lemon_30064.mp3" -c copy {name}')
    # os.remove('lemon_30280.mp4')
    # os.remove('浪子闲话.mp3')
if __name__ == '__main__':
    main()
