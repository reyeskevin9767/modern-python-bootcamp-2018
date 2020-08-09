
# * Write DictWriter
# from csv import DictReader, DictWriter
# with open("example.csv", "w") as file:
#     headers = ["Character", "Move"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Character": "Ryu",
#         "Move": "Hadouken"
#     })

# with open("example.csv", 'w') as file:
#     headers = ["Name", "Breed", "Age"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         'Name': 'Garfield',
#         "Breed": "Orange Tebby",
#         "Age": 10
#     })


def cm_to_in(cm):
    return float(cm) * 0.393701


with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("inches_fighters.csv", 'w') as file:
    headers = ["Name", "Country", "Height"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": cm_to_in(f["Height (in cm)"])
        })
