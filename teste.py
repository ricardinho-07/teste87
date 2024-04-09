class aluno:
    def __init__(self, matricula, nome, sexo, idade):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        
if __name__=="__main__":
 aluno1 = ("123456", "maria", "f", "17")
 print(aluno1.matricula)
 print(aluno1.idade)
 print(aluno1.nome)
 print(aluno1.sexo)