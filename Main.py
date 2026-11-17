
def main(nums: list):
	run = 0
	best = 0
	
	for i in range(len(nums)):
		if nums[i] == 1:
			run += 1
			best = max(best, run)
		elif nums[i] == 0:
			run = 0
	
	print(best)

if ___name__ == "__main__":
	main(input("please enter your masive: "))