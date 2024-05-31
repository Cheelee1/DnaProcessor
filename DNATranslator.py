"""
Aurelio Amparo
Program: DNA Translator
"""
from DNAUtilities import*

#reads the DNA Sequence in the file
with open('DNAsequence.txt',"r") as file:
    dnaData = file.read()
rnaData = ""
#DNA to RNA
for i in dnaData:
    nulceotide = ""
    if i in rnaConverter:
        nulceotide +=rnaConverter[i]
    rnaData += nulceotide
#split RNAData into codons
for i in range(0, len(rnaData), 3): 
    rnaCodons.append(rnaData[i:i+3]) 
strandBuilder(rnaCodons)
frcyTkr(proteinStrands)
proteinConverter(proteinStrands)
#keeps track of each RNa Codons
rnaCodonCounter = { "Ala":0, "Asn":0, "Asp":0, "Arg":0, "Cys":0, "Gln":0, "Glu":0, 
                    "Gly":0, "Gly":0, "His":0, "Ile":0, "Leu":0, "Lys":0, "Met":0,
                    "Phe":0, "Pro":0, "Ser":0, "Thr":0, "Val":0, "Trp":0, "Tyr":0, "STOP":0, "Total":0}
for i in range(len(rnaCodons)):
    if rnaCodons[i] in conversionChart:
        if (conversionChart[rnaCodons[i]] == "STOP"):
            rnaCodonCounter["STOP"]+=1
            rnaCodonCounter["Total"]+=1
        else:
            rnaCodonCounter[conversionChart[rnaCodons[i]]]+=1
            rnaCodonCounter["Total"]+=1


results = open("ProteinTranslation.txt", "w")
results.writelines([
    "----DNA Sequence----"+"\n"+dnaData+"\n",
    "\n","\n",
    "----RNA Sequence----"+"\n"+rnaData+"\n","\n","\n"
])


results.writelines(["----Total Proteins:"+str(len(convertedProteins))+" ----"+"\n"])


temp = ""
counter = 0
for i in range(len(convertedProteins)):
    for j in convertedProteins[i]:
        temp += j
        temp += "-"
    convertedProteins[i] = temp
    temp = ""
for key in proteinFrcy:
    results.writelines([convertedProteins[counter],
    "\n"
    ])

    counter+=1
    for count in proteinFrcy[key]:
        if (count=="Total"):
            pass
        else:
            results.writelines([""+count+ ": {:.2%}\n".format((proteinFrcy[key][count]/proteinFrcy[key]["Total"])),
    "\n"        
    ])

results.writelines(["----Protein Frequencies----\n"])
for key in rnaCodonCounter:
    if (rnaCodonCounter[key] <= 0):
        pass
    else:
        results.writelines([""+key+ ": {:.2%}\n".format((rnaCodonCounter[key]/rnaCodonCounter["Total"])),     
    ])
results.close()


