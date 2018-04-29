# average of list
def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


# zipping lists
drop_first_last([2, 45, 5, 6, 6, 7, 4, 3, 34, 4, 5, 6, 6, 5, 34])

first = {'csdafc', 'sdadfd', 'dsfafdsf'}
last = {'dsfaf', 'dsafsdfg', 'sadfsdf'}

names = zip(first, last)

for a, b in names:
    print(a, b)

# lambda ausdruck

answer = lambda x: x * 7
print(answer(5))

stocks = {
    'GOOG': 550,
    'BMW': 34,
    'EBY': 54,
    'ALB': 43
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
