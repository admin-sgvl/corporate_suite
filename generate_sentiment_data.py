import pandas as pd
import random

def generate_sentiment_data():
    reviews = [
        "I love this product, it works perfectly!",
        "Absolute waste of money. Broke after two days.",
        "It's okay, does what it says but a bit expensive.",
        "The customer service was amazing and very helpful.",
        "Disappointed with the quality. Expected better.",
        "Fast shipping and great packaging. Highly recommend.",
        "The app crashes every time I try to log in. Fix it!",
        "Average experience, nothing special.",
        "Best purchase I've made this year!",
        "The interface is confusing and hard to navigate."
    ]
    
    data = {'ReviewText': [random.choice(reviews) for _ in range(200)]}
    df = pd.DataFrame(data)
    df.to_csv('customer_reviews.csv', index=False)
    print("✅ Created customer_reviews.csv")

if __name__ == "__main__":
    generate_sentiment_data()