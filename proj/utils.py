from bs4 import BeautifulSoup
def find_resources(tag:str, attribuite:str, soup:BeautifulSoup) -> list:
    """this will get all http and https links per tag and attribuite and return a list of them"""
    list = []
    for item in soup.find_all(tag):
        if item.get(attribuite) is not None and item.get(attribuite) not in list:
            if(item.get(attribuite)[0:2] == "//"):
                list.append(item.get(attribuite))
            elif(item.get(attribuite)[0] == "/"):
                list.append(item.get(attribuite))
            elif("http" in item.get(attribuite)):
                list.append(item.get(attribuite))

    return list