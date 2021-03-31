# Given an array of positive integers representing the values of coins in your possession,
# write a function that returns the minimum amount of change (the minimum sum of
# money) that you cannot create. The given coins can have any positive integer value and
# aren't necessarily unique (i.e., you can have multiple coins of the same value).
# For example, if you're given coins
# [1, 2, 5] , the minimum amount of change
# that you can't create is 4 . If you're given no coins, the minimum amount of change
# that you can't create is 1 .
# Sample Input:
# coins : [5, 7, 1, 1, 2, 3, 22]
# Sample Output:
# 20



def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
	count =0
	for coin in coins:
		if coin>count+1:
			return(count+1)
		else:
			count+=coin
	return(count+1)
