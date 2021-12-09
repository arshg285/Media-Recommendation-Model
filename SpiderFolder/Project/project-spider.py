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
