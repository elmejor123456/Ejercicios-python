#compra
precio=int(input("valor compra"))

balotaroja=(precio*10)  /100
balotaverde=(precio*15) /100
balotoazul=(precio*20) /100
balotaamarilla=(precio*50) /100
balotanegra=(precio*100) /100

aleatorio = random.choice(["roja","verde","azul","amarilla","negra"]).     