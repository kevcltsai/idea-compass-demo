"""Offline, reproducible character n-gram TF-IDF + latent semantic (SVD) vectors.
Does not use pretrained OpenAI or other commercial embedding APIs.
"""
import json, pathlib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize
BASE=pathlib.Path(__file__).resolve().parents[1]
entries=[]
for line in (BASE/'data'/'concepts.tsv').read_text(encoding='utf-8').splitlines():
    if not line.strip() or line.startswith('#'): continue
    parts=line.split('|')
    if len(parts)!=5: raise ValueError(line)
    id,name,domain,description,mechanism=parts
    entries.append(dict(id=id,name=name,domain=domain,description=description,mechanism=mechanism))
texts=[(' '.join([e['name']]*3+[e['domain']]*2+[e['description']]*2+[e['mechanism']])) for e in entries]
vec=TfidfVectorizer(analyzer='char',ngram_range=(2,4),min_df=1,sublinear_tf=True)
x=vec.fit_transform(texts)
dims=min(48,x.shape[0]-1,x.shape[1]-1)
svd=TruncatedSVD(n_components=dims,random_state=42,n_iter=12)
v=normalize(svd.fit_transform(x))
# Ensure representation of clear global cluster across small corpus by fusing SVD and TFIDF cosine.
tfidf_cos=(x@x.T).toarray();svd_cos=v@v.T
similarities=np.clip(.55*tfidf_cos+.45*np.maximum(0,svd_cos),0,1)
# Existing bilingual concept names often have very few shared Chinese ngrams;
# use domain and curated cross-links as explanatory scaffolding, not fabricated distances.
for i,e in enumerate(entries):
    ordered=np.argsort(-similarities[i])
    e['related']=[entries[j]['id'] for j in ordered if j!=i][:10]
    e['vector']=[round(float(z),5) for z in v[i]]
# Precomputed exact cosine similarities from the same hybrid representation for deterministic display.
output={'metadata':{'algorithm':'Character n-gram TF-IDF (2–4) + TruncatedSVD (48D), weighted cosine','language':'zh-Hant','nodes':len(entries),'warning':'Corpus-specific statistical vectors; not a pretrained semantic embedding model. Scores are relative within this curated demo.'},'nodes':entries,'similarity':[[round(float(z),5) for z in row] for row in similarities]}
(BASE/'data'/'knowledge.json').write_text(json.dumps(output,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print('Built',len(entries),'nodes with',dims,'D latent vectors; file bytes:',(BASE/'data'/'knowledge.json').stat().st_size)
