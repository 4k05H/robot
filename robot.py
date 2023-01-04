def beker():
    utvonallsita = []
    utvonal = input("kérem adjon meg egy útvonalat! (E, D, K, N): ")
    utvonal = utvonal.upper()
    for elem in utvonal:
        utvonallsita.append(elem)
    for elem in utvonallsita:
        while not (elem == "E" or elem == "D" or elem == "K" or elem == "N"):
            utvonal = input("Hibás adat! Kérem adjon meg egy útvonalat! (E, D, K, N): ")
            utvonal = utvonal.upper()
            utvonallsita.clear()
            for elem in utvonal:
                utvonallsita.append(elem)
    print(utvonallsita)
    return utvonallsita

def szamolas():
    utvonal = beker()
    ebetu = 0
    dbetu = 0
    kbetu = 0
    nbetu = 0

    for elem in utvonal:
        if elem == "E":
            ebetu += 1
        elif elem == "D":
            dbetu += 1
        elif elem == "K":
            kbetu += 1
        elif elem == "N":
            nbetu += 1

    print(f"Az E betűk száma: {ebetu}")
    print(f"Az D betűk száma: {dbetu}")
    print(f"Az K betűk száma: {kbetu}")
    print(f"Az N betűk száma: {nbetu}")
    utvonalszamolas(ebetu, dbetu, kbetu, nbetu)

def utvonalszamolas(e, d, k, n):
    utvonal = ""
    if e < d:
        utvonal += (d - e) * "D"
    elif d < e:
        utvonal += (e - d) * "E"

    if k < n:
        utvonal += (n - k) * "N"
    elif n < k:
        utvonal += (k - n) * "K"

    print(utvonal)