import heapq
from collections import Counter

grades = [32, 32, 4231, 5435, 756, 23, 3465, 7557, 34, 2375]
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'asdad', 'price': 213123},
    {'ticker': 'wer', 'price': 23243},
    {'ticker': 'sdfs', 'price': 223},
    {'ticker': 'gher', 'price': 2123},
    {'ticker': 'ghf', 'price': 2123},
    {'ticker': 'fgcv', 'price': 234}
]

shares = {
    'asdad': 213123,
    'wer': 23243,
    'sdfs': 223,
    'gher': 2123,
    'ghf': 2123,
    'fgcv': 234
}

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))

min_price = min(zip(shares.values(), shares.keys()))
print(min_price)

text = "Eberhard and Tarpenning funded the company until the Series A" \
       "round. Musk led the Series A in February 2004, joining the" \
       "board of directors as its chairman as well as in operational roles." \
       "Musk was then the controlling investor in Tesla, providing the large" \
       "majority of the US$7.5 million round with personal funds. Co-founder" \
       "Martin Eberhard was the original CEO of Tesla until he was asked to" \
       "resign in August 2007 by the board of directors.Eberhard then took the" \
       "title of President of Technology before ultimately leaving the company" \
       "in January 2008 along with co-founder Marc Tarpenning, who served as the" \
       "CFO and subsequently the Vice President of Electrical Engineering of" \
       "the company until 2008"

words = text.split()
print(words)

counter = Counter(words)
top_five =counter.most_common(5)
print(top_five)