# Kiem tra, dam bao nguoi dung lua chon dung chuc nang
def checking_request(param):
    while (not param.isnumeric()) or len(param) != 1 or (not 0 < int(param) <= 8):
        print("Oops!")
        print("Vui lòng nhập chính xác số thứ tự hiển thị trên màn hình!")
        param = input("Mời bạn nhập chức năng mong muốn: ")
    return int(param)


# Kiem tra thong tin co bi de trong hay khong
def len_checking(param):
    while len(str(param)) < 1:
        print("Bạn không được bỏ trống thông tin này!")
        param = input("Vui lòng nhập lại: ")
    return param


# Kiem tra thong tin trong, kiem tra so duong
def positive_checking(param):
    try:
        while len(str(param)) < 1:
            print("Bạn không được bỏ trống thông tin này!")
            param = input("Vui lòng nhập lại: ")
        while float(param) < 0:
            print("Bạn phải nhập một số dương!")
            param = input("Vui lòng nhập lại: ")
    except ValueError:
        while (
            (len(str(param)) < 1)
            or param.isalpha()
            or param.isalnum()
            or (float(param) < 0)
        ):
            print("Bạn cần nhập đúng định dạng!")
            param = input("Vui lòng nhập lại: ")
    if str(param)[-2 : len(str(param)) + 1] == ".0":
        param = str(param)[:-2]
    return param


# Chuan hoa chuoi so theo form
def string_standardize(param):
    list_tmp = list()
    for i in str(param):
        list_tmp.append(i)
    if 4 <= len(list_tmp) <= 6:
        list_tmp.insert(-3, ",")
    elif 7 <= len(list_tmp) <= 9:
        list_tmp.insert(-3, ",")
        list_tmp.insert(-7, ",")
    elif 10 <= len(list_tmp) <= 12:
        list_tmp.insert(-3, ",")
        list_tmp.insert(-7, ",")
        list_tmp.insert(-11, ",")
    string = ""
    for j in list_tmp:
        string += j
    string += " (VND)"
    return string


# Tra gia tri tien te duoc chuan hoa ve dang gia tri so
def return_number(param):
    list_tmp = str(param).split(",")

    def remove_vnd(last_index):
        num = last_index[:-6]
        return num

    list_tmp.insert(-1, remove_vnd(list_tmp[-1]))
    list_tmp.pop(-1)
    value = ""
    for i in list_tmp:
        value += i
    return int(value)


# Kiem tra dinh dang thong tin cua nhan vien duoc chinh sua
def modify_checking(param):
    try:
        while float(param) < 0:
            print("Bạn phải nhập một số dương!")
            param = input("Vui lòng nhập lại: ")
    except ValueError:
        while (
            (len(str(param)) < 1)
            or param.isalpha()
            or param.isalnum()
            or (float(param) < 0)
        ):
            print("Bạn cần nhập đúng định dạng!")
            param = input("Vui lòng nhập lại: ")
    if str(param)[-2 : len(str(param)) + 1] == ".0":
        param = str(param)[:-2]
    return param


# Tra ve gia tri ban dau neu enter khi chinh sua thong tin nhan vien
def modify_returning(old, new):
    if len(str(new)) < 1:
        return old
    else:
        return new
