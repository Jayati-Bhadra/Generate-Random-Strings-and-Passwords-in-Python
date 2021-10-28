import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

get_random_string(8)
get_random_string(6)
get_random_string(4)
import random
import string

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    print(result_str)

# string of length 8
get_random_string(8)
get_random_string(8)
import random

# Random string of length 5
result_str = ''.join((random.choice('abcdxyzpqr') for i in range(5)))
print(result_str)
# Output ryxay
import random
import string

for i in range(3):
    # get random string of length 6 without repeating letters
    result_str = ''.join(random.sample(string.ascii_lowercase, 8))
    print(result_str)
