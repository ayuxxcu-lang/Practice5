import re

# 1. Match 'a' followed by zero or more 'b'
pattern1 = r"ab*"
text1 = "abbb"
print("1:", re.fullmatch(pattern1, text1))


# 2. Match 'a' followed by two or three 'b'
pattern2 = r"ab{2,3}"
text2 = "abbb"
print("2:", re.fullmatch(pattern2, text2))


# 3. Find lowercase letters joined with underscore
pattern3 = r"[a-z]+_[a-z]+"
text3 = "hello_world test_string exampleTest"
print("3:", re.findall(pattern3, text3))


# 4. One uppercase letter followed by lowercase letters
pattern4 = r"[A-Z][a-z]+"
text4 = "Hello World Python Programming"
print("4:", re.findall(pattern4, text4))


# 5. 'a' followed by anything ending with 'b'
pattern5 = r"a.*b"
text5 = "axxxb"
print("5:", re.fullmatch(pattern5, text5))


# 6. Replace space, comma or dot with colon
text6 = "Hello, world. Python is fun"
result6 = re.sub(r"[ ,\.]", ":", text6)
print("6:", result6)


# 7. Convert snake_case to camelCase
def snake_to_camel(text):
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

print("7:", snake_to_camel("hello_world_python"))


# 8. Split string at uppercase letters
text8 = "HelloWorldPython"
result8 = re.findall(r"[A-Z][^A-Z]*", text8)
print("8:", result8)


# 9. Insert spaces between words starting with capital letters
text9 = "HelloWorldPython"
result9 = re.sub(r"([A-Z])", r" \1", text9).strip()
print("9:", result9)


# 10. Convert camelCase to snake_case
def camel_to_snake(text):
    result = re.sub(r'([A-Z])', r'_\1', text)
    return result.lower().lstrip('_')

print("10:", camel_to_snake("helloWorldPython"))