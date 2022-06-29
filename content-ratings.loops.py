ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+', '13+']

content_ratings = {}

content_ratings ['4+'] = 0
content_ratings ['9+'] = 0
content_ratings ['12+'] = 0
content_ratings ['17+'] = 0
content_ratings ['13+'] = 0

for element in ratings:

    if element in content_ratings: 
        content_ratings[element] += 1
    else:
        content_ratings[element] = 1
    
print (content_ratings)