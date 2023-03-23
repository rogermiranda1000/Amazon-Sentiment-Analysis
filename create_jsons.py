import gzip
import re
import numpy as np
import datetime
import json
import ipdb
from nltk.corpus import stopwords

if __name__ == "__main__":
	lines=[line.strip() for line in gzip.open('data/Watches.txt.gz')]
	splitters=np.where(map(lambda x: x=='',lines))[0]
	reviews=[dict()]*(splitters.shape[0])
	for review_id in xrange(splitters.shape[0]):
		try:
			review=dict([re.match(r'^([^:]+):(.*)',lines[r_field]).groups() for r_field in xrange(splitters[review_id-1]+1 if review_id else 0,splitters[review_id])])
		except:
			print xrange(splitters[review_id-1]+1 if review_id else 0,splitters[review_id])
		review['review/time']=datetime.datetime.fromtimestamp(float(review['review/time'].strip()))
		review['review/score']=float(review['review/score'].strip())
		review['review/text']=re.sub(r'\s\s+',' ',re.sub(r'[^A-Za-z 0-9]',' ',review['review/text'].strip().lower())).split()
		review['review/text']=[w for w in review['review/text'] if not w in stopwords.words()]   
		review=dict([('year',int(review['review/time'].strftime("%Y"))),('score',review['review/score']),('text',review['review/text'])])
		reviews[review_id]=review
	file=gzip.open('data/Watches.json.gz','wt')
	json.dump(reviews,file)
	file.close()