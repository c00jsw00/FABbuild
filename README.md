# FABbuild (python 3.X) for linux and windoes
Building the 3D FAB (antibody) PDB form amino sequence
please installing the packages

1. conda install -c salilab modeller
2. conda install -c conda-forge m2w64-gcc
3. conda install -c msys2 m2-base
4. conda install -c conda-forge m2w64-gcc-libgfortran
5. conda install -c anaconda git
6. git clone https://github.com/c00jsw00/FABbuild.git
7. g++ -static -O3 -ffast-math -lm -o TMalign TMalign.cpp
#KEY_MODELLER
C:/ProgramData/Anaconda3\Library\modeller/modlib/modeller/config.py
-------------------------------------------------------------------
config.py:
install_dir = r'C:/ProgramData/Anaconda3\Library\modeller' 
license = r'XXXXXXX' 
-------------------------------------------------------------------
How to run the software 
1. python3 main.py
- to generate the Final.pdb
