# 숫자들의 배열이 주어지고 표적 숫자가 주어졌다고 합시다.
# 배열에 주어진 숫자들 중 두 개의 숫자를 더하면 표적 숫자가 되는데요,
# 이때 어떤 두 수를 더하면 표적숫자가 되는지 찾는 문제를 풀어 봅시다.
# 예를 들어서, [2, 8, 19, 37, 4, 5] 가 배열로 주어지고 12 가 표적으로 주어지면 8,4 를 찾아내시면 됩니다.
# 	•입력 배열에는 중복되는 수가 없습니다.
# 	•입력 배열에는 합해서 표적이 되는 어떤 두 수가 반드시 있습니다.
# 	•출력의 순서는 상관 없습니다. 위 예시의 경우, 8,4 와 4,8은 둘 다 정답으로 인정합니다.


def twoSum(nums, target):
	# checkNums = {num:1 for num in nums}
	# print(checkNums)
	checkNums = {}
	for i in range(len(nums)):
		firstNumber = nums[i]
		numberToFind = target - firstNumber
		if numberToFind in checkNums:
			return numberToFind, firstNumber
		else:
			checkNums[firstNumber] = 1


# but) 효율성의 문제. => 즉 오래 걸린다. (naive(나이브) 하다)
# 문제가 뭘까?
# 1. for 문을 한 개로 줄여라. => target - firstNumber
# 2. element in list 는 for 문 하나 만큼의 시간이 든다. => nums 리스트를 dictionary(hash map)로 변경해준다.
#
# 		for i in range(len(nums)):
# 	        firstNumber = nums[i]
# 	        for j in range(i+1, len(nums)):
# 	            secondNumber = nums[j]
# 	            if firstNumber + secondNumber == target:
# 	                return firstNumber, secondNumber

def main():
	print(twoSum([2, 8, 19, 37, 4, 5], 12))

if __name__ == "__main__":
	main()
