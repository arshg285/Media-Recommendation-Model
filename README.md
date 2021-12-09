# PIC 16B Project

This repository contains a descriptive tutorial and all the code for Hiral Kotecha and Arsh Gupta's project for PIC 16B taken at UCLA during the Fall 2021 quarter. The project is titled "Intersectionality in the Film Industry" and is focused around promoting diversity and representation of marginalized communities in said industry. In this project, we have built a TV shows and movies recommender system which will suggest most relevant titles to the user based on their preferred characteristics and preferred representations that they wish to see in their entertainment choices.

# Lights, Camera, Python!

## Group Contributions Statement

For the purposes of this project, we split the work up among the two of us in a way that each member was working on areas of their strength and could in turn supply code that would effectively be utilized with the code being written by the other person.

A more descriptive outline of our delegation of our responsibilities is as follows:

### Arsh Gupta

- Arsh created the webscraper that incorporates input from the user in order to crawl on multiple webpages across the internet to fetch results of movies and TV shows that are most relevant to the parameters of interest identified by the user.
- Part of this exercise using the library Scrapy to create the class that would perform the different parsing methods and preparing the Python script sulf-sufficient in the sense that it was able to generate the appropriate `start_urls` based on whatever input was provided by the user without any need for hardcoding.
- The spider would then start of the appropriate webpage and locate various elements for each title displayed including the movie/TV show name, certification, and year of release based on the CSS attributes for the different parts of the webpage.
- These are then yielded by the class method in the form of a dictionary forming a singular row of the table containing all results that would be displayed to the user.
- Some pieces of information such as year of release were fetched in a way that required additional data manipulation in order for it to be presented in a comprehensible format which was also accomplished in the scraper.
- Finally, the spider checks if there are multiple webpages containing more results for titles with the provided keywords and if so then it yields the `scrapy.Request` method with the callback to the same `self.parse` class method.
- Addiitonally, Arsh consolidated the code from the webapp into a single `function_definitions.py` file which could then be imported into the Jupyter Notebook being used to deploy the webapp.
- This included creating a class and re-adjusting the the function definitions

### Hiral Kotecha

- Created a web app using PyWebIO that outputs prompts to a web browser, and takes in input from the user. This includes a scrolldown list of keywords, and radio buttons for what the user would like to rank result by. 
- Researched intersectionality and applicable keywords
- Saved approrpiate user input to csv file to be used by Arsh's web scraper. 
- Used BeautifulSoup for image scraping: including obtaining links of all results pages matching user input, then using those links to obtain all movie poster links.
- Converted CSV file created by Arsh's scraper into a dataframe, appended image links as column 
- Converted image links to HTML tags and rendered images using HTML method
- Sorted results based on user input/selection for rank-by
- Saved dataframe as a webpage 
- Displayed the results with message including reminder of user's chosen keywords and html table 

## What is "Lights, Camera, Python!"?

This project is an interactive WebApp, where users can explore intersectionality in film and televison. This is done by allowing users to select two keywords that will result in a table displaying shows and movies at the intersection of those identities. 

# Instructions on how to use our code and run the webapp on your own device!

1. Download all the files in this repository, named **Web App.ipynb**, **project-spider.py**, **function_definitions.py**, and **Cat-Movie.png** in the directory of your choice that you can access easily.
2. Open the terminal, set the directory to where all your downloaded files are using the command `cd /Users/...` and enter the command `scrapy startproject IMDB_scraper`.
3. Then, place the **project-spider.py** file in the folder titled **spiders** within the scrapy project that would be created in your directory.
4. Now, open the Jupyter Notebook titled **Web App.ipynb** in the web browser of your choice using Anaconda Navigator or simply runnning the command `jupyter notebook` in the terminal.
5. Go to the **kernel** tab on the top bar of the Jupyter Notebook and select the option **Restart Kernel and Run All**.
6. Enjoy your selections!

## Webapp: PywebIO

To make the webapp, we used the Python library "PywebIO" which supports synchornization, callback, and couroutine to obtain and process user inputs. 

From PywebIO, we imported:
_____________________________________________________________________________________________    

### pywebio.input : get input from web broswer
#### Examples:

• input ➪ text input

• actions ➪ action selection

• file_upload ➪ file uploading

• input_update ➪ update input item

#### Read more on input functions: https://pywebio.readthedocs.io/en/latest/input.html
_____________________________________________________________________________________________    
                                              
### pywebio.output : make output to web browser
#### Examples:

• put_text ➪ output plain text

• put_warning ➪ output warning message

• put_collapse ➪ output collapsible content 

• toast ➪ show a notification message

#### Read more on output functions: https://pywebio.readthedocs.io/en/latest/output.html
_____________________________________________________________________________________________    

### pywebio.session : more control to session
#### Examples:

• download ➪ send file to user; user browser will download 

• eval_js ➪ execute JavaScript expression in the user's browser and get the value of the exprssion

• set_env ➪ configure the environment of the current session 

#### Read more on session functions: https://pywebio.readthedocs.io/en/latest/session.html
_____________________________________________________________________________________________ 
## Page Welcome

First, using pywebio.session, we set the title of the page. 
Then, using pywebio.output, we created a popup that welcomes the user. We indicated that a user click on a button will close the popup. 

```python
# Configuring environment: title of page 
set_env(title = "Intersectionality in Film and Television")

# Welcome popup that closes with click 
popup('Welcome to ~Lights, Camera, Python~ :)', [
    put_button('Find something to watch!', onclick = close_popup)
])
```
_____________________________________________________________________________________________ 
## User Input

Then, we created a list of keywords. Using pywebio.input (input_group), we asked for the user to select from these keywords, and to select how they would like to rank the results (using radio buttons). These selections are saved in "interests_selection"

```python
# Keywords that user can select from 
KEYWORDS = ['Select','activism', 'african-american', 'aging', 'asian-american', 'bisexual',
             'childhood', 'childhood-trauma', 'class-differences', 'college', 'coming-of-age',
             'disability', 'education', 'europe', 'experimental-film', 'gay', 'gay-parent',
             'high-school', 'hispanic', 'homelessness', 'immigrant', 'independent-film', 
             'indigenous', 'lesbian', 'lgbtq', 'mental-health', 'midlife-crisis',
             'old-age', 'parenthood', 'poverty', 'sexual-orientation', 'student-film',
             'transgender', 'wealth']

# User keyword selection and "rank-by" selection
interests_selection = input_group('What are your interests?', [
                            select(label = 'Choose A Keyword', options = KEYWORDS, name = 'FirstKeyword'),
                            select(label = 'Choose A Second Keyword (Optional)', options = KEYWORDS, name = 'SecondKeyword'),
                            radio(label = 'Rank Results By', options = ['Most Popular', 'Highest Rated', 'Year of Release'], name = 'RankBy')
                            ])

```
_____________________________________________________________________________________________ 
## Save Keywords 

Next, we used list comprehension to get only (valid) user inputted keywords from "interests_selection" and stored them in *keywords*. Then we turned *keywords* into a dataframe that could be converted to a csv file called "keywords.csv"

```python
# Save keywords into csv file disregarding "select" as a keyword and "rank-by" choice
keywords = list(interests_selection.values())[:2]
keywords = ([key for key in keywords if key != "Select"])
df = pd.DataFrame(keywords, columns = ["column"])
df.to_csv("keywords.csv", index=False)
```
_____________________________________________________________________________________________
## Loading Screen

Using pywebio.output, we displayed a "process bar", and an image of a cat watching movies. We displayed text to go along with the image. Then, we created a function called *show_msg* that displays some additional text. We have a popup message appear, and when the user clicks on it, *show_msg* is called. 

```python
# Loading bar 
put_processbar('bar')
for i in range(1, 11):
    set_processbar('bar', i / 10)
    time.sleep(0.1)

# Display Monsieur Mittens 
put_text("Monsieur Mittens is making your watchlist!").style('color: black; font-family: "Free Mono"')   
put_image(open('Cat-Movie.png', 'rb').read())

# Message to show when user clicks on Monsieur Mittens message pop-up 
def show_msg():
    put_text('"am working v hard 2 make!"').style('color: black; font-family: "Free Mono"')  

# Monsieur Mittens message pop-up 
toast("Message from Monsieur Mittens", position = "right", duration=0, onclick=show_msg)
```
_____________________________________________________________________________________________

## Web Scraper

The code for the entire webscraper is as follows:

```python
import scrapy
import pandas as pd
import csv

file = open("keywords.csv", 'r')
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
file = open("keywords.csv", 'r')
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

We now start with the class `MoviesSpider` which will run all the methods we need to perform the required tasks. The `name` field specifies how this spider will be called in the terminal for when we want to run it. Additionally, depending on the number of keywords supplied by the user, the `start_url` is amended accordingly which will be the starting point for our webscraper to start its scraping. The list `names` will be used to collect the all the titles that our scraper collects.

### `parse` function

We then begin with defining the `parse` function.

```python
for movie in response.css("div.lister-item.mode-detail"):

    name = movie.css("div.lister-item-content").css("a::text").get()
    if name in names:
        break
    else:
        names.append(name)
    rating = movie.css("div.lister-item-content").css("strong::text").get()
    certificate = movie.css("div.lister-item-content").css("span.certificate::text").get()
    year = movie.css("div.lister-item-content").css("span.lister-item-year.text-muted.unbold::text").get()
```
In the above code block, the webpage is returned in the form of a `response` after runnning `scrapy shell` on it and we can access the various CSS elements of this webpage using `response.css`.

We can access the name of the movie/TV show using `div.lister-item-content` and then followed by `.css("a::text").get()` to get the text associated.

A similar format is followed to get `rating`, `certificate`, and `year`.

```python
if len(year) == 6:
      year = year[1:-1]
  else:
      if year[1] == "I":
          year = year[-5:-1]
      else:
          year = year[1:-1]
  year = year[:4]
```

The above part is primarily used to reformat the string we get for `year` into a more understandable and comprehensible format by removing unneccessary characters.

```python
if self.num < max_titles:

  yield {
      "Name" : name,
      "Rating" : rating,
      "Year" : year,
      "Certification" : certificate
            }

self.num += 1
```

The above part of our code makes the scraper yield a dictionary containing all the information about the TV show/movie. The `if` condition `self.num < max.titles` ensures that only the top 20 results are displayed.

```python
if len(response.css("a.lister-page-next.next-page")) != 0:

  next_page = response.css("a.lister-page-next.next-page").attrib["href"]

    if next_page:
        next_page = response.urljoin(next_page)

        yield scrapy.Request(next_page, callback = self.parse)
```

This part checks if there are multiple webpages containing titles that are relevant to the keywords selected by the user, which is checked by the `if len(response.css("a.lister-page-next.next-page")) != 0:` condition and if so, then the scraper yields `scrapy.Request` and calls back the `self.parse` function over again to run on the next webpage.
_____________________________________________________________________________________________
## Image Scraping
Our project scrapes moves and shows from IMDB. However, an IMDB page that we want to scrape from can have results on multiple "next" pages. To get the links of all the pages, we used the following imports:

#### import requests 
➪ Make a request to a webpage 

#### from bs4 import BeautifulSoup 
➪ A python library for pulling data out of HTML and XML files 

#### from urllib.parse import urljoin 
➪ Construct a full URL by combining a "base URL" with another URL 
_____________________________________________________________________________________________

A starter url is made based on the user inputted keywords. 

This link is saved to a list called *all_links*.

BeautifulSoup checks if the indicator for a *next* page is found on this link (*soup.find*), and if there is, it goes onto the next page and saves that link. This process is done until there are no more indicators that there is a *next* page. 

```python
with requests.Session() as session:
    
    # For saving links 
    all_links = []
    
    # Start on page 1 
    page_number = 1
    
    # Link formatting if there is only 1 keyword
    if len(keywords) == 1:
        url = "https://www.imdb.com/search/keyword/?keywords=" + keywords[0] + "&ref_=fn_kw_kw_1"
    
    # Link formatting if there are 2 keywords 
    if len(keywords) == 2:
        url = "https://www.imdb.com/search/keyword/?keywords=" + keywords[0] + "%2C" + keywords[1] + '&ref_=kw_ref_key&sort=moviemeter,asc&mode=detail&page=1'
    
    # Append url 
    while True:
        # Append url
        all_links.append(url)
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # check if there is next page, break if not
        next_link = soup.find("a", text="Next »")
        if next_link is None:
            break
        
        # Go onto next page
        url = urljoin(url, next_link["href"])
        page_number += 1
```
_____________________________________________________________________________________________

Next, we use the saved links to scrape the movie posters. 
We are again using BeautifulSoup, and we are also using 
_____________________________________________________________________________________________

#### from urllib.parse import urlopen
➪ Open the URL, which can be either a string or a Request object
_____________________________________________________________________________________________

BeautifulSoup looks for all objects in our saved links that match the tag *img*. If it has the attribute *loadlate* (which is for movie posters on imdb), then we save the image link in a list. 

```python
# For storing movie posters 
movie_posters = []

for link in all_links:
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
    
    # Til limit of 50 results 
    if len(movie_posters) < 50:
        # Find all images on link 
        images = bs.find_all('img')
        for img in images:
            # If it has the poster attribute, append 
            if img.has_attr('loadlate'):
                movie_posters.append(img['loadlate'])
```
______________________________________________________________________________________________
## Create results table and render images 
Next, we create a dataframe using the csv file created by our scraper. The links for the posters are added as a column to this dataframe. 
______________________________________________________________________________________________

If the user indicated "Most Popular", as their ranking choice: then we do nothing; the scraping naturally takes place in that order. 

If the user indicated "Highest rating" as their ranking choice: we short the dataframe values by the *Rating* column. 

If the user indicated "Year of Release" as their ranking choice: we short the dataframe values by the *Year* column. 
______________________________________________________________________________________________

For the following section we will need: 

### from IPython.core.display import HTML
______________________________________________________________________________________________

Using the function *path_to_image_html*, we convert the image links to html tags. 

Then, using df.to_html we render the dataframe as an HTMl table. 

*formatters = dict(Poster = path_to_image_html))* is what will allow us to convert the Poster column of image links into actual images. 

We finally save the dataframe as a webpage.

```python
# Create a dataframe using csv file
df = pd.read_csv('movies.csv')

# Assign posters list as new column of the dataframe
df.insert(0, 'Poster', movie_posters[:df.shape[0]])

# Rank dataframe by Highest rating if that was selected
if list(interests_selection.values())[-1] == 'Highest Rated':
    df = df.sort_values(by = ['Rating'], ascending = False)

# Rank dataframe by Year of Release if that was selected
if list(interests_selection.values())[-1] == 'Year of Release':
    df = df.sort_values(by = ['Year'], ascending = False)
    
#Converting links to html tags
def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'

#Rendering the dataframe as HTML table
df.to_html(escape=False, formatters=dict(Poster=path_to_image_html))

# Rendering the images in the dataframe using the HTML method.
HTML(df.to_html(escape=False,formatters=dict(Poster=path_to_image_html)))

# Saving the dataframe as a webpage
df.to_html('resultspage.html',escape=False, formatters=dict(Poster=path_to_image_html))
```
______________________________________________________________________________________________
## Display results

In this final section, we display the table using pywebio.output (put_html)!

```python
# Message stating that results shown are for the specified keywords 
put_text('"ah oui, here are you choices! enjoy!"').style('color: black; font-family: "Free Mono"') 
if len(keywords) == 1:
    put_text("Showing results for keyword" + keywords[0]).style('color: black; font-family: "Free Mono"') 

if len(keywords) == 2:
    put_text("Showing results for keywords " + keywords[0] + " and " + keywords[1] + ":").style('color: black; font-family: "Free Mono"') 

# Display table 
with open('resultspage.html', 'r') as f:
    html = f.read()
    put_html(html)

put_markdown(":D")
```

Last but not least, we delete the movies.csv file. 

```python
os.remove('movies.csv')
```
