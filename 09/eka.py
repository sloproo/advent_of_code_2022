with open("data.txt") as f:
    paan_liikkeet = []
    for r in f:
        liike = r.strip().split(" ")
        paan_liikkeet.append((liike[0], int(liike[1])))


