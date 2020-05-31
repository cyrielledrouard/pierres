def merge(pierrestri):
    final = []
    pierrestri.sort()

    if len(pierrestri) == 0:
        return "La liste entrée est vide."

    while len(pierrestri) > 1:
        i = 1

        if pierrestri[0] == pierrestri[len(pierrestri) - 1]:
            i = len(pierrestri)
        else:
            while pierrestri[i - 1] == pierrestri[i]:
                i = i + 1

        valeur = pierrestri[0]
        del pierrestri[0:i]

        if i % 2 == 0:
            for j in range(0, int(i / 2)):
                pierrestri.insert(0, valeur + 1)

        if i % 2 == 1:
            for j in range(0, int((i - 1) / 2)):
                pierrestri.insert(0, valeur + 1)
            final.append(valeur)

    final.append(pierrestri[0])
    return final


# pierres = []
pierres = [1, 2, 3, 5, 1, 1, 1, 2, 5, 2]
res = merge(pierres)
print(res)
