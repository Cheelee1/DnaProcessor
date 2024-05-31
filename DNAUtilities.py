
proteinStrands = []
convertedProteins = []
rnaCodons = []
proteinFrcy = {}
rnaConverter ={"A":"U","T":"A","G":"C","C":"G"}
conversionChart= {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
                        "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
                        "UAU":"Tyr", "UAC":"Tyr", "UAA":"STOP", "UAG":"STOP",
                        "UGU":"Cys", "UGC":"Cys", "UGA":"STOP", "UGG":"Trp",
                        "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",
                        "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
                        "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",
                        "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",
                        "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",
                        "ACU":"Thr", "ACC":"Thr", "ACG":"Thr", "ACA":"Thr",
                        "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",
                        "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",
                        "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",
                        "GCU":"Ala", "GCA":"Ala", "GCC":"Ala", "GCG":"Ala",
                        "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",
                        "GGU":"Gly", "GGC":"Gly", "GGG":"Gly", "GGA":"Gly"}
#creates a list of nonconverted proteinstrands
def strandBuilder(codonlist):
    temp = []

    for i in range(len(codonlist)):
        if (conversionChart[codonlist[i]] == "STOP"):
            temp.append(codonlist[i])
            proteinStrands.append(temp)
            temp = []
        else:
            temp.append(codonlist[i])
# takes the list of nonconverted proteins and counts each frequency per protein. 
# then creates a a dictionary were the key is the protein strand and the value is the stats of all frequencies
def frcyTkr(_lists):
    
    for i in _lists:
        frcyCtr = {"A":0, "C":0, "G":0, "U":0, "Total":0}
        for k in frcyCtr:  
            for j in i:
                for n in j:
                    if (n == k):
                        frcyCtr[k]+=1
                        frcyCtr["Total"]+=1         
                    elif (j == "UAA" or "UGA" or "UAG"):
                        proteinFrcy[str(i)] = frcyCtr
#converts our proteinStrands list               
def proteinConverter(proLists):
    temp = [] 
    for i in proteinStrands:
        for j in i:
            if j in conversionChart:

                if (conversionChart[j]  == "STOP"):
                    temp.append(conversionChart[j])
                    convertedProteins.append(temp)
                    temp = [] 
                else:
                    temp.append(conversionChart[j])