maListe = [4, 8, 415, 1, 25, 75, 6]

def tri(ml):
    FlagPermutation = True
    limit = len(ml)
    while FlagPermutation:
        for i in range(0, limit-1):
            FlagPermutation = False
            if (ml[i] > ml[i+1]):
                ml[i+1], ml[i] = ml[i], ml[i+1]
                FlagPermutation = True
        limit = limit-1
    print(ml)

tri(maListe)

