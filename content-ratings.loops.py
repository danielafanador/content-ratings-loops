ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}

content_ratings ['4+'] = 0
content_ratings ['9+'] = 0
content_ratings ['12+'] = 0
content_ratings ['17+'] = 0

for element in ratings:

    if element == '4+': 
        content_ratings['4+'] += 1
    if element == '9+': 
        content_ratings['9+'] += 1
    if element == '12+': 
        content_ratings['12+'] += 1
    if element == '17+': 
        content_ratings['17+'] += 1
    #print (content_ratings)

#print (' ')
print (content_ratings)