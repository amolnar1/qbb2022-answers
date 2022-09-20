#!/usr/bin/env python3

import numpy as np
import sys
from fasta import readFASTA
##import the right stuff

input_sequences = readFASTA(open(sys.argv[1]))

##need to import these matrixes appropriately as an array so its readable

matrix = np.loadtxt(sys.argv[2], dtype ="object", skiprows=1)
##system agrument is saying to work with the second file listed
header = list(matrix[:,0])
#print(header)
scorematrx = matrix[:,1:].astype(float)
#print(scorematrx)
# print(header)
# exit()

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

##we need to know how big our sequences are to make the array
##we just make the array idk?

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
Trace_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

# Now we need to fill in the values in the first row and
# first column, based on the gap penalty. Let's fill in the
# first column.

gap_penalty = float(sys.argv[3])

for i in range(len(sequence1)+1) :
    F_matrix[i,0] = i * gap_penalty
    Trace_matrix[i,0] = 3

# Now fill in the first row

for j in range(len(sequence2)+1) :
    F_matrix[0,j] = j * gap_penalty
    Trace_matrix[0,j] = 2
    
##checking the stuff cause it didnt work:
#trace_vals, trace_counts = np.unique(Trace_matrix, return_counts = True)
#print(trace_vals)
#print(trace_counts)

#### d = 1
#### h = 2
#### v = 3

#print(F_matrix)
#print(Trace_matrix)

##the penalties for stuff

# match_score = float(sys.argv[1])
# ##turning sys.argv output into a float
#
# mismatch_score = float(sys.argv[2])
#gap_penalty = float(sys.argv[3])
##gap penalty should be a negative value

##now we populate the matrixes
##we need to index the substitution matrix to figure out the match/mismatch score

#argmaxes = []

for i in range(1, len(sequence1)+1):
    ##i is the header
    for j in range(1, len(sequence2)+1):
        ##j is the score
        # n1 = sequence1[i-1]
#         n2 = sequence2[j-1]

        # you dont have nucleotide for sequence 1
        # you dont have nucleotide for sequence 2
        # define n1 and n2
        # find where in scorematrx n1 and n2 fall in
        # find d from scorematrx
        # compute match/mismatch/gap value to define F_matrix[i,j]
        #if i < 5 and j < 5:
            #print(sequence1[i-1])
            #print(sequence2[j-1])
            #print(header.index(sequence1[i-1]))
            #print(header.index(sequence2[j-1]))
            #print(scorematrx[header.index(sequence1[i-1]), header.index(sequence2[j-1])])
        index_i = header.index(sequence1[i-1])
        index_j = header.index(sequence2[j-1])
        ##needed to put n1 and n2 in index so we can get them
        d = F_matrix[i-1, j-1] + scorematrx[index_i, index_j]
        ##adding scorematrx values based on our index for i and j
        h = F_matrix[i, j-1] + gap_penalty
        v = F_matrix[i-1, j] + gap_penalty

        F_matrix[i,j] = max(d,h,v)
        #argmaxes.append(np.argmax([d,h,v]) +1)
        ##when we run it for hw we will care
        ##now our F matrix is populated

        ##now we need to populate the traceback matrix

       #### d = 1
       #### h = 2
       #### v = 3

        if d >= h and d >= v :
            Trace_matrix[i,j] = 1
        elif h >= v :
            Trace_matrix[i,j] = 2
        else :
            Trace_matrix[i,j] = 3
        ##this is populating the traceback matrix with either d h or v
        ##we need to fix this so that the sides are not only 0s because then we will stop at the wrong spot

#trace_vals, trace_counts = np.unique(Trace_matrix, return_counts = True)
#print(trace_vals)
#print(trace_counts)

#argmax_vals, argmax_counts = np.unique(argmaxes, return_counts = True)
#print(argmax_vals)
#print(argmax_counts)

#quit()


#print(Trace_matrix)

        ##we want to iterate backwards up the matrix
        ##can go up one and left one or 0
        ##we can be 1 distance from where we were or -1 distance

#print(Trace_matrix[::-1])

#for i, row in Trace_matrix[::-1] :
    ##so this is specifying that we start from the bottom corner


#Trace_matrix.shape
##idk what we need to do ummmmmm
##need a while loop and do an elif for all the options of gettin h, d, or v
##so like if its h, align1 += something, align2 += some stuff idk
##we have to do this for all the options
##i know while loops help us to edit the stuff without makign the loop confused


#print(Trace_matrix.shape)
#print(Trace_matrix.shape[0], Trace_matrix.shape[1])
#print(i-1, j-1)

# very bottom corner is which of the following ...
#print(Trace_matrix[i-1, j-1])
#this is not the bottom corner, it's diagonally above it.

#print(Trace_matrix[i, j])
#this is the very bottom corner, because when you filled the matrix with your nested for loop, i and j stopped at the bottom corner

#print(Trace_matrix[Trace_matrix.shape[0]-1, Trace_matrix.shape[1]-1])
#the line above is also giving us the bottom corner

#print(Trace_matrix[Trace_matrix.shape[0], Trace_matrix.shape[1] ])
#the line above doesn't work because it's out of bounds

#### d = 1
#### h = 2
#### v = 3

# this is us moving through our traceback matrix
#and building our alignments
seq1_alignment = ''
seq2_alignment = ''
## need to put the stuff in a list 

next_value = Trace_matrix[i, j]
##going through the different values in the matrixs
traceback = [next_value]
while i > 0 and j > 0 :
    ##going through the while loop so it doesnt go one forever
    if next_value == 2:
        seq1_alignment = "-" + seq1_alignment
        seq2_alignment = sequence2[j-1] + seq2_alignment
        ##making it move horizontally through the alignment for seq 2 or keeping the seq 1 value 
        j = j-1
    elif next_value == 1:
        seq1_alignment = sequence1[i-1] + seq1_alignment
        seq2_alignment = sequence2[j-1] + seq2_alignment
        i = i-1
        j = j-1
        ##making it ove through the sequence diagnoally and recoriding that value for i and j for sequence 1 and 2 
    elif next_value == 3:
        seq1_alignment = sequence1[i-1] + seq1_alignment
        seq2_alignment = "-" + seq2_alignment
        i = i -1
        ##making it move through the sequence vertically through it, recording the alignment for seq2 but a gap for seq1 
    next_value = Trace_matrix[i, j]
    traceback.append(next_value)
    ##going to the next value 

uniq_vals, uniq_counts = np.unique(traceback, return_counts = True)
print(uniq_vals)
print(uniq_counts)
print(seq1_alignment)
print(seq2_alignment)


##me trying to figure it out before haha:

# while i > 0
#
#
#
#     if i == 0 :
#         best_index = len(row)
#     else :
#         v_gap = best_index
#         v_match = best_index - 1
#         ## -1 makes it go up to the left from the corner
#         if row[v_gap] < row[v_match] :
#             best_index = v_match
#             ##this selects for the matching over the gapping if the score is            the same
#             ##best_index is us choosing to go left or not, its is our j
#
# ##how do we put this into the F_matrix?
# ##how do we rebuild the sequence from this information
# ##we need to align sequence 2 to sequence 1
# ##we need to repopulate sequence 2 with the best options based on F matrix scores
# ##we have to say the movement of diagnol or straight up equals its corresponding j sequence position
# ##idk how to do this erhgjahd'piqwnd
