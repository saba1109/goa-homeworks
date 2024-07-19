#შევქმნათ ცარიელი სია, სიაში დავამატოთ, კიდევ 2 სია და გადავატაროთ for loop ში
main_list = []

list1 = [1, 2, 3]
list2 = [4, 5, 6]

main_list.append(list1)
main_list.append(list2)

for i in range(len(main_list)):
    sublist = main_list[i]
    print("Sublist", i + 1, ":", sublist)
