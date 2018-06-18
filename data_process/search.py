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


def search(query):
    with open('/Users/henrique/Desktop/hack-in-sampa-2/extraction/data_extraction/ocs_full_data.json',
              encoding='utf-8') as f:
        ocs = json.load(f)

    fornecedores = [{
        "CNPJ": "00000000000",
        "Razao_Social": "None",
        "Cidade": "Osasco",
        "UF": "SP",
        "Email": "queryguy@the00mock.com",
        "Classe": query,
        "Produto": query
    }]
    result = {}
    response = {}

    for fornecedor in fornecedores:
        fornecedor_classe = fornecedor['Classe']
        fornecedor_produto = fornecedor['Produto']
        fornecedor_email = fornecedor['Email']
        similarities = []
        for oc in ocs:
            oc = oc[0]
            items = oc['ITENS']
            for item in items:
                rate_classe = process_text(str_cmp=fornecedor_classe.upper(),
                                           str_exact=item['DESCRICAO_CLASSE'].upper())
                # rate_item = process_text(str_cmp=fornecedor_classe.upper(), str_exact=item['DESCRICAO_ITEM'].upper())

                rate_item = 0
                if fornecedor_produto.upper() in item['DESCRICAO_ITEM'].upper():
                    rate_item = 100

                comparison_classe = Comparison(item['DESCRICAO_CLASSE'], fornecedor_classe, fornecedor_email,
                                               rate_classe, oc)
                comparison_item = Comparison(item['DESCRICAO_ITEM'], fornecedor_produto, fornecedor_email, rate_item,
                                             oc)
                similarities.append(comparison_classe)
                similarities.append(comparison_item)

        similarities.sort(key=lambda x: x.rate, reverse=False)

        for similarity in similarities:
            if similarity.rate >= min_rate:
                ocs_code = set()
                ocs_code.add(similarity.oc['OC'])
                if similarity.fornecedor_email not in result:
                    result[similarity.fornecedor_email] = ocs_code
                else:
                    result[similarity.fornecedor_email].add(similarity.oc['OC'])

                for index in result:
                    if similarity.oc['OC'] in result[index]:
                        if index not in response:
                            response[index] = {
                                'oc': similarity.oc['OC'],
                                'uf': similarity.oc['UF'],
                                'municipio': similarity.oc['MUNICIPIO'],
                                'unidade_compradora': similarity.oc['UNIDADE_COMPRADORA'],
                                'modalidade': similarity.oc['MODALIDADE'],
                                'itens': similarity.oc['ITENS']
                            }
    return json.dumps(response, cls=SetEncoder)


if __name__ == '__main__':
    search('Arroz')
