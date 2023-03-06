sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_list = set(sample_list)

print(type(sample_list))

sample_list.update(sample_set)
print(sample_list)