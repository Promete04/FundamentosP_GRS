DOLLAR_TO_EUR= 0.2
def to_eur (text: str):
    dollar_pos = text. find ("$")
    text_lenght = len(text)
    while dollar_pos != -1:
        aux = dollar_pos -1
        while text[aux] != " ":
            aux -= 1
        amount = text[aux+1: dollar_pos]
    if amount. isnumeric():
        amount = float (amount)
        amount = f"{amount * DOLLAR_TO_EUR: •2f}"
        text = text[:aux+1] + amount + "€" + text[dollar_pos+1:]
        # Comprobar que tras hacer la conversión no se ha alargado la cadena:
    diff = len(text) - text_lenght
    dollar_pos = text.find("$", dollar_pos + 1 + diff)
    text_lenght = len(text)
    return text