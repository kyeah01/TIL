# def find_same_name(Lists):
#     same_name = set()
#     for idx in range(len(Lists)):
#         if Lists[idx] in Lists[idx+1:]:
#             same_name.add(Lists[idx])
#     return same_name


# def find_same_name2(Lists):
#     same_name = set()
#     for i in range(len(Lists)):
#         for j in range(i+1, len(Lists)):
#             if Lists[i] == Lists[j]:
#                 same_name.add(Lists[i])
#     return same_name


# print(find_same_name(['Tom', 'same', 'same', 'betty', 'Tom']))
# print(find_same_name2(['Tom', 'same', 'same', 'betty', 'Tom']))

def zzak(Lists):
    result = []
    for i in range(len(Lists)):
        for j in range(i+1, len(Lists)):
            result.append([Lists[i], Lists[j]])
    return result

print(zzak(['T', 'A', 'B']))