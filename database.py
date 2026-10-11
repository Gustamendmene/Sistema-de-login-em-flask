
USUARIOS ={
    "aluno":{
        "senha":"123",
        "nome":"João Silva",
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
        "turma":"3° ano TDS ",
        "notas":[
            {"disciplina":"Desenvolvimento Web II", "nota":10.0},      
            {"disciplina":"Banco de Dados", "nota":8.0}, 
            {"disciplina":"Estrutura de dados", "nota":9.2} 
        ]
    }
}
def get_data():
    return USUARIOS