import db
from models import Euromillions
from webScraper import WebScraper
from datetime import datetime

url = 'https://www.euro-millions.com/results/26-03-2024'
scraper = WebScraper(url)
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
db.add(data)

