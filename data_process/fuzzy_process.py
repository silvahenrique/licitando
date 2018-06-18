import json
from fuzzywuzzy import fuzz

min_rate = 95


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


class Comparison:
    def __init__(self, desc, fornecedor_classe, fornecedor_email, rate, oc):
        self.desc = desc
        self.fornecedor_classe = fornecedor_classe
        self.rate = rate
        self.oc = oc
        self.fornecedor_email = fornecedor_email

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.desc, self.fornecedor_classe, self.fornecedor_email, self.rate, self.oc)


def process_text(str_cmp, str_exact):
    return fuzz.ratio(str_exact, str_cmp)


with open('../data_extraction/ocs_full_data.json', encoding='utf-8') as f:
    ocs = json.load(f)

with open('../data_extraction/fornecedores.json', encoding='utf-8') as f:
    fornecedores = json.load(f)

fornecedor = fornecedores[3]['Classe']

result = {}

for fornecedor in fornecedores:
    fornecedor_classe = fornecedor['Classe']
    fornecedor_email = fornecedor['Email']
    similarities = []
    for oc in ocs:
        oc = oc[0]
        items = oc['ITENS']
        for item in items:
            rate = process_text(str_cmp=fornecedor_classe.upper(), str_exact=item['DESCRICAO_CLASSE'].upper())
            comp = Comparison(item['DESCRICAO_CLASSE'], fornecedor_classe, fornecedor_email, rate, oc)
            # if min_rate >= rate:
            similarities.append(comp)

    similarities.sort(key=lambda x: x.rate, reverse=False)

    for similarity in similarities:
        if similarity.rate >= min_rate:
            ocs_code = set()
            ocs_code.add(similarity.oc['OC'])
            if similarity.fornecedor_email not in result:
                result[similarity.fornecedor_email] = ocs_code
            else:
                result[similarity.fornecedor_email].add(similarity.oc['OC'])
print(json.dumps(result, cls=SetEncoder))
