import subprocess
import re

def drive(path): # Sincroniza o backup local com o Google Drive
    comand = ["./rclone", "sync", "-v", path, "gdrive:/Backup"] # Comando para sincronizar o backup
    subprocess.run(comand) # Executa o comando no terminal

def backup(path): # Faz o backup local
    comand = ["./kopia", "snapshot", "create", path] # Comando para fazer o backup
    subprocess.run(comand) # Executa o comando no terminal

def arguments(): # Pega os argumentos passados no arquivo config.yaml
    arguments = []
    with open("./config.yaml", 'r', encoding='utf-8') as file:
        text = file.read() # Pega o conteúdo do arquivo

    regex = r'path:\s*"(.*)"' # Regex para pegar o caminho da pasta
    result = re.search(regex, text) # Procura o caminho da pasta no arquivo
    arguments.append(result.group(1))

    regex = r'repository:\s*"(.*)"' # Regex para pegar o caminho do repositorio
    result = re.search(regex, text) # Procura o caminho do repositorio no arquivo
    arguments.append(result.group(1))

    return arguments

def main():
    try:
        args = arguments()
        backup(args[0])
        drive(args[1])
    except Exception as e:
        print("Erro:", e)

# python backup.py
if __name__ == '__main__':
    main()