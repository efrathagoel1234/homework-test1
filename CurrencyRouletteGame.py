from currency_converter import CurrencyConverter

#get_money_interval -Will get the current currency rate from USD to ILS and will
#generate an interval as follows:
#a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
#(5 - d))

#2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
#value to a given amount of USD
#3. play - Will call the functions above and play the game. Will return True / False if the user
#lost or won.


c = CurrencyConverter()
print(c.convert(100, 'EUR', 'USD'))
