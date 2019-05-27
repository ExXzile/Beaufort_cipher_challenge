# Mark Geyzer
# Rating A+

def mark_geyzer_beaufort_cipher(message, key, chars=[chr(ord('A') + c) for c in range(26)] + ['_']):
    import itertools
    return ''.join(chars[chars.index(k) - chars.index(m)] for m, k in zip(message, itertools.cycle(key)))

# -------------------------------------------------------------------------------------------------------
# Mark Geyzer
# Rating A

def mark_geyzer_beaufort_cipher1(message, key):
    import itertools
    import string
    chars=list(string.ascii_uppercase) + ['_']
    return ''.join(chars[chars.index(k) - chars.index(m)] for m, k in zip(message, itertools.cycle(key)))
 
 # -------------------------------------------------------------------------------------------------------
