# 04_Classify_Taxonomy Documentation
This is the fourth file to run in this distribution. It first imports the QIIME2 artifacts constructed in step 03 into the QIIME2 Artifact API environment that is available in python (specifially in jupyter notebooks, however I have converted the file into a normal `.py` file.). Then, it will train a naieve bayes classifier using the reference taxonomy artifacts. Next, this program will use the trained classifier to assign taxonomy to the user's inuput sequences. Finally, these results will be exported as `.csv` files.

**BEFORE RUNNING THIS FILE, MAKE SURE THE QIIME2 ENVIRONMENT HAS BEEN SOURCED ON THE TERMINAL**

To source (assuming proper [installation](https://docs.qiime2.org/2020.2/install/native/):
```
~% source activate qiime2-2020.2
```
Then, after the QIIME2 command line environment has been accessed the file can be run as:
```
~ECEV32000_Project % python3 04_Classify_Taxonomy.py
```
### Import packages
qiime2 can only be imported if the qiime2 bash environment was used to call the python script. Pandas and re may need to be reinstalled to this environment for proper function.
```
# Note, before running *must* change source to qiime2 -- trying to fix in future
# Use: source /Users/arnoldj/opt/anaconda3/bin/activate qiime2-2020.2
# Import
from qiime2 import Artifact
from qiime2.plugins import feature_classifier
from qiime2.plugins import metadata
import pandas as pd
from datetime import datetime
import re
import csv

# Get folder name (based on method from previous programs using date)
time_now = datetime.now()
folder_name = time_now.strftime("%y_%m_%d")+"_16s_Sequencing"
folder  = 'data/'+folder_name
```
Loading the artifacts into python store them as variables. `query` is the query of sequences that are to be classified taxonomically. `ref_reads` and `ref_tax` are artifacts from the reference database obtained from [greengenes](http://qiime.org/home_static/dataFiles.html)
```
# Import the sequencing artifact generated from 03_compile_sequences
query = Artifact.load(folder+'/sequences.qza')
ref_reads = Artifact.load(folder+'/ref-seqs.qza')
ref_tax = Artifact.load(folder+'/taxonomy_ref.qza')
```
For QIIME2 to classify the taxonomy of queried sequences, a classifier must be assembled. In this project, a naieve bayes classsifier was trianed according to the reference reads and taxonomy artifacts as described above.
```
# Assemble the classifier using reference reads and taxonomic assignment
classifier = feature_classifier.actions.fit_classifier_naive_bayes(ref_reads,ref_tax)

# Assign Taxonomy
taxonomy = feature_classifier.actions.classify_sklearn(query, classifier.classifier)
```
After the taxonomy has been assigned, it must be parsed into a readable format (readable and easy to work with in R) so a `.csv` format was chosen. Note: otu_count is an artifact from attempts at using phyloseq in R which will likely be explored in future iterations of this project.
```
# Write and export Taxononomy classifications as a readable .csv

taxon = taxonomy.classification.view(pd.DataFrame)
rows = []
otu_count = []
for line in taxon.Taxon.values:
    t = re.findall(r'\w\__(\w+)', line) # Locate & store data links
    while len(t) < 7:
        t.append(None)
    rows.append(t)
    otu_count.append([1])
    
i = 0
for row in rows:
    row.insert(0,taxon.index[i])
    row.append(taxon.Confidence[i])
    i = i+1
    
i = 0
for row in otu_count:
    row.insert(0,taxon.index[i])
    i = i+1
    

rows.insert(0,['ID','Kingdom','Phylum','Class','Order','Family','Genus','Species','Confidence'])
otu_count.insert(0,['ID','Sample1'])
    
with open(folder+"/taxonomy_formatted.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open(folder+"/otu_count.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(otu_count)
```
