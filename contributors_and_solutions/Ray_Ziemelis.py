
# Ray Ziemelis
# Rating 'A+'

def beaufort_cipher_mathematical(m, key):

    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'

    key = (key * (int(len(m) / len(key) + 1)))[0: len(m)]

    answr = [u[(u.index(k) - u.index(m)) % len(u)] for m, k in zip(m, key)]

    return ''.join(answr)


# -------------------------------------------------

# Ray Ziemelis
# Rating 'C'

def beaufort_cipher_manual(message, key):

    UPPERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    alpha_len = len(UPPERS)
    answer = ''
    matrix = [[UPPERS[(n + mod) % alpha_len] for n in range(alpha_len)]
              for mod in range(alpha_len)]

    while len(key) <= len(message):
        key += key
    key = key[0: len(message)]

    for m, k in zip(message, key):
        idx = matrix[0].index(m)
        for check in matrix:
            if check[idx] == k:
                answer += check[0]
                break

    return answer
