import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('txt'):
            return sys.stderr.write("Formato inválido\n")
        with open(path_file, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return
