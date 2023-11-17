def removesw(text: str,stopwords:list)->list:
    for i in range(len(stopwords)):
        stopwords[i]= stopwords[i].upper()
    words= text.upper().split()
    for word in list(words):
        if word in stopwords:
            words.remove(word)
    return words

stopwords = ["The", "a", "some", "in", "of", "is", "there"]
text= "There is a good opportunity in some of the companies"
print(removesw(text, stopwords))


