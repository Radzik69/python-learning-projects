import requests
from bs4 import BeautifulSoup

url = ""
quotes_counter = 0
page = 1

def get_user_requirements():
    global url
    number_of_quotes = int(input("Choose number of quotes to scrape: "))
    quotes_tags = input(
        '\nPress 1 to search all quotes\n'
        'Press 2 to search quotes with tag "love"\n'
        'Press 3 to search quotes with tag "inspirational"\n'
        'Press 4 to search quotes with tag "life"\n'
        'Press 5 to search quotes with tag "humor"\n'
    )

    match quotes_tags:
        case "1":
            url = "http://quotes.toscrape.com/page/1/"
        case "2":
            url = "https://quotes.toscrape.com/tag/love/page/1/"
        case "3":
            url = "https://quotes.toscrape.com/tag/inspirational/page/1/"
        case "4":
            url = "https://quotes.toscrape.com/tag/life/page/1/"
        case "5":
            url = "https://quotes.toscrape.com/tag/humor/page/1/"
        case _:
            print("Wrong input")
            get_user_requirements()
            return

    scrape_data_from_url(url, number_of_quotes)

def scrape_data_from_url(url, number_of_quotes):
    global quotes_counter
    global page

    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    if not quotes:
        print("No more quotes found.")
        return

    for quote, author in zip(quotes, authors):
        if quotes_counter >= number_of_quotes:
            return
        print(f"{quote.text} -- {author.text}")
        quotes_counter += 1

    if quotes_counter < number_of_quotes:
        page_number = str(page + 1)
        url = url.replace(f"page/{page}/", f"page/{page_number}/")
        page += 1
        scrape_data_from_url(url, number_of_quotes)

get_user_requirements()
