from keyword import iskeyword

def contains_keys(*args):
    is_a_key = False
    for arg in args:
        if iskeyword(arg):
            is_a_key = True
    return is_a_key


print(contains_keys("hello", "goodbye"))
print(contains_keys("def", "haha", "lol", "chickens are evil", 42))
print(contains_keys("four", "for", "if"))
print(contains_keys("blabla", "doggo", "crab", "anchor"))
print(contains_keys("grizzly", "ignore", "return", "False"))

