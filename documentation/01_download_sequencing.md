# 01_download_sequencing Documentation
This is the first file to run in this distribution. It will download sequencing files from a webpage (github repository for this example) and save the files on the local disk.

Run from terminal:
```
~ECEV32000_Project % python3 01_download_sequencing.py
```
### Import Packages
```
# Run first - will download sequencing data from a sequencing repositiory 
import process_file as pf
import re
from datetime import datetime
```
Folder for data storage is based on the day the data is downloaded.
```
time_now = datetime.now() # Date used to make local folder for data
```
### Initialize Variables

```
url = "https://github.com/jackarnold13/ECEV32000_Project_Seq_Data/tree/master/fasta_data" # Github repository to simulate sequencing website
folder_name = time_now.strftime("%y_%m_%d")+"_16s_Sequencing" # Name the outdir with today's date in YY_MM_DD format

print('destination', folder_name) # Print the destination
```
### Use [process_file.py](../process_file.py) functions to download data
First Page to scrape the links to the other files
```
first_page = pf.download_first_page(url, folder_name) # Download the first page to find data links
```
Use regular expressions to find specific download links
```
href_links = re.findall(r'href="/jackarnold13/ECEV32000_Project_Seq_Data/blob/master/fasta_data/(.+)"', first_page) # Locate & store data links
```
Download remaining links and store in a folder
```
# For each link, downolad and save within the data folder

for link in href_links:
	name = link
	link = "https://github.com/jackarnold13/ECEV32000_Project_Seq_Data/raw/master/fasta_data/"+link
	pf.download_links(link,folder_name,name)

```
