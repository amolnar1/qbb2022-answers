import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

##plots before filtering 
sc.tl.pca(adata, svd_solver='arpack')
sc.pl.pca(adata, save = 'unfiltered.png')
#sc.pl.StackedViolin.savefig(unfiltered_pca)


##now we want to filter the stuff########################

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)

#print(adata)

##make a da plot
sc.tl.pca(adata, svd_solver='arpack')
sc.pl.pca(adata, save = 'filtered.png')
#sc.pl.StackedViolin.savefig(filtered_pca)

##now we need to cluster the stuff########################
##it is mad if we dont make friends with our neighbors

sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)

sc.tl.leiden(adata)
##tl does the math and pl plots the math
sc.tl.umap(adata, maxiter= 1000)
sc.pl.umap(adata, color='leiden', save = 'umap.png')
sc.tl.tsne(adata)
sc.pl.tsne(adata, save ='tsneplt.png')

##distinguishing genes####################################


sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)

###################some nonsense#####################################

# genes = []
# genes.append
#
# for i in range(0len())


##cell types??##############################################

marker_genes = ['Nrxn3', 'Igfbpl1', 'Basp1', 'Dbi', 'Stmn2', 'Meg3']

sc.tl.rank_genes_groups(adata, 'leiden', groups=['0'], reference='1', method='wilcoxon')
sc.pl.rank_genes_groups(adata, groups=['0'], n_genes=20)

new_cluster_names = ['AC','FB3','MG','OL', 'aEC','FB2', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
adata.rename_categories('leiden', new_cluster_names)

sc.pl.umap(adata, color='Nrxn3', legend_loc='on data', title='', frameon=False, save='nrxm3.pdf')
sc.pl.umap(adata, color='Igfbpl1', legend_loc='on data', title='', frameon=False, save='igfbp1.pdf')
sc.pl.umap(adata, color='Basp1', legend_loc='on data', title='', frameon=False, save='basp1.pdf')
sc.pl.umap(adata, color='Dbi', legend_loc='on data', title='', frameon=False, save='dbi.pdf')
sc.pl.umap(adata, color='Stmn2', legend_loc='on data', title='', frameon=False, save='stmn2.pdf')
sc.pl.umap(adata, color='Meg3', legend_loc='on data', title='', frameon=False, save='meg3.pdf')

