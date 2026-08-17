import json

def abrir_usuarios():
    with open("dados/usuarios.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_usuarios(dados):
    with open("dados/usuarios.json", "w", encoding="utf-8") as arquivo:
            return json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def abrir_solicitacoes():
    with open("dados/solicitacoes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

def salvar_solicitacoes(solicitacoes):
    with open("dados/solicitacoes.json", "w", encoding="utf-8") as arquivo:
            return json.dump(solicitacoes, arquivo, indent=4, ensure_ascii=False)


def ler_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Digite um valor válido.")

def fazer_login(dados_usuarios):
    id_digitado = input("Digite seu ID: ").strip()
    senha_digitada = input("Digite sua senha: ").strip()

    for usuario in dados_usuarios:
        if (dados_usuarios[usuario]["id"] == id_digitado
                and dados_usuarios[usuario]["senha"] == senha_digitada):

            print("\nLogin bem-sucedido!")
            return usuario

    print("\nID ou senha incorretos.")
    return None


def menu_gn(usuario_logado):
    print("""================================
     GERENTE DE NEGÓCIOS
================================
1 - Nova solicitação
2 - Minhas solicitações
3 - Solicitações para corrigir
4 - Sair""")
    opcao = input("escolha: ").strip()
    match opcao:
        case "1":
            criar_solicitacao(usuario_logado)
        case "2":
            minhas_solicitacoes(usuario_logado)
        case "3":
            pass #solicitacoes_para_corrigir()
        case "4":
            pass #sair()
        case _:
            print("Opção inválida.")

def menu_ga():
    print("""================================
     GERENTE DE AGENCIA
================================""")

def menu_cadastro():
    print("""================================
     TIME DE CADASTRO
================================""")




def criar_solicitacao(usuario_logado):
    print("""================================
       NOVA SOLICITAÇÃO
================================""")
    solicitacoes = abrir_solicitacoes()
    quantidade = len(solicitacoes)
    numero = quantidade + 1
    id_solicitacao = f"SOL{numero:03d}"

    cliente = input("Cliente: ").strip()
    print("""Tipo de atualização:

1 - Renda
2 - Patrimônio
3 - Endereço""")
    opcao = input("Escolha uma opção (1-3): ").strip()
    match opcao:

        case "1":
            tipo = "Renda"
            renda_atual =ler_valor("Renda Atual: ")
            nova_renda = ler_valor("Nova Renda: ")
            dados_antigos = renda_atual
            dados_novos = nova_renda


        case "2":
            tipo = "Patrimônio"
            patrimonio_atual = ler_valor("patrimonio Atual: ")
            novo_patrimonio = ler_valor("Nova patrimonio: ")

            dados_antigos = patrimonio_atual
            dados_novos = novo_patrimonio



        case "3":
            tipo = "Endereço"
            endereco_atual = input("Endereço Atual: ").strip()
            novo_endereco = input("Novo Endereço: ").strip()
            dados_antigos = endereco_atual
            dados_novos = novo_endereco

        case _:
            tipo = "None"

    documento = input("Documento comprobatório: ").strip()
    criado_por = usuario_logado
    status = "AGUARDANDO_GA"
    historico = [
    {
        "acao": "Solicitação criada",
        "usuario": usuario_logado
    }
    ]

    solicitacao = {
    "id": id_solicitacao,
    "cliente": cliente,
    "tipo": tipo,
    "dados_antigos":dados_antigos,
    "dados_novos":dados_novos,
    "documento":documento,
    "criado_por":criado_por,
    "status":status,
    "historico":historico
    }
    solicitacoes.append(solicitacao)
    salvar_solicitacoes(solicitacoes)

def minhas_solicitacoes(usuario_logado):
    solicitacoes = abrir_solicitacoes()
    contador = 1
    encontradas = 0
    for solicitacao in solicitacoes:
        if solicitacao["criado_por"] == usuario_logado:
            print()
            print("=" * 40)
            print(f"[{contador}] id: {solicitacao["id"]}")
            
            
            print(f"\ncliente: {solicitacao['cliente']}")
            print(f"tipo: {solicitacao['tipo']}")

            print(f"\ndados_antigos: {solicitacao['dados_antigos']}")
            print(f"dados_novos: {solicitacao['dados_novos']}")

            print(f"\ndocumento: {solicitacao['documento']}")
            print(f"criado_por: {solicitacao['criado_por']}")
            print(f"status: {solicitacao['status']}")

            for item in solicitacao['historico']:
                acao = item["acao"]
                usuario = item["usuario"]

                print(f"\nhistorico:- {usuario}: {acao}")
            contador += 1
            encontradas += 1

    if encontradas == 0:
        print("Nenhuma solicitação encontrada.")
        input()

def visualizar_solicitacao(usuario_logado):
    solicitacoes = abrir_solicitacoes()
    for solicitacao in solicitacoes:
        if solicitacao["criado_por"] == usuario_logado:
            pass


            
            
            
            


dados = abrir_usuarios()

usuario_logado = fazer_login(dados)

if usuario_logado:
    print(f"Usuário: {usuario_logado}")
    perfil = dados[usuario_logado]["perfil"]
    
    if perfil == "GN":
        menu_gn(usuario_logado)
    elif perfil == "GA":
        menu_ga()
    elif perfil == "CAD":
        menu_cadastro()
