def alumn_schema(alumn) -> dict:
    response = {"alumne" : alumn}
    return response
def alumns_schema(alumns)-> list[dict]:
    response = [alumn_schema(alumn) for alumn in alumns]
    return response