
def get_questions():

	return [
["What color is the daytime sky on a clear day? ", "blue"],
["What is the answer to life, the universe and everything? ", "42"],
["What is a three letter word for mouse trap? ", "cat"],
["What color of the building near the mall? ", "Red"],
["What city is your favorite in Indonesia? ", "Bali"],
["What food is your favorite in Indonesia? ", "Indomie goreng"]

]


def main(questionBank):

	if len(questionBank) == 0:
		print("No questions were given.")
	else:
		index = 0
		right = 0
		while index < len(questionBank):
			# print(questuinBank[index])

			q = questionBank[index][0]
			a = questionBank[index][1]

			user_ans = input(q)
			if user_ans == a:
				print("Correct!")
				right += 1
			else:
				print(f"Incorrect!, correct was : {a}")

			index += 1
		print(f"your score is {right/len(questionBank)*100}")


main(get_questions())