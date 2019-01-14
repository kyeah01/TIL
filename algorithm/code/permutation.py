def Baby_Gin(data):
    chk = 0
    for i1 in range(3):
        for i2 in range(3):
            if i1 != i2:
                for i3 in range(3):
                    if i1 != i2 and i2 != i3:
                        for i4 in range(3):
                            if i1 != i2 and i2 != i3 and i3 != i4:
                                for i5 in range(3):
                                    if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5:
                                        for i6 in range(3):
                                            if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6:
                                                if data[i1] == data[i2] and data[i2] == data[i3]:
                                                    chk += 1
                                                if data[i4] == data[i5] and data[i5] == data[i6]:
                                                    chk += 1
                                                if data[i4] == data[i5] and data[i5] == data[i6]:
                                                    chk += 1
                                                if data[i1]+1 == data[i2] and data[i2]+1 == data[i3]:
                                                    chk += 1
                                                if data[i4]+1 == data[i5] and data[i5]+1 == data[i6]:
                                                    chk += 1
                                                if chk == 2:
                                                    return 'Baby-Gin'
                                                else:
                                                    print(f'{data[i1]},{data[i2]},{data[i3]},{data[i4]},{data[i5]},{data[i6]}')

print(Baby_Gin([3,2,1,7,6,7]))