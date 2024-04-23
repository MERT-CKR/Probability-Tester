import random

while True:
    print("Tahmin etmeye çalıştığınız olasılık yüzdesi nedir? Örn: 50\n")#sample: 50
    targetProbability = int(input(">> "))
    print("\n")

    print("kaç kez denemek istersin ? \nDenk gelene kadar denemek için 0: ")
    limit = int(input(">> "))
    print("\n")


    unlimited = 0
    if limit == 0:
        unlimited = 1
        limit = 1
    counter = 0

    while limit > 0:
        if unlimited != 1:
            limit -= 1
        input("Denemek için Enter'e basın")
        randomNumber = random.randint(1,100)
        counter += 1
        if randomNumber <= targetProbability:
            print(f"{counter}. deneme Başarılı :D")
            break
        else:
            print(f"{counter}. deneme Başarısız \n")
    
