import math
wordlist = ['cat','dog','rabbit']

# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

answer_list = []

for word in wordlist:
    for char in word:
        if not char in answer_list:
            answer_list.append(char)
        else:
            continue

print(answer_list)
