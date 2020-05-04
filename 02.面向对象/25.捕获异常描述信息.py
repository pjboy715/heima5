try:
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)
