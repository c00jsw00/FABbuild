import re
def FASTA(sequenceid):
    rule        = 1
    countheavy  = 0
    countlight  = 0
    firstheay   = '>P1;Heavy'
    secondheavy = 'sequence:Heavy:::::::0.00: 0.00'
    firstlight  = '>P1;Light'
    secondlight = 'sequence:Light:::::::0.00: 0.00'
    with open('pdb_seqres.txt') as file:
        with open('Heavy.ali',"w") as outputheavy, open('Light.ali',"w") as outputlight:   
            for line in file:
                pdbid    = line[1:5]
                if (pdbid == sequenceid):
                    if (rule == 1):
                        heavy = re.search(r"heavy chain", line, re.I)
                        judgementheavy = heavy.group().upper()
                        rule = 2
                    elif (rule == 2):
                        light = re.search(r"light chain", line, re.I)
                        judgementlight = light.group().upper()
                        rule = 3
                    elif (judgementheavy == 'HEAVY CHAIN') and (countheavy == 0):
                        countheavy = 1
                    elif (judgementlight == 'LIGHT CHAIN') and (countlight == 0):
                        countlight = 1
                elif(countheavy == 1):
                    outputheavy.write(firstheay+'\n')
                    outputheavy.write(secondheavy+'\n')
                    outputheavy.write(line+'\n')
                    countheavy = 2
                elif (countlight == 1):
                    outputlight.write(firstlight+'\n')
                    outputlight.write(secondlight+'\n')
                    outputlight.write(line+'\n')
                    countlight = 2