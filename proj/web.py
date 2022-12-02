from utils import find_resources
from bs4 import BeautifulSoup
import requests
import json
import re
URL = "https://www.cfcunderwriting.com/en-gb/"
res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html5lib')

#type of resources used on the website, a more wide approach would be to pass all type of resources
resDict = {'a':"href", 'script':"src", 'svg': "xmlns"}

#get all links and place it in a dict by resource type
dictOfResources = {}
for key, value in resDict.items():
    result = find_resources(key, value, soup)
    if result:
        dictOfResources[key] = result

jsonDump = {}
jsonList = []
enumeratedList = []
index = 1

#create 
for name, values in dictOfResources.items():
    for item in values:
        #make links interactable
        if(item[0:2] == "//"):
            item ="http:"+item
        elif(item[0] == "/"):
            item ="https://www.cfcunderwriting.com"+item
        #create external resources list
        if "cfcunderwriting.com" not in item:
            jsonList.append(item)
        #create enumerated list
        enumeratedList.append(f"{index}. {item}")
        index =index+1

#for external resources json file
jsonDump["externalResources"] = jsonList
jsonObject = json.dumps(jsonDump)

with open("externalResources.json", "w") as outfile:
    outfile.write(jsonObject)


#look for the privacy link
privacyLink = [link for link in enumeratedList if "privacy" and "policy" in link]

#duplicate files removed so if it exits it will be index 0 (though this leaves some room for errors)
if privacyLink:
    privRes = requests.get(privacyLink[0][4:])

#get lxml parser this time, better for visible text
privacySoup = BeautifulSoup(privRes.text, 'lxml')
privacyText = privacySoup.get_text()

#clean string from anything except lower and upper case chachters || words with ' have been joined as e.g. google and google's have diferent meanings
privacyText = re.sub('’', '', privacyText)
privacyText = re.sub('[^A-Za-z]+', ' ', privacyText)

#split, count words, and zip words and frequencies together for json
splitText =  privacyText.split()
frequencies=[splitText.count(word) for word in splitText]
dictFreq = dict(zip(splitText, frequencies))
print(dictFreq)


jsonObject = json.dumps(dictFreq)

with open("wordFrequencies.json", "w") as outfile:
    outfile.write(jsonObject)









