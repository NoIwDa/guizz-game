print("Witaj w mini quizie")

playing = input("Czy chcesz zagrac w moja gre? Wybierz t dla 'tak' albo n dla 'nie' \n").lower()

if playing =="n":
    print("Zdecydowales sie nie zagrac. Ok. Do zobaczenia")
    quit()
elif playing !="t":
    print("Nie wiem o co Ci chodzi. Podejrzewam że nie chcesz grac. Do zobaczenia")
    quit()
else:
    print("Zdecydowales sie grac. No to do dziela! Powodzenia")

score = 0

answer = input("Jak nazywa sie zmienna ktora przyjmyje wartosci 'True' albo 'False'?\n").capitalize()
if answer == "Boolean":
    print('Zgadza sie!')
    score += 1
else:
    print("Nie zgadza sie :(")

answer = input("Jak nazywa sie zmienna ktora przyjmuje wartosci ktore sa liczbami calkowitymi z nieograniczonego zakresu?\n Wartosci moga byc zarowno ujemnie jak i dodatnie. \n")
if answer == "int":
    print('Zgadza sie!')
    score += 1
else:
    print("Nie zgadza sie :(")

answer = input("Jak nazywa sie zmienna ktora przyjmyje wartosci liczbowe zmiennoprzecinkowe?\n")
if answer == "float":
    print('Zgadza sie!')
    score +=1
else:
    print("Nie zgadza sie :(")

answer = input("Jak nazywa sie zmienna ktora przyjmyje wartosci w postaci liczb zespolonych? (czesc rzeczywista i urojona.\n")
if answer == "complex":
    print('Zgadza sie!')
    score += 1
else:
    print("Nie zgadza sie :(")

answer = input("Jak nazywa sie zmienna przechowujaca sekwencje znakow ktore pozostaja niezmienne?\n")
if answer in ["tuple", "krotka"]:
    print('Zgadza sie!')
    score += 1
else:
    print("Nie zgadza sie :(")

print(f"Twoj wynik to {score}/5. Gratulacje :D")
print("Procentowa poprawnosc wynosi " + str(score/5 *100) + "%.")





