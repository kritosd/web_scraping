from bs4 import BeautifulSoup
import requests
import utils
from urllib.parse import urlparse, parse_qs
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_fixed
from webScraper import WebScraper
import time
from playwright.sync_api import sync_playwright

class MegaScraper(WebScraper):
    def __init__(self, url):
        self.url = url
        self.page_content = self.get_dynamic_soup()

    def get_dynamic_soup(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(self.url)
            page_content = page.content()
            browser.close()
            return page_content

    def check_content_validity(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                winningNumbersPg = soup.find(class_='winningNumbersPg')
                page_content = winningNumbersPg.find(class_='page_content')
                winningNumbersHeader = page_content.find(class_='winningNumbersHeader')
                contentRow = winningNumbersHeader.find(class_='contentRow')
                balls = contentRow.find(class_='numbers')
                draw_column = ''
                for ball in balls.select('.ball'):
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
                winningNumbersPg = soup.find(class_='winningNumbersPg')
                page_content = winningNumbersPg.find(class_='page_content')
                winningNumbersHeader = page_content.find(class_='winningNumbersHeader')
                contentRow = winningNumbersHeader.find(class_='contentRow')
                balls = contentRow.find(class_='numbers')
                print(balls)
                draw_column = ''
                for ball in balls.select('.ball:not(.winNumMB)'):
                    draw_column = draw_column + ',' + ball.text
                    print(ball)
                return draw_column
            except Exception as e:
                print(f"An error occurred: {e}")
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
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        else:
            return None

    def get_joker(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                winningNumbersPg = soup.find(class_='winningNumbersPg')
                page_content = winningNumbersPg.find(class_='page_content')
                winningNumbersHeader = page_content.find(class_='winningNumbersHeader')
                contentRow = winningNumbersHeader.find(class_='contentRow')
                balls = contentRow.find(class_='numbers')
                ballsArray = balls.select('.ball.winNumMB')
                joker = ballsArray[0].text
                print(joker)
                return joker
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        else:
            return None

    def get_balander(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                winningNumbersPg = soup.find(class_='winningNumbersPg')
                page_content = winningNumbersPg.find(class_='page_content')
                winningNumbersHeader = page_content.find(class_='winningNumbersHeader')
                contentRow = winningNumbersHeader.find(class_='contentRow')
                balls = contentRow.find(class_='numbers')
                ballsArray = balls.select('.ball.winNumMB')
                balander = ballsArray[0].text
                print(balander)
                return balander
            except Exception as e:
                print(f"An error occurred: {e}")
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
            return 123

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
            # Extract query parameters
            query_params = parse_qs(parsed_url.query)
            # Get the 'date' parameter
            date = query_params.get('date', [None])[0]
            
            str_date = str(utils.convert_100_ns_intervals_to_date(int(date)))
            
            # Parse the original date string into a datetime object
            date_object = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')

            # Format the datetime object to the desired format
            formatted_date_string = date_object.strftime('%d-%m-%Y')

            return datetime.strptime(formatted_date_string, '%d-%m-%Y').date()

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_dividents(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                allWinners = soup.find(class_='allWinners')
                detailPendingJackpot = allWinners.findAll(class_='detailPendingJackpot')
                tableJackpotWinningNumbers = detailPendingJackpot[1].find(class_='tableJackpotWinningNumbers')
                
                dividents = ''
                for winner in tableJackpotWinningNumbers.select('.ie11-col3')[1:]:
                    print(winner.text)
                    number = utils.lexical_to_number(winner.text)
                    print(number)
                    # number = utils.convert_to_normal_format(str(winner.text))
                    dividents = dividents + '#' + str(number)
                print(dividents)
                return dividents
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        else:
            return None

    def get_multi_winners(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                allWinners = soup.find(class_='allWinners')
                detailPendingJackpot = allWinners.findAll(class_='detailPendingJackpot')
                tableJackpotWinningNumbers = detailPendingJackpot[1].find(class_='tableJackpotWinningNumbers')
                
                multi_winners = ''
                for winner in tableJackpotWinningNumbers.select('.ie11-col4')[1:]:
                    print(winner.text)
                    # number = utils.lexical_to_number(winner.text)
                    # print(number)
                    multi_winners = multi_winners + '#' + utils.convert_to_normal_format(winner.text if winner.text else '0')
                print(multi_winners)
                return multi_winners
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        else:
            return None

    def get_draw_cash_option(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                winningNumbersPg = soup.find(class_='winningNumbersPg')
                page_content = winningNumbersPg.find(class_='page_content')
                winningNumbersHeader = page_content.find(class_='winningNumbersHeader')
                contentRow = winningNumbersHeader.find(class_='contentRow')
                cashOpt = contentRow.find(class_='cashOpt')
                nextCashOpt = cashOpt.find(class_='nextCashOpt')
                draw_cash_option = utils.lexical_to_number(nextCashOpt.text)
                print(draw_cash_option)
                return draw_cash_option
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        else:
            return None
    

    def get_multiplier(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                winningNumbersPg = soup.find(class_='winningNumbersPg')
                page_content = winningNumbersPg.find(class_='page_content')
                winningNumbersHeader = page_content.find(class_='winningNumbersHeader')
                contentRow = winningNumbersHeader.find(class_='contentRow')
                numbers = contentRow.find(class_='numbers')
                megaplier = numbers.find(class_='megaplier')
                winNumMP = megaplier.find(class_='winNumMP')
                multiplier = utils.convert_to_normal_format(winNumMP.text)
                print(multiplier)
                return int(multiplier)
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        else:
            return None

    def get_winners(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                allWinners = soup.find(class_='allWinners')
                detailPendingJackpot = allWinners.findAll(class_='detailPendingJackpot')
                tableJackpotWinningNumbers = detailPendingJackpot[1].find(class_='tableJackpotWinningNumbers')
                
                winners = ''
                for winner in tableJackpotWinningNumbers.select('.ie11-col2')[1:]:
                    number = winner.text
                    winners = winners + '#' + utils.convert_to_normal_format(number)
                
                return winners
            except Exception as e:
                print(f"An error occurred: {e}")
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
                return 0
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
                return 0
        else:
            return None

    def get_prev_draw_url(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                nextResult = soup.find(attrs={"title": "View the Previous EuroMillions Result"})
                link = nextResult.get('href')
                prev_date = datetime.strptime(link.split('/')[-1], '%d-%m-%Y')
                return prev_date
            except:
                return None
        else:
            return None

    def get_next_draw_url(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                nextResult = soup.find(attrs={"title": "View the Next EuroMillions Result"})
                link = nextResult.get('href')
                next_date = datetime.strptime(link.split('/')[-1], '%d-%m-%Y')
                return next_date
            except:
                return None
        else:
            return None

    def get_jackpot(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                winningNumbersPg = soup.find(class_='winningNumbersPg')
                winningNumbersHeader = winningNumbersPg.find(class_='winningNumbersHeader')
                winningNumbersDate = winningNumbersHeader.findAll(class_='winningNumbersDate')
                estJackpot = winningNumbersDate[1].find(class_='estJackpot')
                print(estJackpot)
                jackpot = utils.lexical_to_number(estJackpot.text)
                return jackpot
            except:
                return None
        else:
            return None

    def get_rollover(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                nextJackpot = soup.find(class_='nextJackpot')
                rolloverContainer = nextJackpot.find(class_='rollover')
                rolloverString = rolloverContainer.find('span')
                rollover = utils.extract_number_from_string(rolloverString.text)
                return rollover
            except:
                return 0
        else:
            return None