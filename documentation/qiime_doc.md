# Note on the Qiime2 Environment used in this project
For some of the programs included in this distribution, the QIIME2 Bash environment is needed. In the shell script `03_qiime_imports.sh` this environment can be loaded into a subshell. However, for the python file `04_Classify_Taxonomy.py` there is no such 'subshell' that I could understand how to use for loading. Thus, changing the environment of the terminal is the only way I could run this file, as the QIIME2 Artifact API depends on gathering information from the QIIME2 Bash environment. Outlined below is how to source the QIIME2 environment.

To source (assuming proper [installation](https://docs.qiime2.org/2020.2/install/native/):
```
~% source activate qiime2-2020.2
```

This may, however, alter some previously installed python packages, so reinstalling such packages in this new environment may be necessary for the code to run.
