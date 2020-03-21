# 05_Tree Documentation
This is the fifth and final file to run in this distribution. It will import the `.csv` files generated in step 04 and parse them to import into rotl. rotl is used to classify the phylogeny of the taxa, which is then constructed into a phylogenetic tree using ape. 

To run this file, open in RStudio or run from command line:
```
~ECEV32000_Project % open -na RStudio 05_Tree.R
```

### Import libraries
```
library(tidyverse)
library(rotl)
library(ape)
```
Set the working directory and navigate to the correct folder
```
# Set the working directory as R file location
this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)

time <- format(Sys.time(),"%y_%m_%d")
folder <- paste("data/",time,"_16s_Sequencing/",sep="")
tax_file <- paste(folder,"taxonomy_formatted.csv",sep="")
```
Read the `.csv`
```
# # Finally... Now have in the right format for a phylogenetic tree
# Remove empty cells
taxonomy <- read_csv(tax_file, na = " ")
```
Classify the phylogeny by using entries from the taxonomy file. Then find only the unique Genus species combinations, remove all of the blank entries and store as the taxa vector for input into the rotl classifier.
```
# Classify phylogeny on the Genus species format

tax_genus <- taxonomy$Genus
tax_species <- taxonomy$Species
tax_genus_species <- paste(tax_genus,tax_species)

tax_genus_species

# Find only unique classes (don't need to repeat)
tax_class_unique <- tax_genus_species %>% unique()

# Remove Blank cells
blank_cells <- c(" ")
removal_key <- which(tax_class_unique%in%blank_cells)

# Store as taxa
taxa <-tax_class_unique[-removal_key]
```
Run the rotl classifier to match the taxa names to ott_ids for tree assembly.
```
# Run rotl classification on taxa
resolved_names <- tnrs_match_names(taxa)
resolved_names
```
Using the ape function `tol_induced_subtree` create a phylogenetic tree and plot to the RStudio workspace.
```
# Assemble the tree
my_tree <- tol_induced_subtree(ott_ids = resolved_names$ott_id)
plot(my_tree, no.margin = TRUE)
```
