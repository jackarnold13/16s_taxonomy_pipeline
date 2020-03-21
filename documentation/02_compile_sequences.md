# 02_compile_sequences Documentation
This is the second file to run in this distribution. It will compile all the sequences downloaded in the previous step into a `.fna` file so that data can be loaded into the QIIME command line environment.

Before running make sure to run `~ECEV32000_Project % chmod -x 02_compile_sequences.sh`
To run
```
~ECEV32000_Project % bash 02_compile_sequences.sh
```
```
#!/bin/bash

# Compile all sequences into a fole called sequences.fna
```
Find folder using datetime method as in 01_download_sequencing.py
```
fo="$(date +'%y_%m_%d')" # Assumes that downloading data using other scripts in this project
folder=$fo"_16s_Sequencing"

cd "data/$folder" # Specify directory of sequencing data
```
Checks to see if compiled file aready exists and ask to overwrite.
```
if [ -f sequences.fna ]; # check to see if compiled sequencing file already exists
then
	read -p 'sequences.fna already exists, do you want to overwrite this file? y/n: ' response
	if [ "$response" == "y" ]
```
If response is yes, then make `.fna` file checking to see that files to be compiled are in the `.fasta` format. In this example due to the way sequences were uploaded to the server, they contain a `.ab1.fasta` extension. In the future, a file to convert `.ab1` and `.fastq` files into `.fasta` format will be developed.
```
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
```
