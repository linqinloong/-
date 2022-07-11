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