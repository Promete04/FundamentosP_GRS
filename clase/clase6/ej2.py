def remplazar_vocablos(text:str,palabras:list):
    for palabras in palabras:
        text = text.replace(palabras, "*"*len(palabras))
    return text

print(remplazar_vocablos("eres un pedazo de animal", ["animal"]))