# process_file.py Documentation
This file is used by 01_download_sequencing.py as a source to call functions from. The main functions used from this file are `process_file.download_first_page()` and `process_file.download_links()`
### Import Packages
```
import re # regular expressions
import csv # manipulate csv files
import os # interface with operating system
# from bs4 import BeautifulSoup # HTML parser
import requests
```
`download_first_page` is used for downloading the first page of a given url and placing it in a user specified folder.
```
def download_first_page(url,folder):
    if os.path.exists('data/' + folder) == False:
        os.system('mkdir -p data/' + folder)
    else:
        print('data/'+folder,'already exists')    

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    first_page = requests.get(url, allow_redirects = True, headers=headers).content.decode('UTF8')

    with open('data/' + folder + '/0.html', 'w') as f:
        f.write(first_page)

    return first_page
```
`download_links()` is used for downloading content from a link based on the url, the destination folder, and what the downloaded file should be named.
```
def download_links(url,folder,name):
    if os.path.exists('data/' + folder) == False:
        os.system('mkdir -p data/' + folder)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    page = requests.get(url, allow_redirects = True, headers=headers)
    if os.path.exists('data/' + folder + '/' + name) == False:
        print('downloading',name,'...')
        with open('data/' + folder + '/' + name, 'wb' ) as f:
            f.write(page.content)
    else:
         print(name, 'aready exists') # If the file already exists in that day's folder, don't re-download the data
    
```
This function is an artifact of an older file and is not used in this project.
```
# def process_file(fname):
#     print('processing', fname)
#     with open(fname, 'rb') as f:
#         html = f.read().decode('UTF8')
#     soup = BeautifulSoup(html, 'html.parser')
#     results = []
#     papers = soup.findAll("div", {"class": "highwire-article-citation highwire-citation-type-highwire-article tooltip-enable"})
#     for paper in papers:
#         title = paper.attrs['title']
#         date, paperid = re.findall(r'/early/(\d{4}/\d+/\d+)/(\d+)', paper.attrs['data-apath'])[0]
#         last_names = paper.findAll("span", {"class": "nlm-surname"})
#         num_authors = len(last_names)      
#         results.append([str(paperid), str(date), str(num_authors), str(title)])
#     return results
```
