# Fungsi untuk membaca file FASTA dan mengembalikan label dan sekuen protein
def read_fasta(file_path):
    id = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('>'):
                id.append(getId(line))
    return id

def getId(label):
    return label.split("|")[0].split(">")[1]

def removeDuplicate(ids):
    id_no_duplicate = {}
    for id in ids:
        new_id = id.split("_")[0]
        if (new_id in id_no_duplicate):
            continue
        id_no_duplicate[new_id] = 1
    return id_no_duplicate

def write_id(file_path, ids):
    with open(file_path, "w") as file:
        for id in ids:
            file.write(id+",")

id = read_fasta("rattusnorvegicus.fasta")
id_no_duplicate = removeDuplicate(id)
write_id("rattusnorvegicus-id.txt", id_no_duplicate)