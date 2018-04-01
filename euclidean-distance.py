import json

# Item Recommender
# source: https://github.com/ai-society/ai-society.github.io
# ==============================================================================


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

def recommend(person, bound, similarity=euclidean_similarity):
	scores = [(similarity(person, other), other) for other in data if other != person]

	scores.sort()
	scores.reverse()
	scores = scores[0:bound]

	# print (scores)

	recomms = {}

	for sim, other in scores:
		ranked = data[other]

		for itm in ranked:
			if itm not in data[person]:
				weight = sim * ranked[itm]

				if itm in recomms:
					s, weights = recomms[itm]
					recomms[itm] = (s + sim, weights + [weight])
				else:
					recomms[itm] = (sim, [weight])

	for r in recomms:
		sim, item = recomms[r]
		recomms[r] = sum(item) / sim

	return recomms

print euclidean_similarity("Alan Perlis", "Marvin Minsky")
print recommend("Alan Perlis", 4)