def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return 'Error: Zero division'

print (div42by(2))
print (div42by(13))
print (div42by(0))
print (div42by(5))
