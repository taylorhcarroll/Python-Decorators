def kids(func):
    def do_chore(*args, **kwargs):
        chore_sentence = func(*args, **kwargs)
        return f"{chore_sentence} by the kids"
    return do_chore


def mom(func):
    def do_chore(*args, **kwargs):
        chore_sentence = func(*args, **kwargs)
        return f"{chore_sentence} by mom"
    return do_chore


def dad(func):
    def do_chore(*args, **kwargs):
        chore_sentence = func(*args, **kwargs)
        return f"{chore_sentence} by dad"
    return do_chore


@kids
def garbage():
    return "The garbage was taken out"


@mom
def laundry():
    return "The dirty laundry was cleaned"


@dad
def dust():
    return "The house was dusted"


@kids
def groom():
    return "The cat was brushed"


print(garbage())
print(laundry())
print(dust())
print(groom())
