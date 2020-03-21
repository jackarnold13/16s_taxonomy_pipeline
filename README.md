# ECEV32000_Project
Final Project for ECEV32000


## Brief Overview 
Pipeline for 16S rRNA Analysis
**Note: As of this release, must source the qiime environment before step 04 *works* if sourced at beginning see [qiime_doc](documentation/qiime_doc.md) for more info**
* Download sequencing data from webpage (sanger sequencing) **Python** [01_download_sequencing.py](01_download_sequencing.py)
  * For the purposes of this project, a github repository will be used to simulate the sequencing website
  * Download data (webscraping) -> save files in new folder based on date
  * [More information on 01_download_sequencing](documentation/01_download_sequencing.md)
* Compile downloaded sequencing and prepare for import into Qiime2 **Bash** [02_compile_sequences.sh](02_compile_sequences.sh)
  * Compiles the downloaded raw sequencing files into format for Qiime2
  * [More information on 02_compile_sequences](documentation/02_compile_sequences.md)
* Import sequences and taxonomic data into qiime environment **Qiime2 Bash Environment** [03_qiime_imports.sh](03_qiime_imports.sh)
  * Calls the Qiime2 Bash environment for the subshell processes
  * Imports and creates Qiime2 artifacts for sequence classification
  * [More information on 03_qiime_imports](documentation/03_qiime_imports)
* Create database and classify sequences **Qiime2 Api in Python** [04_Classify_Taxonomy.py](04_Classify_Taxonomy.py)
  * **MUST HAVE QIIME2 ENV TO RUN** [qiime_doc](documentation/qiime_doc.md)
  * Load artifacts created in step 03
  * Create and train a classifier using Qiime2 API elements
  * Classify taxonomy based on 16s sequences
  * Export data to CSV
  * [More information on 04_Classify_Taxonomy](documentation/04_Classify_Taxonomy.md)
* Assemble a phylogenetic tree **R with tidyverse, rotl, ape** [05_Tree.R](05_Tree.R)
  * Import and process data
  * ID Taxonomies using rotl
  * Assemble a phylogenetic tree using ape
  * [More information on 05_Tree](documentation/05_Tree.md)
  
## Dependencies
* 01_download_sequences.py
  * re
  * [process_file.py](process_file.py) which is included in this distribution
    * [More information on process_file](documentation/process_file.md)
* 02_compile_sequences.sh
  * Bash shell
* 03_qiime_imports.sh
  * QIIME 2 enviornment
    * [Install the command line interface natively](https://docs.qiime2.org/2020.2/install/native/)
    * Activate before running this program with `source activate qiime2-2020.2` (not required for this program to function)
* 04_Classify_Taxonomy.py
  * QIIME 2 enviornment
    * [Install the command line interface natively](https://docs.qiime2.org/2020.2/install/native/)
    * Activate before running this program with `source activate qiime2-2020.2`
  * Pandas
  * Datetime
  * re
  * csv
* 05_Tree.R
  * tidyverse
    * In RStudio `install.packages(tidyverse)`
  * rotl
    * In RStudio `install.packages(rotl)`
  * ape
    * In RStudio `install.packages(ape)`
