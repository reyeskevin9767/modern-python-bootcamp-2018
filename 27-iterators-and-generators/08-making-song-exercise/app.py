
# * Making Song Exercise
def make_song(count=99, beverage='soda'):
    while True:
        if count > 1:
            yield '{} bottles of {} on the wall.'.format(count, beverage)
        elif count == 1:
            yield 'Only {} bottle of {} left!'.format(count, beverage)
        else:
            yield 'No more {}!'.format(beverage)
            raise StopIteration
        count -= 1


kombucha_song = make_song(5, "komucha")

print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
