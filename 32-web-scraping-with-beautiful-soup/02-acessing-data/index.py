
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
            <li class="special super-special">This list item is special.</li>
            <li class="special">This list item is also special.</li>
            <li>This list item is not special.</li>
        </ol>
        <div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# for el in soup.select(".special"):
# print(el.get_text())
# print(el.name)
# print(el.attrs)
attr = soup.find("div")["id"]
print(attr)
