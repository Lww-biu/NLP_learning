user_dict = ['我们', '在', '在野', '生动', '野生', '动物园', '野生动物园', '物', '园', '玩']
sentence = '我们在野生动物园玩'


def FMM(user_dict, sentence):
    result = []
    max_length = max([len(item) for item in user_dict])  # 5
    start = 0
    while start != len(sentence):
        index = start + max_length
        if index > len(sentence):
            index = len(sentence)
        for i in range(index, start, -1):
            if (sentence[start:i] in user_dict) or (len(sentence[start:i]) == 1):
                result.append(sentence[start:i])
                break
        start = i
    return result


def BMM(user_dict, sentence):
    result = []
    max_length = max([len(item) for item in user_dict])  # 5
    start = len(sentence)
    while start != 0:
        index = start - max_length
        if index < 0:
            index = 0
        for i in range(index, start):
            if (sentence[i:start] in user_dict) or (len(sentence[i:start]) == 1):
                result.append(sentence[i:start])
                break
        start = i
    return result


def Twoway_maximum_match(user_dict, sentence):
    FMM_ = FMM(user_dict, sentence)
    BMM_ = BMM(user_dict, sentence)
    if (len(FMM_)) != (len(BMM_)):
        if (len(FMM_)) <= (len(BMM_)):
            return FMM_
        else:
            return BMM_
    else:
        FMM_single = 0
        BMM_single = 0
        for i in range(len(FMM_)):
            if len(FMM_[i]) == 1:
                FMM_single += 1
        for j in range(len(BMM_)):
            if len(FMM_[i]) == 1:
                BMM_single += 1
        if FMM_single > BMM_single:
            return BMM_single
        else:
            return FMM_single


print(Twoway_maximum_match(user_dict, sentence))
