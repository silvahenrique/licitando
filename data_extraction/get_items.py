# import requests
# import json
# import codecs
#
#
# def save_json_file(data, file_name, file_ext):
#     with open('{}.{}'.format(file_name, file_ext), 'wb') as f:
#         json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)
#
#
# # situacoes = set()
# url = "https://www.bec.sp.gov.br/BEC_API/API/pregaoM/NegociacaoItemOC"
# headers = {}
# response = requests.request("GET", url, headers=headers)
#
# extraction = json.loads(response.text)
# save_json_file(extraction, 'items', 'json')
#
# # situacao = 'EDITAL PUBLICADO'
#
# print('STARTED!')
#
# ocs_save = []
# for item in extraction:
#     url = "https://www.bec.sp.gov.br/BEC_API/API/pregaoM/NegociacaoItemOC/{}".format(item['Codigo'])
#     response = requests.request("GET", url, headers=headers)
#     ocs = json.loads(response.text)
#
#     for oc in ocs:
#         ocs_save.append(oc)
#         # situacoes.add(oc['SITUACAO'])
#         # if situacao == oc['SITUACAO']:
#         #     print(oc)
#         print(oc)
#
# save_json_file(ocs_save, 'ocs', 'json')
# print('DONE!')
