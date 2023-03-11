# def raqam(n, m):
#     n = input(">> ").split()
#     m = n
#
#     for i in range(len(m)):
#         if n[i] == "6":
#             m[i] = "9"
#         elif n[i] == "9":
#             m[i] = "6"
#     n.reverse()
#     if n == m:
#         print(True)
#     else:
#         print(False)
#
#
# s = input(">> ")
# n = []
# for i in range(len(s)):
#
#1
def Qalam(pen, con):
    for i in range(len(pen) - 1):
        if pen[i] == pen[i + 1]:
            print(pen[i] + "-" + pen[i + 1])
            con += 1
            print(con)
        return con


pattern = input(">> ").split()
count = 2 * len(pattern)
if count == 2:
    print(count)
else:
    print(Qalam(pattern, count))