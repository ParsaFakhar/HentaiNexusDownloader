import requests
from bs4 import BeautifulSoup
import random
from tqdm import tqdm
import os, sys
import threading

from lxml.html import fromstring
from itertools import cycle


def download(urls, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(urls, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, urls.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for datas in progress:
            # write data read to the file
            f.write(datas)
            # update the progress bar manually
            progress.update(len(datas))


def repeater(start_num):

    for i in range(start_num, num+1, 2):
        if i == 0:
            continue
        if i < 10:
            url = url_domain + hen_id + "/00" + str(i)
        if 100 > i > 9:
            url = url_domain + hen_id + "/0" + str(i)
        if 1000 > i > 99:
            url = url_domain + hen_id + "/" + str(i)

        user_agent_list = [
            # Chrome
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            # Firefox
            'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
        ]
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}



        # def get_proxies():
        #     proxy_url = 'https://free-proxy-list.net/'
        #     proxy_response = requests.get(proxy_url)
        #     parser = fromstring(proxy_response.text)
        #     proxys = set()
        #     for i in parser.xpath('//tbody/tr')[:10]:
        #         if i.xpath('.//td[7][contains(text(),"yes")]'):
        #             # Grabbing IP and corresponding PORT
        #             the_proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
        #             proxys.add(the_proxy)
        #     return proxys
        #
        #
        # proxies = get_proxies()
        # proxy_pool = cycle(proxies)
        # proxy = next(proxy_pool)

        # while flag and counter < 10:
        #     flag = False
        #     try:
        #         response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
        #     except KeyError as e:
        #         print("\n", e, "\n")
        #         flag = True
        #         counter += 1
        #         user_agent = random.choice(user_agent_list)
        #         headers = {'User-Agent': user_agent}
        #         proxy = next(proxy_pool)

        # response = requests.get(url, headers=headers)
        # soup = BeautifulSoup(response.content.decode("utf-16"), "html.parser")
        #
        # soup_img = soup.findAll("img")
        #
        # print(soup)
        html_content = requests.get(url, headers=headers).text

        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")
        soup_img = soup.findAll("img")

        img_url = soup_img[0].get("src")
        download(img_url, download_folder)


if __name__ == "__main__":
    # sys.argv[1] is for the Id of the Hentai  EXP: 9012
    # sys.argv[2] is for the number of the page it has  EXP: 12
    hen_id = str(sys.argv[1])
    num = int(sys.argv[2])

    url = ""
    url_domain = "https://hentainexus.com/read/"
    hen_title_url = "https://hentainexus.com/view/" + hen_id

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    html_content = requests.get(hen_title_url, headers=headers).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    title = soup.findAll("h1", attrs={"class": "title"})
    download_folder = "/Users/macintosh/Downloads/" + str(title[0].getText())

    # creating thread
    t1 = threading.Thread(target=repeater, args=(1,))
    t2 = threading.Thread(target=repeater, args=(0,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

































