
# * API PROJECT
from pyfiglet import figlet_format
from termcolor import colored
from random import choice
import requests

url = 'https://icanhazdadjoke.com/search'
tell_joke = 'Let me tell you a joke! Give me a topic: '
title = 'Dad Joke 3000'

ascii_title = figlet_format(title)
colored_title = colored(ascii_title, color='magenta')

print(colored_title)
user_input = input(tell_joke)
test_input = user_input.isalpha()

while not test_input:

    print('Please Enter A Word')
    user_input = input(tell_joke)
    test_input = user_input.isalpha()

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={'term': user_input},
)

data = response.json()
total_jokes = len(data['results'])


def joke():
    single_joke = choice(data['results'])
    joke = single_joke['joke']
    print(joke)


if total_jokes > 1:
    print(f"I've got {total_jokes} jokes about {user_input}. Here's one: ")
    joke()
elif total_jokes == 1:
    print(f"I've got one joke about {user_input}. Here's it is: ")
    joke()
else:
    print(f"Sorry, I don't have jokes about {user_input}! Please try again")
