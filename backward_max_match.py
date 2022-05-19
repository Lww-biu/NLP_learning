custom_dict = {'我们', '在', '在野', '生动', '野生', '动物园', '野生动物园', '物', '园', '玩'}
input_sentence = "我们在野生动物园玩"
max_word_len = 0
for word in custom_dict:
    if len(word) > max_word_len:
        max_word_len = len(word)

if len(input_sentence) < max_word_len:
    max_word_len = len(input_sentence)

end = len(input_sentence)
seg_results = []
while end > 0:
    temp_len = max_word_len
    if end < max_word_len:
        temp_len = end
    while temp_len > 0:
        sub_sentence = input_sentence[end - temp_len: end]
        if sub_sentence in custom_dict:
            seg_results.append(sub_sentence)
            end -= temp_len
            break
        else:
            temp_len -= 1
    # 没有子串匹配，则单独成词
    if temp_len == 0:
        sub_sentence = input_sentence[end - 1: end]
        seg_results.append(sub_sentence)
        end -= 1
print(seg_results)
