# In the examples below, 's' occurs at index 3, 6 and 10

# count the entire string

count = 'This is a string'.count('T', 1, 7)
print(count)


brand = 'Apple'
exchangeRate = 1.235235245

message = \
    'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' \
    %(brand, 1299, exchangeRate)
print(message)

message2 = \
'The price of this {0:s} laptop is {1:7d} USD and the exchange rate is {2:7.2f} USD to 1 EUR'\
.format('Apple', 1299, 1.235235245)
print(message2)
