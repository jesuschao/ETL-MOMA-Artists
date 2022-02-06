def arrange_table(x):
    elementos= []
    for fila in x:
        i =[]
        for e in fila:
            i.append(e.text)
        elementos.append(i)
    return elementos