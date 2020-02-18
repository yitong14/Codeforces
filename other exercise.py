# 20190730
# strings

# 输入输出
'''
str = input();
print(str)
'''

# 01-anton and polyhedrons
'''
x = input();
x = int(x)
y = 0
for i in range(x):
    polyhedron = input()
    if polyhedron == 'Tetrahedron':
        y += 4
    elif polyhedron == 'Cube':
        y += 6
    elif polyhedron == 'Octahedron':
        y += 8
    elif polyhedron == 'Dodecahedron':
        y += 12
    else:
        y += 20
print(y)
'''

# 02-love A
'''
s = input();
numbers_a = s.count('a')
length = len(s)
numbers_a2 = 2 * numbers_a - 1
if length > numbers_a2:
    print(numbers_a2)
else:
    print(length)
'''

# 03-anton and danik
'''
n = input();
n = int(n)
s = input();
a = s.count("A")
d = s.count("D")
if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
'''

# 04-file name
'''
n = input();
n = int(n)
s = input();
y = 0
for i in range(100):
    if s.find("xxx") == -1:
        print(y)
        break
    else:
        s1 = list(s)
        del s1[s.find("xxx")]
        y += 1
        s = ''.join(s1)
'''

# 05-even substrings
'''
n = input();
n = int(n)
s = input();
y = 0;
for i in range(n):
    x = int(s[i])
    if x % 2 == 0:
        y += i+1
print(y)
'''


# class

# 01-binary search tree
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.v = val
        self.l = left
        self.r = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is None:
                node.l = Node(val)
            else:
                self._add(val, node.l)
        else:
            if node.r is None:
                node.r = Node(val)
            else:
                self._add(val, node.r)

    def printtree(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self._printtree(self.root)

    def _printtree(self, node):
        if node is not None:
            self._printtree(node.l)
            print(str(node.v), end=" ")
            self._printtree(node.r)


tree = Tree()
n = int(input())
for i in range(n):
    tree.add(int(input()))
tree.printtree()
'''

# 02-iterator
'''
class myrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration


m = int(input())
for i in myrange(m):
    print(i, end=' ')
'''

# 03-generator
'''
def anotherrange(n):
    i = 0
    while i < n:
        yield(i)
        i += 1


m = int(input())
for i in anotherrange(m):
    print(i, end=" ")
'''

# 20190808
# 复习class

# 01-binary search tree
'''
class Node:
    def __init__(self,val):
        self.v = val
        self.l = None
        self.r = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is None:
                node.l = Node(val)
            else:
                self._add(val, node.l)
        else:
            if node.r is None:
                node.r = Node(val)
            else:
                self._add(val, node.r)

    def printTree(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v), end=" ")
            self._printTree(node.r)


tree = Tree()
tree.printTree()
m = int(input())
for i in range(m):
    tree.add(int(input()))
tree.printTree()
'''

# 02-generator
'''
def myrange(n):
    i = 0
    while i < n:
        yield(i)
        i += 1


m = int(input())
for i in myrange(m):
    print(i, end=" ")
'''

# excercises
# 01 - stopwords
'''
artical = input().lower()
words = artical.split(' ')
variety = 0
allwords = []
for i in range(len(words)):
    if words[i] not in allwords:
        print(words[i])
        print(allwords)
        allwords.append(words[i])
        print(allwords)
        variety += 1
print(variety)
print(allwords)
'''