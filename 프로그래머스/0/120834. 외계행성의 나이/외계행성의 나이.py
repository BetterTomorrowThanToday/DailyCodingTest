def solution(age):
    answer = ''
    
    charMap = ['a','b','c','d','e','f','g','h','i','j']
    age = str(age)
    for digit in age:
        answer += charMap[int(digit)]
    return answer