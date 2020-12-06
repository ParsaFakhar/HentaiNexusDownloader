import requests
from bs4 import BeautifulSoup
import random
from tqdm import tqdm
import os, sys
import threading
import math

from lxml.html import fromstring
from itertools import cycle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager



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

    if start_num == 1:
        url = url_domain + "#001"
        driver.get(url)
        time.sleep(1)
        print("\n",url,"\n")
        for i in range(start_num, second_part):
            page_source = driver.page_source

            # print(soup)
            # html_content = requests.get(url, headers=headers).text
            html_content = page_source

            # Parse the html content
            soup = BeautifulSoup(html_content, "lxml")

            # print("\n",soup,"\n")


            soup_img = soup.findAll("img")

            # print("\n",soup,"\n")

            img_url = soup_img[0].get("src")
            download(img_url, download_folder)
            # driver.findElement(By.linkText("Login")).click();
            # driver.findElements(By.className("pagination-next reader-pagination-next")).get(0).click();
            # print("\n\n",driver.find_element_by_class_name("pagination-next reader-pagination-next"),"\n\n")
            linkElem = driver.find_element_by_link_text("Next page")
            linkElem.click()
            time.sleep(1)


    else:
        if start_num < 10:
            url = url_domain + "#00" + str(start_num)
        if 100 > start_num > 9:
            url = url_domain + "#0" + str(start_num)
        if 1000 > start_num > 99:
            url = url_domain + "#" + str(start_num)

        print("\n",url,"\n")
        driver.get(url)
        time.sleep(1)
        for i in range(second_part, num):
            page_source = driver.page_source

            # print(soup)
            # html_content = requests.get(url, headers=headers).text
            html_content = page_source

            # Parse the html content
            soup = BeautifulSoup(html_content, "lxml")

            # print("\n",soup,"\n")


            soup_img = soup.findAll("img")

            # print("\n",soup,"\n")

            img_url = soup_img[0].get("src")
            download(img_url, download_folder)
            # driver.findElement(By.linkText("Login")).click();
            # driver.findElements(By.className("pagination-next reader-pagination-next")).get(0).click();
            # print("\n\n",driver.find_element_by_class_name("pagination-next reader-pagination-next"),"\n\n")
            linkElem = driver.find_element_by_link_text("Next page")
            linkElem.click()
            time.sleep(1)





        # driver.get(url)
        # print("\n\n",driver,"\n\n")
        # time.sleep(5)

        # driver.current_url = url

        # print("\n",url,"\n")






        # page_source = driver.page_source
        #
        # # print(soup)
        # # html_content = requests.get(url, headers=headers).text
        # html_content = page_source
        #
        # # Parse the html content
        # soup = BeautifulSoup(html_content, "lxml")
        #
        # # print("\n",soup,"\n")
        #
        #
        # soup_img = soup.findAll("img")
        #
        # # print("\n",soup_img,"\n")
        #
        # img_url = soup_img[0].get("src")
        # download(img_url, download_folder)
        # # driver.findElement(By.linkText("Login")).click();
        # # driver.findElements(By.className("pagination-next reader-pagination-next")).get(0).click();
        # # print("\n\n",driver.find_element_by_class_name("pagination-next reader-pagination-next"),"\n\n")
        # linkElem = driver.find_element_by_link_text("Next page")
        # linkElem.click()
        # time.sleep(5)




if __name__ == "__main__":
    # sys.argv[1] is for the Id of the Hentai  EXP: 9012
    # sys.argv[2] is for the number of the page it has  EXP: 12
    hen_id = str(sys.argv[1])
    num = int(sys.argv[2])
    party = int(sys.argv[3])


    url = ""
    url_domain = "https://hentainexus.com/read/" + hen_id
    hen_title_url = "https://hentainexus.com/view/" + hen_id

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #driver = webdriver.Chrome("/Users/macintosh/.wdm/drivers/chromedriver/mac64/86.0.4240.22/chromedriver", options=options)




    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    html_content = requests.get(hen_title_url, headers=headers).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    title = soup.findAll("h1", attrs={"class": "title"})
    download_folder = "/Users/macintosh/Downloads/" + str(title[0].getText())

    if num%2==0:
        second_part = int((num/2)+1)
    else:
        second_part = int(math.ceil(num/2))

    if party == 1:
        repeater(1)
    else:
        repeater(second_part)


    # # creating thread
    # t1 = threading.Thread(target=repeater, args=(1,))
    # t2 = threading.Thread(target=repeater, args=(second_part,))
    #
    # # starting thread 1
    # t1.start()
    # # starting thread 2
    # t2.start()
    #
    # # wait until thread 1 is completely executed
    # t1.join()
    # # wait until thread 2 is completely executed
    # t2.join()
    # driver.quit()
