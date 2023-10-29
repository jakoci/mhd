import re
import requests
from bs4 import BeautifulSoup

# URL webov� str�nky, kterou chcete scrapovat
url = "https://idos.idnes.cz/olomouc/spojeni/vysledky/?f=U%20Sv.Morice&fc=305003&t=Hlavni%20nadrazi&tc=305003"
url_decode = url.encode('utf-8').decode('latin-1')
# Ode�lete HTTP po�adavek a z�skejte obsah str�nky
response = requests.get(url)
# Zkontrolujte, zda byl po�adavek �sp�n� (k�d 200 znamen� �sp�ch)
if response.status_code == 200:
    # Analyzujte HTML obsah pomoc� BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Najd�te v�echny titulky �l�nk� (p�edpokl�d�me, �e jsou zabaleny v elementech <h2>)
    #article_titles = soup.find_all("ul", {"class": "reset stations first last"})
    article_titles = soup.find_all("div", {"class": "line-item"})
    print(article_titles)
    time_values = []  # Vytvo��me pr�zdn� seznam pro ukl�d�n� hodnot
    station_values = []
    tram_values = []
    for ul in article_titles:
        time_elements = ul.find_all("p", {"class": "reset time"})
        station_elements = ul.find_all("p", {"class": "station"})
        for time_element in time_elements:
            time_values.append(time_element.text)
        for station_element in station_elements:
            station_values.append(station_element.text)
    h3_tags = soup.find_all('h3')
    for h3_tag in h3_tags:
    # Najd�te tag <span> v r�mci tagu <h3>
        tram_elements = h3_tag.find_all('span')
        # Z�sk�n� textu z tagu <span>
        for tram_element in tram_elements:
            tram_numbers = re.findall(r'\d+', tram_element.text)
            tram_values.append(tram_numbers)            
    print(time_values)
    print(station_values)
    print(tram_values)

