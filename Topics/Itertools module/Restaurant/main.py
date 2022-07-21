import itertools

total = 30
dishes = itertools.product(main_courses, desserts, drinks)
prices = itertools.product(price_main_courses, price_desserts, price_drinks)

for dish, price in list(zip(dishes, prices)):
    if sum(price) <= total:
        print(*dish, sum(price))
