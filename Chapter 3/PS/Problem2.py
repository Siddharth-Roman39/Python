# My Program
#----------------------------------------------
# name = input("Enter your name: ")

# date = input("Enter date YYYY/MM//DD: ")

# letter = f'''Dear {name},
# You are selected!
# {date}'''

# print(letter)

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>","Siddharth").replace("<|Date|>","2025/05/10"))