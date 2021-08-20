import csv

with open("archivo.csv") as csv_file:
    csv_reader = list(csv.reader(csv_file,delimiter=","))

    for row in csv_reader:
        if csv_reader.index(row) == 0:
            print("Las columnas son: {}".format(", ".join(row)))

        else:
            print("{}: {}\n{}: {}\n{}: {}".format(csv_reader[0][0],row[0],csv_reader[0][1],row[1],csv_reader[0][2],row[2]))

        print("-"*50)
    
    print(len(csv_reader))