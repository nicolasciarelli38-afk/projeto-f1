# Arquivo: equipes.py

def buscar_equipe(nome):
    
    dados = {
        "red bull": {"motor": 10, "aero": 10, "tecnico": 10},
        "mercedes": {"motor": 8, "aero": 8, "tecnico": 9},
        "ferrari":  {"motor": 10, "aero": 9, "tecnico": 6},
        "haas":     {"motor": 5, "aero": 4, "tecnico": 5},
        "williams":  {"motor": 7, "aero": 6, "tecnico": 7},
        "audi":  {"motor": 6, "aero": 6, "tecnico": 7}
    }
    
    # Para os q quiserem quebrar o jogo
    return dados.get(nome, {"motor": 5, "aero": 5, "tecnico": 5})
