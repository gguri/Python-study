
# 스트리밍 데이터의 이동 평균
#
# 정수 데이터가 스트리밍으로 (한번에 하나씩) 주어진다고 합시다. 이때, 주어진 범위 만큼의 이동 평균을 구하는 클래스 MovingAvg를 만들어 봅시다.
#
# MovingAvg는 처음에 이동 평균의 범위를 입력받아서 초기화 되며, 매 정수 데이타가 입력되는 nextVal(num)함수는 이때까지의 이동 평균을 반환합니다.
#
# 예를 들어서, 2,8,19,37,4,5 의 순서로 데이터가 입력되고, 이동 평균의 범위는 3이라고 합시다. 이 경우 다음과 같이 MovingAvg가 사용 될 것입니다.
# ma = MovingAvg(3)
# print(ma.nextVal(2))
# 현재까지 입력된 값이 2밖에 없으므로, 2를 반환합니다.

import queue

# 1. 배열을 큐로 활용
# 시간 복잡도 : O(N)
# class MovingAvg():
#     def __init__(self, size):
#         self.size = size
#         self.lst = []
#
#     def nextVal(self, num):
#         self.lst.insert(0, num)
#         if len(self.lst) > self.size:
#             self.lst.pop()
#
#         return sum(self.lst) / len(self.lst)

# 2. 매번 sum() 해줄 필요 없이 시작, 끝의 갑을 뺴고 더해주는 sum 변수를 만듬
# class MovingAvg():
#     def __init__(self, size):
#         self.size = size
#         self.lst = []
#         self.sum = 0
#
#     def nextVal(self, num):
#         self.lst.insert(0, num)
#         self.sum += num
#         if len(self.lst) > self.size:
#             popNumber = self.lst.pop()
#             self.sum -= popNumber
#
#         return self.sum / len(self.lst)


# queue 라이브러리 사용
class MovingAvg():
	def __init__(self, size):
		self.size = size
		self.q = queue.Queue()
		self.sum = 0

	def nextVal(self, num):
		self.q.put(num)
		self.sum += num
		if self.q.qsize() > self.size:
			popNumber = self.q.get()
			self.sum -= popNumber

		return self.sum / self.q.qsize()


def queueExample():
	q = queue.Queue()
	q.put(5)
	q.put(9)
	print(q.qsize())
	print(q.get())
	print(q.qsize())
	print(q.get())


def main():
	queueExample()

	nums = [2, 8, 19, 37, 4, 5]
	ma = MovingAvg(3)
	results = []
	for num in nums:
		avg = ma.nextVal(num)
		results.append(avg)
	print(results)  # [2.0, 5.0, 9.666666666666666, 21.333333333333332, 20.0, 15.333333333333334]


if __name__ == "__main__":
	main()