def encuentra_secuencia(seq,times)-> bool:
    
    ant= seq[0]
    nveces = 1
    siguiente_idx= 1
    while nveces < times and siguiente_idx < len (seq):
        if seq[siguiente_idx] == ant:
             nveces +=1
        else:
            nveces = 1
        ant = seq[siguiente_idx]
        siguiente_idx = siguiente_idx+1
    return (siguiente_idx - times, True) if nveces == times else (None, False)

print(encuentra_secuencia([0,5,5,5,6,9,8,10],4))
print(encuentra_secuencia([0,5,5,5,6,9,8,10],3))
