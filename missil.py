def radar(m):
    return True if m == True else False

missil = True
leitura = radar(missil)

if leitura == True:
    print("Alerta missil a caminho")
else:
    print("Nenhum missil detectado")
