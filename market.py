import random
import math
from itertools import permutations
import copy
import time

# Generator danych
def GenerateWorkers(workers):
    # Podanie ilosci pracownikow
    print("Ilu pracownikow pracuje w sklepie: ")
    workersCount = int(input())
    for x in range(workersCount):
        workers.append([])
        # Numer pracownika
        workers[x].append(x+1)
        ## Ile maksymalnie godzin pracy dziennie
        workers[x].append(8)
        # Plec
        sex = ["Male", "Female"]
        workers[x].append(random.choice(sex))
        # Wiek
        if random.randrange(1,5) < 4:
            workers[x].append(random.randrange(18,51))
        else:
            workers[x].append(random.randrange(51,65))
        # Czy pali
        if random.randrange(1,7) < 6:
            workers[x].append("No")
        else:
            workers[x].append("Yes")
        # Co idzie mu najlepiej [Register - Kasa, Shop - Zajecia na sklepie]
        jobs = ["Register", "Shop"]
        workers[x].append(random.choice(jobs))
        # Pracowitosc [1-slabo 5-bardzo]
        workers[x].append(random.randrange(1,6))
        # Zaufana osoba
        #trustWorthy = ["Yes", "No"]
        #workers[x].append(random.choice(trustWorthy))
        # Dobra z matematyki [1-slabo 5-bardzo]
        workers[x].append(random.randrange(1,6))
        # Zdolnosc persfazji [1-slabo 5-bardzo]
        workers[x].append(random.randrange(1,6))
        # Zarabia na godzine
        workers[x].append(random.randrange(20,31))

    print("--- Pracownicy ---")
    for x in workers:
        print(x)
    return workersCount



# Okreslenie podstawowych zasad sklepu
def defineShopRules(shopRules):
    print("Ilu jednostek pracy potrzebnych na kasie: ")
    cashRegisterNormal = int(input())
    print("Ilu jednostek pracy potrzebnych na kasie w trakcie godziny szczytu: ")
    cashRegisterBusy = int(input())
    print("Ilu jednostek pracy potrzebnych na sklepie (rozkladanie towaru, noszenie): ")
    shopNormal = int(input())
    print("Ilu jednostek pracy potrzebnych na sklepie w trakcie godziny szczytu (rozkladanie towaru, noszenie): ")
    shopBusy = int(input())
    print("Godziny otwarcia w tygodniu (Podac w takiej formie: x y)")
    a, b = input().split()
    shopOpenHoursWeek = [int(a), int(b)]
    print("Godziny otwarcia w sobote (Podac w takiej formie: x y)")
    a, b = input().split()
    shopOpenHoursWeekend = [int(a), int(b)]

    # Wskazanie godzin szczytu w sklepie
    # W tygodniu
    busyHoursWeek = []
    print("Ile godzin w dniu to godziny szczytu: ")
    busyHoursCount = int(input())
    print("Godziny szczytu w tygodniu: ")
    for x in range(busyHoursCount):
        busyHoursWeek.append(int(input()))

    # W sobote
    busyHoursWeekend = []
    print("Ile godzin w sobote to godziny szczytu: ")
    busyHoursWeekendCount = int(input())
    print("Godziny szczytu w sobote: ")
    for x in range(busyHoursWeekendCount):
        busyHoursWeekend.append(int(input()))

    busyHoursWeek.sort()
    busyHoursWeekend.sort()

    shopRules.append(cashRegisterNormal)
    shopRules.append(cashRegisterBusy)
    shopRules.append(shopNormal)
    shopRules.append(shopBusy)
    shopRules.append(shopOpenHoursWeek)
    shopRules.append(shopOpenHoursWeekend)
    shopRules.append(busyHoursWeek)
    shopRules.append(busyHoursWeekend)

# Generator Podstawowych zasad sklepu
def GenerateShopRules(shopRules, workersCount):
    cashRegisterNormal = math.ceil(workersCount/5)
    cashRegisterBusy = math.ceil(workersCount/3)
    shopNormal = math.ceil(workersCount/5)
    shopBusy = math.ceil(workersCount/3)
    shopOpenHoursWeek = []
    shopOpenHoursWeek.append(random.randrange(6,11))
    shopOpenHoursWeek.append(random.randrange(20,24))
    shopOpenHoursWeekend = []
    shopOpenHoursWeekend.append(random.randrange(7,11))
    shopOpenHoursWeekend.append(random.randrange(15,21))
    busyHoursWeek = [shopOpenHoursWeek[0], 15, 16, 17]
    busyHoursWeekend = [shopOpenHoursWeekend[0], shopOpenHoursWeekend[1]-1, shopOpenHoursWeekend[1]]

    shopRules.append(cashRegisterNormal)
    shopRules.append(cashRegisterBusy)
    shopRules.append(shopNormal)
    shopRules.append(shopBusy)
    shopRules.append(shopOpenHoursWeek)
    shopRules.append(shopOpenHoursWeekend)
    shopRules.append(busyHoursWeek)
    shopRules.append(busyHoursWeekend)

# Generowanie Planu Pracy Sklepu 
def GenerateWorkPlan(shopRules, Shop):  
    # 0 - Closed   1 - Open   2 - Busy
    #Shop = []
    for x in range(7):
        Shop.append([])
        for y in range(24):
            Shop[x].append(0)
    for x in range(5):
        for y in range(shopRules[4][1] - shopRules[4][0]):
            Shop[x][shopRules[4][0] + y] = 1 
    for y in range(shopRules[5][1] - shopRules[5][0]):
            Shop[5][shopRules[5][0] + y] = 1 
    for x in range(5):
        for y in (shopRules[6]):
            Shop[x][y] = 2
    for y in (shopRules[7]):
            Shop[5][y] = 2

    # Drukowanie Wizualizacji Planu Sklepu
    print("--- Plan pracy sklepu ---")

    print("Monday:    ", Shop[0])
    print("Tuesday:   ", Shop[1])
    print("Wednesday: ", Shop[2])
    print("Thursday:  ", Shop[3])
    print("Friday:    ", Shop[4])
    print("Saturday:  ", Shop[5])
    print("Sunday:    ", Shop[6])

# Obliczanie wartosci pracownikow
def ValueChecker(workers, workersValues):
    registerValue = []
    shopValue = []
    for x in workers:
        registerValue.append(1)
        shopValue.append(1)
    for x in range(len(workers)):
        # Mezczyzni lepiej wydajni na sklepie, Kobiety na kasie
        if workers[x][2] == "Male":
            shopValue[x] += 0.05
        if workers[x][2] == "Female":
            registerValue[x] += 0.05
        # Zmniejszanie wydajnosci z wiekiem
        registerValue[x] -= (workers[x][3] - 18) / 1000
        shopValue[x] -= (workers[x][3] - 18) / 1000
        # Zmniejszanie wydajnosci zwiazana z paleniem
        if workers[x][4] == "Yes":
            registerValue[x] -= 0.05
            shopValue[x] -= 0.05
        # Wydajnosc lepsza przy ulubionym zajeciu
        if workers[x][5] == "Register":
            registerValue[x] += 0.1
        if workers[x][5] == "Shop":
            shopValue[x] += 0.1
        # Im wieksza pracowitosc tym lepsza wydajnosc
        registerValue[x] += (workers[x][6] * 0.05)
        shopValue[x] += (workers[x][6] * 0.05)
        # Im lepsza z matematyki tym lepsza wydajnosc na kasie
        registerValue[x] += (workers[x][7] * 0.03)
        # Im wieksza zdolnosc persfazji tym wieksza szansa na sprzedanie wiekszej ilosci 
        registerValue[x] += (workers[x][8] * 0.02)

        registerValue[x] = round(registerValue[x], 2)
        shopValue[x] = round(shopValue[x], 2)
    
    print("--- Wydajnosc Pracownikow ---")
    print("                RV   SV")
    for x in range(len(workers)):
        print("Pracownik", x ,": ", registerValue[x], shopValue[x])
    workersValues.append(registerValue)
    workersValues.append(shopValue)
    #print(workersValues)
    return



# Rozwiazanie problemu algorytmem Brute Force
def BruteForce(workers, shopRules, workersValues, Shop):
    
    
    
    # Mozliwosci ulozen pracownikow
    pos = []
    minL = []
    for x in range(len(workers)):
        minL.append(x)
        
    for x in range(1, len(workers) + 1):
        comb = permutations(minL, x)
        for i in comb:
            t = list(i)
            pos.append(t)
    #print(pos)
    
    
    
    results = []
    out = []
    out2 = []
    result = 0

    # W tygodniu
    #while(result == 0):
    ShopR = []
    ShopS = []

    for j in pos:
        i = 0
        #ShopS.append(Shop[0])
        #ShopS.append(Shop[5])
        #ShopR.append(Shop[0])
        #ShopR.append(Shop[5])
        ShopS = copy.deepcopy(Shop)
        ShopR = copy.deepcopy(Shop)
        #print(Shop)
        for x in range(24):
            if ShopR[0][x] == 2:
                ShopR[0][x] = shopRules[1]
            elif ShopR[0][x] == 1:
                ShopR[0][x] = shopRules[0]
        for x in range(24):
            if ShopS[0][x] == 2:
                ShopS[0][x] = shopRules[3]
            elif ShopS[0][x] == 1:
                ShopS[0][x] = shopRules[2]
        
        val = 0
        money = 0
        while(sum(ShopR[0]) != 0):
            if (i+1 > len(j)):
                break
            #print(j[i])
            #print(ShopR[0])
            val = workersValues[0][j[i]]
            
            hours = 8
            for y in range(24):
                if ShopR[0][y] > 0:
                    ShopR[0][y] -= val
                    #print(ShopR[0][y])
                    hours -= 1
                    money += workers[j[i]][9]
                if ShopR[0][y] < 0:
                    ShopR[0][y] = 0
                
                
                if(hours == 0):
                    break
            #print(money)
            i += 1
        
        if(sum(ShopR[0]) == 0) and (len(j) == i):
            out.append(j)
            out2.append(money)
        
    
    results.append(out)
    results.append(out2)

    minVal = min(out2)
    minValPlace = 0
    for i in [i for i,x in enumerate(out2) if x == minVal]:
        minValPlace = i
        break
    
    #print(len(results[0]), len(results[1]))
    print("Optymalna kolejnosc pracownikow: ", results[0][minValPlace])
    print("Koszt dzienny: ", results[1][minValPlace], "zl")
    print("Godziny pracy pracownikow: ")
    # Ustalenie godzin pracy pracownikow optymalnych
    ShopR = copy.deepcopy(Shop)
    workersHours = []


    for x in range(24):
        if ShopR[0][x] == 2:
            ShopR[0][x] = shopRules[1]
        elif ShopR[0][x] == 1:
            ShopR[0][x] = shopRules[0]

    i = 0
    while(sum(ShopR[0]) != 0):
            if (i+1 > len(results[0][minValPlace])):
                
                break
            #print(ShopR[0])
            hoursList = []
            val = workersValues[0][results[0][minValPlace][i]]
            ifBool = 0
            #print(val)
            #print(workersHours)
            hours = 8
            for y in range(24):
                
                if ShopR[0][y] > 0:
                    ShopR[0][y] -= val
                    #print(ShopR[0][y])
                    hoursList.append(y)
                    hours -= 1
                    #money += workers[j[i]][9]
                elif ShopR[0][y] < 0:
                    ShopR[0][y] = 0
                
                
                if(hours == 0):
                    workersHours.append(hoursList)
                    ifBool = 1
                    break
            if ifBool == 0:
                workersHours.append(hoursList)
            i += 1

    print(workersHours)
    
    return

# Rozwiazanie problemu algorytmem zachlannym
def Greedy(workers, shopRules, workersValues, Shop):
    # Ustalenie kolejnosci na podstawie wartosci pracownikow
    greedyValues = []
    greedyWorkersNumbers = []
    for i in range(len(workersValues[0])):
        val = 0
        val = workersValues[0][i] / workers[i][9]
        greedyValues.append(val)
        greedyWorkersNumbers.append(i)

    for i in range(len(greedyValues)):
        for j in range(len(greedyValues)-1):
            if greedyValues[j] < greedyValues[j+1]:
                greedyValues[j], greedyValues[j+1] = greedyValues[j+1], greedyValues[j]
                greedyWorkersNumbers[j], greedyWorkersNumbers[j+1] = greedyWorkersNumbers[j+1], greedyWorkersNumbers[j]

    ShopR = copy.deepcopy(Shop)
    workersHours = []
    money = 0

    for x in range(24):
        if ShopR[0][x] == 2:
            ShopR[0][x] = shopRules[1]
        elif ShopR[0][x] == 1:
            ShopR[0][x] = shopRules[0]

    i = 0
    while(sum(ShopR[0]) != 0):
            if (i+1 > len(greedyWorkersNumbers)):
                break

            ifBool = 0
            hoursList = []
            val = workersValues[0][greedyWorkersNumbers[i]]
            
            hours = 8
            for y in range(24):
                
                if ShopR[0][y] > 0:
                    ShopR[0][y] -= val
                    #print(ShopR[0][y])
                    hoursList.append(y)
                    hours -= 1
                    money += workers[greedyWorkersNumbers[i]][9]
                if ShopR[0][y] < 0:
                    ShopR[0][y] = 0
                
                
                if(hours == 0):
                    workersHours.append(hoursList)
                    ifBool = 1
                    break
            if ifBool == 0:
                workersHours.append(hoursList)
            i += 1
    while(i+1 <= len(greedyValues)):
        greedyWorkersNumbers.pop()
        i += 1
    print("Optymalna kolejnosc pracownikow: ", greedyWorkersNumbers)
    print("Koszt dzienny: ", money, "zl")
    print("Godziny pracy pracownikow: ")
    print(workersHours)


    return

# Main
workers = []
shopRules = []
workersValues = []
Shop = []
workersCount = 0

# Generowanie Pracownikow
workersCount = GenerateWorkers(workers)

# Generowanie Zasad Sklepu
#defineShopRules(shopRules)
GenerateShopRules(shopRules, workersCount)

# Zasady Sklepu
print("--- Zasady Sklepu ---")
print(shopRules)

# Generowanie Planu Sklepu
GenerateWorkPlan(shopRules, Shop)

ValueChecker(workers, workersValues)


pog = -1
while(pog != 0):
    print("")
    print("Wybierz zadanie:")
    print("1. Wybranie najlepszego rozwiazania algorytmem Bruteforce")
    print("2. Wybranie najlepszego rozwiazania algorytmem Greedy")
    print("0. Koniec pracy programu")
    pog = int(input())
    if pog == 1:
        print("")
        print("Bruteforce: ")
        start_time = time.time()
        BruteForce(workers, shopRules, workersValues, Shop)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Czas dzialania algorytmu BruteForce: {elapsed_time:.3f} sekund/y')

    elif pog == 2:
        print("")
        print("Greedy: ")
        start_time = time.time()
        Greedy(workers, shopRules, workersValues, Shop)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Czas dzialania algorytmu Greedy: {elapsed_time:.3f} sekund/y')
    
    elif pog == 0:
        break
