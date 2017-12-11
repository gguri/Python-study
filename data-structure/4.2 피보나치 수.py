
# 피보나치 수
#
# 피보나치 수열은 N 번째 수가 N-1번째 수와 N-2번째 수의 합인 수열입니다.
# 즉, F(0) = 0, F(1) = 1이며 그 이외의 모든 F(n) = F(n-1) + F(n-2) 입니다.
#
# 예를 들어서 피보나치 수열을 0~ 10번째까지 적어보면
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
#
# 와 같습니다.
#
# F(10) = F(9) + F(8) = 21 + 34 = 55 임을 확인 할 수 잇습니다.
#
# 0보다 크거나 같은 입력 정수 n이 주어졌을때 n번째 피보나치 수를 반환하는 함수를 구현 해 봅시다.
#
# 예를 들어서, 10이 입력으로 주어지면 55를 반환해야 합니다.
#
# 앞의 팩토리얼 문제와 마찬가지로 재귀 방법과 반복 방법으로 구현 해 보도록 합시다. 메모이제이션도 활용 해 보도록 합시다.

class Fib():
	def __init__(self):
		self.memo = {}

	def fibonacci(self, num):
		# 피보나치 수열은 반복문이 더 좋다.
		if num == 0:
			return 0
		if num == 1:
			return 1
		fibA = 0
		fibB = 1
		fibC = 1
		for i in range(2, num + 1):
			fibC = fibA + fibB
			fibA = fibB
			fibB = fibC

		return fibC

		# if num == 0:
		# 	return 0
		# if num == 1:
		# 	return 1
		#
		# # 이것과
		# if num in self.memo:
		# 	return self.memo[num]
		#
		# toReturn = self.fibonacci(num-2) + self.fibonacci(num-1)
		# self.memo[num] = toReturn
		# return toReturn
		#
		# # 이것은 같은 코드
		# if num not in sel.memo:
		# 	self.memo[num] = self.fibonacci(num-2) + self.fibonacci(num-1)
		#
		# return self.memo[num]


# toreturn 과 self.memo 안쓰면
# fib(10)
# -> fib(9)
#     -> fib(8)
#     -> fib(7)
# -> fib(8)
#     -> fib(7)
#     -> fib(6)
#     ... 계산이 계속 된다


# 메모이제이션 단점
# time complexity 는 줄어들지만 space complexity 가 늘어난다.


def main():
	f = Fib()
	print(f.fibonacci(10))  # should return 55


if __name__ == "__main__":
	main()