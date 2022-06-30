ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}

for element in ratings:

    if element in content_ratings: 
        content_ratings[element] += 1
    else:
        content_ratings[element] = 1

print (content_ratings)