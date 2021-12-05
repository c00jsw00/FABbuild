def SSBONDCHECKPDB(pdbfile,chainid): 
    global referencea
    global referenceb
    renamepdbfile = 'OK.'+pdbfile
    CYX = 'CYX' 
         
    with open(pdbfile) as file:
        with open(renamepdbfile,"w") as output:
            for line in file:
                SSBOND    = line[0:6]
                SSBONDID  = line[15:16] 
                atom      = line[0:4]
                number    = line[22:26]
                numbera   = line[0:17]
                numberb   = line[17:20]
                numberc   = line[20:78]
                if (SSBOND == 'SSBOND') and (SSBONDID == chainid) :
                    SSBONDresidue1 = line[17:21]
                    SSBONDresidue2 = line[31:35]
                    referencea = SSBONDresidue1
                    referenceb = SSBONDresidue2
                elif (atom == 'ATOM') and (number == referencea):
                    linetotal = numbera+CYX+numberc
                    output.write(linetotal+'\n')
                elif (atom == 'ATOM') and (number == referenceb):
                    linetotal = numbera+CYX+numberc
                    output.write(linetotal+'\n')
                else:
                    linetotal = numbera+numberb+numberc
                    output.write(linetotal+'\n')
  