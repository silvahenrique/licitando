import json
import codecs


def save_json_file(data, file_name, file_ext):
    with open('{}.{}'.format(file_name, file_ext), 'wb') as f:
        json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)