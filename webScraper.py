from bs4 import BeautifulSoup
import requests
import utils
from urllib.parse import urlparse
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_fixed

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.page_content = self._get_page_content()

    def _get_page_content(self):
        response = self.fetch_data()
        if response.status_code == 200:
            return response.content
        else:
            print("Failed to retrieve page content.")
            return None
    # Define a retry decorator
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(120))  # Retry 3 times with a fixed wait time of 2 minutes between retries
    def fetch_data(self):
        response = requests.get(self.url)
        return response

    def check_content_validity(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')                        
                resultInfo = soup.find(class_='resultInfo')
                balls = resultInfo.find(class_='balls')
                draw_column = ''
                for ball in balls.select('.resultBall.ball'):
                    draw_column = draw_column + ',' + ball.text

                return draw_column
            except:
                return None
        else:
            return None

    def get_draw_column(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_millionaire_maker(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_joker(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_balander(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_draw_number(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_next_jackpot_1(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_draw_date(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_dividents(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_winners(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_total_winners(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_columns(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_prev_draw_url(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_next_draw_url(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_jackpot(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_rollover(self):
        raise NotImplementedError("Subclass must implement this method")