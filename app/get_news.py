import requests
import json


def get_news(search_terms):
    data = []
    choice = input("How would you like to sort your news by popularity or time (p/t) ")
    for search_term in search_terms:
        if choice == "t":
            news = requests.get(
                #url="https://newsapi.org/v2/everything?language=en&q=" + search_term + "&scoring=n&sortBy=popularity&apiKey=5740068485274299a2a0e08302f3e1b7")
                url = "https://newsapi.org/v2/everything?language=en&q=" + search_term + "&domains=Venturebeat.com,techcrunch.com,businessinsider.com,slashdot.org,hackaday.com,makezine.com,theverge.com,engadget.com,lifehacker.com,wired.com&scoring=n&sortBy=publishedAt&apiKey=5740068485274299a2a0e08302f3e1b7")
        elif choice == "p":
            news = requests.get(
                url="https://newsapi.org/v2/everything?language=en&q=" + search_term + "&scoring=n&sortBy=popularity&apiKey=5740068485274299a2a0e08302f3e1b7")
                #url="https://newsapi.org/v2/everything?language=en&q=" + search_term + "&domains=Venturebeat.com,techcrunch.com,businessinsider.com,slashdot.org,hackaday.com,makezine.com,theverge.com,engadget.com,lifehacker.com,wired.com&scoring=n&sortBy=publishedAt&apiKey=5740068485274299a2a0e08302f3e1b7")

        news = news.json()
        #print(json.dumps(news, indent=4, sort_keys=True))
        for i in range(10):
            temp = []
            temp.append((news["articles"][i]["author"]))
            temp.append((news["articles"][i]["description"]))
            temp.append((news["articles"][i]["title"]))
            temp.append((news["articles"][i]["urlToImage"]))
            temp.append((news["articles"][i]["url"]))
            temp.append((news["articles"][i]["publishedAt"]))
            data.append(temp)
    return data

#print(get_news(["linux","android","open-source"]))