import copy
l = [1,2,3,4,5]
r = []
for i in xrange(len(l)):
    ll = copy.deepcopy(l)
    ll[i] = 'a'
    r.append(ll)
print r
