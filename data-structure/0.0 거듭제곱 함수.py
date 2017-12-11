def pow(a, b):
	# edge case 적용
	# time complexity O(N)
	# if b < 0:
	# 	return 1.0/pow(a, -b)
	#
	# returnNumber = 1
	# for i in range(b):
	# 	returnNumber *= a
	# return returnNumber

	# recursion 을 아니?
	# time complexity 를 고려 했나?
	# edge case, 효율성 있는 코드를 짤 수 있는가?

	# time complexity O(logN)
	if b < 0:
		return 1.0 / pow(a, -b)
	if b == 0:
		return 1
	if b == 1:
		return a

	subPow = 0
	if b % 2 == 0:
		subPow = pow(a, b / 2)
		return subPow * subPow
	else:
		subPow = pow(a, ((b - 1) / 2))
		return a * subPow * subPow

	# if b%2 == 0:
	# 	return pow(a, b/2) * pow(a, b/2)
	# else:
	# 	return pow(a, ((b-1)/2)) * pow(a, ((b-1)/2)) * a
	# maximum => b가 짝순지 홀순지 구분해야함

print(pow(3, 5))

## b 가 음수라면? edge case
## math 라이브러리 사용 x
## retrun a**b 사용 x

# pow(a,N) = a * pow(a, N-1)
# pow(a,N) = pow(a, N/2) * pow(a,N/2)