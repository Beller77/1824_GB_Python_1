import utils as ut

cur_input = 'usd'
print(f"Курс {cur_input.upper()}: {ut.currency_rates(cur_input)[0]} "
      f"за {ut.currency_rates(cur_input )[1]} ед., {ut.date_cur()}")

cur_input = 'eur'
print(f"Курс {cur_input.upper()}: {ut.currency_rates(cur_input)[0]} "
      f"за {ut.currency_rates(cur_input )[1]} ед., {ut.date_cur()}")

cur_input = 'KGS'
print(f"Курс {cur_input.upper()}: {ut.currency_rates(cur_input)[0]} "
      f"за {ut.currency_rates(cur_input )[1]} ед., {ut.date_cur()}")
