class Mylist:
    def __init__(self, my_list) -> None:
        self.my_list = my_list

    def delete_last_item(self):
        self.my_list = self.my_list[:-1]

    def __str__(self) -> str:
        return f"{self.my_list}"

    def append_item(self, ele):
        self.my_list.append(ele)

lst = [1, 2, 3, 4, 5]
lst2 = Mylist(lst)
lst2.append_item(6)
print(lst2)
lst2.delete_last_item()
print(lst2)
