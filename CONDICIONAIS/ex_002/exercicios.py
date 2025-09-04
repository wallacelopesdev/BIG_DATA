timeDoCoraçao = input("Digite o nome do seu time do coração: ")
time = "galo" or "Galo"     

while True:
    if timeDoCoraçao == time:
        print("Vai galo!")
        break
    else:
        print("Ahh, que pena! Você não é galo!")
        break
        
organizadao = "galo\n cruzeiro\n america\n flamengo\n palmeiras\n corinthians\n santos\n vasco\n botafogo\b fluminense\n"

organizadao = input("Digite o nome de uma organização esportiva que você conhece: ")

if organizadao == "atletico":
    print("É o melhor time do mundo!")
elif organizadao == "cruzeiro":
    print("Time rival, mas é um time forte!")
elif organizadao == "america":
    print("Time tradicional de Minas Gerais!")
elif organizadao == "flamengo":
    print("Time com uma grande torcida!")
elif organizadao == "palmeiras":
    print("Time com uma grande torcida!")
elif organizadao == "corinthians":
    print("Time com uma grande torcida!")
elif organizadao == "santos":
    print("Time com uma grande torcida!")
elif organizadao == "vasco":
    print("Time com uma grande torcida!")
elif organizadao == "botafogo":
    print("Time com uma grande torcida!")
elif organizadao == "fluminense":
    print("Time com uma grande torcida!")
else:
    print("Não conheço essa organização.")

    for i in range(1,3, 6):
        print(i)
