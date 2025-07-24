def calcular_digito(cpf_parcial, multiplicadores):
    total = sum(int(dig) * mult for dig, mult in zip(cpf_parcial, multiplicadores))
    resto = total % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"

    primeiro_digito = calcular_digito(cpf[:9], range(10, 1, -1))
    segundo_digito = calcular_digito(cpf[:9] + primeiro_digito, range(11, 1, -1))
    
    return "Válido" if cpf[-2:] == primeiro_digito + segundo_digito else "Inválido"

cpf_input = input("Digite o CPF (XXX.XXX.XXX-XX): ")
print(validar_cpf(cpf_input))
