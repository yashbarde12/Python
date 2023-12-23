# Variable Datatypes
'''
Python provides several built-in data types:
    - Numeric Types: 
        1. Integers ( int )
        2. Floating-point numbers ( float )
        3. Complex numbers ( complex )
    - Sequence Types:
        1. Strings ( str )
        2. Lists ( list )
        3. Tuples ( tuple )
    - Mapping Type: 
        1. Dictionaries ( dict )
    - Set Types: 
        1. Sets ( set )
        2. Frozen sets ( frozenset )
    - Boolean Type: Boolean ( bool )
'''
#--------------------------------------------------------

a = 10
b = 20.5
c = 5+6j
d = 's'
e = "hello"
f = '''this is multi 
      line string'''
g = """" this is also
      multi line string"""
h = True
i = False

print(a, " ", type(a)) #10   <class 'int'>
print(b, " ", type(b)) #20.5   <class 'float'>
print(c, " ", type(c)) #(5+6j)   <class 'complex'>       
print(d, " ", type(d)) #s   <class 'str'>
print(e, " ", type(e)) #hello   <class 'str'>
print(f, " ", type(f)) #<class 'str'>
print(g, " ", type(g)) #<class 'str'>
print(h, " ", type(h)) #True   <class 'bool'>
print(i, " ", type(i)) #False   <class 'bool'>

j = [10,20]
k = (10,20)
m = {50,60}
n = frozenset({50,60})
p = {"name":"raj"}

print(j, " ", type(j)) #[10, 20]   <class 'list'>
print(k, " ", type(k)) #(10, 20)   <class 'tuple'>
print(m, " ", type(m)) #{50, 60}   <class 'set'>
print(n, " ", type(n)) #frozenset({50, 60})   <class 'frozenset'>
print(p, " ", type(p)) #{'name': 'raj'}   <class 'dict'>


#--------------------------------------------------------
#--------------------------------------------------------
