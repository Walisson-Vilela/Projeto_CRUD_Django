from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'joao', 'idade': 20},
        {'nome': 'pedro', 'idade': 27},

    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome': ' Nao encontrado', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    print(result)
    return HttpResponse('A pessoa foi encontrada, ela tem ' + str(result['idade']) + ' anos.')


def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})
