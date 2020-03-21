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

# Import the sequencing artifact generated from 03_compile_sequences
query = Artifact.load(folder+'/sequences.qza')
ref_reads = Artifact.load(folder+'/ref-seqs.qza')
ref_tax = Artifact.load(folder+'/taxonomy_ref.qza')

# Assemble the classifier using reference reads and taxonomic assignment
classifier = feature_classifier.actions.fit_classifier_naive_bayes(ref_reads,ref_tax)

# Assign Taxonomy
taxonomy = feature_classifier.actions.classify_sklearn(query, classifier.classifier)

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





