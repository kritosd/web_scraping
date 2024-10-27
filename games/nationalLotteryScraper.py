from bs4 import BeautifulSoup
import requests
import utils
from urllib.parse import urlparse
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_fixed
from webScraper import WebScraper
import re

class nationalLotteryScraper(WebScraper):
    def check_content_validity(self, game):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".main_content")
                block = container[0].select(".wa_results_block."+game)
                numbers = block[0].find(class_='draw_numbers')
                draw_column = ''
                for number in numbers.select('.number.main'):
                    if number.text.isdigit():
                        draw_column = draw_column + ',' + number.text
                        return draw_column
                    else:
                        return None
            except Exception as e:
                return f"An error occurred: {e}"
                return None
        else:
            return None
    
    def get_draw_date(self, game=""):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".main_content")
                block = container[0].select(".wa_results_block."+game)
                strDate = block[0].find(class_='draw_date').text
                cleanedStrDate = strDate.strip()
                return datetime.strptime(cleanedStrDate, "%a %d %b %Y").date()
            except Exception as e:
                return f"An error occurred: {e}"
                return None
        else:
            return None

    def get_draw_column(self, game=""):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".main_content")
                block = container[0].select(".wa_results_block."+game)
                numbers = block[0].find(class_='draw_numbers')
                draw_column = ''
                for number in numbers.select('.number.main'):
                    draw_column = draw_column + ',' + number.text.strip()
                return draw_column
            except Exception as e:
                return f"An error occurred: {e}"
                return None
        else:
            return None

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

    def get_joker(self, game=""):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".main_content")
                block = container[0].select(".wa_results_block."+game)
                numbers = block[0].find(class_='draw_numbers')
                draw_column = ''
                for number in numbers.select('.number.special'):
                    bonus_number = number.find('span', class_='vh').next_sibling.strip()
                    draw_column = draw_column + ',' + bonus_number
                    return draw_column
            except Exception as e:
                return f"An error occurred: {e}"
                return None
        else:
            return None

    def get_balander(self, game=""):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".main_content")
                block = container[0].select(".wa_results_block."+game)
                numbers = block[0].find(class_='draw_numbers')
                draw_column = ''
                for number in numbers.select('.number.special'):
                    bonus_number = number.find('span', class_='vh').next_sibling.strip()
                    draw_column = draw_column + ',' + bonus_number
                    return draw_column
            except Exception as e:
                return f"An error occurred: {e}"
                return None
        else:
            return None

    def get_draw_number(self, game=""):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".main_content")
                block = container[0].select(".wa_results_block."+game)
                draw_content = block[0].find(class_='draw_content')
                list_inline = block[0].find(class_='list_inline')
                liTags = list_inline.findAll('li')
                # Find the <a> tag
                a_tag = liTags[1].find('a')
                # Get the 'href' attribute (the URL)
                url = a_tag['href']

                # Use a regular expression to find the number after "prize-breakdown/"
                match = re.search(r'/prize-breakdown/(\d+)', url)

                if match:
                    draw_number = match.group(1)
                    return draw_number
                else:
                    print("No number found")
                    return None
            except:
                return None
        else:
            return None

        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                ticket = soup.find(class_='ticket')
                rolloverBox = ticket.find(class_='rollover-box')
                rolloverString = rolloverBox.find('span')
                rollover = utils.extract_number_from_string(rolloverString.text)
                return rollover
            except:
                return 0
        else:
            return None