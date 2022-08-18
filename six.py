sides = (
(' ----- ', ' ----- ', ' ----- ', ' ----- ', ' ----- ', ' ----- '),
('|     |', '|    o|', '|    o|', '|o   o|', '|o   o|', '|o o o|'),
('|  o  |', '|     |', '|  o  |', '|     |', '|  o  |', '|     |'),
('|     |', '|o    |', '|o    |', '|o   o|', '|o   o|', '|o o o|'),
(' ----- ', ' ----- ', ' ----- ', ' ----- ', ' ----- ', ' ----- '))


def six_sided(numbers:list):
	for i in range(5):
		for num in numbers:
			print(sides[i][num-1], end='')
		print()


if __name__== "__main__":
	six_sided([1, 2, 3, 4, 5, 6])
