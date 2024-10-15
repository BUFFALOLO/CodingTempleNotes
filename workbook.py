"""
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
     ]

def capitalize_words(reviews):
    keywords = ["good", "excellent", "bad", "Poor", "average"]
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        print(review)

capitalize_words(reviews)

split_reviews = [review.split(',') for review in reviews]
print(split_reviews)

def word_counter(split_reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    positive_count = 0
    negative_count = 0

    for words in split_reviews:
        if words in positive_words:
            positive_count += 1
        elif words in negative_words:
            negative_count += 1

    return positive_count, negative_count

postive_count, negative_count = word_counter(split_reviews)
print(f" There are {postive_count} postive words.")
print(f" There are {negative_count} negative words.")
"""


