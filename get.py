from bs4 import BeautifulSoup
import requests, lxml, time
from prettytable import PrettyTable

while True:
    url = "http://www.bbc.co.uk/news/election/2017/results"
    page = requests.get(url).text

    soup = BeautifulSoup(page, "lxml")
    parties = soup.find_all("thead", {"class": "ge2017-banner__head"})[0]
    results = soup.find_all("tbody", {"class": "ge2017-banner__body"})[0]

    partynames = [x.text for x in parties.find_all("span", {"class": "vh"})][1:]
    seatstable = results.find("tr", {"class": "ge2017-banner__row--seats"})
    seats = [x.text for x in seatstable.find_all("td", {"class": "ge2017-banner__value"})]

    t = PrettyTable(['Party', 'Seats'])
    for i in range(len(seats)):
        t.add_row([partynames[i], seats[i]])

    f = open('/var/www/html/2017','w+')
    print >>f, str(t)
    f.close()
    time.sleep(5)
