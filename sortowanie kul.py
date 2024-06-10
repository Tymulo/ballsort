#- wczytaj z pliku N lini z kolorami oddzielonymi przecinkami, wynikiem powinna być sekwencja ruchów, które pozwolą rozwiązać układ.
# start getting used to writing code in english.
# do not write very wide lines. Each line typically should have less than
# 80 chars (old standard) or 100 chars (never do more than 120)
def ilosc_kolumn(nazwa_pliku):
    # i don't think you need this function, see comment on line 14
    with open(nazwa_pliku, "r") as plik:
        ilosc_kolumn = len(plik.readlines())
    return ilosc_kolumn
# there should be at least one blank line between functions
def wczytaj_do1listy(nazwa_pliku):
    wszystkie_kule = []
    with open(nazwa_pliku, 'r') as plik:
        # you can read all balls already into convenient structure
        for linia in plik:
            kule_lini = linia.strip().split()
            for kula in kule_lini:
                wszystkie_kule.append(kula)
    return wszystkie_kule
def wczytywanie_kolumny(numer_kolumny):
    # see comment on line 14
    with open("kule.txt", "r") as plik:
        linia = plik.readlines()[numer_kolumny]
        kolumna = linia.strip().split()
    return kolumna
def lista_kolorow(lista_wszystkich):
    # once you have all balls read into correct structure, you can use set type
    # to identify unique colors
    lista_kolorow = []
    for i in lista_wszystkich:
        if i not in lista_kolorow:
            lista_kolorow.append(i)
    return lista_kolorow
def sprawdzanie_czy_kol_rozwiazana(kolumna):
    if len(lista_kolorow(kolumna)) == 1:
        print("kolumna ",i," rozwiazana") # you should avoid using non-ascii chars
                                          # at least for now.
        return True
    else:
        print("kolumna ",i,"nie rozwiazana")
        return False
def kolumna_pusta(kolumna):
    if len(kolumna) == 0:
        return True
    else:
        return False
def dlg_kol(kolumna1):
    # a little useless, don't you think?
    dlg = len(kolumna1)
    return dlg
def pkt_koloru(lista_wszystkich,lista_kolorow,m_dlg_kol):
    T=[]
    b = 0
    while b < len(lista_kolorow):
        ilosc_pkt = 0
        for i in lista_wszystkich:
            if lista_kolorow[b] == i:
                ilosc_pkt += lista_wszystkich.index(i)
        T.append(ilosc_pkt//m_dlg_kol)
        b+=1
    return T
def najm_pkt(T,lista_kolorow):
    i = T.index(min(T))
    kolor_kuli = lista_kolorow[i]
    return kolor_kuli
# def wypelnianie_pustej(kolumna,m_dlg,najm_kolor):
#     if kolumna_pusta(kolumna) == True:
#         for i in range(m_dlg):
#             kolumna = wczytywanie_kolumny(i)
#             if dlg_kol(kolumna)>0:
#                 if kolumna[0] ==najm_kolor:
#                     kolumna_pusta(kolumna).append(kolumna[0])
#                     kolumna.remove(kolumna[0])
if __name__ == "__main__":
    nazwa = "kule.txt" # this kind of constant should be at the begining of the file
    # are you sure this is how you want the input data to be stored?
    # the color names are long, there are 5 blue and 7 red balls. Not sure at this stage whether
    # you want to sort it horizontaly or vertically, but either way, this input data is wrong.
    ilosc_kolumn(nazwa) # you are not saving the result
    wszystkie_kule=(wczytaj_do1listy(nazwa)) # why saving to tuple? a list should be fine
                                             # though i'm not sure why do you need all balls in a list
                                             # each operator should have a ' ' around:
                                             # ' = ', ' + ', ' / ' and son on
    rodz =(lista_kolorow(wczytaj_do1listy(nazwa))) # there is a neat thing called 'set' which is a tuple without repetitions
    m_dlg = dlg_kol(wczytywanie_kolumny(1)) # why 1? what if there is no column no. 1?
    pkt=pkt_koloru(wczytaj_do1listy(nazwa),rodz,m_dlg ) # you have saved wszystkie_kule before, why calling the function again?
    najm_kolor = najm_pkt(pkt,rodz)
    for i in range(m_dlg):
        kolumna = wczytywanie_kolumny(i)
        print(sprawdzanie_czy_kol_rozwiazana(kolumna))
    print(najm_kolor)
    print(pkt)
    print(rodz)
