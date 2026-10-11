
USUARIOS ={
    "aluno":{
        "senha":"123",
        "nome":"João Silva",
        "idade":16,
        "turma":"3° ano TDS ",
        "notas":[
            {"disciplina":"Desenvolvimento Web II", "nota":9.5},      
            {"disciplina":"Banco de Dados", "nota":8.0},
            {"disciplina":"Estrutura de dados", "nota":8.8}
        ]
    },
    "maria":{
        "senha":"abc",
        "nome":"Maria Oliveira",
        "idade":17,
        "turma":"3° ano TDS ",
        "notas":[
            {"disciplina":"Desenvolvimento Web II", "nota":9},      
            {"disciplina":"Banco de Dados", "nota":8}, 
            {"disciplina":"Estrutura de dados", "nota":7}
        ]
    }
}
def get_data():
    return USUARIOS