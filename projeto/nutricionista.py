from dataclasses import dataclass

from projeto.funcionario import Funcionario


@dataclass
class Nutricionista(Funcionario):
    crn: str

    def mostrar_dados_funcionario(self):
        return "Mostra dados nutricionista"
    