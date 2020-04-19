# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．


def count_char_num_list(string: str) -> 'return_list':

    # 文字列を受け取り,単語毎に分解,文字数をカウントする関数
    # Parameter
    #     string:str : カウントしたい文字列
    # Return
    #     list : 単語数を格納したリスト 

    result_list = []

    split_str = string.replace(',', "")
    split_str = split_str.replace('.', "")
    split_str = split_str.split(" ")

    for c in split_str:
        result_list.append(len(c)) 
    
    return result_list

def main():
    str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    result = count_char_num_list(str)

    print(result)

if __name__ == '__main__':
    main()