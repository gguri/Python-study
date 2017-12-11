# 0 이동시키기
#
# 여러개의 0과 양의 정수들이 섞여 있는 배열이 주어졌다고 합시다.
# 이 배열에서 0들은 전부 뒤로 빼내고, 나머지 숫자들의 순서는 그대로 유지한 배열을 반환하는 함수를 만들어 봅시다.
# 예를 들어서, [0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0] 가 입력으로 주어졌을 경우
# 			[8, 37, 4, 5, 50, 34, 0, 0, 0, 0, 0, 0] 을 반환하면 됩니다.
#
# 이 문제는 공간 복잡도를 고려하면서 풀어 보도록 합시다. 공간 복잡도 O(1)으로 이 문제를 풀 수 있을까요?

def ON1(nums):
	newNums = []  # O(N)
	newZeros = []  # O(N)
	for num in nums:
		if num == 0:
			newzeros.append(num)
		else:
			newNums.append(nums)

	return newNums + newZeros


def ON2(nums):
	index = 0
	newNums = [0 for _ in nums]  # O(N)
	# for num in nums 와 같이 안쓰는 변수를 받아줘야 할 경우
	# _ 사용함.
	for num in nums:
		if num != 0:
			newNums[index] = num
			index += 1
	return newNums


def moveZerosToEnd(nums):
	# 그렇다면? 같은 array에서 하면 되지 않을까?
	index = 0
	for i in range(len(nums)):
		num = nums[i]
		if num != 0:
			nums[index] = num
			nums[i] = 0
			index += 1

	return nums


def main():
	print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))


if __name__ == "__main__":
	main()
