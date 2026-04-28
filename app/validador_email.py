def validar_email(email: str) -> bool:
    if "@" not in email:
        return False

    usuario, dominio = email.split("@", 1)

    if not usuario:
        return False

    if "." not in dominio:
        return False

    return True
