# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．


def revStr(x:str) -> str:

    y = x[-1::-1]

    return y

def main():
    print('文字列を入力:')
    str = input()

    print("逆順表示:")
    print(revStr(str))

if __name__ == '__main__':
    main()

