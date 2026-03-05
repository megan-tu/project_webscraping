#!/usr/bin/python3

'''
# Lab: Analyzing Trump Tweets

In this lab, you will analyze all tweets sent by president Trump from 2009-2018.
You will get practice
1. loading datasets stored in JSON files,
2. creating plots in python, and
3. writing "fully open ended" code where I don't give you any starter code/doctests to guide you.

The data we will analyze is used to create the following two websites:
1. [An analysis of which types of tweets Trump is likely to send himself, versus which his staffers send.](http://varianceexplained.org/r/trump-tweets/)
2. [A search engine for all of Trump's tweets.](https://www.thetrumparchive.com/)

> **Note:**
> I am using Markdown formatting within this python docstring.
> This is a *very* common practice.
> Markdown (unlike HTML) is designed to be human readable in it's "uncompiled" form,
> and so programmers write markdown *everywhere*.

## Part 0: Setup Project

You will have to upload files to github to submit this lab.
Complete the following steps to setup your project.

1. Create a new github repo through the github interface.

2. Clone that project onto your computer.

3. Copy this `lab_tweets.py` file into your project folder.

## Part 1: Download the Data

The github repo <https://github.com/bpb27/trump_tweet_data_archive> contains an archive of tweets sent by Donald Trump.

1. Download these files `master_*.json.zip`, where * is a year.
    There should be 10 total files (2009-2018).

    > **Note:**
    > This particular archive stops in 2018 because the maintainer moved their codebase to <https://github.com/bpb27/tta-elastic>.
    > The newer archive has data that goes through the current year (and includes messages sent on Truth Social),
    > but it's a bit more complicated to access the data,
    > so we will use this older archive for this assignment.

2. Unzip these files into the project folder you created in Part 0 above.
    You should get a bunch of files that look like `master_*.json`.

## Part 2: Data Analysis

1. Modify this python file so that it:

    1. Opens each json file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.

    2. Prints the total number of tweets.

    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.

       > **NOTE:**
       > It's important to remember that each of these words can appear with many different capitalizations,
       > and your program should count the word no matter how it is capitalized.
       > For example, `OBAMA`, `obama`, and `ObAmA` all need to count as an occurrence of the word `Obama`.
       > Recall that the easiest way to do this is to use the .lower() function and in keyword.

    4. Prints out a count of each of these words.

        > **Hint:**
        > My program gives the following output:
        > ```
        > len(tweets)= 36307
        > counts= {'trump': 13924, 'obama': 2712 ... }
        > ```
        > You'll know your program is correct if you get the same numbers.

2. Select at least 3 more interesting words/phrases to count in trump's tweets,
    and modify your program to display those words.

3. Calculate the percentage of tweets that contain each word.  (Both your new words and Trump's original tweets.)

4. Display the results nicely in a markdown table.

    The display must have all words right justified and the percents printed with two
    significant figures (on both sides of the decimal) as shown in the example output below.

    ```
    | phrase            | percent of tweets |
    | ----------------- | ----------------- |
    |              daca | 00.17             |
    |         fake news | 00.92             |
    |  mainstream media | 00.06             |
    |            mexico | 00.55             |
    |             obama | 07.47             |
    |            russia | 01.13             |
    |             trump | 38.35             |
    |              wall | 00.91             |
    ```

    There are many ways to achieve this effect in python,
    but I recommend using python's f-string syntax.
    Here is a little cheat sheet using doctests:

    >>> name = "Alice"
    >>> f"{name:<10}"
    'Alice     '
    >>> f"{name:>10}"
    '     Alice'
    >>> f"{name:^10}"
    '  Alice   '
    >>> f"{name:*^10}"
    '**Alice***'

    >>> pi = 3.14159265
    >>> f"{pi:.2f}"
    '3.14'
    >>> f"{pi:.4f}"
    '3.1416'
    >>> f"{pi:8.2f}"
    '    3.14'
    >>> f"{pi:08.2f}"
    '00003.14'

5. Plot the results in a bar graph.

    > HINT:
    > The most common way to plot in python is with the matplotlib library.
    > We won't be covering how to use it in class in order to get you practice figuring things out by yourself.
    > You can find a tutorial here: <https://www.w3schools.com/python/matplotlib_bars.asp>.
    > You are also welcome to ask your favorite AI.

## Submission

Create a properly formatted markdown file `README.md` that contains:
1. the markdown table created by your program
2. the image created by your program
3. a short description (1 sentence is fine) for your table/image above

Ensure that you have uploaded to your github repo:
1. your modified python file
2. your python image

You do not need to pass any github actions for this submission.

Upload your github url to canvas.

## Extra Credit

There are two extra credit opportunities for this lab, worth one point each.

1. If you use the latest version of the data (instead of the files in the github repo) you will get +1 point.
    You can find instructions for accessing the data at <https://www.thetrumparchive.com/faq> under the question "Can I have the data?"

2. If you make a plot of other interesting information in this dataset (that doesn't use the 'text' key).
    For example, you could plot: what time of day does Trump tweet most often? or what state does Trump tweet from most often?
    If you add this to your repo you will get +1 point.
'''
import json
import zipfile

zip_paths = [
    'trump_tweet_data_archive/condensed_2009.json.zip',
    'trump_tweet_data_archive/condensed_2010.json.zip',
    'trump_tweet_data_archive/condensed_2011.json(1).zip',
    'trump_tweet_data_archive/condensed_2012.json(1).zip',
    'trump_tweet_data_archive/condensed_2013.json(1).zip',
    'trump_tweet_data_archive/condensed_2014.json(1).zip',
    'trump_tweet_data_archive/condensed_2015.json.zip',
    'trump_tweet_data_archive/condensed_2016.json.zip',
    'trump_tweet_data_archive/condensed_2017.json.zip',
    'trump_tweet_data_archive/condensed_2018.json.zip',
]
#import glob
tweets = []
for zip_path in zip_paths:
    with zipfile.ZipFile(zip_path, "r") as z:
        for file_name in z.namelist():
            with z.open(file_name) as f:
                for line in f:
                    text = line.decode("utf-8").strip()
                    tweets.extend(json.loads(text))

print("len(tweets)=", len(tweets))
#num_tweets = 0
#trump_tweets = 0
#for tweet in tweets:
    #if 'Trump' in tweet.get['text', ''].lower():
        #trump_tweets += 1
        #print(tweet['text'])
#print('num_tweets=', num_tweets)
#print('trump_tweets=', trump_tweets)

word_counts = { # keys are words, values are counts
    'obama': 0,
    'trump': 0,
    'mexico': 0,
    'russia': 0,
    'fake news': 0,
    'immigration': 0,
    'make america great again': 0,
    'tax': 0,
    'wall': 0,
}
for tweet in tweets:
    #for word in word_counts:
        #if word in tweet['text'].lower():
            #word_counts[word] += 1
    #if "text" in tweet:
        #print(type(tweet))
        #tweets.append(tweet["text"])
    #else:
        #tweets.append(tweet)
    tweet_text = tweet.get('text', '').lower()
    for word in word_counts:
        if word in word_counts:
            if word in tweet_text:
                word_counts[word] += 1
print("Word counts:")
for word, count in word_counts.items():
    print(f'{word}: {count}')

table = '| Phrase | Percent of tweets |\n'
table += '|-------:|-------------------|\n'

for word, count in word_counts.items():
    percentage = (count / len(tweets) * 100)
    table += f'| {word.title():>25} | {percentage:05.2f}% |\n'
#print("len(tweets) =", total)

import matplotlib.pyplot as plt
words = list(word_counts.keys())
counts = list(word_counts.values())
plt.figure(figsize=(8, 5))
plt.bar(words, counts)
plt.xlabel('Phrases')
plt.ylabel('Number of Tweets Containing Phrase')
plt.title('Phrase Mentions in Trump Tweets')
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
plt.show()
image_filename = 'trump_tweets.png'
plt.savefig(image_filename)
plt.close()

with open("README.md", 'w') as f:
    f.write('# Trump Tweet Phrase Analysis\n\n')
    f.write('## Phrase Frequency Table\n\n')
    f.write(table)
    f.write('\n\n')
    f.write('Bar Plot\n\n')
    f.write(f'![Phrase Counts]({trump_tweets.png})\n')
    f.write('This graph shows that "Trump" is by far the most tweeted phrase from 2009 to 2018.\n')