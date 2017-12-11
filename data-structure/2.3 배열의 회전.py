# 배열의 회전

# 배열을 회전 시켜봅시다. 정수들이 포함되어 있는 배열과, 숫자 k가 입력으로 주어집니다. 이때 해당 배열을 k 만큼 회전 시켜 봅시다.
#
# 예를 들어서, [1, 2, 3, 4, 5, 6, 7, 8, 9] 와 4가 입력으로 주어졌을 경우 [6,7,8,9,1,2,3,4,5] 를 반환하면 됩니다.
#  • k 는 배열의 길이 n 보다 작다고 가정합시다.
#  • 다양한 방법으로 풀어 보도록 합시다.
#  • (추가) 공간 복잡도 O(1)으로 풀 수 있는 방법도 생각 해 봅시다. 이때 주어진 함수 partialReverse 를 활용해도 됩니다.

# 이 함수를 수정 해 주세요.
def rotateArray(nums, k):

	# 방법1
	# for i in range(len(nums)-k, len(nums)):
	# 	newNums.append(nums[i])
	#
	# for i in range(0, len(nums)-k):
	# 	newNums.append(nums[i])
	#
	# return newNums

	# 방법2
	# return nums[-k:] + nums[:-k]
	# 새로운 자료구조 생성
	# 방법1, 방법2 둘다 space complexity는 O(N)

	# 1,2,3,4,5,6,7,8,9
	# 9,8,7,6,5,4,3,2,1 (전체)
	# 6,7,8,9, 5,4,3,2,1 (0부터 k-1)
	# 6,7,8,9, 1,2,3,4,5 (k부터 끝까지)

	partialReverse(nums, 0, len(nums) - 1)
	partialReverse(nums, 0, k - 1)
	partialReverse(nums, k, len(nums) - 1)
	return nums


# 추가적인 공간 사용없이 배열을 돌려주는 함수
# 다음 함수는 추가적인 공간 사용 없이 배열의 일부를 뒤집어 주는 함수입니다.
# 예를 들어, nums = [1,2,3,4,5]
# partialReverse(nums, 1, 3)
# 을 실행 할 경우, nums = [1, 4, 3, 2, 5] 가 됩니다.
# 필요하다면 사용하세요.
def partialReverse(nums, start, end):
	for i in range(0, int((end - start) / 2) + 1):
		temp = nums[start + i]
		nums[start + i] = nums[end - i]
		nums[end - i] = temp


def main():
	# nums = [1,2,3,4,5]
	# partialReverse(nums, 1, 3) # [1, 4, 3, 2, 5] 를 반환합니다.
	# print(nums)
	print(rotateArray([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))


# [6,7,8,9,1,2,3,4,5] 를 반환해야 합니다.


if __name__ == "__main__":
	main()
