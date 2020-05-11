#This is a solution to the problem on https://github.com/smartninja/wd1-py3-exercises/tree/master/lesson-11/CSI.


suspects = {"Eva": ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "Larisa": ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
          "Matej": ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "Miha": ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]
          }


with open('dna.txt', 'r') as dna_sequence:
    dna_string = dna_sequence.read()

for suspect in suspects:
    counter = 0
    for char in suspects[suspect]:
        if char in dna_string:
            counter += 1
            if counter == 5:
                print(f"We found the suspect. The ice cream thief was {suspect} all along!")
