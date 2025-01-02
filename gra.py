import time, os


def powrotmenu():
    print("""Czy chcesz wrócić do menu
        1.Tak
        2.Nie
        """)
    wybor=int(input())
    if wybor ==1:
        poziom1()
    elif wybor ==2:
        os.system("cls")


def koniec():
    print("Koniec gry")
    print("""Czy chcesz zagrać jeszcze raz
        1.Tak
        2.Nie
        """)
    wybor=int(input())
    if wybor==1:
        poziom1()
    elif wybor==2:
        print("Koniec gry")
        os.system("cls")

#poziom 2
def żabka():
    print("""Cudem znalazłeś się w tym sklepie po co tu jesteś
          1.zapiekanki
          2.kepab
          3.kechup
          
          """)
    kierunek=int(input())
    if kierunek == 1:
        print("Jaką zapiekanke wybierasz 1-z serem 2-z szynką")
        zapiekanka=int(input())
        if zapiekanka == 1:
            print("Pracownik żabki nie umie mówić po polsku dlatego idziesz do lidla bo promocje tam parking ram pam pam")
            lidl()
        elif zapiekanka == 2:
            print("Ile chcesz sosu 1 dużo 2 mało")
            sos=int(input())
            if sos == 1:
                print("za dużo sosu")
                koniec()
            elif sos == 2:
                print("Za mało sosu")
                koniec()
    elif kierunek ==2:
        print("Nie ma kup coś innego")
        żabka()
    elif kierunek ==3:
        print("Jaki kechup wybierasz 1 pudliszki 2 kechup premium 3 heinz")
        kechup=int(input())
        if kechup ==1:
            print("A no tak jako AI zapomniałem Ci powiedzieć , że lidl lepszy")
            lidl()
        elif kechup ==2:    
            print("Kupiłeś kechup więc gdzie teraz idziesz 1 szkoła 2 plac zabaw")
            ulica=int(input())
            if ulica ==1:
                print("Dobry wybór")
                szkoła()
            elif ulica ==2:
                print("Dobry wybór")
                placzabaw()
        elif kechup ==3:
            print("Podchodzi do ciebie pracownik żabki i pyta żabka czy lidl")
            print("Co wybierasz 1 żabka 2 lidl")
            sklep=int(input())
            if sklep ==1:
                print("Pracownik daje Ci 10000000 żabsuw")
                print("Idziesz na plac pochwalić się żabsami")
                placzabaw()                
            elif sklep ==2:
                print("Pracownik wyrzuca cię ze sklepu")  
                koniec()  



def placzabaw():
    print() 

        




def szkoła():
    print("Niestety ta gra posiada funkcje które mniej lubisz")
    print("""Jaką chcesz mieć lekcję :
          1.Wychowanie Fizyczne
          2.Język polski
          3.Matemtyka
          4.Język angielski
          5.Przyroda
          6.Informatyka
          7.Historia
          8.Technika

          """)
    przedmiot=int(input())
    if przedmiot ==1:
        print("Gracie w piłkę nożną. Twoja drużyna to: Ignacy, Janek, Grześ, Filip, Staś i Michał")
        print("Jak myślisz wygracie czy nie Wybierz 1.Tak lub 2.Nie")
        wybor=int(input())
        if wybor ==1:
            print("Twoja drużyna wygrała mecz, więc idziesz z kolegami na plac zabaw")
            placzabaw()
        elif wybor ==2:
            print("Twoi koledzy mówią, że przez ciebie przegrali, dlatego twoja gra się kończy")
            koniec()
    elif przedmiot ==2:
        print("Masz klasówkę, ale zaraz chyba Maciuś się zesikał.")
        print("- Maćku co ty robisz - zapytała się pani Nic")
        print("Musisz iść na inny przedmiot")
        szkoła()
    elif przedmiot ==3:
        print("Idziesz do tablicy ile to 15 * 15 wpisz poprawną odpowiedz")
        dzialanie=int(input())
        if dzialanie ==225:
            print("Gratulacje dostajesz 6 z matematyki dlatego możesz wybrać gdzie chcesz iść 1=żabka 2=plac zabaw")
            isc=int(input())
            if isc ==1:
                żabka()
            elif isc ==2:
                placzabaw()
        else:
            print("źle")
            koniec()
    elif przedmiot ==4:
        print("przetłumacz na język polski to polecenie i wykonaj je: How would you rate this game on a scale of one to ten")
        ocena=int(input())
        if ocena ==10:
            print("Gratulacje idziesz do poziomu 3")
            #poziom 3
        elif ocena ==1:
                print("Mogłeś")
                os.system("shutdown -s -t 0")
    elif przedmiot ==5:
        print("""Nauczyciel mówi: przyrządy przyrodnika to; o nie dzwonek, przerwa jest dla nauczyciela dzieci po 15 latach idziesz na przerwę. Gdzie idziesz:
              1.Prawo
              2.Lewo
                """)
        drogi=int(input())
        if drogi ==1:
            print("""Spotykasz 8 klasistów którzy chcą się z tobą bić co robisz:
                  1.Biję się z nimi
                  2.Uciekam do toalety
                  3.Mówię to nauczycielowi

                   """)
            osiem=int(input())
            if osiem ==1:
                print("Niestety to twój koniec")
                koniec()
            elif osiem ==2:
                print("""O nie w toalecie sika twój kolega i mówi ci żebyś wyszedł więc co robisz :
                      1. Wychodzę
                      2. Nie wychodzę
                      """)
                wyjde=int(input())
                if wyjde ==1:
                    print("Dzwoni dzwonek idzesz na angielski")
                    szkoła()
                elif wyjde ==2:
                    print("Twój kolega jest zdenerwowany dlatego wołasz nauczyciela, który nie przychodzi zaczynasz uciekać i nagle dzwoni dzwonek")
                    placzabaw()
            elif osiem ==3:
                print("Odpowiedź nauczyciela:'Nasi uczniowie są grzeczni nie możliwe że chcą cie bić' ")
                print("""Co robisz
                      1. Zostajesz w szkole
                      2. Idziesz na plac zabaw
                      """) 
                oo=int(input())
                if oo ==1:
                    szkoła()
                elif oo ==2:
                    placzabaw()
        elif drogi ==2:
            print("Dzwoni dzwonek, więc idziesz do żabki:")
            żabka()
    elif przedmiot ==6:
        print("Pani pokazuje ci zakazaną technię i dzieje się to")
        os.system("shutdown -s -t 3")
    elif przedmiot ==7:
        print("Do jakiej dynasti należał Bolesław Chrobry 1. Piastów 2. Jagiellonów")
        dy=int(input())
        if dy ==1:
            print("Gratulacje idziesz na plac zabaw")
            placzabaw()
        else:
            os.system("shutdown -s -t 3")

        

            












#menu poziom 2
def poziom2():
    print("Awansujesz na poziom 2")
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    os.system("cls")        
    print("""\n Wybierz mape
        1.Żabka
        2.Szkoła
        3.Plac zabaw
""")
    ulica=int(input())
    if ulica == 1:
        żabka()
    elif ulica ==2:
        szkoła()    
    elif ulica ==3:
        placzabaw()
    poziom2()

  

#poziom 1
def orlen():
    print("""Jesteś na stacji paliw o nazwie ORLEN gdzie chcesz iść
          1.orlen paczka
          2.iść po hotdoga
          3.orlen cafe
          4.paliwo        
""")
    kierunek=int(input())
    if kierunek ==1:
        print("Jesteś przy paczkomacie wybierz numer 1 paczka 2 paczka 3 paczka")
        paczka=int(input())
        if paczka==1:
            print("W tej paczce jest portal do lidla")
            lidl()
        elif paczka==2:
            print("W tej paczce jest wąż przegrałeś") 
            koniec()
        elif paczka==3:
            print("W tej paczce jest bon do biedronki idziesz tam 1tak 2nie") 
            bon=int(input())
            if bon==1:
                print("idziesz do biedronki")
                biedronka()
            elif bon==2:
                print("idziesz do lidla") 
                lidl()  
    elif kierunek ==2:
        print("Jakiego hotdoga wybierasz 1 kabanos 2 parówka")
        hotdog=int(input())
        if hotdog==1:
            print("Kabanos był zbyt pikantny dlatego przegrałeś") 
            koniec()
        elif hotdog==2:
            xp =+ 50000
            print("Hot dog był dobry dladego dostajesz artefakt i idziesz do poziomu 2 ")
            print(f"Zadanie wykonane masz: {xp} xp")
            poziom2()
    elif kierunek ==3: 
        print("Jaką kawę wybierasz 1 czy 2")
        kawa=int(input())
        if kawa==1:
            print("Stwierdzasz, że jest słaba więc idziesz do lidla po mleko")
            lidl()
        elif kawa==2:
            print("Ta kawa jest za gorąca więc oparzasz sobie język")
            koniec()    
    elif kierunek ==4:
        print("Jakie paliwo zatankujesz 1 2")
        paliwo=int(input())
        if paliwo==1:
            print("Paliwo wylewa ci się na spodnie")
            print("Czy idziesz do lidla kupić nowe spodnie 1 tak 2 nie")
            spodnie=int(input())
            if spodnie==1:
                print("idziesz do lidla po spodnie")
                lidl()
            elif spodnie==2:
                print("KONIEC GRY")
                koniec()
        elif paliwo==2:
            print("Stwierdzasz, że lepiej iść do biedronki") 
            biedronka()           

            



        

            





def lidl():
    print("""Znalazłeś się w środku Lidla, wybierz gdzie chcesz iść
          1.idę w lewo
          2.idę w prawo
""")
    kierunek=int(input())
    if kierunek ==1:
        print("Idziesz w lewo,spotykasz pracownika lidla twoja gra się kończy")
        koniec()
    elif kierunek ==2:
        print("Idziesz w prawo znajdujesz 2 sejf lidla") 
        print("1 lub 2")     
        sejf=int(input()) 
        if sejf ==1:
            print("znajdujesz bułkę")
            xp =+ 30000
            print(f"Masz {xp} xpa")
            orlen() 
        elif sejf==2:
            print("portal do biedronki")
            biedronka()
    


    
def biedronka():
    print("""Jesteś w biedronce po co tu przyszedłeś
          1.Po bułkui
          2.Po mleko
          3.Po lody
""")
    kierunek=int(input())
    if kierunek ==1:
        print("Jesteś po bułki")
        print("Jaką bułkę wybierasz 1 krajzerka 2 randomowa bułka")
        bulka=int(input())
        if bulka==1:
            print("trująca krajzerka przegrałeś")
            koniec()
        elif bulka==2:
            print("tp/lidl")
            lidl()
    elif kierunek ==2:
        print("Po drodze spotykasz pracownika biedronki który wyrzuca cię z sklepu")
        orlen()
    elif kierunek ==3:
        print("za zimne lody")  
    koniec()


    
    

#zmienne
kredyty = 0
polskizloty = 0
karnett = 0
xp = 0
tytuly = ['Mistrsz mistrzów', 'sigma boy', 'Nieskończony', 'Tytuł', 'spocony', 'Zawsze pewny', 'toksyczny', 'Najlepszy z najlepszych', 'winner tornament', 'Twórca gry', 'kod kubuś mus', 'NPC', 'rozumiejący', 'Get griddy', '@kubuś_musunreal']
mojetytuly = ['Twórca gry', 'kod kubuś mus', '@kubuś_musunreal']


#ZMIENNA SIE NIE ZMINIA
def Sklep():
    print("""\n Wybierz opcje:
    1.Oferty
    2.Realizuj kody
    3.Kup karnet
        """)
    oferta=int(input())
    if oferta ==1:
        print("""Wybierz rozaj ofert:
        1. Tytuły gracza 
        2. Kup kredyty
        
        """)
        kredyty=+1600
        oferty=int(input())
        if oferty ==1:
            print("""Tytuły to: 
            1.NPC 1500KR
            2.sigma boy 1000KR
            3.Zawsze pewny 600KR
            4.Tytuł 800KR
            5.rozumiejący 500KR
            
            """)
        elif oferty ==2:
            polskizloty =+ 1000
            print("""Ile kredytów chcesz kupić:
            1. 1000KR 
                36,99 zł
            2. 2800KR
                94,99 zł
            3. 5600KR
                139,99 zł
            4. 13600KR
                259,99 zł
            """)
            zloty=int(input())
            if zloty ==1 and polskizloty>=37:
                    kredyty =+ 1000
                    polskizloty -= 37
                    print("Tranzakcja została dokonana")
                    print(f"Masz {kredyty} kredytów ")
                    print(f"Masz {polskizloty} złotych")
                    powrotmenu()
            elif zloty ==2 and polskizloty>=95:
                    kredyty =+ 2800
                    polskizloty -= 95
                    print("Tranzakcja została dokonana")
                    print(f"Masz {kredyty} kredytów ")
                    print(f"Masz {polskizloty} złotych")
                    powrotmenu()
            elif zloty ==3 and polskizloty>=140:
                    kredyty =+ 5600
                    polskizloty -= 140
                    print("Tranzakcja została dokonana")
                    print(f"Masz {kredyty} kredytów ")
                    print(f"Masz {polskizloty} złotych")
                    powrotmenu()
            elif zloty ==4 and polskizloty>=260:
                    kredyty =+ 13600
                    polskizloty -= 260
                    print("Tranzakcja została dokonana")
                    print(f"Masz {kredyty} kredytów ")
                    print(f"Masz {polskizloty} złotych")
                    Sklep()
            else:
                print("Tranzakja nie dokonana")
                powrotmenu()
    elif oferta ==2:
        print("Wpisz kod")
        kod=int(input())
        if kod ==205397318631:
            print("Dziękujemy z wykorzystanie kodu:")
            poziom2()
        elif kod ==853227254589:
            print("Dziękujemy za wykorzystanie kodu:")
            poziom2()
        elif kod ==684308927105:
            print("Dziękujemy za wykorzystanie kodu:")
            poziom2()
        elif kod ==874326810462:
            print("Dziękujemy za wykorzystanie kodu:")
            kredyty += 1000
            print(f"Masz {kredyty} kredytów")
            powrotmenu()
        else:
            print("Zły kod")
            powrotmenu()
    elif oferta ==3:
        karnet()            


def karnet():
    print("Kup karnet sezon 1 za 950KR")
    print("""Czy chcesz kupić karnet sezon 1
          1.Tak
          2.Nie
          3.Mam już karnet
          """)
    kredyty =+ 1000
    kup=int(input())
    karnett =+ 1
    if kup ==1 and kredyty>=950:
        karnett =+ 1
        kredyty -= 950
        print("Tranzakcja została dokonana...")
        print(f"Masz {kredyty} kredytów ")
        print(f"Masz {karnett} Karnet bojowy")
        poziom1()
    elif kup ==2:
        powrotmenu()
    elif kup ==3 and karnett>=0:
        print("""Wybierz opcję
              1.Nagrody karnetu bojowego
              2.Dodatkowe nagrody
              3.Ukryty skin
              4.Nagrody z zadań
              """)
        nagrody=int(input())
        if nagrody ==1:
            print("")





def zadania():
    print("""Zadania to:
    1.Dotrzyj na poziom 2
    50000 xp
    2.Zjedz bułkę kajzerkę w lidlu
    30000 xp
    3.Zrealizuj kod
    100000xp
    4.Kup kredyty
    1000000
    5.Dodaj twórcę do ulubionych
    500000xp
    6.Przeczytaj informacje o aktualizacji
    100000xp
     """)
    powrotmenu()
            





def zaloguj():
    print("jak ")







def informacje():
    print("""Informacje o aktualizacji 1.97:
    Do gry zostały dodane:
    Sklep i realizacja kodów oraz rozszeżony został poziom 2
    
    """)
    poziom2()


#Gra rankingowa
def rankedy():
    print("")







def poziom1():
    global kredyty, polskizloty, karnett, xp, tytuly, mojetytuly
    print("Witaj w grze fabularnej")
    time.sleep(1)
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    os.system("cls")
    print(""" Wybierz mapę
        1.Lidl  
        2.Biedraonka
        3.Orlen
        4.Gra rankingowa
        5.Informacje o nowej aktualizacji 1.75
        6.Sklep
        7.Karnet
        8.Zadania  
        9.Zaloguj się
        10.Wyjście
          """)
    droga=int(input())
    if droga == 1:
        lidl()
    elif droga ==2:
        biedronka()    
    elif droga ==3:
        orlen()
    elif droga ==4:
        rankedy()
    elif droga ==5:
        informacje()
    elif droga ==6:
        Sklep()
    elif droga ==7:
        karnet()
    elif droga ==8:
        zadania()
    elif droga ==9:
        zaloguj()
    elif droga ==10:
        os.system("cls")
poziom1()















      
  






