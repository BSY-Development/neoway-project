import unicodedata
import re

# A função valida os números do CPF. 
# Fonte: https://www.vivaolinux.com.br/script/Validador-e-gerador-de-CPF-em-Python

def cpf_validate(numbers):
    cpf = [int(char) for char in numbers if char.isdigit()]

    # Valida se possui 11 digitos.
    if len(cpf) != 11:
        return False

    # Valida se o cpf não possui a repetição dos mesmos números
    if cpf == cpf[::-1]:
        return False

    # Retorna True se o cpf for válido ou False caso seja inválido.
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

# Função para formatar o CPF
def format_cpf(cpf):
    # Remove os . (pontos) e - (hífens).
    formatted = re.sub('[.-]', '', cpf)
    is_valid = cpf_validate(formatted)
    # Verifica se é um cpf válido, e retorna ele ou False.
    if is_valid:
        return { "formatted": formatted, "is_valid": True }
    else:
        return { "formatted": formatted, "is_valid": False }


def format_name(name):
    # Caso não seja necessário remover nenhum titulo, apenas comente as proximas 4 linhas.
    regex = r'(\w{2,}\.( ){1,})|(, \w+)|Miss|I |II|III|IV|V |MD|DDS|PhD|DVM|PHD'
    cleaned_name = re.sub(regex, r'', name).rstrip().lstrip() ## Remove alguns titulos
    no_accent = ''.join(c for c in unicodedata.normalize('NFD', cleaned_name)
        if unicodedata.category(c) != 'Mn') ## Remove Titulos restantes
    return no_accent.upper() ## Retorna o nome em upper case.
