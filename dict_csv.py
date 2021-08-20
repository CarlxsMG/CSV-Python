import csv

with open("archivo.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file,delimiter=",")
    
    for row in csv_reader:
        print(", ".join(row.keys())+"\n"+", ".join(row.values())+"\n"+("-"*50))
    
    print(csv_reader.line_num)

with open("archivo.csv", "a", newline="") as animal:
    csv_writer = csv.writer(animal, delimiter=",")

    csv_writer.writerow(['Grillo','23456','2000'])
    csv_writer.writerow(['Pollo_Loco','345','2'])

with open("archivo.csv", "a", newline="") as animal:
    csv_writer = csv.DictWriter(animal, fieldnames=['Animal','Body','Brain'])

    csv_writer.writeheader()
    csv_writer.writerow({'Animal':'Grillo','Body':'23456','Brain':'2000'})
    csv_writer.writerow({'Animal':'Pollo_Loco','Body':'345','Brain':'2'})