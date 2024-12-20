import db
from models.models import Euromillions, Megamillions, AllGamesJackpots, Powerball, PowerballDoublePlay
from models.models import UK_lotto, UK_lotto_hotpicks, UK_euromillions, UK_euromillions_hotpicks, UK_set_for_life, UK_thunderball

from euroScraper import EuroScraper
from megaScraper import MegaScraper
from powerballScraper import PowerballScraper
from games.nationalLotteryScraper import nationalLotteryScraper
from datetime import datetime, timedelta
import sys
import utils

def getTodayJackpotEuro():
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

def getTodayJackpotMega():
    url = 'https://www.megamillions.com/Winning-Numbers.aspx'
    scraper = MegaScraper(url)
    
    data = AllGamesJackpots(
        state='EURO',
        game_name='MEGAMILLIONS',
        next_draw_jackpot=scraper.get_jackpot(),
        draw_cash_option=scraper.get_draw_cash_option()
    )
    if db.record_exists('game_name', 'MEGAMILLIONS', AllGamesJackpots):
        db.update_record('game_name', 'MEGAMILLIONS', data, AllGamesJackpots)
    else:
        db.add(data)

def getTodayJackpotPowerball(date):
    print('Scrap date: '+date.strftime('%d-%m-%Y'))
    url = 'https://www.powerball.net/numbers/'+date.strftime('%Y-%m-%d')
    print(url)
    scraper = PowerballScraper(url)
    
    validity = scraper.check_content_validity()
    if validity:
        data = AllGamesJackpots(
            state='USA',
            game_name='POWERBALL',
            next_draw_jackpot=scraper.get_jackpot(),
            draw_cash_option=scraper.get_draw_cash_option(),
            rollover=scraper.get_rollover()
        )
        if db.record_exists('game_name', 'POWERBALL', AllGamesJackpots):
            db.update_record('game_name', 'POWERBALL', data, AllGamesJackpots)
        else:
            db.add(data)
    else:
        return None

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
    intervals = utils.convert_date_to_100_ns_intervals(date.strftime('%d-%m-%Y'))
    url = 'https://www.megamillions.com/Winning-Numbers/Previous-Drawings/Previous-Drawing-Page.aspx?date='+str(intervals)
    
    scraper = MegaScraper(url)
    validity = scraper.check_content_validity()
    if validity:
        draw_date = scraper.get_draw_date()
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
                next_jackpot_1=scraper.get_next_jackpot_1(),
                big_winners_5=scraper.get_big_winners_5(),
                big_winners_5M=scraper.get_big_winners_5M(),
            )
        if db.record_exists('draw_date', draw_date, Megamillions):
            try:
                db.update_record('draw_date', draw_date, data, Megamillions)
            except ValueError as e:
                print(e)
        else:
            db.add(data)
            
        return date + timedelta(days=1)
    else:
        if (retry < 10):
            retry = retry + 1
            # Add one day to the date
            nextDayDate = date + timedelta(days=1)
            return scrapMegamillions(nextDayDate, retry)
        else:
            return None
        

def scrapPowerball(date, retry = 0):
    print('Scrap date: '+date.strftime('%d-%m-%Y'))
    url = 'https://www.powerball.net/numbers/'+date.strftime('%Y-%m-%d')
    scraper = PowerballScraper(url)
    validity = scraper.check_content_validity()
    if validity:
        draw_date = scraper.get_draw_date()
        data = Powerball(
                draw_date=draw_date,
                draw_column=scraper.get_draw_column(),
                joker=scraper.get_joker(),
                balander=scraper.get_balander(),
                columns=scraper.get_columns(),
                total_winners=scraper.get_total_winners(),
                winners=scraper.get_winners(),
                dividents=scraper.get_dividents(),
                multi_winners=scraper.get_multi_winners(),
                next_jackpot_1=scraper.get_next_jackpot_1(),
                multiplier=scraper.get_multiplier(),
                big_winners_5M=scraper.get_big_winners_5M()
            )
        if db.record_exists('draw_date', draw_date, Powerball):
            db.update_record('draw_date', draw_date, data, Powerball)
        else:
            db.add(data)
        
        draw_column_db = scraper.get_draw_column_db()
        if (draw_column_db is not None):
            data = PowerballDoublePlay(
                draw_date=draw_date,
                draw_column=scraper.get_draw_column_db(),
                joker=scraper.get_joker_db(),
                balander=scraper.get_balander_db(),
                columns=scraper.get_columns(),
                total_winners=scraper.get_total_winners(),
                winners=scraper.get_winners_db(),
                dividents=scraper.get_dividents_db(),
                next_jackpot_1=scraper.get_next_jackpot_1(),
                multiplier=scraper.get_multiplier()
            )
            if db.record_exists('draw_date', draw_date, PowerballDoublePlay):
                db.update_record('draw_date', draw_date, data, PowerballDoublePlay)
            else:
                db.add(data)

        return scraper.get_next_draw_url()
    else:
        if (retry < 10):
            retry = retry + 1
            # Add one day to the date
            nextDayDate = date + timedelta(days=1)
            return scrapPowerball(nextDayDate, retry)
        else:
            return None


def scrapNationalLottery(date, retry = 0):
    print('Scrap date: '+date.strftime('%d-%m-%Y'))
    url = 'https://www.national-lottery.co.uk/results/'
    scraper = nationalLotteryScraper(url)
    game = 'lotto'
    validity = scraper.check_content_validity(game)
    if validity:
        draw_number = scraper.get_draw_number(game)
        data = UK_lotto(
                draw_number=draw_number,
                draw_date=scraper.get_draw_date(game),
                draw_column=scraper.get_draw_column(game),
                joker=scraper.get_joker(game),
                balander=scraper.get_balander(game)
            )
        if db.record_exists('draw_number', draw_number, UK_lotto):
            db.update_record('draw_number', draw_number, data, UK_lotto)
        else:
            db.add(data)

        game = 'euromillions'
        draw_number = scraper.get_draw_number(game)
        data = UK_euromillions(
                draw_number=draw_number,
                draw_date=scraper.get_draw_date(game),
                draw_column=scraper.get_draw_column(game),
                joker=scraper.get_joker(game),
                balander=scraper.get_balander(game)
            )
        if db.record_exists('draw_number', draw_number, UK_euromillions):
            db.update_record('draw_number', draw_number, data, UK_euromillions)
        else:
            db.add(data)

        game = 'set-for-life'
        draw_number = scraper.get_draw_number(game)
        data = UK_set_for_life(
                draw_number=draw_number,
                draw_date=scraper.get_draw_date(game),
                draw_column=scraper.get_draw_column(game),
                joker=scraper.get_joker(game),
                balander=scraper.get_balander(game)
            )
        if db.record_exists('draw_number', draw_number, UK_set_for_life):
            db.update_record('draw_number', draw_number, data, UK_set_for_life)
        else:
            db.add(data)

        game = 'thunderball'
        draw_number = scraper.get_draw_number(game)
        data = UK_thunderball(
                draw_number=draw_number,
                draw_date=scraper.get_draw_date(game),
                draw_column=scraper.get_draw_column(game),
                joker=scraper.get_joker(game),
                balander=scraper.get_balander(game)
            )
        if db.record_exists('draw_number', draw_number, UK_thunderball):
            db.update_record('draw_number', draw_number, data, UK_thunderball)
        else:
            db.add(data)

        game = 'lotto-hotpicks'
        draw_number = scraper.get_draw_number(game)
        data = UK_lotto_hotpicks(
                draw_number=draw_number,
                draw_date=scraper.get_draw_date(game),
                draw_column=scraper.get_draw_column(game),
                joker=scraper.get_joker(game),
                balander=scraper.get_balander(game)
            )
        if db.record_exists('draw_number', draw_number, UK_lotto_hotpicks):
            db.update_record('draw_number', draw_number, data, UK_lotto_hotpicks)
        else:
            db.add(data)

        game = 'euromillions-hotpicks'
        draw_number = scraper.get_draw_number(game)
        data = UK_euromillions_hotpicks(
                draw_number=draw_number,
                draw_date=scraper.get_draw_date(game),
                draw_column=scraper.get_draw_column(game),
                joker=scraper.get_joker(game),
                balander=scraper.get_balander(game)
            )
        if db.record_exists('draw_number', draw_number, UK_euromillions_hotpicks):
            db.update_record('draw_number', draw_number, data, UK_euromillions_hotpicks)
        else:
            db.add(data)
        
        return None
    else:
        if (retry < 10):
            retry = retry + 1
            # Add one day to the date
            nextDayDate = date + timedelta(days=1)
            return scrapPowerball(nextDayDate, retry)
        else:
            return None

   

def scrap(date, game):
    result = None
    if game == 'euromillions':
        getTodayJackpotEuro()
        result = scrapEuromillions(date)
    if game == 'megamillions':
        # getTodayJackpotMega()
        result = scrapMegamillions(date)
    if game == 'powerball':
        getTodayJackpotPowerball(date)
        result = scrapPowerball(date)
    if game == 'national-lottery':
        result = scrapNationalLottery(date)

    return result


def main():
    # Check if argument provided
    if len(sys.argv) < 2:
        game = None
        print('define a game.')
        return
    else:
        game = sys.argv[1]

    # Check if 2 arguments provided
    if len(sys.argv) < 3:
        date_str1 = None
        date1 = None
    else:
        date_str1 = sys.argv[2]
        date1 = datetime.strptime(date_str1, '%d-%m-%Y')

    # Check if 3 arguments provided
    if len(sys.argv) < 4:
        date_str2 = None
        date2 = None
    else:
        date_str2 = sys.argv[3]
        date2 = datetime.strptime(date_str2, '%d-%m-%Y')


    if date1 is not None and date2 is not None:
        next_date = scrap(date1, game)
        while next_date is not None and next_date <= date2:
            next_date = scrap(next_date, game)
    elif date1 is None and date2 is None:
        # Get the current date and time
        current_datetime = datetime.now()
        # Extract only the date part
        today = datetime.strptime(current_datetime.strftime('%d-%m-%Y'), '%d-%m-%Y')
        yesterday = today - timedelta(days=1)
        next_date = scrap(yesterday, game)
        while next_date is not None and next_date <= today:
            next_date = scrap(next_date, game)
    elif date1 == date2:
        next_date = scrap(date1, game)
    elif date1 is not None and date2 is None:
        next_date = scrap(date1, game)

    print('Script completed.')


if __name__ == "__main__":
    main()
    