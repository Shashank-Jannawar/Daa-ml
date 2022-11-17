def fractionalKnapsack(w, val, maxW):
	arr = []
	for i in range(len(w)):
		arr.append((w[i], val[i]))
	
	arr.sort(key=lambda x: x[1]/x[0], reverse=True)
	
	ans = 0
	for ele in arr:
		if ele[0]<maxW:
			ans += ele[1]
			maxW -= ele[0]
		else:
			ans += (ele[1]/ele[0]) * maxW
			break
	return ans
	

w = [10,20,30]
val = [60,100,120]
maxW = 50
print(fractionalKnapsack(w, val, maxW))