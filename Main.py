from urllib.request import urlopen
url = "https://api.scratch.mit.edu/users/YourUsernameHere/messages/count"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
content = html[start_index:end_index]
print(content)
