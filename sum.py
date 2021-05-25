# 寫一個function來算出清單中數字的總數
# function應該要有一個參數讓使用者投入（傳遞進去）一個清單，
# function應該回傳(return)清單中數字的總數。
# 預期結果：
# print(sum_of_list([1, 2, 3]))
# 應該要印出 6

def sum_of_list(num):    
    return sum(num)

print(sum_of_list([1, 2, 3]))