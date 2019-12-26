"""def reading_sequence():
  input = open("input.txt", "r")
  readable_seq = open("readable_seq.txt", "w")
  input_lines = input.readlines()
  input_lines.append("stop")
  a = 0
  while input_lines[a] != "stop":
    sequence = ""
    if input_lines[a][0] == ">":
      readable_seq.write(input_lines[a].replace("\r","").replace("\n","") + "\n")
      a += 1
    else:
      while input_lines[a][0] != ">":
        sequence += str(input_lines[a]).replace("\r","").replace("\n","")
        a+=1
        if input_lines[a] == "stop" or input_lines[a][0] == ">":
          break
      readable_seq.write(sequence + "\n")
    if input_lines[a] == "stop":
      break
  readable_seq.close()
reading_sequence()
input = open("readable_seq.txt", "r")
input_lines = input.readlines()

profile = {
  "A":[],
  "C":[],
  "G":[],
  "T":[]
}

n = 0
consensus = ""
while n != len(input_lines[1].replace("\n","")):
  a = 0
  c = 0
  g = 0
  t = 0
  for line in input_lines[1::2]:
    if line[n] == "A":
      a += 1
    elif line[n] == "C":
      c += 1
    elif line[n] == "G":
      g += 1
    elif line[n] == "T":
      t += 1
  profile["A"] += str(a)
  profile["C"] += str(c)
  profile["G"] += str(g)
  profile["T"] += str(t)
  if a == max([a, c, g, t]):
    consensus += "A"
  elif c == max([a, c, g, t]):
    consensus += "C"
  elif g == max([a, c, g, t]):
    consensus += "G"
  elif t == max([a, c, g, t]):
    consensus += "T"
  n += 1
print(consensus)
for key in profile:
  print(key + ": " + str(profile[key]).replace("[","").replace("]","").replace(",","").replace("'",""))"""


## Pseudo code

#Uses the "list of lists" approach to creating a matrix and assumes we're given three strings.

"""class MatrixObject:
    self.matrix = [ [length of DNA string], [length of DNA string], [length of DNA string] ]
    self.profile = [ [A-count goes here], [G-count goes here], [C-count goes here], [T-count goes here] ]
    #Each of the lists inside of self.profile is the same length as the DNA string.
    def add_string_to_matrix(dna_string): 
        self.matrix.append(list(dna_string))
    def create_profile():
        pos = 0
        for strand in self.matrix:
            for nuc in strand:
                if nuc == 'A':
                    self.profile[0][pos] += 1
                if nuc == 'G':
                    self.profile[1][pos] += 1
                if nuc == 'C':
                    self.profile[2][pos] += 1
                if nuc == 'T':
                    self.profile[3][pos] += 1
                pos += 1
     def create_con_string():
          con_string = ""
          for pos in range(length of DNA string):
              arg_max(self.profile[0][pos], self.profile[1][pos], self.profile[2][pos], self.profile[3][pos])
              if arg_max == 0:
                    con_string += 'A'
              if arg_max == 1:
                    con_string += 'G'
              if arg_max == 2:
                    con_string += 'C'
              if arg_max == 3:
                    con_string += 'T'
         return con_string"""

# with biopython

from Bio import SeqIO
from collections import Counter
s=[]
handle = open('rosalind_cons.txt', "r")
for record in SeqIO.parse(handle, "fasta"):
    s.append(str(record.seq))
handle.close()

a=[Counter([seq[x] for seq in s]) for x in range(len(s[0]))]
print(''.join([a[x].most_common(1)[0][0] for x in range(len(a))]))
print('A: ' + ' '.join([str(a[x]['A']) for x in range(len(a))]))
print('C: ' + ' '.join([str(a[x]['C']) for x in range(len(a))]))
print('G: ' + ' '.join([str(a[x]['G']) for x in range(len(a))]))
print('T: ' + ' '.join([str(a[x]['T']) for x in range(len(a))]))