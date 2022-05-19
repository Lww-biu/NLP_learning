# %%
Dict = {
    "经常": 0.1,
    "经": 0.05,
    "有": 0.1,
    "常": 0.001,
    "有意见": 0.1,
    "歧": 0.001,
    "意见": 0.2,
    "分歧": 0.2,
    "见": 0.05,
    "意": 0.05,
    "见分歧": 0.05,
    "分": 0.1
}


def DAG(sentence):
    DAG = {}  # DAG空字典，用来构建DAG有向无环图
    N = len(sentence)
    for k in range(N):
        tmplist = []
        i = k
        frag = sentence[k]
        while i < N:
            if frag in Dict:
                tmplist.append(i)
            i += 1
            frag = sentence[k:i + 1]
        if not tmplist:
            tmplist.append(k)
        DAG[k] = tmplist
    return DAG


print(DAG("经常有意见分歧"))

# %%
sentence = "经常有意见分歧"
N = len(sentence)
route = {}
route[N] = (0, 0)
DAG = {0: [0, 1], 1: [1], 2: [2, 4], 3: [3, 4], 4: [4, 6], 5: [5, 6], 6: [6]}
for idx in range(N - 1, -1, -1):
    distance = (((Dict.get(sentence[idx:x + 1]) or 0) + route[x + 1][0], x)
                for x in DAG[idx])
    route[idx] = max(distance)
    # 列表推倒求最大概率对数路径
    # route[idx] = max([ (概率值，词语末字位置) for x in DAG[idx] ])
    # 以idx:(概率最大值，词语末字位置)键值对形式保存在route中)
    # route[x+1][0] 表示 词路径[x+1,N-1]的最大概率值,
    # [x+1][0]即表示取句子x+1位置对应元组(概率对数，词语末字位置)的概率对数
print(route)

# %%
x = 0
segs = []
while x < N:
    y = route[x][1] + 1
    word = sentence[x:y]
    segs.append(word)
    x = y
print(segs)
# %%
