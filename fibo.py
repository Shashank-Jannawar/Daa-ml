class fibo:
	def __init__(self):
		self.step = 0
	def recursive(self, n):
		self.step += 1

		if n <= 1:
			return n
		else:
			return self.recursive(n-1)+self.recursive(n-2)
	def nonRecursive(self, n):
		arr = [0, 1]
		if n<2:
			return n
		else:
			for i in range(n-1):
				arr.append(arr[-1]+arr[-2])
			return arr[-1]

obj = fibo()
n = int(input("Enter the value of n : "))
print("Recursive : ", obj.recursive(n))
print("Step Count : ", obj.step)
print("Non-Recursive", obj.nonRecursive(n))