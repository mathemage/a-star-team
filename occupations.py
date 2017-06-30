def load_occupations():
    occupations = []
    with open("occupations.csv", "r") as file:
        for line in file:
            occupations.append(line.replace("\n",""))
    return occupations

occupations = load_occupations()