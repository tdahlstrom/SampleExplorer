import anndata as ad
import numpy as np
import pandas as pd
import pickle
import snakemake

rows = snakemake.params.rows
cols = snakemake.params.cols

memmap_filename = snakemake.input[1]
reloaded_memmap_matrix = np.memmap(memmap_filename, dtype='float16', mode='r', shape=(rows, cols))

test = np.copy(reloaded_memmap_matrix)
adata = ad.AnnData(test)
obs_df = pd.read_pickle(snakemake.input[0])
var_df = pd.read_pickle(snakemake.input[2])
var_df.columns = ["gene"]
adata.obs = obs_df
adata.var = var_df

with open(snakemake.output[0], 'rb') as file:
    embedding_matrix = pickle.load(file) 

adata.obsm["embedding"] = embedding_matrix
adata.write(snakemake.output[1])

