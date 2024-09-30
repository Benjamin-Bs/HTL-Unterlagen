import sys

state1 = 0
state2 = 0

oldstate1 = 0
oldstate2 = 0

f = open('cat.dec', 'w')


roundkeys = [0x00022312, 0x005fa32b, 0x005ac810]

sbox = [0xb7e15162, 0xbf715880, 0x38b4da56, 0x324e7738, 0xbb1185eb]


def aes_add_round_key(round_):
    global state1
    global state2
    state1 = state1 ^ roundkeys[(round_ & 1)] ^ round_
    state2 = state2 ^ roundkeys[(round_ & 1) + 1]


def aes_undo_round(round_):
    global state1
    global state2
    t = sbox[round_ % 5]

    Tm = t ^ state1
    Tmp = state2 ^ (Tm >> 16 | ((Tm * 0x10000) & 0xffffffff))

    Tm = ((Tm - (Tmp >> 0x18 | ((Tmp << 8) & 0xffffffff)) + 0x100000000) & 0xffffffff) ^ t

    Tmp = Tmp ^ (Tm >> 31 | ((Tm * 2)) & 0xffffffff)
    Tm = (((Tm - Tmp) + 0x100000000) & 0xffffffff) ^ t

    Tmp = Tmp ^ (Tm >> 17 | ((Tm * 0x8000) & 0xffffffff))
    Tm = ((Tm - (Tmp >> 0x11 | Tmp << 0xf) + 0x100000000) & 0xffffffff) ^ t

    state2 = Tmp ^ (Tm >> 0x18 | ((Tm * 0x100) & 0xffffffff))
    state1 = (Tm - (state2 >> 0x1f | ((state2 << 1) & 0xffffffff)) + 0x100000000) & 0xffffffff


def aes_undo(input1, input2):
    global state1
    global state2
    global oldstate1
    global oldstate2

    state1 = input1
    state2 = input2

    # undo final round
    aes_add_round_key(0)

    # undo round 9 to 0
    for i in range(9, -1, -1):
        aes_undo_round(i)
        aes_add_round_key(i)

    # undo CBC mode
    state1 = state1 ^ oldstate1
    state2 = state2 ^ oldstate2

    oldstate1 = input1
    oldstate2 = input2


def le_hex(intval):
    hex_string = format(intval, '08x')
    swapped_hex_string = ''.join(reversed([hex_string[i:i + 2] for i in range(0, len(hex_string), 2)]))
    return swapped_hex_string


with open(sys.argv[1], 'r') as file:
    hex_string = file.read().strip()

    for i in range(0, len(hex_string), 16):
        byte_string1 = hex_string[i:i + 8]
        byte_string2 = hex_string[i + 8:i + 16]

        little_endian1 = byte_string1[6:8] + byte_string1[4:6] + byte_string1[2:4] + byte_string1[0:2]
        little_endian2 = byte_string2[6:8] + byte_string2[4:6] + byte_string2[2:4] + byte_string2[0:2]

        value1 = int(little_endian1, 16)
        value2 = int(little_endian2, 16)

        aes_undo(value1, value2)
