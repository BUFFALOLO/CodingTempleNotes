def capitalize_words(reviews):
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
    for word in reviews:
        if word == 'good':
            reviews.append('GOOD')
        elif word == 'excellent':
            reviews.append('EXCELLENT')
        elif word == 'bad':
            reviews.append('BAD')
        elif word == 'poor':
            reviews.append('POOR')
        elif word == 'average':
            reviews.append('AVERAGE')
        else:
            reviews.append(word)
    return ''.join(reviews)

capitalize_words(reviews)