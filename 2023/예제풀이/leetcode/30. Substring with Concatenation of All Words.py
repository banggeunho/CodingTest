import copy

def checkSubstring(wordCount, s, wordLen):
    # 잘라진 스트링을 단어 길이만큼 확인하면서 wordCount에 존재하는지 확인한다.
    for i in range(0, len(s), wordLen):
        w = s[i:i+wordLen]
        print(w)
        if w in wordCount:
            if wordCount[w] >= 1:
                wordCount[w] -= 1
            # wordCount에서 숫자가 1개 이상이 아닐경우
            else:
                return False
        # wordCount에 단어가 존재하지 않을 경우
        else:
            return False

    return True


words = []
for _ in range(2):
    words.append(input())

s = input()
result = []

wordLen = len(words[0])
sLen = len(s)
wordsWindow = len(words) * wordLen
wordCount = {}

# 단어 카운트 저장
for i in range(len(words)):
    if words[i] in wordCount:
        wordCount[words[i]] += 1
    else:
        wordCount[words[i]] = 1

# 스트링을 탐색하면서, 합쳐진 스트링 길이만큼 잘라서 확인한다.
i = 0
while (i + wordsWindow) <= sLen:
    print('--------')
    print(s[i:i+wordsWindow])
    tempWordCount = copy.deepcopy(wordCount)
    if checkSubstring(tempWordCount, s[i:i+wordsWindow], wordLen):
        result.append(i)

    i += 1

print(result)



# foo
# bar
# barfoothefoobarman