# 세번째로 큰 숫자 찾아내기
#
# 0보다 큰 정수들의 배열이 주어졌다고 합시다. 이 배열에서 세번째로 큰 수를 찾아 내 봅시다.
#
# 예를 들어서, [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23] 가 입력으로 주어졌을 경우
# 가장 큰 수는 50, 두번째로 큰 수는 37, 세번째로 큰 수는 34입니다. 따라서 34를 반환해야 합니다.
#
# 시간 복잡도를 고려하면서 여러가지 방법으로 문제를 풀어 봅시다.


def thirdMax(nums):
	# O(NlogN)
	# nums.sort()
	# nums.reverse()
	#
	# return nums[2]


	# maxNum = max(nums)  #O(N)
	# nums.remove(maxNum) #O(N)
	#
	# maxNum = max(nums) #O(N)
	# nums.remove(maxNum) #O(N)
	#
	# return max(nums)

	#  해당 방법은 세 번째 큰수를 찾기 때문에 가능한 방법
	# k번째 큰 값을 찾을 때는 다른 자료구조를 사용해서 코드를 짜야한다
	maxNumbers = [0, 0, 0]
	for num in nums:
		if num > maxNumbers[2]:
			maxNumbers = [maxNumbers[1], maxNumbers[2], num]
		elif num > maxNumbers[1]:
			maxNumbers = [maxNumbers[1], num, maxNumbers[2]]
		elif num > maxNumbers[0]:
			maxNumbers = [num, maxNumbers[1], maxNumbers[2]]

	return maxNumbers[0]


def main():
	print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23]))  # should return 34


if __name__ == "__main__":
	main()
