#- wczytaj z pliku N lini z kolorami oddzielonymi przecinkami, wynikiem powinna być sekwencja ruchów, które pozwolą rozwiązać układ.
def ilosc_kolumn(nazwa_pliku):
    with open(nazwa_pliku, "r") as plik:
        ilosc_kolumn = len(plik.readlines())
    return ilosc_kolumn
def wczytaj_do1listy(nazwa_pliku):
    wszystkie_kule = []
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            kule_lini = linia.strip().split()
            for kula in kule_lini:
                wszystkie_kule.append(kula)
    return wszystkie_kule
def wczytywanie_kolumny(numer_kolumny):
    with open("kule.txt", "r") as plik:
        linia = plik.readlines()[numer_kolumny]
        kolumna = linia.strip().split()
    return kolumna
def lista_kolorow(lista_wszystkich):
    lista_kolorow = []
    for i in lista_wszystkich:
        if i not in lista_kolorow:
            lista_kolorow.append(i)
    return lista_kolorow
def sprawdzanie_czy_kol_rozwiazana(kolumna):
    if len(lista_kolorow(kolumna)) == 1:
        print("kolumna ",i," rozwiązana")
        return True
    else:
        print("kolumna ",i,"nie rozwiązana")
        return False
def kolumna_pusta(kolumna):
    if len(kolumna) == 0:
        return True
    else:
        return False
def dlg_kol(kolumna1):
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
    nazwa = "kule.txt"
    ilosc_kolumn(nazwa)
    wszystkie_kule=(wczytaj_do1listy(nazwa))
    rodz =(lista_kolorow(wczytaj_do1listy(nazwa)))
    m_dlg = dlg_kol(wczytywanie_kolumny(1))
    pkt=pkt_koloru(wczytaj_do1listy(nazwa),rodz,m_dlg )
    najm_kolor = najm_pkt(pkt,rodz)
    for i in range(m_dlg):
        kolumna = wczytywanie_kolumny(i)
        print(sprawdzanie_czy_kol_rozwiazana(kolumna))
    print(najm_kolor)
    print(pkt)
    print(rodz)
