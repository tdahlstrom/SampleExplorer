import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import snakemake

RAG_data = pd.read_csv(snakemake.input[0])

smaller_df_for_RAG = RAG_data[["title", "summary", "overall_design","series_id"]]

smaller_df_for_RAG["rag_text"] = RAG_data["title"] + "\n." + RAG_data["summary"] + "\n." + RAG_data["overall_design"]

rag_input = smaller_df_for_RAG[['series_id', 'rag_text']].drop_duplicates()

rag_input.to_pickle(snakemake.output[0])

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Sentences we want to encode. Example:
#sentence = ['This framework generates embeddings for each input sentence']

# Sentences are encoded by calling model.encode()
#embedding = model.encode(sentence)

sentences = rag_input["rag_text"].to_list()
embedding = model.encode(sentences)

file_path = "snakemake.output[1]"

# Save the matrix to a pickled file
with open(file_path, 'wb') as file:
    pickle.dump(embedding, file)
