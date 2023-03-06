import add
import search
import list_word
while True:
    print("\t##### Menu #####\n5\n1.Add New Word\n2.Search Word\n\tEn->Uz\n\tUz->En\n3.Update Word\n4.List Words\n5.exit")
    n = int(input("Please select the desired menu👉 "))
    if n == 1:
        add.inp()
    elif n == 2:
        search.search()
    elif n == 3:
        print("Yepsan🤪🤪🤪")
    elif n == 4:
        list_word.list_word()
    elif n == 5:
        print("Bye Bye👋")
        break
    else:
        print("++++++++++++++++++++")
        print("||Bunday Menu yo'q||")
        print("++++++++++++++++++++")

