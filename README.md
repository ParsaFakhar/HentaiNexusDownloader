# HentaiNexusDownloader (Hentai Nexus Downloader)
don't know about windows but it works on mac!

USE THIS ONE "HentaiNexus alternative copy.py", the other one doesn't work since the website turned their image's source dynamic and the images get's added with javascript on the site so we have to use selenium to get the images


open 2 TABS in terminal, 

in the first tab type:
type "python" or "python3", drag the "HentaiNexus alternative copy.py" file into the terminal, {number of  the hentai for example 4509} space {number of the page it has for example 24} 1

in the second tab type:
type "python" or "python3", drag the "HentaiNexus alternative copy.py" file into the terminal, {number of  the hentai for example 4509} space {number of the page it has for example 24} 2

here is the final format:
python /Users/macintosh/Downloads/HentaiNexusDownloader.py 4089 24 1,,,,,,,,,in tab 1,,,,,,
python /Users/macintosh/Downloads/HentaiNexusDownloader.py 4089 24 2,,,,,,,,,in tab 2,,,,,,

the reason is selenium doesn't support multiThread so it's more efficeint to let one tab downloads the first half of the hentai and let the other tab download the rest



download_folder = "/Users/macintosh/Downloads/"           but you can change it if you named your folder something else other than macintosh (ex: "/Users/Sam/Downloads/)



if you have slow internet connection change time.sleep(1) to time.sleep(5 or 10)




in case you don't have the  modules or you got an errot just import these:
pip install requests
pip install bs4
.
.
.

"do pip install all the below one by one"
requests
bs4
random
tqdm
lxml
