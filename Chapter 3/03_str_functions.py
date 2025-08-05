# 1. lower() - Converts to lowercase
print("HELLO".lower())  # "hello"

# 2. upper() - Converts to uppercase
print("hello".upper())  # "HELLO"

# 3. strip() - Removes leading/trailing whitespace
print("  hello  ".strip())  # "hello"

# 4. replace(old, new) - Replaces all old with new
print("I like Java".replace("Java", "Python"))  # "I like Python"

# 5. split(sep) - Splits string into list by separator
print("a,b,c".split(","))  # ['a', 'b', 'c']

# 6. join(list) - Joins list into string with separator
print("-".join(['2025', '08', '05']))  # "2025-08-05"

# 7. find(sub) - Finds first index of substring or -1
print("hello world".find("world"))  # 6

# 8. startswith(prefix) - Checks if string starts with prefix
print("project.doc".startswith("pro"))  # True

# 9. endswith(suffix) - Checks if string ends with suffix
print("image.png".endswith(".png"))  # True

# 10. isdigit() - Checks if string is all digits
print("12345".isdigit())  # True

# 11. isalpha() - Checks if string is all letters
print("Python".isalpha())  # True

# 12. isalnum() - Checks if string is letters and/or digits
print("abc123".isalnum())  # True

# 13. capitalize() - Capitalizes first letter
print("hello world".capitalize())  # "Hello world"

# 14. title() - Capitalizes first letter of each word
print("hello world".title())  # "Hello World"

# 15. count(sub) - Counts how many times sub appears
print("banana".count("a"))  # 3
