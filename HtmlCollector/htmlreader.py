from bs4 import BeautifulSoup
from langdetect import detect
import functions as ft
from datetime import datetime

def convert_to_datetime(date_str):
    # Remove non-breaking spaces and other non-standard characters
    cleaned_date_str = date_str.replace('\u2009', ' ').replace('・', '').replace(' ', '')

    # Define the date format to match the input string
    date_format = "%H:%M - %d de %b. de %Y"

    # Parse the cleaned date string into a datetime object
    try:
        dt = datetime.strptime(cleaned_date_str, date_format)
        return dt
    except ValueError:
        return None  # Return None in case of parsing error

with open('../agro.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
container = soup.find('main', id='container')
tweets = container.find_all('div', {'tabindex': '-1'})

for tweet in tweets:
    class_name = tweet.get('class')

    handle = tweet.find('span', class_='tweet-header-handle').text.strip()
    text = tweet.find('span', class_='tweet-body-text').text.strip()
    date = tweet.find('a', class_='tweet-date').text.strip()
    interact = tweet.find('div', class_='tweet-interact')

    replies = interact.find('span', class_='tweet-interact-reply').text.strip()
    retweets = interact.find('span', class_='tweet-interact-retweet').text.strip()
    likes = interact.find('span', class_='tweet-interact-favorite').text.strip()

    #views = interact.find('span', class_='tweet-interact-views').text.strip()

    if(text == ""):
        continue
    elif(not(ft.check_word(text, "mst"))):
        continue
    elif(detect(text) != "pt"):
        continue
    date = ft.horarioParaDate(date)
    print('Class id:', class_name[1][9:30])
    print('Handle:', handle)
    print('Text:', text)
    print('Date:', date)
    print('Replies:', replies)
    print('Retweets:', retweets)
    print('Likes:', likes)
    print('---')
