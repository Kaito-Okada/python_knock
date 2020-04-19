# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．


def getOddChar(x:str) -> str:
    return x[0::2]

def main():
    print('入力文字の奇数番目を抜き出します\n何か文字を入力してください:')
    str =input()
    print('結果:',getOddChar(str))

if __name__ == '__main__':
    main()