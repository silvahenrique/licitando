import json
import requests
import codecs


def save_json_file(data, file_name, file_ext):
    with open('{}.{}'.format(file_name, file_ext), 'wb') as f:
        json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)


select_ocs = set()
with open('ocs.json', encoding='utf-8') as f:
    ocs = json.load(f)

for oc in ocs:
    if oc['PROCEDIMENTO'] == 'Pregão Eletrônico' and (oc['SITUACAO'] == 'EDITAL PUBLICADO' or oc['SITUACAO'] == 'AGUARDANDO RECEBIMENTO DE PROPOSTAS'):
        select_ocs.add(oc['OC'])

print(len(select_ocs))

# save_ocs = []
# for oc in select_ocs:
#     url = "https://www.bec.sp.gov.br/BEC_API/API/pregaoM/NegociacaoItemOC/0000/{}".format(oc)
#     headers = {}
#     response = requests.request("GET", url, headers=headers)
#     save_ocs.append(json.loads(response.text))
#     print(json.loads(response.text))
# save_json_file(save_ocs, 'ocs_full_data', 'json')
