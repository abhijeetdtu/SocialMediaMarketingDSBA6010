# Purpose
* Goal of this Repository is to make easier for people looking to do social media marketing.

# Repo Structure

* In ``` ./DataExtract/ ```
  There are scripts that help scrape Amazon Products

* ``` ./DataExtract/Data/ ``` has data that was used for the product and scraped from
  - Instagram
  - Twitter
  - Youtube
    - Data was extracted using free version of OctoParse

* Major outcomes are available under ``` ./Results/```

* All the scripts for Data Analysis in R are under ``` ./Scripts/ ```
  - These are markdown files and should be self explainatory


## R - Libraries used
  - SentimentAnalysis
    - For analysing sentiments of various tweets
  -  syuzhet
    - For emotion analysis
  - wordcloud
    - To get an overall sense of things happening
  - tm
    - The backbone text analytics package
  - treemap
    - For specific visualizations needed to view hierarchical information


## Key Take Aways
1.	Continuing with the story and the analysis
2.	Idea is to find what consumers want and why they want it
3.	Data collected
    a.	Hashtags tracked hairdye hairdo haircolor hairstyle
    b.	Around 10K pieces of content
4.	Interesting insights
  a.	Helped understand and have confidence in the recommendations
5.	First step sentiment / emotion analysis
  a.	Throw text at it and figure out whats going on
  b.	Positive stands out
  c.	Closely followed by negative – we will come to that
  d.	Then are joy and anticipation and trust
  e.	Once you drill down on the anticipation / trust and positive tweets a theme emerges
      i.	Impulsive
      ii.	When ?
      1.	Bored
      2.	Or adventure parks maybe Carowinds
      3.	Or Halloween ?
      4.	Or renaissance Fairs
      5.	Salary days ?
  f.	Drilling down on the content that was flagged as negative
      i.	Not feeling good about themselves
      ii.	Circumstances are overwhelming
      iii.	When ?
      1.	Exam season for students?
      2.	Job hunt? Advertise on linkedin ?
      3.	Listen to sad music on youtube/spotify ?
      a.	If after this horrible presentation I go home
      b.	And if I was loreal I would use it as an opportunity
6.	Marketing Analysis
  a.	Element of time
    i.	Won’t go into the details as its pretty obvious that
    ii.	When pressurized people make suboptimal decisions
  b.	Engagement
    i.	Asking people their opnion on social media , questions feedbacks comments
    ii.	A tried and tested way to keep people engaged
7.	Product Analysis
  a.	We see blonde brown black “traditional” colors are definitiely being talked about
  b.	But we also see these vibrant and bright colors like red,purple, orange , green show up
    i.	Corroborated by amazon
  1.	Company called raw has fewer people buying it compared to bigger brands but whoever is
    a.	They are buying bright colors
    b.	And they are very happy about it
8.	Pricing Analysis
  a.	Based of of amazon.
    i.	Data of about 70 products
  b.	Two price points emerge one is around 8.45 and another is around15.45
  c.	We see as price increases the number of ratings on a product decrease
    i.	I use number of ratings as an indicator of demand itself
    ii.	People are not buying products after 10-15 maybe its just cheaper or more efficient in time and money combined to go to a salon after that point
  d.	Right pricing is important not just for profit but to efficiently use the channel
    i.	IN this case amazon
