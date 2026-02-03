#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

kuukausi=int(input("anna kuukausi:"))
kevät=(3,4,5)
kesä=(6,7,8)
syksy=(9,10,11)
talvi=(12,1,2)
if kuukausi in (3,4,5):
    print("kevät")
elif kuukausi in (6,7,8):
    print("kesä")
elif kuukausi in (9,10,11):
    print("syksy")
elif kuukausi in (12,1,2):
    print("talvi")
else:
    print("tuntematon")



