def main():
    with open('ct.txt') as file:
        data = [i for i in file.read().split('\n') if i]
    data = [[k for j in i.split('  ') for k in j.split(' ')] for i in data]
    print(data)
    with open('known_plaintext.txt') as file:
        plain = [i for i in file.read().split('\n') if i]
    key = construct_key(plain, data)
    m = [['_' for _ in row] for row in data]
    for i, c in enumerate(data):
        for j, num in enumerate(c):
            if num.isalnum():
                for k in key:
                    if num in k:
                        m[i][j] = key[k]
            else:
                if num:
                    m[i][j] = num
                else:
                    m[i][j] = ' '
    m = [''.join(i) for i in m]
    print('\n'.join(m))
    with open('plaintext.txt', 'w') as file:
        file.write('\n'.join(m))


def construct_key(m, c):
    k1 = dict()
    for i, row in enumerate(m):
        k2 = dict()
        for j, char in enumerate(row):
            if char.isalnum():
                k2.update({c[i][j]: char})
        k1 = update_key(k1, k2)
    return k1


def update_key(d1: dict, d2: dict):
    for key2, char2 in d2.copy().items():
        for key1, char1 in d1.copy().items():
            if char1 == char2:
                if key2 not in key1:
                    new_key = ' '.join([key1, key2])
                    d1.update({new_key: char1})
                    d1.pop(key1)
                    if key2 in d2:
                        d2.pop(key2)
    d1.update(d2)
    return d1


if __name__ == "__main__":
    main()