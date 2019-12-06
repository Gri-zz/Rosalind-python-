# FASTA format -> string number, GC ratio

""" the most awkward tryout
import collections

print(collections.Counter())


print((+)/(+++)*100)
"""

# ideal solution

import re

f=open("C:\\Users\\tony9\Desktop\\Y\\rosalind_gc.txt","r")


lines = f.readlines()
name=[]
score=[]
seq=[]
temp=[]
lengthlines = len(lines)-1

for line in lines:
    if re.match(">",line):
        name.append(line.replace(">",""))
        if temp :
            seq.append("".join(temp))
            temp=[]

    else:
        if lines[lengthlines]==line:
            temp.append(line)
            seq.append("".join(temp))
        else :
            temp.append(line)

for i in range(0,len(seq)):
    length = len(seq[i]) - seq[i].count("\n")
    score.append((seq[i].count("C")+seq[i].count("G"))/length*100)


maxvalue = score.index(max(score))
print(name[maxvalue])
print(round(score[maxvalue],6))
f.close()

#another sol
"""
f = open('rosalind_gc.txt', 'r')

max_gc_name, max_gc_content = '', 0

buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
f.close()
"""

# and another one
"""
dna = {}

while True:
  try:
    line = input()
    if line[0] == '>':
      label = line[1:]
      dna[label] = ""
    else:
      dna[label] += line
  except EOFError:
    break

def gc_content(e):
  l, s = e
  return 100 * (s.count('G') + s.count('C')) / len(s)

e = max(dna.items(), key=gc_content)
print(e[0])
print(gc_content(e))
"""