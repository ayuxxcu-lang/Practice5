import re

# 1. 'a' followed by zero or more 'b'
pattern1 = r"ab*"
print("1:", bool(re.fullmatch(pattern1, "abb")))

# 2. 'a' followed by 2 to 3 'b'
pattern2 = r"ab{2,3}"
print("2:", bool(re.fullmatch(pattern2, "abbb")))

# 3. lowercase letters joined with underscore
pattern3 = r"^[a-z]+_[a-z]+$"
print("3:", bool(re.fullmatch(pattern3, "hello_world")))

# 4. One uppercase followed by lowercase letters
pattern4 = r"[A-Z][a-z]+"
text4 = "Hello world MyName Python"
print("4:", re.findall(pattern4, text4))

# 5. 'a' followed by anything, ending in 'b'
pattern5 = r"a.*b"
print("5:", bool(re.fullmatch(pattern5, "a123b")))

# 6. Replace space, comma, dot with colon
text6 = "Hello, world. Python is fun"
result6 = re.sub(r"[ ,\.]", ":", text6)
print("6:", result6)

# 7. Snake case to Camel case
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

print("7:", snake_to_camel("hello_world_test"))

# 8. Split string at uppercase letters
text8 = "HelloWorldPython"
result8 = re.findall(r"[A-Z][^A-Z]*", text8)
print("8:", result8)

# 9. Insert spaces before capital letters
text9 = "HelloWorldPython"
result9 = re.sub(r"([A-Z])", r" \1", text9).strip()
print("9:", result9)

# 10. Camel case to Snake case
def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')

print("10:", camel_to_snake("helloWorldPython"))