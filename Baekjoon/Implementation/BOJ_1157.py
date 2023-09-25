#실수했던 거: 입력이 한 글자인 경우를 고려 안함

from collections import Counter

word = input()
word = word.lower()

freq_list = Counter(word).most_common()

#입력이 한 글자인 경우
if len(word) == 1:
    print(word.upper())
#가장 많은 빈도수의 문자가 2개 이상인 경우
elif freq_list[0][1] == freq_list[1][1]:
    print('?')
else:
    print(freq_list[0][0].upper())