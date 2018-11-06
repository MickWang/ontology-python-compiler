#!/usr/bin/env python3
from ontology.builtins import print, range, len, list

x = 6
y = [9,8,7,6]
a = ["wo",2,3,4,5]
z = {a[1]:'hello', a[2]:'world', a[3]:x, a[4]:y}
# map in map
b = {a[1]:'hello', a[2]:'world', a[3]:x, a[4]:y, a[0]: z}

def main():
    c = b[2]
    d = b[3]
    e = b[4]
    f = b[5]
    g = b['wo']
    assert(c == 'hello')
    assert(d == 'world')
    assert(e == x)
    print(c)
    print(d)
    print(e)
    #print(f)
    for i in range(0,len(f)):
        assert(f[i] == y[i])
        print(i)

    assert(g[a[1]] == 'hello')
    assert(g[a[2]] == 'world')
    assert(g[a[3]] == x)
    print(g[a[1]])
    print(g[a[2]])
    print(g[a[3]])
    h = g[a[4]]
    for i in range(0,len(h)):
        assert(h[i] == y[i])
        print(i)
    print("all done")
