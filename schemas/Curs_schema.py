def curs_schema(curs) -> dict:
    response = {"curs" : curs}
    return response
def cursos_schema(cursos)-> list[dict]:
    response = [curs_schema(curs) for curs in cursos]
    return response