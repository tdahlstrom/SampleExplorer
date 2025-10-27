import archs4py as a4
import pandas as pd
import snakemake

file = snakemake.input[0]

metadata = a4.meta.meta(file, ".*", meta_fields=["series_id", "characteristics_ch1", "extract_protocol_ch1", "source_name_ch1", "title"])
metdata_clean = metadata.drop_duplicates()
metdata_clean.to_csv(snakemake.output[0])

result_superseries = metdata_clean[metdata_clean['series_id'].str.contains(',')]
result_superseries.to_csv(snakemake.output[1])

result_no_superseries = metdata_clean[~(metdata_clean['series_id'].str.contains(','))]
result_no_superseries.to_csv(snakemake.output[2])

x = pd.read_csv(snakemake.output[2])
x1 = pd.DataFrame(x["series_id"].unique())
x1.columns = ["gse_id"]
x1.to_csv(snakemake.output[3])

x2 = pd.read_csv(snakemake.output[2])
x2_parsed = pd.DataFrame(x2["series_id"].str.split(",", expand = True).stack().reset_index(drop=True).unique()).dropna()
x2_parsed.columns = ["gse_id"]# 3106
x2_parsed.to_csv(snakemake.output[4])
