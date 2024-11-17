from bs4 import BeautifulSoup
import requests
import utils
from urllib.parse import urlparse
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_fixed
from webScraper import WebScraper
import re

class PowerballScraper(WebScraper):
    def check_content_validity(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".container-fluid.l-bg.-alt")
                lballs = container[0].find(class_='l-balls')
                balls = lballs.find(class_='balls')
                draw_column = ''
                for ball in balls.select('.new.ball'):
                    if ball.text.isdigit():
                        draw_column = draw_column + ',' + ball.text
                        return draw_column
                    else:
                        return None
            except Exception as e:
                return f"An error occurred: {e}"
                return None
        else:
            return None

    def get_draw_column(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".container-fluid.l-bg.-alt")
                lballs = container[0].find(class_='l-balls')
                ballsAscending = lballs.find(id='ballsAscending')
                balls = ballsAscending.find(class_='balls')
                draw_column = ''
                for ball in balls.select('.new.ball'):
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
                container = soup.select(".container-fluid.l-bg.-alt")
                lballs = container[0].find(class_='l-balls')
                balls = lballs.find(class_='balls')
                joker = ''
                for ball in balls.select('.new.powerball'):
                    joker = joker + ',' + ball.text

                return joker
            except:
                return None
        else:
            return None

    def get_balander(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".container-fluid.l-bg.-alt")
                lballs = container[0].find(class_='l-balls')
                balls = lballs.find(class_='balls')
                joker = ''
                for ball in balls.select('.new.powerball'):
                    joker = joker + ',' + ball.text

                return joker
            except:
                return None
        else:
            return None

    
    def get_draw_column_db(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".container-fluid.l-bg.-alt")
                lballs = container[0].find(class_='l-balls')
                ballsAscendingDP = lballs.find(id='ballsAscendingDP')
                balls = ballsAscendingDP.find(class_='balls')
                draw_column = ''
                for ball in balls.select('.new.ball'):
                    draw_column = draw_column + ',' + ball.text

                return draw_column
            except:
                return None
        else:
            return None

    def get_joker_db(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".container-fluid.l-bg.-alt")
                lballs = container[0].find(class_='l-balls')
                ballsDrawnDP = lballs.find(id='ballsDrawnDP')
                balls = ballsDrawnDP.find(class_='balls')
                joker = ''
                for ball in balls.select('.new.powerball'):
                    joker = joker + ',' + ball.text

                return joker
            except:
                return None
        else:
            return None

    def get_balander_db(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".container-fluid.l-bg.-alt")
                lballs = container[0].find(class_='l-balls')
                ballsDrawnDP = lballs.find(id='ballsDrawnDP')
                balls = ballsDrawnDP.find(class_='balls')
                joker = ''
                for ball in balls.select('.new.powerball'):
                    joker = joker + ',' + ball.text

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
                container = soup.select(".container-fluid.l-bg.-alt")
                statsBox = container[0].find(class_='l-stats-box')
                jackpot = statsBox.find(class_='-jackpot')
                jackpotValue = jackpot.find('div')
                next_jackpot_1 = utils.convert_to_normal_format(jackpotValue.text)
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
                convertedDate = datetime.strptime(date, '%Y-%m-%d').date()
                revertedDate = convertedDate.strftime('%d-%m-%Y')

            return datetime.strptime(revertedDate, '%d-%m-%Y').date()

        except:
            return None

    def get_dividents(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                payoutTable = soup.findAll(class_='payoutTable')
                tbody = payoutTable[0].find('tbody')
                dividents = ''
                for row in tbody.select('tr'):
                    prizePerWinner = row.find(attrs={"data-title": "Prize Amount"})
                    prizePerWinnerNo = prizePerWinner.text
                    dividents = dividents + '#' + utils.convert_to_normal_format(prizePerWinnerNo)
                    
                return dividents
            except:
                return None
        else:
            return None

    def get_dividents_db(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                payoutTable = soup.findAll(class_='payoutTable')
                tbody = payoutTable[2].find('tbody')
                dividents = ''
                for row in tbody.select('tr'):
                    prizePerWinner = row.find(attrs={"data-title": "Prize Amount"})
                    prizePerWinnerNo = prizePerWinner.text
                    dividents = dividents + '#' + utils.convert_to_normal_format(prizePerWinnerNo)
                    
                return dividents
            except:
                return None
        else:
            return None

    def get_multiplier(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".container-fluid.l-bg.-alt")
                lballs = container[0].find(class_='l-balls')
                balls = lballs.find(class_='balls')
                powerPlay = balls.select('.new.power-play')
                multiplier = utils.convert_to_normal_format(powerPlay[0].text)
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
                payoutTable = soup.findAll(class_='payoutTable')
                tbody = payoutTable[0].find('tbody')
                winners = ''
                for row in tbody.select('tr'):
                    winnersDiv = row.find(attrs={"data-title": "Winners"})
                    rollover = winnersDiv.find('span')
                    if (rollover is not None and rollover.text == 'Rollover'):
                        winners = winners + '#0'
                    else:
                        number = winnersDiv.text
                        winners = winners + '#' + utils.convert_to_normal_format(number)
                    
                return winners
            except:
                return None
        else:
            return None


    def get_multi_winners(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                payoutTable = soup.findAll(class_='payoutTable')
                tbody = payoutTable[1].find('tbody')
                multi_winners = ''
                for row in tbody.select('tr'):
                    winnersDiv = row.find(attrs={"data-title": "Winners"})
                    rollover = winnersDiv.find('span')
                    if (rollover is not None and rollover.text == 'Rollover'):
                        multi_winners = multi_winners + '0'
                    else:
                        number = winnersDiv.text
                        multi_winners = multi_winners + '#' + utils.convert_to_normal_format(number)
                    
                return multi_winners
            except:
                return None
        else:
            return None


    def get_winners_db(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                payoutTable = soup.findAll(class_='payoutTable')
                tbody = payoutTable[2].find('tbody')
                multi_winners = ''
                for row in tbody.select('tr'):
                    winnersDiv = row.find(attrs={"data-title": "Winners"})
                    rollover = winnersDiv.find('span')
                    if (rollover is not None and rollover.text == 'Rollover'):
                        multi_winners = multi_winners + '0'
                    else:
                        number = winnersDiv.text
                        multi_winners = multi_winners + '#' + utils.convert_to_normal_format(number)
                    
                return multi_winners
            except:
                return None
        else:
            return None

    def get_total_winners(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".container-fluid.l-bg.-alt")
                statsBox = container[0].find(class_='l-stats-box')
                jwinners = statsBox.find(class_='-winners')
                winners = jwinners.find('div')
                total_winners = utils.convert_to_normal_format(winners.text)
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
                return 0
        else:
            return 0

    def get_prev_draw_url(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                container = soup.select(".container-fluid.l-bg.-alt")
                statsBox = container[0].find(class_='l-stats-box')
                btnPrev = statsBox.find('_prev')
                link = btnPrev.get('href')
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
                container = soup.select(".container-fluid.l-bg.-alt")
                statsBox = container[0].find(class_='nav-btns')
                btnNext = statsBox.select(".nav-btn._next")
                link = btnNext[0].get('href')
                date_obj = datetime.strptime(link.split('/')[-1], "%Y-%m-%d")
                next_date_str = date_obj.strftime("%d-%m-%Y")
                next_date = datetime.strptime(next_date_str, "%d-%m-%Y")
                return next_date
            except:
                return None
        else:
            return None

    def get_jackpot(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                ticket = soup.find(class_='ticket')
                jackpotBox = ticket.find(class_='jackpot-box')
                jackpot_div = jackpotBox.find('div', class_='jackpot')
                # Extract the text content of the div
                jackpot_text = jackpot_div.get_text(strip=False)
                jackpot = utils.lexical_to_number(jackpot_text)
                return jackpot
            except:
                return None
        else:
            return None

    def get_draw_cash_option(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                ticket = soup.find(class_='ticket')
                cta = ticket.find(class_='cta')
                el = cta.find('div')
                normal = el.find(class_='normal').text
                # Extract the text after '*Cash Lump Sum:'
                match = re.search(r'\*Cash Lump Sum:\s*(\$\d+)', el.text)
                if match:
                    cash_lump_sum = match.group(1)
                    draw_cash_option = utils.lexical_to_number(cash_lump_sum + normal)
                    return draw_cash_option
                else:
                    return None
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        else:
            return None

    def get_big_winners_5M(self):
        if self.page_content:
            try:
                soup = BeautifulSoup(self.page_content, 'html.parser')
                media = soup.find(class_='media')
                mediaBody = media.find(class_='media-body')
                winnerNote = mediaBody.find(class_='winner-note')
                stateElArray = winnerNote.findAll('strong')
                
                big_winners_5M = ''
                counter = 0
                for state in stateElArray:
                    if counter > 0:
                        big_winners_5M = big_winners_5M + ','
                    big_winners_5M = big_winners_5M + state.text
                    counter += 1

                return big_winners_5M
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        else:
            return None

    def get_rollover(self):
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