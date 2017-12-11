
# 연결 리스트 <> 배열 변환하기
#
# 연결 리스트 클래스 LinkedList와, 그 노드 클래스 Node가 주어졌습니다.
#
# 연결 리스트 객체가 주어졌을때 이를 배열로 변환해서 반환하는 함수 toArray와,
# 배열이 주어졌을때 이를 연결 리스트로 변환해서 반환하는 함수 toLinkedList를 구현 해 봅시다.
#
# 1. Node 는 정수 val만을 가진다고 가정합니다.
# 2. 입력으로 주어지는 배열과 연결 리스트는 항상 하나 이상의 값을 가진다고 가정합시다.

# 연결 리스트의 노드. 단일 연결 리스트의 경우입니다.
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

	def __str__(self):
		return str(self.val)


# 연결 리스트 클래스. head 와 tail을 가지고 있으며, 가장 뒤에 새로운 노드를 추가하는 addToEnd 함수가 있습니다.
class LinkedList:
	def __init__(self, node):
		self.head = node
		self.tail = node

	def addToEnd(self, node):
		self.tail.next = node
		self.tail = node

	def __str__(self):
		node = self.head
		toPrint = []
		while node:
			toPrint.append(str(node.val))
			node = node.next
		return "->".join(toPrint)


####################################################################################################################################

# 주어진 연결 리스트 ll을 배열로 변환해 봅시다.
# 이때 연결 리스트 LinkedList의 객체가 입력으로 주어진다고 가정합니다.
def toArray(ll):
	curNode = None
	curNode = ll.head
	# linkedlist를 다루기 위해서는 일단 node를 하나 만들어도됨
	# python은 아름다운 언어 : 데이터 타입 지정 필요없다

	lst = []
	while curNode is not None:
		lst.append(curNode.val)
		curNode = curNode.next

	return lst


# 주어진 배열을 연결 리스트로 변환 해 봅시다.
def toLinkedList(lst):
	ll = LinkedList(Node(lst[0]))
	for i in range(1, len(lst)):
		ll.addToEnd(Node(lst[i]))
	return ll


def example():
	## Linkedlist 클래스와 Node 클래스를 사용하는 예시입니다.
	ll = LinkedList(Node(3))
	ll.addToEnd(Node(4))
	ll.addToEnd(Node(8))
	print(ll)
	print(ll.head)
	print(ll.tail)


def main():
	# node1 = Node(3)
	# example()
	nums = [2, 8, 19, 37, 4, 5]
	ll = toLinkedList(nums)
	print(ll)
	lst = toArray(ll)


# print(lst)

if __name__ == "__main__":
	main()
