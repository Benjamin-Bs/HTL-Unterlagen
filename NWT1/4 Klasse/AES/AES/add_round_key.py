state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    """ Führt die AddRoundKey-Operation durch, indem die entsprechenden Elemente der Zustands- und Rundenschlüsselmatrizen XOR-verknüpft werden. """
    # Initialisiere einen leeren String, um das Ergebnis zu speichern
    result = ""

    # Iteriere über jede Zeile in den Zustands- und Rundenschlüsselmatrizen
    for i in range(len(s)):
        for j in range(len(s[i])):
            # Führe die XOR-Verknüpfung zwischen den entsprechenden Elementen der Zustands- und Rundenschlüsselmatrizen durch
            # und konvertiere das Ergebnis in ein Zeichen und füge es zum Ergebnisstring hinzu
            result += chr(s[i][j] ^ k[i][j])

    # Gib den Ergebnisstring zurück
    return result


print(add_round_key(state, round_key))
