

# Map ---- map(fun, iter)
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 

result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 


# Lambda ---- lambda arguments : expression
x = lambda a, b : a * b
print(x(5, 6))


# Filter ---- filter(function, iterable)
letters = ['a', 'e', 'i', 'o', 'u']

def filterVowels(alphabet):
    return alphabet in ['a', 'e', 'i', 'o', 'u']

filteredVowels = filter(filterVowels, letters)
print(list(filteredVowels))


if __name__ == '__main__':
    symbols = '$¢£¥€¤'
    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(beyond_ascii)

