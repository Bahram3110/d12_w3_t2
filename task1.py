# list_ = [[1, 2, 3], [4, 5, 6], [{'key': 'value'}, ], [7, 8, 9],
# [10, 11, 12]]
# print(list_)
# list_ = [[1, 2, 3], [4, 5, 6], [{'key': 'value'}, ], [7, 8, 9], [10,
# 11, 12]]
# new_list = []
# for i, x in enumerate(list_):
#     if type(x) == type([]):
#         for k in list_[i]:
#             if type(x) == type([]):
#                 for j in list_[i]:
#                     try:
#                         if type(j) != type([]):
#                             raise Exception("Error")
#                     except Exception:
#                         if j not in new_list and type(j) == type(2):
#                             new_list.append(j)

# print(new_list)

list_ = [[1, 2, 3], [4, 5, 6], [{'key': 'value'}, ], [7, 8, 9], [10,
11, 12]]

try:
    new_list = [x for y in list_ for x in y]
    new_list1 = [x for y in new_list for x in y]
except Exception:
    del new_list[6]
print(new_list)


