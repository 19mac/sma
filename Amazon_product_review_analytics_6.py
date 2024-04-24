import pandas as pd
from textblob import TextBlob

# Load the dataset from CSV file
df = pd.read_csv('/content/sample_data/AmazonReview (1).csv')

# Handle missing values in the 'Review' column
df['Review'].fillna('', inplace=True)

# Perform sentiment analysis on each review
sentiments = []
for review in df['Review']:
    sentiment_score = TextBlob(str(review)).sentiment.polarity
    if sentiment_score > 0:
        sentiment = 'Positive'
    elif sentiment_score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    sentiments.append(sentiment)

# Add sentiment analysis results to the DataFrame
df['Sentiment'] = sentiments

# Display the DataFrame with sentiment analysis results
print(df[['Review', 'Sentiment']])


positive_reviews = df[df['Sentiment'] == 'Positive']
# Display only the positive sentiment reviews
print(positive_reviews[['Review', 'Sentiment']])


neutral_reviews = df[df['Sentiment'] == 'Neutral']
print(neutral_reviews['Sentiment'])


negative_reviews = df[df['Sentiment'] == 'Negative']
print(negative_reviews['Sentiment'])