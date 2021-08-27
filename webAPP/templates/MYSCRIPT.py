from gensim.models.doc2vec import Doc2Vec
import pandas as pd
model= Doc2Vec.load("d2v.model")
df_tag=pd.read_csv('Stage 2A/SummerInternship/version 3/df_lab_IFRS_full_2021.csvdf_lab_IFRS_full_2021.csv')
def return_label(A):
    tokens = A.split()
    new_vector = model.infer_vector(tokens)
    sims = model.docvecs.most_similar([new_vector])
    Top10=[]
    for i in range(10):
        Top10.append(list(df_tag['IFRS_tag'])[int(sims[i][0])])

    return Top10