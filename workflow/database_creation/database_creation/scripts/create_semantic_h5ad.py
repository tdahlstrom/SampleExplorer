import pickle
import anndata as ad
import pandas as pd
import snakemake

# Specify the path to your pickle file
pickle_file_path = snakemake.input[0]

# Open the pickle file in binary mode (rb) to read
with open(pickle_file_path, "rb") as f:
    # Load the data from the pickle file
    data = pickle.load(f)

dfs = pd.read_pickle(snakemake.input[1]).reset_index(drop = True)

adata = ad.AnnData(data)

adata.obs = dfs

adata.write(snakemake.output[0])
