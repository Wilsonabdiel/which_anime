import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import json


class Comparer:
    def __init__(self):
        self.base_url = "https://www.imdb.com/"

    def get_data(self, title):
        response = requests.get(self.base_url + "search/title/?genres=anime&title=" + title)
        page_soup = soup(response.text, 'html.parser')
        # Extract the necessary data from page_soup
        # This will depend on the structure of the webpage
        # Return the data as a pandas DataFrame
        rating_div = page_soup.find('div', class_='ratingValue')
    # Return the data as a pandas DataFrame
        if rating_div is not None:
             rating = rating_div.text
        else:
            rating = None
        return pd.DataFrame({'title': [title], 'rating': [rating]})

    def compare(self, anime_list):
        data_frames = [self.get_data(anime) for anime in anime_list]
        # Here's where you'd implement your comparison logic
        # For example, you might want to compare the average ratings of the animes
        avg_ratings = [df['rating'].mean() for df in data_frames]
        comparison_results = pd.DataFrame({
            'anime': anime_list,
            'avg_rating': avg_ratings
        })
        return comparison_results

class Searcher:
    def __init__(self):
        self.base_url = "https://www.imdb.com/"

    def search(self, title, year=None, tv=False, person=False):
    
        url = f"{self.base_url}search/anime/?name={name}" 

        if year is not None:
            url += f"&year={year}"
        if tv:
            url += "&type=tv"
        if person:
            url += "&type=person"
        response = requests.get(url)
        page_soup = soup(response.text, 'html.parser')

        
        watch_trailler_div = page_soup.find('a', class_='ipc-lockup-overlay ipc-focusable')
        rate = page_soup.find('div', class_ ='sc-e-7b78b2c-5 dWdOca')
        if watch_trailler_div is not None:
            watch_trailler = watch_trailler_div.get('href')
        else:
            watch_trailler = None
        return{
             'title': title,
            'watch_link': self.base_url + watch_trailler,
            'rate_link': self.base_url + rate
        }
if __name__ == "__main__":
    searcher = Searcher()
    print(searcher.search("Naruto"))


# if __name__ == "__main__":
#     comparer = Comparer()
#     anime_list = ["Naruto", "Bleach", "One Piece"]  # Add the animes you want to compare
#     print(comparer.compare(anime_list))
