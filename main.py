import db
from models import Euromillions
from webScraper import WebScraper
from datetime import datetime
import sys

def scrap(date):
    url = 'https://www.euro-millions.com/results/'+date.strftime('%d-%m-%Y')
    scraper = WebScraper(url)
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
        if db.record_exists(draw_number):
            db.update_record(draw_number, data)
        else:
            db.add(data)

        return scraper.get_next_draw_url()
        

def main():
    # Check if argument provided
    if len(sys.argv) < 2:
        print("No parameter provided. Please provide at least one parameter.")
        sys.exit(1)
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


    if date1 is not None and date2 is not None:
        next_date = scrap(date1)
        while next_date <= date2:
            next_date = scrap(next_date)
    elif date1 == date2:
        next_date = scrap(date1)
    elif date1 is not None and date2 is None:
        next_date = scrap(date1)


if __name__ == "__main__":
    main()
    