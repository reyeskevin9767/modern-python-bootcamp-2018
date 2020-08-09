
# * (**kwwargs)
def favorite_colors(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")


favorite_colors(rusty='green', colt='blue')

# rusty's favorite color is green
# colt's favorite color is blue


def special_greeting(**kwargs):
    if "Colt" in kwargs and kwargs["Colt"] == "special":
        return "You get a special greeting Colt!"
    elif "Colt" in kwargs:
        return f"{kwargs['Colt']} Colt!"

    return "Not sure who this is..."


special_greeting(Colt='Hello')  # Hello Colt!
special_greeting(Bob='hello')  # Not sure who this is...
special_greeting(Colt='special')  # You get a special greeting Colt!
