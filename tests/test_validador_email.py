from app.validador_email import validar_email


def test_email_valido():
    assert validar_email("usuario@gmail.com") == True


def test_email_sin_arroba():
    assert validar_email("usuariogmail.com") == False


def test_email_sin_usuario():
    assert validar_email("@gmail.com") == False
