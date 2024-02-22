from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pdp


class comparer:
    def __init__(self) -> None:
        self.base_url = "https://www.imdb.com/"
        

    def get_data(self, title):

        response = requests.get(self.base_url + "search/title/?genres=anime&title=" + title)

        page_soup = Soup(response.text, 'html.parser')

    def compare(self, anime_list):
        # Use the get_anime_data method to get data for each anime
        # Compare the data
        # This could involve looking at ratings, number of reviews, etc.
        # Return the comparison results

    if __name__ == "__main__":
        comparer = AnimeComparer()
        anime_list = ["Naruto", "Bleach", "One Piece"]  # Add the animes you want to compare
        print(comparer.compare_animes(anime_list))
