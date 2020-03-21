import re # regular expressions
import csv # manipulate csv files
import os # interface with operating system
# from bs4 import BeautifulSoup # HTML parser
import requests

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

