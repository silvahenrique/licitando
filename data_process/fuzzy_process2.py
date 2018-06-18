import json
import operator
from collections import OrderedDict
from fuzzywuzzy import fuzz

min_rate = 2


class Comp:
    def __init__(self, desc, fornecedor_classe, rate, oc):
        self.desc = desc
        self.fornecedor_classe = fornecedor_classe
        self.rate = rate
        self.oc = oc

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.desc, self.fornecedor_classe, self.rate, self.oc)


def process_text(str_cmp, str_exact):
    return fuzz.ratio(str_exact, str_cmp)


with open('../data_extraction/ocs_full_data.json', encoding='utf-8') as f:
    ocs = json.load(f)

with open('../data_extraction/fornecedores.json', encoding='utf-8') as f:
    fornecedores = json.load(f)

fornecedor = fornecedores[3]['Produto']

similarities = []
for oc in ocs:
    oc = oc[0]
    items = oc['ITENS']
    for item in items:
        rate = process_text(str_cmp=fornecedor.upper(), str_exact=item['DESCRICAO_ITEM'].upper())

        comp = Comp(item['DESCRICAO_ITEM'], fornecedor, rate, oc)
        similarities.append(comp)

similarities.sort(key=lambda x: x.rate, reverse=False)

for similarity in similarities:
    if similarity.rate >= min_rate:
        print(similarity)
