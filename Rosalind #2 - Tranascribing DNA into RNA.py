seq = "GTAACTACGGAAAGGTCACCCTCGCACGGAGCCGGTGAGCGGAACTTCGTGAGGCGGAGGTGACACAATTATTGTAACCCCATCGCAATTATCAGGTTAGTGAATTCAGGCCCTCCACCCTTTCTCATCGCCGAGTCAAACCCTTCATCGTTGGGGTTTCTATCCCACCTTTCCGCAGGAAATACCAGCCGTTACTGAGGGCCATGTGAGATGTCATGGCGGTAAAGTGTCGCACGATATATATAAAACTACAGTCCTCGTACTTCCGCATCTCACGAGTGTCTTCTTTTACTTCCGCGCATCAGAAGACATGCGATGGCTTATAGCCGATTGGGTGGCGTTGGCCAATCACTAGTACGTTCTGGATTGCCGTTATACTAAACTCATAGGTGGGAACAGACACTGTGCTAAGGGTCGGCATAAAGGTCATGTAAGGGTAAGCACCCAACGGAATGCTACAGCGTGTTCGTAATGAGATGGACTTCGTTTATTCACGCTAGTATCCGAAGAGCATCAGCGCATATCATTCAACGCGGCGAATCTTGCGCACAGGCCGCTTATAGCTCGGCTCACGCCCACGGAGATTGGTCAGATAGCTTGGTGGGCTAGTATCGTCTCACCTAGAGGTCGAAAGAAAGAGTCGAGCAGTCGGTTCTCTGTGCGAATTCAATCCAGCGACTACGAGGCTGTCCAACTATATCTATATGGTCGGGGGGTTACGCGGGTAGTATGCGAACTGCCAGTGGCAGACTGTCTCCATGTACATGAGTCCACTGCAGCCCCCTTATTGGGACACTAAACGGTACCTTCAAAGAGCACCGACGCCCCATACAATGGATAATCTCGGGCCATCACGTACATGCACCGGCGGCCGGAGGAGTCTACGTCCTGTGACGGTCCGCCCACTGACATGCTACAACGGTCAGGTTAGTACGGGCGAGAGACAAC"

RNA_seq = ""

for s in seq:
    if s == "A":
           RNA_seq += "A"
    if s == "T":
         RNA_seq += "U"
    if s == "G":
          RNA_seq += "G"
    if s == "C":
        RNA_seq += "C"

print(RNA_seq)

# faaaaaaaar mor easy way -> RNA_seq = seq.replace("T", "U")

