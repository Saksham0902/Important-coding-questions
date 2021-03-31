


def getNthFib(n):
    # Write your code here.
    lastTwo = [0,1]
	counter = 3
	while counter <= n:
		nextnum = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextnum
		counter+=1
	return lastTwo[1] if n>1 else lastTwo[0]


# def getNthFib(n,memoize = {1:0,2:1}):
#     # Write your code here.
#     if n in memoize:
# 		return memoize[n]
# 	else:
# 		memoize[n] = getNthFib(n-1,memoize) + getNthFib(n-2,memoize)
# 		return memoize[n]
