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

Hiral created the web app that takes in user input (including desired keywords, and what the user would like to rank results by), and saved this information to a csv file that could be used by Arsh's scraper. She created the image scraper to get the links to the desired movies' posters and then created a dataframe that combines Arsh's scraped info with the image links. She wrote code that sorts the table based on the user-inputted "Rank-by" setting (either Highest Rated or Year of Release). She rendered the dataframe as an HTML table and rendered the images in the table. She displayed the results to the user.
