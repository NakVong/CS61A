def remove(n, digit): # not digit
    kept, digits = 0, 0
    while n != 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept += last * 10 ** digits 
            digits += 1
    return kept

def inverse_cascade(n):
        grow(n // 10)
        print(n)
        shrink(n // 10)

def grow(n):
    if n < 10:
         print(n)
    else:
        grow(n // 10)
        print(n)

def shrink(n):
    if n < 10:
         print(n)
    else:
         print(n)
         shrink(n // 10)

def count_partitions(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif k == 0:
        return 0
    else:
        return count_partitions(n - k, k) + count_partitions(n, k - 1)
    
"""for _ in range(4):
    print("Go Bears!")""" # convention _ (not that it matters)
 
"""odd = [1, 3, 5, 7]
[x + 1 for x in odd if 25 % x == 0]""" # list comprehension

def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

numerals = {'I': 1, 'V': 5, 'X': 10} #access using numerals['I']
#numerals.values() list(numerals)
#{<key exp>: <value exp> for x in odd if 25 % x == 0} dictionary comprehension

def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which 
    match(k, v) is a true value
    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}

def sums(n, m):
    result = []
    for k in range(1, min(m + 1, n)):
        for rest in sums(n - k, m):
            if rest[0] != k:
                result.append([k] + rest)
    if n <= m:
        result.append([n])
    return result 

"""
    >>> a = [10]
    >>> b = a
    >>> a == b
    True
    >>> a.append(20)
    >>> a 
    [10, 20]
    >>> b
    [10 , 20]
    Needs to be different lists or it's considered a label for the same object (basically pointers)
"""

"""
    >>> a = [10, 20]
    >>> b = a
    >>> a is b ("is" checks same object instead of same value)
    True
    >>> c = [a, b]
    >>> c
    [[10, 20], [10, 20]]
    >>> c[0].append(30)
    >>> c 
    [[10, 20, 30], [10, 20, 30]]
    Again, pointing to the same object
"""

"""
    >>> s = [2, 7, [1, 8]]
    >>> t = s[2]
    >>> t.append([2])
    >>> e = s + t
    >>> t[2].append(8)
    >>> print(e)
"""

# manipulating return value vs passing value into recursive call
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    # return fact_times(n, 1)
    
def fact_times(n, k): # k is the sum of (k * n)!
    if n == 0:
        return k
    else:
        fact_times(n - 1, k * n)

s = (1, 2, 3) # tuple: immutable list

t = iter(s) # iterator: useful when you want to pass around and let others draw like a deck of cards

next(t) # goes to the next element in the iterator (or first if you are starting)

def double(x):
    return x * 2

any([True, True, False]) # return if any is True
all([True, True, False]) # return if all is True

t = map(double, range(5)) # iterator with function 
next(t)

x = all(map(print, range(-3, 3)))

"""def exclude(t, x):
    filtered_branches = map(lambda y: exclude(y, x), branches(t))
    bs = []
    for b in filtered_branches:
        if label(b) == x:
            bs.extend(branches(b)) # adds list to end of list
        else:
            bs.append(b)
    return tree(label(t), bs)"""

# Generators (iterators): can return multiple times instead of once
# Easy to pick what range instead of waiting for whole thing to return
def plus_minus(x): 
    yield x
    yield -x

"""
>>> t = plus_minus(3)
>>> next(t)
3
>>> next(t)
-3
>>> next(t)
<generator object plus_minus...>
"""

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)

a = {k: 'hi' for k in countdown(5)}

def park(n):
    if n < 0:
        return []
    elif n == 0:
        return ['']
    else:
        return (['%' + s for s in park(n - 1)] +
                ['.' + s for s in park(n - 1)] +
                ['<>' + s for s in park(n - 2)])
    """
    if n == 0:
        yield ''
    elif n > 0:
        for s in park(n - 1):
            yield '%' + s   
            yield '.' + s
        for s in park(n - 2):
            yield '<>' + s
    """
    
def f(x):
    return x - 1
def g(x):
    return 2 * x
def h(x, y):
    return int(str(x) + str(y))
def small(n):
    "Yield all small expressions with n calls"
    if n == 0:
        yield '5'
    else:
        for operand in small(n - 1):
            yield 'f(' + operand + ')'
            yield 'g(' + operand + ')'

    for k in range(n):
        for operand0 in small(k):
            for operand1 in small(n - k - 1):
                if eval(operand0) > 0 and eval(operand1) > 0:
                    yield 'h(' + operand0 + ', ' + operand1 + ')'


"""
def fastest_player(match, num_players, word_index):
    return min(range(num_players), key=lambda p: time(match, p, word_index))
"""

# Class
class Account: 
    # suite: block of code in the class
    # class attributes: attributes that are shared by all instances
    interest = 0.02
    # instance attributes: attributes that are specific to each instance
    def __init__(self, account_holder): # self refers to instance, everything else are parameters 
        self.balance = 0
        self.holder = account_holder

    # bound methods: a function that has its first parameter "self" bound to the instance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
    
    def deposit_check(self, check):
        if self.holder == check.payee:
            self.deposit(check.amount)
        else:
            return 'No way! This is not your check.'
    
    def split(self, percentage):
        original = self.balance
        self.balance = self.balance * (1 - percentage)
        return Account(self.holder)
        
    def am_i_rich(self):
        if self.balance > 20:
            return 'heck, yes'
        else:
            return 'heck, no'
class Check:
    def __init__(self, payee, amount):
        self.payee = payee
        self.amount = amount

"""
>>> a = Account('John)
>>> a.backup = Account('Jessica')
>>> a.backup.holder
'Jessica'
>>> a.holder
'John'
"""

"""
>>> type(Account.deposit)
<class 'function'>
>>> type(a.deposit)
<class 'method'>

>>> Account.deposit(a, 100)
100
>>> a.deposit(100)
200
"""

"""
>>> a = Account('John')
>>> b = Account('Tom')
>>> a.interest 
0.02
>>> b.interest
0.02
>>> Account.interest = 0.04
>>> a.interest
0.04
>>> b.interest
0.04
>>> a.interest = 0.08 # creates a new instance attribute
0.08
>>> b.interest
0.04
>>> Account.interest = 0.05
>>> a.interest
0.08
>>> b.interest
0.05
"""

# Inheritance
class CheckingAccount(Account): # superclass in parameter
    """A bank account that charges for withdrawals."""
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee) # redefining
        # return super().withdraw(amount + self.withdraw_fee)

# base class atrributes aren't copied into subclasses
"""
>>> ch = CheckingAccount('Tom) # Calls Account.__init__
>>> ch.interest # Found in CheckingAccount
0.01
>>> ch.deposit # Found in Account
20
>>> ch.withdraw(5) # Found in CheckingAccount
14
"""

# String Representation
class Bear:
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'oski the bear'
    
    def __repr__(self):
        return 'Bear()'
    
    def __str__(self): # when you print instance, something a human can read
        return 'a bear' # can also include atrributes. {self.size} when in ' '. Needs f'...' though.
    
"""
>>> oski = Bear()
>>> type(oski)
<class '__main__.Bear'>
>>> oski.__repr__
<function Bear.__init__.<locals>.<lambda> at 0x1025b40d0>
# Instance Attributes
>>> oski.__repr__()
'oski'
>>> oski.__str__()
'oski the bear'
# Class Atrributes
>>> type(oski).__repr__
<function Bear.__repr__ at 0x1025b0a60>
>>> type(oski).__repr__(oski)
'Bear()'
>>> type(oski).__str__
<function Bear.__str__ at 0x1025b0af0>
>>> type(oski).__str__(oski)
'a bear'
>>> print(oski)
a bear
>>> oski
Bear()
"""

class Mascot(Bear):
    how_great = 'Great'

# Composition

class Eye:
    def __init__(self, closed=False):
        self.closed = closed
        
    def draw_eye(self):
        if self.closed:
            return '-'
        else:
            return '.'
    
    def __str__(self):
        return self.draw_eye()

class Bear:
    def __init__(self):
        self.nose_and_mouth = 'ᴥ'

    def eye(self):
        return Eye()
    
    def __str__(self):
        return 'ʕ' + str(self.eye()) + self.nose_and_mouth + str(self.eye()) + 'ʔ'
    
class SleepyBear(Bear):
    def eye(self):
        return Eye(True)
    
class WinkingBear(Bear):
    def __init__(self):
        super().__init__() # can even use methods from superclass!
        self.eye_calls = 0

    def eye(self):
        self.eye_calls += 1
        return Eye(self.eye_calls % 2)
    
# Linked List

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def last(s):
    assert s is not Link.empty
    if s.rest is Link.empty:
        return s.first
    else:
        return last(s.rest)
    
def tens(s):
    def f(suffix, total):
        if total % 10 == 0:
            print(total)
        if suffix.rest is not Link.empty:
            f(suffix.rest, total + suffix.first)
        else:
            if (suffix.first + total) % 10 == 0:
                print(suffix.first + total)
    f(s.rest, s.first)

# Tree
def twins(t):
    count = 0
    n = len(t.branches)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if t.branches[i].label == t.branches[j].label:
                count += 1
    return count + sum([twins(b) for b in t.branches])

"""def remove(t, x):
    t.branches = exclude(t, x).branches
    return t"""
# t = Tree(t.label, [exclude(b, x) for b in t.branches]) creates a new tree
# only modify the original tree

class CallCounter:
    def __init__(self):
        self.n = 0

    def count(self, f):
        def counted_f(n):
            self.n += 1
            return f(n)
        return counted_f
    
# Memoization: remember results that have been computed before
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
    
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

"""
Common Orders of Growth
    Exponential growth: recursive calls
    Incrementing n multiplies time by a constant

    Quadratic growth: 
    Incrementing n increases time by n times a constant

    Linear growth:
    Incrementing n increases time by a constant

    Logarithmic growth:
    Doubling n only increments time by a constant

    Constant growth: 
    Incrementing n does not affect time
"""

def length(s):
    if s is Link.empty:
        return 0
    else:
        return 1 + length(s.rest)

def iter_length(s):
    k = 0
    while s is not Link.empty:
        s, k = s.rest, k + 1
    return k

def append(s, x):
    while s.rest is not Link.empty:
        s = s.rest
    s.rest = Link(x)

def iter_append(lst, x):
    if s.rest is not Link.empty:
        append(s.rest, x)
    else:
        s.rest = Link(x)

def pop(s, i):
    assert i > 0 and i < length(s)
    for x in range(i - 1):
        s = s.rest
    result = s.rest.first
    s.rest = s.rest.rest
    return result

def range_link(start, end):
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))
    
def iter_range_link(start, end):
    s = Link.empty
    k = end - 1
    while k >= start:
        s = Link(k, s)
        k -= 1
    return s

def another_range_link(start, end):
    if end <= start:
        return Link.empty
    else:
        head = Link(start)
        tail = head
        start += 1
        while start < end:
            tail.rest = Link(start)
            tail = tail.rest
            start += 1
        return head
    
# Scheme!

# Scheme programs consist of expressions (everything has a value):
# - Self-evaluating expressions:  2, 3.4, true
# - Symbols:                      + - quotient not and or
# - Call expressions:             (quotient 10 2), (not true)
# - Special forms:                (define (h n) (if (zero? n) 1 (* n (h (- n 1))))), (and (f 3) (f 4)) 
"""
scm> x
20
scm> 'x
x

scm> (define pi 3.14)
scm> (* pi 2)
6.28

scm> (define (f x) (+ 1 x))
f
scm> (f 3)
4
"""

# The value of a call expression is the value of the last body expression of the procedure. It needs () to call a function, otherwise, it just returns it.
"""
scm> (define (sum-squares x y)
        (+ (* x x) (* y y)))
"""

# Recursion is required to iterate. Usually most efficient way is to use 'if' on a symbol, instead of a call expression.
"""
a-plus-abs-b takes numbers a and b and returns a + abs(b) without calling abs.
scm> (define (a-plus-abs-b a b)
        ((if (< b 0) - +) a b)
"""

# Lambda expressions evaluate to anonymous procedures.
"""
scm> (define plus4 (lambda (x) (+ x 4)))
scm> ((lambda (x y z) (+ x y (square z))) 1 2 3)
"""

# cond is an if-elif-else statement in Python.
"""
scm> (cond ((> x 10) (print 'big))
           ((> x 5)  (print 'medium))
           (else     (print 'small)))

scm> (print
        (cond ((> x 10) 'big)
              ((> x 5)  'medium)
              (else     'small)))
"""

# begin: combines multiple expressions into one expression.
"""
scm> (cond ((> x 10) (begin (print 'big)   (print 'guy)))
        (else     (begin (print 'small) (print 'fry))))
"""

# let: binds symbols to values temporarily; just for one expression.
""" 
scm> (define c (let ((a 4)
                     (b (+ 2 2)))
                    (sqrt (+ (* a a) (* b b)))))
"""

# Scheme lists
# cons: two-argument procedure that creates a linked list
# car: procedure that returns that first element of a list
# cdr: procedure that returns the rest of a list
# nil: the empty list
"""
scm> (define x (cons 1 (cons 2 nil)))
x
scm> x
(1 2)
scm> car x
1
scm> cdr x
(2)
scm> ((car (cons + nil)) 2 3)
5
scm> (list 4 5 6 7)  values of the list
(4 5 6 7)
scm> (list 3 x)
(3 (1 2))
scm> (append x x)    only lists and estends
(1 2 1 2)
"""

# Return a list of two lists; the first n elements of s and the rest
"""
(define (split s n)
    ; The first n elements of s
    (define (prefix s n)
        (if (zero? n) nil (cons (car s) (prefix (cdr s) (- n 1)))))
    ; The elements after the first n
    (define (suffix s n)
        (if (zero? n) s (suffix (cdr s) (- n 1))))
    (list (prefix s n) (suffix s n)))
"""

# Symbolic Programming: referring to symbols directly
"""
scm> (list 'a 'b)
(a b)
scm> (list (quote a) (quote b))
(a b)
scm> (define x '(define x (+ 1 1)))
x
scm> (car x)
define
scm> (cdr (cdr x))
((+ 1 1))
scm> (car (car (cdr (cdr x))))
+
scm> (eval (car (car (cdr (cdr x)))))
#[+]
scm> ((eval (car (car (cdr (cdr x))))) 1 2)
3
"""

