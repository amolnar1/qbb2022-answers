#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    in1_fname, in2_fname, bin_fname, in3_fname, out_fname = sys.argv[1:6]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))
    data3 = numpy.loadtxt(in3_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1
                                       
    #print(start_bin)
    #print(end_bin)
    #print(data1)

    
    ##picking things out by the starts and the ends of the things
    
    #print(data1['F1'] >= start_bin)
    
    data1_pos = numpy.where( (data1['F1'] >= start_bin) & (data1['F2'] <= end_bin) ) 
    data1_filtered = (data1[data1_pos])
    data1_filtered['score'] = numpy.log( data1_filtered['score'])
    data1_filtered['F1'] = data1_filtered['F1'] - start_bin
    data1_filtered['F2'] = data1_filtered['F2'] - start_bin
    data1_filtered['score'] =  data1_filtered['score'] - numpy.min(data1_filtered['score'])
    #print(data1_filtered)
    
    data2_pos = numpy.where( (data2['F1'] >= start_bin) & (data2['F2'] <= end_bin) ) 
    data2_filtered = (data2[data2_pos])
    data2_filtered['score'] = numpy.log( data2_filtered['score'])
    data2_filtered['F1'] = data2_filtered['F1'] - start_bin
    data2_filtered['F2'] = data2_filtered['F2'] - start_bin
    data2_filtered['score'] =  data2_filtered['score'] - numpy.min(data2_filtered['score'])
    #print(data2_filtered)
    
    mat1 = numpy.zeros( [end_bin - start_bin + 1, end_bin - start_bin + 1] )
    mat1[data1_filtered['F1'], data1_filtered['F2']] = data1_filtered['score']
    mat1[data1_filtered['F2'], data1_filtered['F1']] = data1_filtered['score']
    ##putting our stuff in the matrix
    
    #print(mat1)
    
    mat2 = numpy.zeros( [end_bin - start_bin + 1, end_bin - start_bin + 1] )
    mat2[data2_filtered['F1'], data2_filtered['F2']] = data2_filtered['score']
    mat2[data2_filtered['F2'], data2_filtered['F1']] = data2_filtered['score']
    ##putting our stuff in the matrix
    
    #print(mat1)

    
    ##make the heat map
    fig, ax = plt.subplots(3)
    ax[0].imshow(mat1,cmap='magma')
    #ax[0].imshow(mat1, vmin = 0, vmax = 1, cmap='magma')
    ax[0].set_title('ddCTCF')
    
    
    ##make the heat map

    ax[1].imshow(mat2,cmap='magma')
    #ax[0].imshow(mat1, vmin = 0, vmax = 1, cmap='magma')
    ax[1].set_title('dCTCF')
    
    
    mat1_modified = remove_dd_bg(mat1)
    mat2_modified = remove_dd_bg(mat2)
    
    mat1_modified = smooth_matrix(mat1_modified)
    mat2_modified = smooth_matrix(mat2_modified)
    
    final = (mat2_modified - mat1_modified)
    #print(final)
    
    ax[2].imshow(final,cmap='magma')
    #ax[0].imshow(mat1, vmin = 0, vmax = 1, cmap='magma')
    ax[2].set_title('dCTCF - ddCTCF')
    fig.tight_layout()
    plt.show()
    fig.savefig( "week6" + ".png" )
    
    #####################################
    ######################################
    
    data3_pos = numpy.where( (data3['F1'] >= 54878) & (data3['F2'] <= 54951) ) 
    data3_filtered = (data3[data3_pos])
    data3_filtered['score'] = numpy.log( data3_filtered['score'])
    data3_filtered['F1'] = data3_filtered['F1'] - 54878
    data3_filtered['F2'] = data3_filtered['F2'] - 54878
    print(data3_filtered)
    data3_filtered['score'] =  data3_filtered['score'] - numpy.min(data3_filtered['score'])
    #print(data1_filtered)

    
    mat3 = numpy.zeros( [54951 - 54878 + 1, 54951 - 54878 + 1] )
    mat3[data3_filtered['F1'], data3_filtered['F2']] = data3_filtered['score']
    mat3[data3_filtered['F2'], data3_filtered['F1']] = data3_filtered['score']
    ##putting our stuff in the matrix
    
##do stuff to data before plot

#########################################3
############################################
##making insulation scores

    insulation_scores = []
    nt_list = []
    
    for i in range(5, 54951 - 54878 + 1) :
        insulation_scores.append(numpy.mean(mat3[(i - 5):i, i:(i + 5)]))
        #print(insulation_scores)
        
    nt_list = numpy.linspace(10400000, 13400000, len(insulation_scores))
    
    
    fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    ax[0].axis('off')
    plt.margins(x=0)
    ax[1].set_xlim(10400000, 13400000)
    plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=1.0,
                    top=1.0,
                    wspace=0.4,
                    hspace=0.0)
                    
    ax[0].imshow(mat3,cmap='magma')
    #ax[0].imshow(mat1, vmin = 0, vmax = 1, cmap='magma')
    ax[0].set_title('dCTCF 40000')
    
    ax[1].scatter(nt_list, insulation_scores)
    ax[1].set_xlabel("nucleotide position")
    ax[1].set_ylabel("insulation score")
    ax[1].set_title("Insulation Scores")
    fig.tight_layout()
    
    
    
    plt.show()
    fig.savefig( "dCTCF_40000" + ".png" )



def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2


def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat
    
   

if __name__ == "__main__":
    main()
    
    

