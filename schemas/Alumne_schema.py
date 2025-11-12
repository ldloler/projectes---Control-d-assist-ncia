from models.Alumne import Alumne
def alumn_schema(alumn) -> Alumne:
    response = alumn
    return response
def alumns_schema(alumns)-> list[dict]:
    response = [alumn_schema(alumn) for alumn in alumns]
    return response