#!/bin/bash
# Import sequences and taxonomy_ref into qiime format (Aritifacts)

fo="$(date +'%y_%m_%d')" # Assumes that downloading data using other scripts in this project
folder=$fo"_16s_Sequencing"

cd "data/$folder" # Specify directory of sequencing data

echo "Initialize qiime2"

# Change source to access qiime
source /Users/arnoldj/opt/anaconda3/bin/activate qiime2-2020.2

qiime tools import \
	--input-path sequences.fna \
	--output-path sequences.qza \
	--type 'FeatureData[Sequence]'

# To change % Identity below, specify xx_otu_taxonomy.txt below
# Options include: 61, 64, 67, 70, 73, 76, 79, 82, 85, 88 working on uploading 91 and 94... darn filesize limits...
# Here we choose 85 % ID (from greengenes database)

qiime tools import \
	--input-format HeaderlessTSVTaxonomyFormat \
	--input-path 85_otu_taxonomy.txt \
	--output-path taxonomy_ref.qza \
	--type 'FeatureData[Taxonomy]'

qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path 85_otus.fasta \
  --output-path 85_otus.qza

qiime feature-classifier extract-reads \
  --i-sequences 85_otus.qza \
  --p-f-primer GTGCCAGCMGCCGCGGTAA \
  --p-r-primer GGACTACHVGGGTWTCTAAT \
  --p-trunc-len 120 \
  --o-reads ref-seqs.qza