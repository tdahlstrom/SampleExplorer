import archs4py as a4
import pandas as pd
import snakemake

file = snakemake.input[0]
df = a4.data.rand(file, 100, remove_sc=True)

x = pd.DataFrame(df.index)
x.index = x[0]
x.index.name = "gene_name"
x.columns = ["gene_name"]

x.to_pickle(snakemake.output[0])
