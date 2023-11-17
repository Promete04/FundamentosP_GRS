"""
def remplace_hasgtags(text,remplace_str):
    words= text.split()
    new_words= []
    for word in words:
        if word.startswith("#"):
            new_words.append(remplace_str)
        else:
            new_words.append(word)
    new_text= " ".join(new_words)
    return new_text

text = "hola #mundo"
remplace_str = "[HASHTAG]"
new_text = remplace_hasgtags(text,remplace_str)
print(new_text)
"""



