
# 팩토리얼 계산하기
#
# 팩토리얼(!) 은 하나의 정수를 n을 입력받고 n X n-1 X n-2 X …. X 1 을 반환하는 연산자입니다.
#
# 예를 들어서, 5! = 5 X 4 X 3 X 2 X 1 = 120 입니다.
#
# 팩토리얼 연산자를 파이선 함수로 구현 해 봅시다. 재귀(recursion)방법과 반복(iteration)방법의 두 가지 다른 방법으로 구현 해 보도록 합시다.
#  • 1! = 1, 0! = 1 입니다.
#  •입력값은 0보다 크거나 같은 정수라고 가정합시다.

def factorial(num):

	# 재귀방식
	# if num == 0 or num == 1:
	# 	return 1
	# return num * factorial(num-1)


	if num == 0 or num == 1:
		return 1

	returnNumber = 1
	for i in range(1, num + 1):
		returnNumber *= i
	return returnNumber


def main():
	print(factorial(5))  # should return 120


if __name__ == "__main__":
	main()