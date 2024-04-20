import db
from models import Euromillions
from webScraper import WebScraper
from datetime import datetime
import sys

if __name__ == "__main__":
    date = sys.argv[1]
    url = 'https://www.euro-millions.com/results/'+date
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