단순구현 문제인데 한번꼬이면 실수 많아지는 대표유형
```python
def solution(msg):
    ans = []
    indices = [i for i in range(1,27)]
    words = [chr(i) for i in range(ord('A'),ord('Z')+1)] # 색인은 object 필요
    words_map = {k:v for k,v in zip(words,indices)}
    last_index = len(words)
    temp_msg = ""
    i = 0
    while i < len(msg):
        temp_msg += msg[i]
        if temp_msg in words_map : #
            i+=1 #일치하면 계속 가장 긴 단어를 찾는다.
        else:
            words_map[temp_msg] = last_index + 1
            last_index += 1
            ans.append(words_map[temp_msg[:-1]])
            temp_msg = '' # 초기화
    ans.append(words_map[temp_msg])
    return ans
```
