# Zarren Spry
# Rating 'A+'

def beaufont(M, K):
  # Build a list from the required cipher dictonary
  D = [ i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ_" ]
  # Expand key to the same size as the message
  L = (K * (len(M)//len(K) + 1))[:len(M)]
  # Run algebratic magic
  return ''.join([D[i] for i in list(map(lambda i,j: (D.index(j) - D.index(i)) % len(D), M, L))])


