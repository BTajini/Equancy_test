print "-------------------------------------------------------"
print "P1 :"

print" Sum of all multiples of 3 or 5 below 1000 : ",(sum([i for i in range(1000) if i%3==0 or i%5==0]))
#or
print " Sum of all multiples of 3 or 5 below 1000 : ", (sum(i for i in range(1000) if i%3==0 or i%5==0))

print "-------------------------------------------------------"
print "P2 :"

text = "AAAAAAAAAAmBBBBBBBBCCCCCC DD E FFFF XXXXXXXXXXX"
d = {}
letters = set(text)
for l in letters:
    d[text.count(l)] = l

print "Occurences of the most common letter :" ,d[d.keys()[-1]], d.keys()[-1]

print "-------------------------------------------------------"
print "P3 :"


def get_products(list):
    if len(list) < 2:
        print('Error, must give at least 2 numbers')
    get_products = [None] * len(list)
    prod = 1
    i = 0
    while i < len(list):
        get_products[i] = prod
        prod *= list[i]
        i += 1
    prod = 1
    i = len(list) - 1
    while i >= 0:
        get_products[i] *= prod
        prod *= list[i]
        i -= 1
    return get_products

list = [1,5, 7, 9]
#from left to right [5 * 7 * 9,  1 * 7 * 9,  1 * 5 * 9,  1 * 5 * 7]
result = get_products(list)
print "list of our example :", list
print "result of our function : ", result

#in our case, we consider a worst case , then, the complexity of time is O(n) and complexity of space is : O(n).
# the algorithm is based on Greedy Approach

