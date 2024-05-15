def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i + 4]) for i in range(0, len(text), 4)]


def matrix2bytes(matrix):
    """ Konvertiert eine 4x4-Matrix in einen String. """
    # Erstelle eine leere Liste, um die Bytes zu speichern
    bytes_array = []

    # Iteriere über jede Spalte in der Matrix
    for col in matrix:
        # Füge die Elemente der aktuellen Spalte der bytes_array-Liste hinzu
        bytes_array.extend(col)

    # Konvertiere die Liste von Bytes in einen String und gib ihn zurück
    return ''.join(chr(byte) for byte in bytes_array)

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))
