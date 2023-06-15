import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    object = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file),
        'linhas_do_arquivo': file,
    }

    for item in instance.queue:
        if item['nome_do_arquivo'] == object['nome_do_arquivo']:
            return False

    instance.enqueue(object)

    print(object, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos')
        return
    file = instance.dequeue()
    print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
