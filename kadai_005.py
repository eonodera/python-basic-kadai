#test1
age = 18
if age < 20 :
    #未成年の場合
    print("ジュースで乾杯")
else :
    print("お酒で乾杯")
    
#test2
print ("降水確率" + str(50) + "％")

#test3
user_name = "eijionodera"
print (user_name)

user_name = "kaitoonodera"
print (user_name)

#test4
number1 = 25
number2 = 12
print (number1 + number2)

last_name = "onodera"
first_name = "eiji"
dog_name = "kaito"
print (last_name + first_name)

#test5
#文字列の中に変数を組み込む時はfを先頭に追加する
print (f"私の名前は{first_name}{last_name}です。愛犬の名前は、{dog_name}{last_name}です。")

#test6
upper = 10
lower = 20
height = 5

menseki = ((upper + lower ) * height / 2)

print (f"{menseki}㎠")