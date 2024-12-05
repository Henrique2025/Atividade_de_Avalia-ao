from projeto.engenheiro import Engenheiro

from projeto.nutricionista import Nutricionista


engenheiro = Engenheiro()
engenheiro.nome = input("Digite seu nome: "),
engenheiro.crea = input("Digite seu CREA: "),
engenheiro.endereco.logradrouro = input("Digite o Logradouro: "),
engenheiro.endereco.numero = input("Digite o número da residência: "),
engenheiro.salario = float(input("Informe seu salario"))

engenheiro.mostrar_dados_funcionario()

nutricionista = Nutricionista()
nutricionista.nome = input("Digite seu nome: "),
nutricionista.salario = float(input("Informe seu salario"))
nutricionista.crn = input("Digite seu CRM: "),
nutricionista.endereco.logradrouro = input("Digite o Logradouro: "),
nutricionista.endereco.numero = input("Digite o número da residência: "),

nutricionista.mostrar_dados_funcionario()