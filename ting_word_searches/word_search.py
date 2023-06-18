from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    check_word = txt_importer(word)
    if not check_word:
        return []
    result = {
        'palavra': word,
        'arquivo': instance.queue[0]['nome_do_arquivo'],
        'ocorrencias': [],
    }
    for i, line in enumerate(instance.queue[0]['linhas_do_arquivo'],
                             start=1):
        if word in line.lower():
            result['ocorrencias'].append({'linha': i})
    if len(result['ocorrencias']) == 0:
        return []
    print(result)
    return [result]


def search_by_word(word, instance):
    check_word = txt_importer(word)
    if not check_word:
        return []
    result = {
        'palavra': word,
        'arquivo': instance.queue[0]['nome_do_arquivo'],
        'ocorrencias': [],
    }
    for i, line in enumerate(instance.queue[0]['linhas_do_arquivo'],
                             start=1):
        if word in line.lower():
            result['ocorrencias'].append({'linha': i, 'conteudo': line})
    if len(result['ocorrencias']) == 0:
        return []
    print(result)
    return [result]


project = Queue()
process("statics/nome_pedro.txt", project)
exists_word("pedro", project)
