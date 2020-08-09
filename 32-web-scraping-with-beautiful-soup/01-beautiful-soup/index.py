
# * Using BeautifulSoup
from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>first HTML Page</title>
</head>
<body>
        <div id="first">
            <h3 data-example="yes">hi</h3>
            <p>more text.</p>
        </div>
        <ol>
            <li class="special">This list item is special.</li>
            <li class="special">This list item is also special.</li>
            <li>This list item is not special.</li>
        </ol>
        <div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(soup.body.div)
# d = soup.find_all(class_="special")
# d = soup.select("#first")
# d = soup.select("[data-example]")
# print(d)


# find an element with an id of foo
soup.find(id="foo")
soup.select("#foo")[0]

# find all elements with a class of bar
# careful! "class" is a reserved word in Python
soup.find_all(class_="bar")
soup.select(".bar")

# find all elements with a data
# attribute of "baz"
# using the general attrs kwarg
soup.find_all(attrs={"data-baz": True})
soup.select("[data-baz]")
