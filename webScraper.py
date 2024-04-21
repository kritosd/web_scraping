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

    def get_millionaire_maker(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                resultInfo = soup.find(class_='resultInfo')
                millionaireMakerContainer = resultInfo.find(class_=["fx","btwn","acen"])
                millionaire_maker = millionaireMakerContainer.find(class_='raffle').text
                return millionaire_maker
            except:
                return None
        else:
            return None

    def get_joker(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                resultInfo = soup.find(class_='resultInfo')
                balls = resultInfo.find(class_='balls')
                joker = ''
                for jball in balls.select('.resultBall.lucky-star'):
                    joker = joker + ',' + jball.text

                return joker
            except:
                return None
        else:
            return None

    def get_balander(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                resultInfo = soup.find(class_='resultInfo')
                balls = resultInfo.find(class_='balls')
                joker = ''
                for jball in balls.select('.resultBall.lucky-star'):
                    joker = joker + ',' + jball.text

                return joker
            except:
                return None
        else:
            return None

    def get_draw_number(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                drawInfo = soup.find(class_='drawInfo')
                dInfos = drawInfo.find_all(class_='dInfo')
                dInfo = dInfos[0]
                draw_number_US = dInfo.find(class_='title2').text
                draw_number = utils.convert_to_normal_format(draw_number_US)
                return draw_number
            except:
                return None
        else:
            return None

    def get_next_jackpot_1(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                drawInfo = soup.find(class_='drawInfo')
                dInfos = drawInfo.find_all(class_='dInfo')
                dInfo2 = dInfos[1]
                next_jackpot_1 = utils.convert_to_normal_format(dInfo2.find(class_='title2').text)
                return next_jackpot_1
            except:
                return None
        else:
            return None


    def get_draw_date(self):
        try:
            # Parse the URL
            parsed_url = urlparse(self.url)
            # Get the path component
            path = parsed_url.path
            # Split the path by '/'
            path_components = path.split('/')
            # Filter out empty components
            path_components = [component for component in path_components if component]
            # Return the last component
            date = '';
            if path_components:
                date =  path_components[-1]

            return datetime.strptime(date, '%d-%m-%Y').date()

        except:
            return None

    def get_dividents(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                prizeTotals = soup.find(id="PrizeTotals")
                prizeTotalsBody = prizeTotals.find('tbody')
                dividents = ''
                for row in prizeTotalsBody.select('tr:not(.totals)'):
                    prizePerWinner = row.find(attrs={"data-title": "Prize Per Winner"})
                    prizePerWinnerNo = prizePerWinner.text
                    dividents = dividents + '#' + utils.convert_to_normal_format(prizePerWinnerNo)
                    
                return dividents
            except:
                return None
        else:
            return None

    def get_winners(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                prizeTotals = soup.find(id="PrizeTotals")
                prizeTotalsBody = prizeTotals.find('tbody')
                winners = ''
                for row in prizeTotalsBody.select('tr:not(.totals)'):
                    totalWinners = row.find(attrs={"data-title": "Total Winners"}).text
                    number = totalWinners
                    winners = winners + '#' + utils.convert_to_normal_format(number)
                    
                return winners
            except:
                return None
        else:
            return None

    def get_total_winners(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                prizeTotals = soup.find(id="PrizeTotals")
                wrapSM = prizeTotals.find_next_sibling(class_=["fx", "btwn", "wrapSM"])
                acen = wrapSM.find_all(class_=["fx", "acen"])
                TWEl = acen[0].find(class_='title')
                total_winners = utils.convert_to_normal_format(TWEl.text)
                return total_winners
            except:
                return None
        else:
            return None


    def get_columns(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                prizeTotals = soup.find(id="PrizeTotals")
                wrapSM = prizeTotals.find_next_sibling(class_=["fx", "btwn", "wrapSM"])
                acen = wrapSM.find_all(class_=["fx", "acen"])
                columns = utils.convert_to_normal_format(acen[1].find(class_='title').text)
                return columns
            except:
                return None
        else:
            return None
