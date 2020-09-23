# Nathan Hunsberger - Change++ Appilcation
import requests
import random

# Use my unique twitter Bearer Token in header of GET request
auth_token='AAAAAAAAAAAAAAAAAAAAAEUIHwEAAAAACH%2BC9F4sZ5icEtqvSMnX13zg7TY%3DWHnMf5dkhkN0vSHS96iV9RWERjQVDPmcvUdPomX7xCrN8QWPUX'
hed = {'Authorization': 'Bearer ' + auth_token}

# Greet user
print("𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆: 𝕎ℍ𝕆 𝕋𝕎𝔼𝔼𝕋𝔼𝔻 𝕀𝕋?\n")
print("𝕎𝔼 𝕎𝕀𝕃𝕃 𝕊ℍ𝕆𝕎 𝕐𝕆𝕌 𝔸 𝕋𝕎𝔼𝔼𝕋 𝔽ℝ𝕆𝕄 𝔼𝕀𝕋ℍ𝔼ℝ 𝕂𝔸ℕ𝕐𝔼 𝕎𝔼𝕊𝕋 𝕆ℝ 𝔼𝕃𝕆ℕ 𝕄𝕌𝕊𝕂, 𝕐𝕆𝕌ℝ 𝕁𝕆𝔹 𝕀𝕊 𝕋𝕆 𝔾𝕌𝔼𝕊𝕊 𝕎ℍ𝕆 𝕋𝕎𝔼𝔼𝕋𝔼𝔻 𝕀𝕋\n")
print("𝟝 ℝ𝕆𝕌ℕ𝔻𝕊. 𝔾𝕆𝕆𝔻 𝕃𝕌ℂ𝕂!\n")

# Function which, given a Twitter username, retrieves the last 3200 tweets by that user, 
# no links, tags, comments, retweets, pictures
def getTweets(username):
    
    
    tweets = [] # List with only filtered tweets from desired user
    currentPage = [1] # Going to use this with while loop down below

    i = 0 # Going to use to keep track of pages for request
    
    # Let user know the tweets are loading 
    print("Loading...")
    # Loops as long as requests come back with tweets
    while len(currentPage) > 0:
    
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
    
# Get Kanyes's Tweets
kanyeTweets = getTweets('kanyewest')

# Get Elon's Tweets
elonTweets = getTweets('elonmusk')

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
    

# Using Elon and Kanye's Tweets, randomly chooses 1 tweet then prompts user to guess 
# who tweeted it, loops 5 times
def playGame(kanyeTweets, elonTweets):
   
    numRight = 0 # Keeps track of how many tweets user gets right
    
    print("𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆: 𝕎ℍ𝕆 𝕋𝕎𝔼𝔼𝕋𝔼𝔻 𝕀𝕋?")
    
    for _ in range(0,5):
        
        chooseUser = random.randint(0,1) # Pick Kanye or Elon
        
        tweets = [] 
        # Randomly Choose Kanye or Elon
        if chooseUser == 0:
            tweets = kanyeTweets
        else :
            tweets = elonTweets
        
        chooseTweet = random.randint(0,len(tweets)-1) # Depending on which public figure, pick a random tweet
        
        # Prompt user with tweet and ask them to guess
        print(f"Who Tweeted this? Elon or Kanye? (Enter 0 for Kanye or 1 for Elon) :\n{tweets[chooseTweet]}")
        userChoice = getUserInput('Kanye', 'Elon')
        
        # If user is right, increment numRight
        if userChoice == chooseUser:
            print("Correct!\n")
            numRight += 1
        
        # User is wrong
        else :
            if chooseUser == 0:
                print("Actually, Kanye tweeted that\n")
            else :
                print("Actually, Elon tweeted that\n")
                
    # Find percent user got right
    percentCorrect = numRight / 5 * 100
    # Show user their score
    print(f"You got {percentCorrect}% right! Play Again? (0 for yes 1 for no)")
    decision = getUserInput('yes', 'no')
    if decision == 0:
        # Run method again if user chooses to play again
        playGame(kanyeTweets, elonTweets)
    else:
        print("You probably wouldn't have done too hot anyways ;)")

# Run Game
playGame(kanyeTweets, elonTweets)


    

        
    
    
