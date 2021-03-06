#!/usr/bin/python
# Naive implementation
def editDist(a, b, dist):
    if a == b:
        return dist
    elif a == "":
        return dist + len(b)
    elif b == "":
        return dist + len(a)
    elif a[0] == b[0]:
        return editDist(a[1:], b[1:], dist)

    return min(editDist(a[1:], b, dist + 1), editDist(a, b[1:], dist + 1))


# Dynamic Programming
def hash(a, b):
    return a + "_" + b
memo = {}

def editDist_dp(a, b, dist):
    if a == b:
        memo[hash(a,b)] = dist
        return dist
    elif a == "":
        memo[hash(a,b)] = dist + len(b)
        return dist + len(b)
    elif b == "":
        memo[hash(a,b)] = dist + len(a)
        return dist + len(a)
    elif a[0] == b[0]:
        memo[hash(a,b)] = editDist_dp(a[1:], b[1:], dist)
        return memo[hash(a,b)]

    if hash(a, b) in memo:
        #print "used the memo for %s, %s = %d" % (a, b, memo[hash(a,b)])
        return memo[hash(a,b)]

    memo[hash(a,b)] = min(editDist_dp(a[1:], b, dist + 1), editDist_dp(a, b[1:], dist + 1))
    return memo[hash(a,b)]


# Testing
print "ab - a = %d (expecting 1)" % editDist_dp("ab", "a", 0)
print "ab - ca = %d (expecting 2)" % editDist_dp("ab", "ca", 0)
print "abc - bca = %d (expecting 2)" % editDist_dp("abc", "bca", 0)
print "abcd - bca = %d (expecting 3)" % editDist_dp("abcd", "bca", 0)
print "asdfasdf - asdf = %d (expecting 4)" % editDist_dp("asdfasdf", "asdf", 0)
print "asdfasdf - aaf = %d (expecting 5)" % editDist_dp("asdfasdf", "aaf", 0)
print editDist("asdghaca", "ahgakgjadfgkljb", 0)
