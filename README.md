# PIC 16B Project

This repository contains a descriptive tutorial and all the code for Hiral Kotecha and Arsh Gupta's project for PIC 16B taken at UCLA during the Fall 2021 quarter. The project is titled "Intersectionality in the Film Industry" and is focused around promoting diversity and representation of marginalized communities in said industry. In this project, we have built a TV shows and movies recommender system which will suggest most relevant titles to the user based on their preferred characteristics and preferred representations that they wish to see in their entertainment choices.

# Lights, Camera, Python!

## Group Contributions Statement

For the purposes of this project, we split the work up among the two of us in a way that each member was working on areas of their strength and could in turn supply code that would effectively be utilized with the code being written by the other person.

A more descriptive outline of our delegation of our responsibilities is as follows:

### Arsh Gupta

- Arsh created the webscraper that incorporates input from the user in order to crawl on multiple webpages across the internet to fetch results of movies and TV shows that are most relevant to the parameters of interest identified by the user uusing the library Scrapy to create the class that would perform the different parsing methods.
- The spider would start at the appropriate webpage and locate various elements for each title including the movie/TV show name, certification, and year of release based on the CSS attributes for the different parts of the webpage which were then yielded by the class method in the form of a dictionary forming a singular row of the table containing all results that would be displayed to the user.
- Some pieces of information such as year of release were fetched in a way that required additional data manipulation in order for it to be presented in a comprehensible format which was also accomplished in the scraper.
- Finally, the spider checks if there are multiple webpages containing more results for titles with the provided keywords and if so then it yields the `scrapy.Request` method with the callback to the same `self.parse` class method.
- Addiitonally, Arsh consolidated the code and functions from the webapp in a class titled `WebApp` in the `function_definitions.py` file which could then be imported into the Jupyter Notebook being used to deploy the webapp.

### Hiral Kotecha

Hiral created the web app that takes in user input (including desired keywords, and what the user would like to rank results by), and saved this information to a csv file that could be used by Arsh's scraper. She created the image scraper to get the links to the desired movies' posters and then created a dataframe that combines Arsh's scraped info with the image links. She wrote code that sorts the table based on the user-inputted "Rank-by" setting (either Highest Rated or Year of Release). She rendered the dataframe as an HTML table and rendered the images in the table. She displayed the results to the user.

-------------------

## HIRAL'S PART

-----------------

## Web Scraper

The code for the entire webscraper is as follows:

```python
import scrapy
import pandas as pd
import csv

file = open("/Users/arshmacbook/Desktop/PIC 16B/Course Project/Project/keywords.csv", 'r')
words = list(csv.reader(file))
keywords = []
for i in range(len(words)):
    keywords.append(words[i][0])
    
max_titles = 50
keywords = keywords[1:]

class MoviesSpider(scrapy.Spider):

    name = "movies"

    if len(keywords) == 1:
        start_url = f"https://www.imdb.com/search/keyword/?keywords={keywords[0]}"

    if len(keywords) == 2:
        start_url = f"https://www.imdb.com/search/keyword/?keywords={keywords[0]}%2C{keywords[1]}&sort=moviemeter,asc&mode=detail&page=1&ref_=kw_ref_key"

    start_urls = [start_url]

    names = []
    num = 0

    def parse(self, response):

        names = []

        for movie in response.css("div.lister-item.mode-detail"):

            name = movie.css("div.lister-item-content").css("a::text").get()
            if name in names:
                break
            else:
                names.append(name)
            rating = movie.css("div.lister-item-content").css("strong::text").get()
            certificate = movie.css("div.lister-item-content").css("span.certificate::text").get()
            year = movie.css("div.lister-item-content").css("span.lister-item-year.text-muted.unbold::text").get()

            if len(year) == 6:
                year = year[1:-1]
            else:
                if year[1] == "I":
                    year = year[-5:-1]
                else:
                    year = year[1:-1]
            year = year[:4]

            if self.num < max_titles:

                yield {
                    "Name" : name,
                    "Rating" : rating,
                    "Year" : year,
                    "Certification" : certificate
                }

                self.num += 1

            if len(response.css("a.lister-page-next.next-page")) != 0:

                next_page = response.css("a.lister-page-next.next-page").attrib["href"]

                if next_page:
                    next_page = response.urljoin(next_page)

                    yield scrapy.Request(next_page, callback = self.parse)
```

We will now analyze each segment of it.

### Importing libraries

```python
import scrapy
import csv
```

We import the scrapy and csv libraries since `scrapy` will be used to run and create the webscraper and `csv` will be used to read the keywords input supplied by the user in the form of a csv file.

### Reading user input

```python
file = open("/Users/arshmacbook/Desktop/PIC 16B/Course Project/Project/keywords.csv", 'r')
words = list(csv.reader(file))
keywords = []
for i in range(len(words)):
    keywords.append(words[i][0])
    
max_titles = 50
keywords = keywords[1:]
```

The above code is the part where the webscraper interprets the user inputted keywords through the csv file supplied containing that information. `max_titles` is the total number of titles that will be displayed by the main recommender system on the webapp.

### Starting with class implementation

```python
class MoviesSpider(scrapy.Spider):

    name = "movies"

    if len(keywords) == 1:
        start_url = f"https://www.imdb.com/search/keyword/?keywords={keywords[0]}"

    if len(keywords) == 2:
        start_url = f"https://www.imdb.com/search/keyword/?keywords={keywords[0]}%2C{keywords[1]}&sort=moviemeter,asc&mode=detail&page=1&ref_=kw_ref_key"

    start_urls = [start_url]

    names = []
    num = 0
```

We now start with the class `MoviesSpider` which will run all the methods we need to perform the required tasks. The `name` field specifies how this spider will be called in the terminal for when we want to run it. Additionally, depending on the number of keywords supplied by the user, the `start_url` is amended accordingly which will be the starting point for our webscraper to start its scraping.

-------------------

## HIRAL'S PART

-----------------
