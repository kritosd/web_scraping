import db
from models import Euromillions, Megamillions, AllGamesJackpots
from euroScraper import EuroScraper
from megaScraper import MegaScraper
from datetime import datetime, timedelta
import sys
import utils

def getTodayJackpot():
    url = 'https://www.euro-millions.com'
    scraper = EuroScraper(url)
    
    data = AllGamesJackpots(
        state='EURO',
        game_name='EUROMILLIONS',
        next_draw_jackpot=scraper.get_jackpot(),
        rollover=scraper.get_rollover()
    )
    if db.record_exists('game_name', 'EUROMILLIONS', AllGamesJackpots):
        db.update_record('game_name', 'EUROMILLIONS', data, AllGamesJackpots)
    else:
        db.add(data)

def getTodayJackpot2():
    url = 'https://www.megamillions.com/Winning-Numbers.aspx'
    scraper = MegaScraper(url)
    
    print('elanterRE')
    print(scraper.get_jackpot())
    data = AllGamesJackpots(
        state='MEGA',
        game_name='MEGAMILLIONS',
        next_draw_jackpot=scraper.get_jackpot(),
        draw_cash_option=scraper.get_draw_cash_option()
    )
    if db.record_exists('game_name', 'MEGAMILLIONS', AllGamesJackpots):
        db.update_record('game_name', 'MEGAMILLIONS', data, AllGamesJackpots)
    else:
        db.add(data)

def scrapEuromillions(date, retry = 0):
    print('Scrap date: '+date.strftime('%d-%m-%Y'))
    url = 'https://www.euro-millions.com/results/'+date.strftime('%d-%m-%Y')
    scraper = EuroScraper(url)
    validity = scraper.check_content_validity()
    if validity:
        draw_number = scraper.get_draw_number()
        data = Euromillions(
                draw_number=scraper.get_draw_number(),
                draw_date=scraper.get_draw_date(),
                draw_column=scraper.get_draw_column(),
                joker=scraper.get_joker(),
                balander=scraper.get_balander(),
                columns=scraper.get_columns(),
                total_winners=scraper.get_total_winners(),
                winners=scraper.get_winners(),
                dividents=scraper.get_dividents(),
                millionaire_maker=scraper.get_millionaire_maker(),
                next_jackpot_1=scraper.get_next_jackpot_1()
            )
        if db.record_exists('draw_number', draw_number, Euromillions):
            db.update_record('draw_number', draw_number, data, Euromillions)
        else:
            db.add(data)

        return scraper.get_next_draw_url()
    else:
        if (retry < 10):
            retry = retry + 1
            # Add one day to the date
            nextDayDate = date + timedelta(days=1)
            return scrapEuromillions(nextDayDate, retry)
        else:
            return None


def scrapMegamillions(date, retry = 0):
    print('Scrap date: '+date.strftime('%d-%m-%Y'))
    url = 'https://www.megamillions.com/Winning-Numbers/Previous-Drawings/Previous-Drawing-Page.aspx?date='+str(utils.convert_date_to_100_ns_intervals(date.strftime('%d-%m-%Y')))
    
    print(str(utils.convert_date_to_100_ns_intervals(date.strftime('%d-%m-%Y'))))
    scraper = MegaScraper(url)
    validity = scraper.check_content_validity()
    print(validity)
    if validity:
        draw_date = scraper.get_draw_date()
        print(draw_date)
        print('heyyyyyyy')
        data = Megamillions(
                draw_date=draw_date,
                draw_column=scraper.get_draw_column(),
                joker=scraper.get_joker(),
                balander=scraper.get_balander(),
                columns=scraper.get_columns(),
                total_winners=scraper.get_total_winners(),
                winners=scraper.get_winners(),
                dividents=scraper.get_dividents(),
                multi_winners=scraper.get_multi_winners(),
                draw_cash_option=scraper.get_draw_cash_option(),
                multiplier=scraper.get_multiplier(),
            )
        if db.record_exists('draw_date', draw_date, Megamillions):
            try:
                db.update_record('draw_date', draw_date, data, Megamillions)
            except ValueError as e:
                print(e)
        else:
            db.add(data)

        return scraper.get_next_draw_url()
    else:
        if (retry < 10):
            retry = retry + 1
            # Add one day to the date
            nextDayDate = date + timedelta(days=1)
            return scrapMegamillions(nextDayDate, retry)
        else:
            return None
        
def scrap(date):
    game = 'megamillions'
    result = None
    if game == 'euromillions':
        result = scrapEuromillions(date)
    if game == 'megamillions':
        result = scrapMegamillions(date)

    return result


def main():
    # Check if argument provided
    if len(sys.argv) < 2:
        date_str1 = None
        date1 = None
    else:
        date_str1 = sys.argv[1]
        date1 = datetime.strptime(date_str1, '%d-%m-%Y')

    # Check if 2 arguments provided
    if len(sys.argv) < 3:
        date_str2 = None
        date2 = None
    else:
        date_str2 = sys.argv[2]
        date2 = datetime.strptime(date_str2, '%d-%m-%Y')

    getTodayJackpot()

    if date1 is not None and date2 is not None:
        next_date = scrap(date1)
        while next_date is not None and next_date <= date2:
            next_date = scrap(next_date)
    elif date1 is None and date2 is None:
        # Get the current date and time
        current_datetime = datetime.now()
        # Extract only the date part
        today = datetime.strptime(current_datetime.strftime('%d-%m-%Y'), '%d-%m-%Y')
        yesterday = today - timedelta(days=1)
        next_date = scrap(yesterday)
        while next_date is not None and next_date <= today:
            next_date = scrap(next_date)
    elif date1 == date2:
        next_date = scrap(date1)
    elif date1 is not None and date2 is None:
        next_date = scrap(date1)

    print('Script terminated.')


if __name__ == "__main__":
    main()
    