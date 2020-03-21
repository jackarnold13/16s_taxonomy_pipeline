library(tidyverse)
library(rotl)
library(ape)

# Set the working directory as R file location
this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)

time <- format(Sys.time(),"%y_%m_%d")
folder <- paste("data/",time,"_16s_Sequencing/",sep="")
tax_file <- paste(folder,"taxonomy_formatted.csv",sep="")

# # Finally... Now have in the right format for a phylogenetic tree
# Remove empty cells
taxonomy <- read_csv(tax_file, na = " ")

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

# Run rotl classification on taxa
resolved_names <- tnrs_match_names(taxa)
resolved_names

# Assemble the tree
my_tree <- tol_induced_subtree(ott_ids = resolved_names$ott_id)
plot(my_tree, no.margin = TRUE)


