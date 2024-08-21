import csv

def read_data(file):
    data = []
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(tuple(row))
        return data

def format_data(data):
    formatted_data = []
    for row in data[1:]:
        cost = float(row[1])
        benef = float(row[2].strip("%"))
    
        formatted_data.append((row[0], cost, benef))
    return formatted_data

def write_formatted_data(formatted_data, output_file):
    with open(output_file, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Action', 'Cost', 'Benefit'])  # Écriture de l'en-tête
        writer.writerows(formatted_data)  # Écriture des données formatées


def compare_csv(file1, file2):
    # Lire les données du premier fichier CSV
    with open(file1, 'r') as f:
        reader = csv.reader(f)
        data1 = {row[0]: row[1:] for row in reader}

    # Lire les données du deuxième fichier CSV
    with open(file2, 'r') as f:
        reader = csv.reader(f)
        data2 = {row[0]: row[1:] for row in reader}

    # Trouver les noms communs aux deux ensembles de données
    common_names = set(data1.keys()) & set(data2.keys())

    # Retourner les entrées avec le même nom
    common_entries = []
    for name in common_names:
        entry1 = [name] + data1[name]
        entry2 = [name] + data2[name]
        common_entries.append((entry1, entry2))

    return common_entries

# Exemple d'utilisation
file1 = "dataSet1_return.csv"
file2 = "tes.csv"
common_entries = compare_csv(file1, file2)
for entry1, entry2 in common_entries:
    print("Entrée 1:", entry1)
    print("Entrée 2:", entry2)
    print()
print(len(common_entries))




