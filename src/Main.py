import helpScript

import criaPasta
import criaArquivo
import excluiArquivo
import excluiPasta




versionScript = str("v.0.1.0")



escolha = input(str("\nDigite um comando para ser executado. Caso não conheça os comandos, digite --help para listar as funcionalidades: \n"))

def escolherOpcao(escolha):

    if(escolha == "--help"):
        helpScript.helpComands()
        escolha = input(str("\nEscolha um comando para ser executado ou digite qualquer letra para encerrar o programa\n"))
        escolherOpcao(escolha)
        print("======================================================\n")
        escolha = ""
        escolherOpcao(escolha)


    else:
    
        match escolha:

            case "--version":
                return print("\nVersão do código: {}\n".format(versionScript))

            case "--createFolder":
                return criaPasta.gerarPasta()

            case "--createFile":
                return criaArquivo.gerarArquivo()

            case "--deleteFile":
                return excluiArquivo.excluirArquivo()

            case "--deleteFolder":
                return excluiPasta.excluirPasta()

escolherOpcao(escolha)




    