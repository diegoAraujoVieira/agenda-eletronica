#Atividade Ativa agenda telefônica
#Aluno: Diego Araujo Vieira
#Curso: Análise e desenvolvimento de sistemas

#mensagem de boas vindas
print('---------- Olá! Seja bem vindo(a) a agenda telefônica.----------')

#Função para salvar os dados em um dicionário
def cadastrar(lista):
    print('-------------------------- Cadastro de Contatos -----------------------------------------------')
    lmt = int(input('Digite o número de contatos que você deseja cadastrar:')) #O usuário pode escolher quantos contatos deseja cadastrar de uma só vez.
    while lmt > 0:
        contato = {'Nome': input('Digite o nome:'),
                        'Telefone': input('Digite o telefone:'),
                        'E-mail': input('Digite o e-mail:'),
                        'Twitter': input('Digite o usuário do Twitter:'),
                        'Instagram': input('Digite o usuário do Instagram:')
                     }
        lista.append(contato)

        print(contato) #Este comando exibe os contatos salvos no dicionário separados por vírgula, na ordem solicitada.

        print('Contato cadastrado com sucesso!')
        print('-------------------------------------------------------------')
        lmt -=1
    else:
        print('Todos os contatos foram cadastrados. Retornando ao menu...') #Depois de todos os contatos serem adicionados, o programa retorna ao Menu.

#Função para fazer a busca de contatos:
def buscar(lista):
    print('------------------- Buscando contanto... ---------------------')
    if len(lista) > 0:
        Nome = input('Digite o nome do contato:')
        for contato in lista:
                if contato['Nome'] == Nome:
                    print('Nome: {}'.format(contato['Nome']))
                    print('Telefone: {}'.format(contato['Telefone']))
                    print('E-mail: {}'.format(contato['E-mail']))
                    print('Twitter: {}'.format(contato['Twitter']))
                    print('Instagram: {}'.format(contato['Instagram']))
                    print('-------------------------------------------------------------')

    #Caso não seja encontrado o contato pesquisado(ou ainda não tenha sido cadastrado), o programa exibe a seguinte mensagem:
    else:
        print('Contato não encontrado ou inexistente.')
        print('----------------------------------------------------------------------')

#Função para editar os dado de um contato
def editar(lista):
        print('------------------------------- Editar Contato -------------------------------------')
        if len(lista) > 0:
                Nome = input('Digite o nome do contato que você deseja editar:')
                if Nome:
                    for contato in (lista):
                        if contato['Nome'] == Nome:
                            print('-------------------------------------------------------------')
                            print('Se algum dado permanecer o mesmo, apenas digite-o novamente.')
                            contato['Nome'] = input('Digite o novo nome do contato:')
                            contato['Telefone'] = input('Digite o novo telefone:')
                            contato['E-mail'] = input('Digite o novo E-mail:')
                            contato['Twitter'] = input('Digite o novo Twitter:')
                            contato['Instagram'] = input('Digite o novo Instagram:')

                            print('Alterações concluídas! Retornando ao Menu Principal...')
                            print('--------------------------------------------------------------')
                            break

#Função que exibe o relatório de contatos:
def relatorio(lista):
    print('--------------------------- Relatório de Contatos. ------------------------------------')
    if len(lista) > 0:
        for contato in (lista):
            print('Nome: {}'.format(contato['Nome']))
            print('Telefone: {}'.format(contato['Telefone']))
            print('E-mail: {}'.format(contato['E-mail']))
            print('Twitter: {}'.format(contato['Twitter']))
            print('Instagram: {}'.format(contato['Instagram']))
            print('-------------------------------------------------------------------------------')

    #Caso não sejam encontrados contatos a seguinte mensagem é exibida:
    else:
        print('Contatos não encontrados ou inexistentes.')

#Função para excluir um contato
def excluir(lista):
    if len(lista) > 0:
        print('------------------------------ Excluir Contato ---------------------------------------------')
        Nome = input('Digite o nome do contato a ser excluído:')
        if Nome:
            for i,  contato in enumerate(lista):
                if contato['Nome'] == Nome:
                    print('Nome: {}'.format(contato['Nome']))
                    print('Telefone: {}'.format(contato['Telefone']))
                    print('E-mail: {}'.format(contato['E-mail']))
                    print('Twitter: {}'.format(contato['Twitter']))
                    print('Instagram: {}'.format(contato['Instagram']))
                    print('---------------------------------------------------------')

                    #Neste bloco de código há uma interação, onde se pergunta ao usuário se realmente deseja deletar o contato.
                    dlt = int(input('Você realmente deseja excluir esse contato?\n Digite "1" para sim e "2" para não =>'))
                    if dlt == 1: #Se a resposta for positiva o contato é deletado.
                            del lista[i]
                            print('Contato excluído com sucesso! Retornando ao Menu principal...')
                            print('-------------------------------------------------------------')
                            break
                    else: #Se a resposta for negativa o programa retorna ao menu principal.
                            print('Ok. Retornando ao Menu Principal...')

#Função do menu de opções
def menu():
    lista = []
    while True:
        try:
            print('------------------- Menu Principal ----------------------')

            #Neste comando "print" há uma orientação ao usuário de como ele deve pesquisar pelos nomes dos contatos.
            print('Dica: nos campos de busca, digite o nome do contato exatamente como você o cadastrou\n'
                  'Exemplo: "Digite o nome do contato que você deseja editar: Diego Araujo Vieira"')
            print('-------------------------------------------------------------------------------------------')

            print('1 - Cadastrar novo contato\n''2 - Buscar contato\n''3 - Editar contato\n''4 - Excluir contato\n'
                  '5 - Relatório de contatos\n''6 - Sair da Agenda')

            #Nesta interação, o usuário deve escolher a opção desejada digitando o número correspondente.
            opção = int(input('Digite o número da opção desejada => '))

            if opção == 1:
                cadastrar(lista)
            elif opção == 2:
                buscar(lista)
            elif opção == 3:
                editar(lista)
            elif opção == 4:
                excluir(lista)
            elif opção == 5:
                relatorio(lista)
            elif opção == 6: #Caso o usuário escolha essa opção a agenda é encerrada.
                print('Saindo da Agenda. Até Logo!')
                break
            else:
                print('Opção inválida. Tente novamente.')

        #Este bloco de código evita que o programa apresente erro, no caso do usuário digitar uma letra ao invés de um número no menu de opções.
        except ValueError:
            print('-------------------------------------------------------------------------------------------------')
            print('Parece que você digitou uma letra. Para escolher uma opção basta digitar o número correspondente.')
            print('-------------------------------------------------------------------------------------------------')
menu()