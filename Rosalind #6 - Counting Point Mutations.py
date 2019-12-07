
seq = [line.strip('\n') for line in open('C:\\Users\\tony9\\Desktop\\dd\\rosalind_hamm.txt')]
hamming = 0
for nt1, nt2 in zip(seq[0],seq[1]):
    if nt1 != nt2:
        hamming += 1

print(hamming)

"""
def hamming(s, t):
    return len (filter(lambda pair: pair[0]!=pair[1], zip(list(s),list(t))))
"""

"""
n = hamming = 0
while n <= len(a)-1:
    if a[n] != b[n]:
        hamming += 1
    n += 1
print hamming
"""