from currency_converter import CurrencyConverter
c = CurrencyConverter()
print(c.convert(100, 'EUR', 'THB'))

from forex_python.converter import CurrencyRates
c = CurrencyRates()
print(c.get_rates('USD'))
print(c.get_rate('USD', 'THB'))




