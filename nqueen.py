def check(row, col):
	for i in range(n):
		if queen[i][col] == 1:
			return False
	for i in range(n):
		if queen[row][i] == 1:
			return False
	
	r = row-1
	c = col-1
	while(r>=0 and c>=0):
		if(queen[r][c] == 1):
			return False
		r -= 1
		c -= 1
	
	r = row-1
	c = col+1
	while(r>=0 and c<n):
		if(queen[r][c] == 1):
			return False
		r -= 1
		c += 1

	r = row+1
	c = col-1
	while(r<n and c>=0):
		if(queen[r][c] == 1):
			return False
		r += 1
		c -= 1

	r = row+1
	c = col+1
	while(r<n and c<n):
		if(queen[r][c] == 1):
			return False
		r += 1
		c += 1
	
	return True

def nqueen(n, row, speR, speC):
	if row == n:
		return True
	
	if row == speR:
		return nqueen(n , row+1, speR, speC)
	
	for col in range(n):
		if check(row, col):
			queen[row][col] = 1
			ans = nqueen(n, row+1, speR, speC)
			if ans:
				return True
			queen[row][col] = 0
			 

if __name__ == "__main__":
	n = int(input("Enter the value of n : "))
	queen = [[0 for _ in range(n)] for _ in range(n)]
	r = int(input("Row of 1st Queen placed : "))
	c = int(input("Col of 1st Queen placed : "))

	queen[r][c] = 1

	nqueen(n, 0, r, c)
	for row in queen:
		print(*row)