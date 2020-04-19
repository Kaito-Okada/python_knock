# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

def joint_char(string1:str ,string2:str, result:str = "") -> 'return_str':
    for tmp1,tmp2 in zip(string1,string2):
        result =  result + tmp1 + tmp2

    return result


def main():
    str1 = "パトカー"
    str2 = "タクシー"
    result = joint_char(str1,str2)

    print(result)


if __name__ == '__main__':
    main()