# simpleWebScrape

Simple application to webscape cfcunderwriting.com

1. Scrape page
2. Get a list of all external resources in the page, then dump that into a json file(thus the jsons file present)
3. enumerate all the links present on the page and find location of the privacy policy page
4. use privacy policy page found on step 3 to webscrape all visable text, and create a word frequency of said words

used packages:
+ BeautifulSoup
+ html5lib
+ regex
+ json
+ zipp
