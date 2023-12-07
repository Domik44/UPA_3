# Název týmu
- Tým xdrtil03
# Seznam řešitelů
- xdrtil03
- xhosad03
- xpopdo00
# URL + název e-shopu
- https://airsoftshop.cz
- Bohemia Air Soft
# Význam sloupců (jdoucí zleva doprava)
- URL produktu
- Název produktu
- Cena produktu
- Úsťová rychlost měřená v m/s
- Verze (typ) mechaboxu
- Materiál těla
- Barva
- Délka hlavně měřená v mm
- Materiál hop-up komory
# Poznámky
- Skript headerFile obsahuje importy knihoven, funkci, která získá rozparsovanou HTML strukturu a dále třídu "Product", která slouží pro uchovávání informací o produktu.
- Skript linkScraper obsahuje funkce pro získání min. 100 URL odkazů na produkty z kategorie AK-47/74 -> https://airsoftshop.cz/aeg-47-74. Nemá žádné vstupní argumenty. Výpis odkazů jde na STDOUT.
- Skript productScraper obsahuje funkce pro získání informací o jednotlivých produktech z poskytnutých URL. Má povinný argument pro výběr vstupu URL odkazů, FILE pro zpracování odkazů z souboru urls.txt, STDIN pro zpracování URL odkazů poskytnutých z STDIN. Dále lze zadat celé číslo jako volitelný argument, který omezý počet zpracovávaných URL odkazů.
- Výstup skriptu productScraper je v kódování UTF-8, proto při zobrazení souboru data.tsv je potřeba mít aktivní toto kódování.
