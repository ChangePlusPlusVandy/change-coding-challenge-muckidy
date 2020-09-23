# Nathan Hunsberger - Change++ Appilcation
import requests
import random
import pandas
import sklearn.feature_extraction.text as sk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Use my unique twitter Bearer Token in header of GET request
auth_token='AAAAAAAAAAAAAAAAAAAAAEUIHwEAAAAACH%2BC9F4sZ5icEtqvSMnX13zg7TY%3DWHnMf5dkhkN0vSHS96iV9RWERjQVDPmcvUdPomX7xCrN8QWPUX'
hed = {'Authorization': 'Bearer ' + auth_token}

# Function which, given a Twitter username, retrieves the last 3200 tweets by that user, 
# no links, tags, comments, retweets, pictures

# Greet user
print("𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆: 𝕎ℍ𝕆 𝕋𝕎𝔼𝔼𝕋𝔼𝔻 𝕀𝕋? 𝔸𝕀 𝔼𝔻𝕀𝕋𝕀𝕆ℕ\n")
print("𝕎𝔼 𝕎𝕀𝕃𝕃 𝕊ℍ𝕆𝕎 𝕐𝕆𝕌 𝔸 𝕋𝕎𝔼𝔼𝕋 𝔽ℝ𝕆𝕄 𝔼𝕀𝕋ℍ𝔼ℝ 𝕂𝔸ℕ𝕐𝔼 𝕎𝔼𝕊𝕋 𝕆ℝ 𝔼𝕃𝕆ℕ 𝕄𝕌𝕊𝕂, 𝕐𝕆𝕌ℝ 𝕁𝕆𝔹 𝕀𝕊 𝕋𝕆 𝔾𝕌𝔼𝕊𝕊 𝕎ℍ𝕆 𝕋𝕎𝔼𝔼𝕋𝔼𝔻 𝕀𝕋\n")
print("𝔸𝕃𝕊𝕆, 𝕎𝔼 ℍ𝔸𝕍𝔼 𝔹𝕌𝕀𝕃𝕋 𝔸ℕ 𝔸𝕀 𝕋𝕆 𝔾𝕌𝔼𝕊𝕊 𝕎ℍ𝕆 𝕋𝕎𝔼𝔼𝕋𝔼𝔻 𝕀𝕋 𝕋𝕆𝕆. 𝕃𝔼𝕋'𝕊 𝕊𝔼𝔼 𝕎ℍ𝕆 𝕎𝕀ℕ𝕊!\n")
print("𝟝 ℝ𝕆𝕌ℕ𝔻𝕊. 𝔾𝕆𝕆𝔻 𝕃𝕌ℂ𝕂!")
def getTweets(username):
    
    tweets = [] # List with only filtered tweets from desired user
    currentPage = [1] # Going to use this with while loop down below

    i = 0 # Going to use to keep track of pages for request
    print("Loading...")
    # Loops as long as requests come back with tweets
    while len(currentPage) > 0:
        
        # Let user know tweets are loading
       
            
        # Make request
        responses = requests.get(f"https://api.twitter.com/1.1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&screen_name={username}&count=200&page={i}", headers=hed)
        responses = responses.json()
        
        # Loop through each tweet
        for response in responses:
            
            containsMedia = False # Will be used to check for media
            
            # Check for urls, quote tweets
            if response['entities']['urls'] == []:
                for key, _ in response['entities'].items():
                    
                    #Check for media
                    if key == 'media':
                        containsMedia = True
                if not containsMedia:
                    
                    #Check for Tags
                    if '@' in response['text']:
                        continue
                    else:
                        tweets.append(response['text'])
        
        # Updates the current page, if empty while loop will stop
        currentPage = responses
        
        # Increments to iterate through pages
        i += 1
    
    return tweets


# Used to validate that user input is either 0 or 1
def getUserInput(choice1, choice2):
    try: 
        userChoice = int(input())
        
        # Validates that user enters 0 or 1
        while (userChoice  != 0) and (userChoice != 1):
            
            print(f"{userChoice} is not a valid response. Please enter 0 for {choice1} or 1 for {choice2}:")
            userChoice = int(input())
        
    # User entered a letter
    except :
        print(f"Hey, I wanted a number. Try again. Please enter 0 for {choice1} or 1 for {choice2}:")
        userChoice = getUserInput()
    return userChoice   

# Get Kanyes's Tweets
kanyeTweets = getTweets('kanyewest')

# Get Elon's Tweets
elonTweets = getTweets('elonmusk')

# ******************* Begin Setup for Logistic Regression Model *******************
kanyes = ' '.join(kanyeTweets) # For the Tfidf - Long string of every Kanye Tweet connected by spaces
elons = ' '.join(elonTweets) # For the Tfidf - Lost string of every Elon Tweet connected by spaces
total = [kanyes, elons] 
vector = sk.TfidfVectorizer() # Create a Tfidf Vectorizer object - Used to compare importance of each word tweeted by Elon and Kanye
vector.fit(total)

kanyeTweets = zip(kanyeTweets, [0] * (len(kanyeTweets)-1)) # For the Regression model, makes a tuple connecting a 0 to each Kanye Tweet
kanyeTweets = [tweet for tweet in kanyeTweets] 
elonTweets = zip(elonTweets, [1] * (len(elonTweets)-1)) # For the Regression model, makes a tuple connecting a 1 to each Kanye Tweet
elonTweets = [tweet for tweet in elonTweets]
df = pandas.DataFrame(kanyeTweets + elonTweets, columns = ['Text', 'Target']) # DataFrame containing each tweet and their respective 1 or 0

# Make a dataframe specific to Kanye and Elon, will be used to send specifc tweet from each public figure to model
elonDF = pandas.DataFrame(elonTweets, columns = ['Text', 'Target'])
kanyeDF = pandas.DataFrame(kanyeTweets, columns = ['Text', 'Target'])

# For the model, split up the tweets into a training set used on the model
x = df['Text']
y = df['Target']
SEED = 50 #  For the train_test_split
x_train, _, y_train, _ = train_test_split(x, y, test_size=.06, random_state=SEED)

# Transform the words in the training set to Tfidf values
x_train_tfidf = vector.transform(x_train)

# Used to initialize Linear Regression model
def createAI():
    clf = LogisticRegression()
    clf.fit(x_train_tfidf, y_train)
    
    return clf

# Uses model to predict who tweeted a specific tweet, using the index and tfidf to find specific tweet
def makeGuess(model, tfidf, index):

    return model.predict(tfidf[index].reshape(1,-1))
"""
for y in y_validation:
    for x in x_validation_tfidf:
        #print(f'{y} is predicted to be {clf.predict(x.reshape(1,-1))}')
#print([x for x in zip(x_train, x_train_tfidf.data)])"""

def playGame(kanyeTweets, elonTweets):
    
    model = createAI() # Initialize new ai
    numRight = 0 # Keeps track of how many tweets user gets right
    aiRight = 0 # Keeps track of how many tweets ai gets right
    
    for _ in range(0,5):
        
        chooseUser = random.randint(0,1) # Pick Kanye or Elon
        
        tweets = [] 
        # Randomly Choose Kanye or Elon
        if chooseUser == 0:
            tweets = kanyeTweets
            tfidf = vector.transform(kanyeDF['Text']) # Transforms each Kanye tweet to tfidf values
        else :
            tweets = elonTweets
            tfidf = vector.transform(elonDF['Text']) # Tranforms each Elon tweet to tfidf values
        
        # Depending on which public figure, pick a random tweet
        chooseTweet = random.randint(0,len(tweets)-1) 
        
        # Prompt user with tweet and ask them to guess
        print(f"Who Tweeted this? Elon or Kanye? (Enter 0 for Kanye or 1 for Elon) :\n{tweets[chooseTweet][0]}")
        userChoice = getUserInput('Kanye', 'Elon')
        
        # Retrieve ai's guess for specific tweet
        aiGuess = makeGuess(model,tfidf,chooseTweet)
        
        # Tell user what the ai tweeted
        if aiGuess == 0:
            print("\nThe ai guesses: Kanye")
        else:
            print("\nThe ai guesses: Elon")
            
        # If ai is right, increment aiRight
        if aiGuess == chooseUser:
                aiRight += 1
                
        # If user is right, increment numRight
        if userChoice == chooseUser:
            print("You were Correct!\n")
            numRight += 1
            
        # User is wrong
        else :
            if chooseUser == 0:
                print("Actually, Kanye tweeted that\n")        
            else :
                print("Actually, Elon tweeted that\n")
                          
    # Find percent user and ai got right
    percentCorrect = numRight / 5 * 100
    aiPercentCorrect = aiRight / 5 * 100
    
    # Show user their score compared to ai, with funny comment :)
    print(f"You got {percentCorrect}% right! The ai got {aiPercentCorrect}% correct!")
    if numRight > aiRight:
        print("You beat the ai! Guess humans are superior... for now")
    elif aiRight == numRight:
        print("You tied the ai! Elon would be disappointed... in the ai")
    else:
        print("The ai beat you. Bow down to your technological master")
    
    # See if user wants to play again?
    print("\nPlay Again? (0 for yes 1 for no)")
    decision = getUserInput('yes', 'no')
    if decision == 0:
        # Run method again if user chooses to play again
        playGame(kanyeTweets, elonTweets)
    else:
        print("You probably wouldn't have done too hot anyways ;)")

# Run Game
playGame(kanyeTweets, elonTweets)