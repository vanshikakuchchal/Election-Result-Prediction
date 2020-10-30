# Election-Result-Prediction
In this project first I collected tweets of Delhi Election 2020 during the
time period of January and February date wise. And store all
the essential information that twitter will provide in a tweet
into a csv file.
We mainly focused on the text field , language field (in which
language tweet is tweeted) , geo coordinates (if present) and
its retweet details..
After dealing with above task created a python script to create a list of languages that are used in tweets.. The main
reason of creating the list of languages to count in how many
languages public can give their opinion and which language
is highly used. According to that list date wise separated
only tweets which are written in English because frequency
of English is very high as compare to other languages.
After separating all the tweets according to our need created
a python script to collect all the hashtags and mentions with
their frequency so that we can clearly identify what are the
trending hashtags and user mentions
Then manually created three lists, First list contain all the
hashtag and user mentions related to AAP, second for BJP
and third for INC. Now for the final opinion extraction and
converting opinions into vote separate tweets into 3 different sections. First section will contain only those tweets in
which keywords present related to AAP political party only.
In similar way second section will contain BJP tweets and
third section with INC tweets
Finally we converted all the positive opinions into votes using NLP for the election result prediction.
After successfully applying SVM with an accuracy of 82 percent , We converted all the positive opinions into votes for the
respective parties and plotted bar graphs to show on which
day which political party is on top
