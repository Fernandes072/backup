import argparse
import subprocess

def backup(path):
    comand = ["kopia", "snapshot", "create", path] # Comando para fazer o backup
    subprocess.run(comand) # Executa o comando no terminal

def arguments(): # Pega os argumentos passados pelo terminal
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", required=True)
    return parser.parse_args()

def main():
    try:
        args = arguments()
        path = args.path # Caminho da pasta para fazer o backup
        backup(path)
    except Exception as e:
        print("Erro:", e)

# python backup.py -p "caminho/da/pasta"
if __name__ == '__main__':
    main()