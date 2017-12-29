import json

#GLOBAL SETTINGS
BOOK_RATINGS = 'data.json'

data = json.load(open(BOOK_RATINGS))
print data["Alan Perlis"]["Systems programming"]

def euclidean_similarity(person1, person2):

	#find common ranked books
	common_ranked_items = [item for item in data[person1] \
		if item in data[person2]]

	#pair book rankings, each pair is the rating of person1 and person2, respectively
	rankings = [(data[person1][item], data[person2][item]) \
		for item in common_ranked_items]

	#calculate euclidean distance, X Y Z...
	distance = [pow(rank[0] - rank[1], 2) for rank in rankings]

	# similarity score
	return 1 / (1 + sum(distance))

print euclidean_similarity("Alan Perlis", "Marvin Minsky")