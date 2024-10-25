def oblicz_punkty

def graj(
    while True:
        try:
            ilosc_kostek = int(print("Ie kostek chcesz rzucić (3-19):"))
            if 3<=ilosc_kostek <= 10:
                break
                ekse:
                print("Podaj liczbę w przedziale od 3 do 10.")
                except ValueError:
                    print("Podano nieprawidłową wartość.Spróbuj ponownie.")


                    wyniki_rzutow = rzuc_kostkami(ilosc_kostek)
                    punkty = oblicz_punkty(wyniki_rzutow)
                    wyswietl_wyniki = (wyniki_rzutow, punkty)

                    zagraj_ponownie = input("Jeszcze raz? (t/n): ").lower()
                    if zagraj_ponownie != 't';
                    print("Dziękujemy za grę!")
                    break

#Uruchamiamy grę przez wywołanie funkcji graj
graj()
)