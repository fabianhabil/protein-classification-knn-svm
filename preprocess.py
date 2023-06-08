import os

# Fungsi untuk membaca file FASTA dan mengembalikan label dan sekuen protein
def read_fasta(file_path, organism, maxData):
    labels = []
    sequences = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        label = None
        sequence = ''
        for line in lines:
            if line.startswith('>'):
                if label is not None:
                    organismName = getOrganismName(label)
                    if(organismName == organism):
                        labels.append(label)
                        sequences.append(sequence)
                label = line.strip()[1:]
                sequence = ''
            else:
                sequence += line.strip()
            if(len(labels) >= 3000 ):
                break
    return labels, sequences

def getOrganismName(strings):
    return strings.split("|")[-1].lower()

def write_fasta(file_path, labels, sequences):
    with open(file_path, "a") as file:
        for i in range(len(labels)):
            file.write(">"+labels[i] +"\n")
            file.write(sequences[i] + "\n")
    print(getOrganismName(labels[0]),"organisms written by",int(len(labels)),"data")

labels1, sequences1 = read_fasta("ecoli-original.fasta", "escherichia coli (562)", 3000)
labels2, sequences2 = read_fasta("homosapiens-original.fasta", "homo sapiens (9606)", 3000)
labels3, sequences3 = read_fasta("musmuculus-original.fasta", "mus musculus (10090)", 3000)
labels4, sequences4 = read_fasta("rattusnorvegicus-original.fasta", "rattus norvegicus (10116)", 3000)

write_fasta("dataset.fasta", labels1 ,sequences1)
write_fasta("dataset.fasta", labels2 ,sequences2)
write_fasta("dataset.fasta", labels3 ,sequences3)
write_fasta("dataset.fasta", labels4 ,sequences4)