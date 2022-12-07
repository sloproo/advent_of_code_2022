with open("data.txt") as f:
    data = f.readline()

for i in range(len(data) - 13):
    merkit = data[i:i+14]
    kirjaimet = set([merkki for merkki in merkit])
    if len(kirjaimet) == 14:
        print(f"Ensimmäisen viestinalkumarkkerin viimeinen merkki on {i+14} :s merkki")
        break
    