# #This is a solution to the problem on https://github.com/smartninja/wd1-py3-exercises/tree/master/lesson-11/CSI.


suspects = {
    "Eva": ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],
    "Larisa": ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
    "Matej": ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
    "Miha": ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]
}


with open("dna.txt", "r") as dna_sequence:
    dna_string = dna_sequence.read()


for suspect in suspects:
    for char in suspects[suspect]:
        found = False
        if char in dna_string:
            found = True
        else:
            break
    if found:
        print(f"We found the suspect. The ice cream thief was {suspect} all along!")
