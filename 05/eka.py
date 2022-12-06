import string

pylvaat = [[] for _ in range(9)]

with open("data.txt") as f:
    for r in f:
        if r[0] == "[":
            for i in range(1, 35, 4):
                if r[i] in string.ascii_uppercase:
                    pylvaat[(i-1) // 4].append(r[i])
        else:
            f.readline()
            break

    for r in f:
            r_listana = r.strip().split(" ")
            kaskyt = [int(r_listana[i]) for i in [1, 3, 5]]
            print(kaskyt)
            