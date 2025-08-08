all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
resulting_names = list(filter(lambda name: name if name[0] == "R" else None, all_names))

print(resulting_names)




