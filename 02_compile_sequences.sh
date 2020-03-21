#!/bin/bash

# Compile all sequences into a fole called sequences.fna

fo="$(date +'%y_%m_%d')" # Assumes that downloading data using other scripts in this project
folder=$fo"_16s_Sequencing"

cd "data/$folder" # Specify directory of sequencing data
if [ -f sequences.fna ]; # check to see if compiled sequencing file already exists
then
	read -p 'sequences.fna already exists, do you want to overwrite this file? y/n: ' response
	if [ "$response" == "y" ]
	then
		rm sequences.fna
		touch sequences.fna
		for i in *
		do
		    if [ -f "$i" ] && [[ $i =~ \.ab1.fasta$ ]]; # Check if file is in .fasta format
		    then
		        filename="${i%%.*}"
		        cat $filename.ab1.fasta >> sequences.fna
		    fi
		done
		echo "Sequences compiled"
	else
		echo "Sequences compiled"
	fi
else
	echo "Compiling sequences.fna"
	touch sequences.fna
	for i in *
	do
	    if [ -f "$i" ] && [[ $i =~ \.ab1.fasta$ ]]; # Check if file is in .fasta format
	    then
	        filename="${i%%.*}"
	        cat $filename.ab1.fasta >> sequences.fna
	    fi
	done
	echo "Sequences compiled"
fi
