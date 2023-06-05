while True:
    year = int(input('When was Python 1.0 released? '))
    if year > 1994:
        print('It was earlier than that!')
    elif year < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break