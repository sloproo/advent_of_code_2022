with open("data.txt") as f:
    data = f.readline()

for i in range(len(data) - 3):
    merkit = data[i:i+4]
    kirjaimet = set([merkki for merkki in merkit])
    if len(kirjaimet) == 4:
        print(f"Ensimmäisen paketinalkumarkkerin viimeinen merkki on {i+4} :s merkki")
        break
    