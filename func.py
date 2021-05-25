# function 函式/功能 是用來收納程式碼的
# 寫一個function來判斷是不是閏年（二月會多一天的年），
# https://en.wikipedia.org/wiki/Leap_year#Algorithm Wikipedia的定義：
#  1.公元年分除以4不可整除，為平年。
#  2.公元年分除以4可整除但除以100不可整除，為閏年。
#  3.公元年分除以100可整除但除以400不可整除，為平年。
#  4.公元年分除以400可整除但除以3200不可整除，為閏年。
# 同學可以依照這個定義直接翻譯成程式碼。
# function應該要有一個參數讓使用者投入（傳遞進去）年份，
# function的回傳值(return)應該是布林值，如果是閏年就return True，不是就return False。
# 請把function命名為is_leap，這樣才可以執行測試。
# （P.S.&nbsp; is_leap&nbsp;就是"是不是閏年"的意思，所以function取的名符其實）

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return False
    elif year % 400 != 0:
        return False
    elif year % 3200 == 0:
        return False
    else:
        return True

y = int(input('請輸入西元年: '))
print('是否為閏年: ', is_leap(y))

    
