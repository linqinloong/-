"""""
import random
import string

code li = []
code li.append(random.choice(string.ascii_lowercase))
code li.append(random.choice(string.digits))
code li.append(random.choice(string.ascii_uppercase))
while len(code li < 6):
    code li.append(random.choice(string.ascii_letters+string.digits))

"""
import random
import string

code_li = []

code_li.append(random.choice(string.ascii_lowercase))
code_li.append(random.choice(string.digits))
code_li.append(random.choice(string.ascii_uppercase))
while len(code_li) < 6:
    code_li.append(random.choice(string.digits+string.ascii_lowercase+string.ascii_uppercase))
print(code_li)
q_code=''.join(code_li)
print(q_code)