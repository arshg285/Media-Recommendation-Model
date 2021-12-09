# Intersectionality In Film

**PIC 16B Group Project:** Machine learning model that provides recommendations for films representing intersectional identities.

## Abstract

Diverse representation empowers viewers who share the same identity as the movie characters and the cast, as it reflects experiences that the viewers can sympathize with.

Accurate representation in media production includes not only having diverse set of cast shown on the big screen but also an equally heterogenous composure of the crew, cast production, and writers whose voices are echoed in the works we see.While the film and TV show industry have slowly included more variety in representations of identities in the starring roles, diverse representation is still sorely lacking and much of the representation that exists presently in the repertoire is far from being accurate.

Our model would allow users to input identities of interest and receive a list of best-rated film and TV shows reflecting those identities either through the story itself or the cast and the crew involved in its creation.

## Planned Deliverables

We are creating a webapp that will allow users to select from a certain criteria (input), such as Asian American, LGBTQ representation, etc., and receive a list of shows and films that are best-rated matches for that criteria (output). 

**Full success:** Full access for users to select the TV shows and movies that they would like to see based on the iMDB repository based on certain preferential characteristics of their choice. Basically, they select some parameters and get a list of recommendations as the output. They can choose what topics they would like and max length of film/episode 

**Partial success:** Code that showcases the pipeline needed to categorize TV shows and movies based on certain parameters that a user selects.

**Interface:** Web App

**How our product differs from IMDB's existing search engine tool?**

As great and powerful IMDB's current Advanced Title Search tool is, we observe that it only offers selection based on certain objective parameters spanning the general descripton of a movie such as genre, production company, etc. We don't see many options for users to filter their movie search based on more individualized or characteristic traits that make a movie such as LGBTQ or certain ethnic representation. This is exactly the area we look to address through our project and empower the audience to filer based on such preferences.

Additionally, it will be a priority for us to ensure that our model places an equal emphasis on small scale production houses or businesses that might not garner as much mainstream media attention as some of the more popular and well established companies out there so that these small businesses aren't at a disadvantage.

## Resources Required

We would be scraping our data from the Explore Keywords function on the IMDb website based on a list of keywords we have identified: https://www.imdb.com/search/keyword/

For instance, if a user selects "Asian American" as one of the criteria that they want to filter their movie results by, we will be scraping all 993 titles from this page with the keyword "Asian American" applied: https://www.imdb.com/search/keyword/?keywords=asian-american&ref_=fn_kw_kw_1

## Tools and Skills Required:

1. Database management
1. Data wrangling
1. Web scraping
1. User input/selection
1. Ranking model: That selects best results based on certain parameters
 
**Packages:** sqlite3, pandas, scikit-learn

## What We Will Learn

While working on this project, we will learn how to manipulate and manage various sources of data so that we can match necessary conditions. In terms of project management, we will also learn how to manage our time, define our goals clearly, distribute work equally, and maintain transparency with each other.

To elaborate on the more technical specifics, it will be our first time building and deploying a webapp using Python for which we identify the following two as the top resources:

1. Django: See if this open source Python framework could be helpful in creating our data-driven model on its own website
2. Flask: Explore this "easier to use" API to implement a web-based application through Python

Another component of our project would be GUI Programming to ensure our application has decent presentability from the user side. For that, we look to explore some open source GUI frameworks such as Kivy, WxPython, PyQt, etc depending on what works best.

A large part of this project revolves around data scraping on the web and hence building successful crawlers that are able to get us the information needed from relevant websites. On that end, we'll learn a lot more about working with HTML and how its used to create different type of webpages in addition to leveraging it to our benefit.

## Risks

1. Vague categorizations might make it challenging to associate a certain media production with a specific characteristic.
1. Additionally, it might be difficult to acquire data about certain movies or for certain characteristics that a user might select.

## Ethics

***1. What groups of people have the potential to benefit from the existence of our product?***

Minority groups would be able to readily and easily access a compilation of specific intersectional identities of their interest.

***2. What groups of people have the potential to be harmed from the existence of our product?***

Results have the potential of including inaccurate, stereotypical depiction of the identities, often reinforcing negative connotations and further the fostering of negative perceptions.

***3. Will the world become an overall better place because of the existence of our product? Describe at least 2 assumptions behind your answer.***

1. Seeing oneself accurately represented on screen has a net positive effect.
1. It is currently difficult to find films and shows that match specified identities.

## Tentative Timeline

**Two Weeks (Week 5):** Set up databases and tables for different movies and characteristics
**Four Weeks (Week 7):** Establish a pipeline to fetch results based on selected criteria
**Six Weeks (Week 9):** Model can make accurate recommendations to user based on selected parameters

*Thank you!*

*Hiral Kotecha, Arsh Gupta*

*Group Name: Lights, Camera, Python!!*
