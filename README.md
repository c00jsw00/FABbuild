# FABbuild-amber (python 3.X) only for linux 
Building the 3D FAB (antibody) PDB form amino sequence
please installing the packages

1. conda install -c salilab modeller
2. conda install -c conda-forge m2w64-gcc
3. g++ -static -O3 -ffast-math -lm -o TMalign TMalign.cpp
4. conda install -c conda-forge ambertools
5. conda install -c ambermd pytraj

#KEY_MODELLER
export KEY_MODELLER=XXXXXXXXXXXX

4. wget https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt.gz
5. wget https://salilab.org/modeller/downloads/pdb_95.pir.gz
6. unzip the two files

How to run the software 
1. python3 main.py
- to generate the Final.pdb
