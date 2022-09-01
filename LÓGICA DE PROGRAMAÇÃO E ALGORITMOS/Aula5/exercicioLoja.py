def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x<=min) and (x>max)):
        x = int(input(pergunta))
    return x
        
def criaArquivo(file):
    try:
        a = open(file, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} criado com sucesso'.format(str(a.name)))
        
def arquivoExiste(file):
    try:
        a = open(file, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def cadastarJogo(file, nomeJogo, nomeConsole):
    try:
        a = open(file, 'at')
    except:
        print('Erro ao cadastar jogo')
    else:
        a.write('Jogo: {} | Console: {} \n'.format(nomeJogo, nomeConsole))
    finally:
        a.close()
        
def listarArquivo(file):
    try:
        a = open(file, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()
        
#programa Principal
arquivo = 'games.txt'

if arquivoExiste(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente, criando um novo...')
    criaArquivo(arquivo)

while True:
    print('----------MENU------------\n',
          '1 - Cadastrar novo jogo\n',
          '2 - Listar todos jogos\n',
          '3 - Sair\n')
    
    op = valida_int('Escolha a opção: ', 1, 3)
    
    
    if op == 1:
        nomeJogo = input('Digite o nome do jogo: ')
        nomeConsole = input('Digite o nome do console: ')
        cadastarJogo(arquivo, nomeJogo, nomeConsole)
        
    elif op == 2:
        print('Listando...')
        listarArquivo(arquivo)
    elif op == 3:
        print('Saindo...')
        break
    
    
    