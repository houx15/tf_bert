# -*- coding: UTF-8 -*-
def sentence_cleaner(src_type, sentence):
    import re
    if src_type == "tweet":
        sentence = sentence.replace("\"", "")
        sentence = sentence.replace("RT", "")
        sentence = sentence.replace(".", "")
        sentence = sentence.replace("\'", "")
        results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:_%,-~]*', re.S)
        sentence = re.sub(results, '', sentence)
        sentence = re.sub('[\u4e00-\u9fa5]', '', sentence)
        # results2 = re.compile(r'[@].*?[ ]', re.S)
        # sentence = re.sub(results2, '', sentence)
        sentence = sentence.replace("\n", " ")
        sentence = sentence.strip()
        results2 = re.compile(r'[@].*?[ ]', re.S)
        sentence = re.sub(results2, '', sentence)
        return sentence
    if src_type == "weibo":
        sentence = sentence.replace("“", "")
        sentence = sentence.replace("”", "")
        sentence = sentence.replace("…", "")
        sentence = sentence.replace("点击链接查看更多->", "")
        results = re.compile(r'[a-zA-Z0-9.?/&=:_%,-~#《》。，：；“”‘’【】（） ]', re.S)
        # results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:_%,-~]*', re.S)
        sentence = re.sub(results, '', sentence)
        results2 = re.compile(r'[//@].*?[:]', re.S)
        sentence = re.sub(results2, '', sentence)
        sentence = sentence.replace("\n", " ")
        sentence = sentence.strip()
        return sentence
