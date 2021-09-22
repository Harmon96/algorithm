def solution(s):
    dic = {
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
    }
    
    result = ""
    temp = ""
    for string in s:
        if string.isdigit():    # 숫자 들어올때
            result += string
        else:   # 문자 들어올때
            temp += string
            if temp in dic.keys():
                result += dic[temp]
                temp =""
    
    answer = int(result)
    return answer
    
    # replace 사용한 성공코드
    # def solution(s):
    # words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    # for i in range(len(words)):
        # s = s.replace(words[i], str(i))

    # return int(s)
