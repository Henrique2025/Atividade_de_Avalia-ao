from dataclasses import dataclass

from projeto.funcionario import Funcionario


@dataclass
class Engenheiro(Funcionario):
    crea: str

    def mostrar_dados_funcionario(self):
        return "Mostra os dados engenheiro"