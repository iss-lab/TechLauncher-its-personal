from bottle import route, run, request, get, post
import feedparser
import random
import os
import spacy
import psycopg2

@get('/test')
def get_test():
    # Gives the 5 top stories from CNN, BBC, ABC, NYTimes, and Fox News to test article output
    # title, summary, link, published
    cnnRss = feedparser.parse("http://rss.cnn.com/rss/edition.rss")
    cnnEntries = cnnRss["entries"]
    bbcRss = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    bbcEntries = bbcRss["entries"] 
    abcRss = feedparser.parse("https://www.abc.net.au/news/feed/45910/rss.xml")
    abcEntries = abcRss["entries"] 
    nytimesRss = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    nytimesEntries = nytimesRss["entries"] 
    foxnewsRss = feedparser.parse("http://feeds.foxnews.com/foxnews/latest")
    foxnewsEntries = foxnewsRss["entries"] 
    myData = cnnEntries[:1] + bbcEntries[:1] + abcEntries[:1] + nytimesEntries[:1] + foxnewsEntries[:1]
    return {"data":myData}

@get('/random')
def get_random():
    # Get the combination of the top 5 stories from CNN, BBC, ABC, NYTimes, and Fox News
    # title, summary, link, published
    cnnRss = feedparser.parse("http://rss.cnn.com/rss/edition.rss")
    cnnEntries = cnnRss["entries"] 
    bbcRss = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    bbcEntries = bbcRss["entries"] 
    abcRss = feedparser.parse("https://www.abc.net.au/news/feed/45910/rss.xml")
    abcEntries = abcRss["entries"] 
    nytimesRss = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    nytimesEntries = nytimesRss["entries"] 
    foxnewsRss = feedparser.parse("http://feeds.foxnews.com/foxnews/latest")
    foxnewsEntries = foxnewsRss["entries"] 
    myData = cnnEntries[:5] + bbcEntries[:5] + abcEntries[:5] + nytimesEntries[:5] + foxnewsEntries[:5]
    
    # Get the current database values
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    sql = ("SELECT title FROM sports")
    cur.execute(sql)
    database = [row[0] for row in cur.fetchall()]
    conn.commit()
    cur.close()
    conn.close()
    
    # Remove the existing articles from the list of new top stories
    myData = [article for article in myData if article["title"] not in database]
    return {"data":random.choice(myData)}

@get('/sports')
def get_news_article():
    # Check articles until one passes the test for a certain topic, then return that article
    # title, summary, link, published
    cnnRss = feedparser.parse("http://rss.cnn.com/rss/edition.rss")
    cnnEntries = cnnRss["entries"] 
    bbcRss = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    bbcEntries = bbcRss["entries"] 
    abcRss = feedparser.parse("https://www.abc.net.au/news/feed/45910/rss.xml")
    abcEntries = abcRss["entries"] 
    nytimesRss = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    nytimesEntries = nytimesRss["entries"] 
    foxnewsRss = feedparser.parse("http://feeds.foxnews.com/foxnews/latest")
    foxnewsEntries = foxnewsRss["entries"] 
    nlp = spacy.load("training/model-best")
    entries = cnnEntries + bbcEntries + abcEntries + nytimesEntries + foxnewsEntries
    random.shuffle(entries)
    myData = []
    #print(len(entries))
    while len(myData) == 0:
        for entry in entries:
            test = nlp(entry['title'])
            #print(test.text)
            #print(test.cats['RELEVANT'])
            #print(test.cats['IRRELEVANT'])
            if test.cats['RELEVANT'] > 0.99:
                myData.append(entry)
                if len(myData) == 5:
                    break
            #print(f"The article has a relevant score of {test.cats['RELEVANT']}")
    return {"data":myData}

@get('/training/sports/<title>/<relevant>')
def get_training(title, relevant):
    # Add article to the training data database
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    sql = ("INSERT INTO sports (title, relevant)"
           "VALUES (%s, %s)")
    data = (title, relevant)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()
    return {"title":title, "relevant":relevant}

@get('/')
def get_ping():
    return("pong")

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='0.0.0.0', port=8090, debug=True)