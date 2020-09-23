{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Thank you for reviewing my project! \
\
I decided to create two solutions to the task proposed, one is the generic solution to the exact question asked, and one utilizes machine learning to put a twist on the tweet-guessing game. In Tweet_Comparison_copy.py, you will find the \'93Who Tweeted it?\'94 game, where the user is shown a tweet from either Kanye West or Elon Musk, and must guess who tweeted what. But, in Tweet_Comparison_ai_copy.py, you will find that I used sci-kit learn to create a logistic regression model which plays along with the user, guessing who tweeted what on the same tweet the user is guessing. I ran into some trouble getting the model to train correctly, and found I got to be able to only be roughly 60% accurate for Musk\'92s tweets, and roughly 90% accurate for West\'92s tweets. I think this is due to West\'92s tweets being more unique (all caps, referencing \'91God\'92 and \'91Love\'92 a lot), as well as a lack of training data, as I had to filter tweets so I was only able to train the model on roughly 200 tweets. It\'92s not perfect, but I figured it\'92s a fun twist to the original game proposed, and I could certainly work to improve the model in the future. \
\
Thank you for your time!\
}