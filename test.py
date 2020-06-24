from lxml import objectify
import lxml.etree

import pandas as pd

## Open General Tweets Train Tagged
try:
    general_tweets_corpus_train = pd.read_csv(r'C:\Users\Abraham Mena V\OneDrive\Professional Development\Proyectos\Programacion\Python\Twitter\NB_tuits\training_databases\general-tweets-train-tagged.xml',encoding = 'utf-8')
except:
    xml  = objectify.parse(open(r'C:\Users\Abraham Mena V\OneDrive\Professional Development\Proyectos\Programacion\Python\Twitter\NB_tuits\training_databases\general-tweets-train-tagged.xml', encoding='utf-8'))
    root = xml.getroot()
    general_tweets_corpus_train = pd.DataFrame(columns = ['content','polarity','agreement'])

    data = []
    tweets = root.getchildren()
    
    for i in range(len(tweets)):
        tweet = tweets[i]

        t = {}
        t['content'] = tweet.content.text
        
        data.append(t)
    
general_tweets_corpus_train = pd.DataFrame(data)