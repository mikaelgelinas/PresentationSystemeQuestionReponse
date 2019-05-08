import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

sentence = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))
print(ne_tree)

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)
print(sent)

pattern = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

NPChunker = nltk.RegexpParser(pattern) 
result = NPChunker.parse(sent)
#result.draw()

from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint

iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
pprint([(X.text, X.label_) for X in doc.ents])

pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])

from bs4 import BeautifulSoup
import requests
import re

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
article = nlp(ny_bb)
print(len(article.ents))

labels = [x.label_ for x in article.ents]
print(Counter(labels))

items = [x.text for x in article.ents]
print(Counter(items).most_common(3))

sentences = [x for x in article.sents]
sentenceNumber = 15
print(sentences[sentenceNumber])

#displacy.render(nlp(str(sentences[sentenceNumber])), jupyter=False, style='ent')

#displacy.render(nlp(str(sentences[sentenceNumber])), style='dep', jupyter = False, options = {'distance': 120})



[(x.orth_,x.pos_, x.lemma_) for x in [y 
                                      for y
                                      in nlp(str(sentences[sentenceNumber])) 
                                      if not y.is_stop and y.pos_ != 'PUNCT']]

dict([(str(x), x.label_) for x in nlp(str(sentences[sentenceNumber])).ents])

#print("**********************************************************")
#print([(x, x.ent_iob_, x.ent_type_) for x in sentences[sentenceNumber]])
#print("**********************************************************")


import string
import ImportInElasticSearch as ES

#pr = PreTraitement()

#datas = pr.PrepareDatas()
#esDatas = pr.PrepareDatasForElasticSearch(datas, index="NER", doc_type="NER")



print("Begin PrepareDatasForElasticSearch")
esDatas = []
index = "test"
doc_type = index
i = 1
for item in sentences:
    esData = {"id": i,
                "index": index,
                "doc_type": doc_type,
                "body": item}
    esDatas.append(esData)
    i += 1

print("End PrepareDatasForElasticSearch")
#return esDatas



es = ES.ES()

es.Imports(esDatas)