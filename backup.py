import subprocess
import re

def backup(path):
    comand = ["kopia", "snapshot", "create", path] # Comando para fazer o backup
    subprocess.run(comand) # Executa o comando no terminal

def arguments(): # Pega os argumentos passados no arquivo config.yaml
    with open("./config.yaml", 'r', encoding='utf-8') as file:
        text = file.read() # Pega o conteúdo do arquivo
    regex = r'path:\s*"(.*)"' # Regex para pegar o caminho da pasta
    result = re.search(regex, text) # Procura o caminho da pasta no arquivo
    return result.group(1) # Retorna o caminho da pasta

def main():
    try:
        path = arguments() # Caminho da pasta para fazer o backup
        backup(path)
    except Exception as e:
        print("Erro:", e)

# python backup.py
if __name__ == '__main__':
    main()