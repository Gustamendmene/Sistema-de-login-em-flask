
USUARIOS ={
    "aluno":{
        "senha":"123",
        "nome":"Daniel",
        "idade":16,
        "turma":"3 TDS B",
        "notas":[
            {"disciplina":"Desenvolvimento Web", "nota":9},      
            {"disciplina":"Banco de Dados", "nota":7},
            {"disciplina":"Programação Orientada a Objetos", "nota":7}
        ]
    },
    "maria":{
        "senha":"456",
        "nome":"Maria",
        "idade":17,
        "turma":"3 TDS A",
        "notas":[
            {"disciplina":"Desenvolvimento Web", "nota":9},      
            {"disciplina":"Banco de Dados", "nota":8}, 
            {"disciplina":"Programação Orientada a Objetos", "nota":7}
        ]
    }
}
def get_data():
    return USUARIOS