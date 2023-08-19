from class_asm3 import *
from func_loading import *
from func_checking import *
import json
import os


def main(param):
    # 1. Mo file hien thi danh sach nhan vien
    if int(param) == 1:
        print()
        print("Danh sách các nhân viên:")
        print("...")
        try:
            with open("json_NV.txt", "r", encoding="utf-8-sig") as read_info_NV:
                list_nv = json.load(read_info_NV)
                # print ra string theo dinh dang json cho de doc
                for nv in list_nv:
                    print("Mã số:", nv["Mã số"])
                    print("Mã bộ phận:", nv["Mã bộ phận"])
                    print("Chức vụ:", nv["Chức vụ"])
                    print("Họ và tên:", nv["Họ và tên"])
                    print("Hệ số lương:", nv["Hệ số lương"])
                    print("Số ngày làm việc:", nv["Số ngày làm việc"])
                    print("Hệ số hiệu quả:", nv["Hệ số hiệu quả"])
                    print("Thưởng:", nv["Thưởng"])
                    print("Số ngày đi muộn:", nv["Số ngày đi muộn"])
                    print("...")
        # Neu file chua ton tai (chua co thong tin nhan vien nao)
        except FileNotFoundError:
            print("Chưa có dữ liệu của bất cứ nhân viên nào...")
            # Tao file json hien thi nhan vien chua co thong tin
            create_data_nv()
            # Mo file vua ghi de lay du lieu ve hien thi ra man hinh
            with open("json_NV.txt", "r", encoding="utf-8-sig") as empty_info:
                list_nv = json.load(empty_info)
                for nv in list_nv:
                    print("Mã số:", nv["Mã số"])
                    print("Mã bộ phận:", nv["Mã bộ phận"])
                    print("Chức vụ:", nv["Chức vụ"])
                    print("Họ và tên:", nv["Họ và tên"])
                    print("Hệ số lương:", nv["Hệ số lương"])
                    print("Số ngày làm việc:", nv["Số ngày làm việc"])
                    print("Hệ số hiệu quả:", nv["Hệ số hiệu quả"])
                    print("Thưởng:", nv["Thưởng"])
                    print("Số ngày đi muộn:", nv["Số ngày đi muộn"])
                    print("...")
    # 2. Mo file hien thi danh sach bo phan
    elif int(param) == 2:
        print()
        print("Danh sách các bộ phận:")
        print("...")
        try:
            with open("json_BP.txt", "r", encoding="utf-8-sig") as read_info_BP:
                list_bp = json.load(read_info_BP)
                for bp in list_bp:
                    print("Mã bộ phận:", bp["Mã bộ phận"])
                    print("Thưởng bộ phận:", bp["Thưởng bộ phận"])
                    print("...")
        except FileNotFoundError:
            print("Chưa có dữ liệu của bất cứ bộ phận nào...")
            create_data_bp()
            with open("json_BP.txt", "r", encoding="utf-8-sig") as empty_info:
                list_bp = json.load(empty_info)
                for bp in list_bp:
                    print("Mã bộ phận:", bp["Mã bộ phận"])
                    print("Thưởng bộ phận:", bp["Thưởng bộ phận"])
                    print("...")
    # 3. Them nhan vien moi
    elif int(param) == 3:
        print()
        # Lay msnv da ton tai them vao list_msnv de kiem tra
        list_msnv = list()
        try:
            with open("json_NV.txt", "r", encoding="utf-8-sig") as read_info_NV:
                list_nv = json.load(read_info_NV)
                for i in list_nv:
                    list_msnv.append(i["Mã số"])
        except FileNotFoundError:
            create_data_nv()
            with open("json_NV.txt", "r", encoding="utf-8-sig") as read_info_NV:
                list_nv = json.load(read_info_NV)
                for i in list_nv:
                    list_msnv.append(i["Mã số"])
        # Lay mbp da ton tai them vao list_mbp de kiem tra
        list_mbp = list()
        try:
            with open("json_BP.txt", "r", encoding="utf-8-sig") as read_info_BP:
                list_bp = json.load(read_info_BP)
                for i in list_bp:
                    list_mbp.append(i["Mã bộ phận"])
        except FileNotFoundError:
            create_data_bp()
            with open("json_BP.txt", "r", encoding="utf-8-sig") as read_info_BP:
                list_bp = json.load(read_info_BP)
                for i in list_bp:
                    list_mbp.append(i["Mã bộ phận"])

        print("Thêm nhân viên mới ...")
        print("...")
        # Add msnv
        msnv = len_checking(input("Nhập mã số: "))
        for i in list_msnv:
            while str(msnv) == str(i):
                print("Mã nhân viên đã tồn tại!")
                msnv = len_checking(input("Nhập mã số: "))

        # Add mbp
        department = len_checking(input("Nhập mã bộ phận: "))
        tmp_department = 0
        if all(i != str(department) for i in list_mbp):
            print(any(i != str(department) for i in list_mbp))
            tmp_department = 1
        if tmp_department == 1:
            bonus_de = positive_checking(
                input("Nhập tiền thưởng của bộ phận mới tại đây: ")
            )
            template_bp = {
                "Mã bộ phận": str(department),
                "Thưởng bộ phận": string_standardize(bonus_de),
            }
            with open("json_BP.txt", "r", encoding="utf-8-sig") as read_info_BP:
                list_bp = json.load(read_info_BP)
            list_bp.append(template_bp)
            with open("json_BP.txt", "w", encoding="utf-8-sig") as write_info_BP:
                json.dump(list_bp, write_info_BP, indent=4, ensure_ascii=False)

        # Add chuc vu
        position = len_checking(input("Nhập chức vụ (NV / QL): "))
        while position != "NV" and position != "QL":
            print("Vui lòng nhập đúng chức vụ!")
            position = len_checking(input("Nhập chức vụ (NV / QL): "))

        # Add ho va ten
        name = len_checking(input("Nhập họ và tên: "))

        # Add he so luong
        salary_base = positive_checking(input("Nhập hệ số lương: "))

        # Add so ngay lam viec
        working_day = positive_checking(input("Nhập số ngày làm việc: "))

        # Add he so hieu qua
        working_performance = positive_checking(input("Nhập hệ số hiệu quả: "))

        # Add tien thuong
        bonus = positive_checking(input("Nhập thưởng: "))

        # Add so ngay di muon
        late_comming_day = positive_checking(input("Nhập số ngày đi muộn: "))

        template_nv = {
            "Mã số": str(msnv),
            "Mã bộ phận": str(department),
            "Chức vụ": str(position),
            "Họ và tên": str(name),
            "Hệ số lương": string_standardize(salary_base),
            "Số ngày làm việc": int(working_day),
            "Hệ số hiệu quả": float(working_performance),
            "Thưởng": string_standardize(bonus),
            "Số ngày đi muộn": int(late_comming_day),
        }
        with open("json_NV.txt", "r", encoding="utf-8-sig") as read_info_NV:
            list_nv = json.load(read_info_NV)
        list_nv.append(template_nv)
        with open("json_NV.txt", "w", encoding="utf-8-sig") as write_info_NV:
            json.dump(list_nv, write_info_NV, indent=4, ensure_ascii=False)
        print("...")
        print("Đã thêm nhân viên mới ...")
    # 4. Xoa nhan vien theo ID
    elif int(param) == 4:
        print()
        # Lay list id nhan vien tai file json_NV
        try:
            with open("json_NV.txt", "r", encoding="utf-8-sig") as del_info:
                list_nv = json.load(del_info)
        except FileNotFoundError:
            create_data_nv()
            with open("json_NV.txt", "r", encoding="utf-8-sig") as del_info:
                list_nv = json.load(del_info)

        # Kiem tra xem id nhan vien co ton tai hay khong
        check_id = list()
        for i in list_nv:
            check_id.append(i["Mã số"])
        del_id = len_checking(input("Nhập mã nhân viên muốn xóa: "))
        tmp_msnv = 0
        if all(str(i) != str(del_id) for i in check_id):
            tmp_msnv = 1
        while tmp_msnv == 1:
            print("Mã nhân viên không tồn tại!")
            print("Vui lòng chọn 1 trong các mã sau:", check_id)
            del_id = len_checking(input("Nhập mã nhân viên muốn xóa: "))
            if any(str(i) == str(del_id) for i in check_id):
                tmp_msnv = 0

        # Tao list moi sau khi xoa de ghi lai vao file json_NV
        after_del = list()
        for i in list_nv:
            if str(i["Mã số"]) != str(del_id):
                after_del.append(i)
        with open("json_NV.txt", "w", encoding="utf-8-sig") as new_info:
            json.dump(after_del, new_info, indent=4, ensure_ascii=False)
        print("Đã xóa thành công!")
        print("...")
    # 5. Xoa bo phan theo ID
    elif int(param) == 5:
        print()
        # Lay list ma bo phan tai file json_NV
        try:
            with open("json_NV.txt", "r", encoding="utf-8-sig") as del_info:
                list_nv = json.load(del_info)
        except FileNotFoundError:
            create_data_nv()
            with open("json_NV.txt", "r", encoding="utf-8-sig") as del_info:
                list_nv = json.load(del_info)
        check_nv = list()
        for i in list_nv:
            check_nv.append(i["Mã bộ phận"])

        # Lay list ma bo phan tai file json_BP
        try:
            with open("json_BP.txt", "r", encoding="utf-8-sig") as del_info:
                list_bp = json.load(del_info)
        except FileNotFoundError:
            create_data_bp()
            with open("json_BP.txt", "r", encoding="utf-8-sig") as del_info:
                list_bp = json.load(del_info)
        check_bp = list()
        for i in list_bp:
            check_bp.append(i["Mã bộ phận"])

        # Kiem tra xem mbp co ton tai hay khong, hoac ma bo phan do co nhan vien hay khong
        del_mbp = len_checking(input("Nhập mã bộ phận muốn xóa: "))
        tmp_bp = 0
        if all(str(i) != str(del_mbp) for i in check_bp):
            tmp_bp = 1
        while tmp_bp == 1:
            print("Mã bộ phận không tồn tại!")
            print("Vui lòng chọn 1 trong các mã sau: ", check_bp)
            del_mbp = len_checking(input("Nhập mã bộ phận muốn xóa: "))
            if any(str(i) == str(del_mbp) for i in check_bp):
                tmp_bp = 0
        tmp_nv = 0
        if any(str(i) == str(del_mbp) for i in check_nv):
            tmp_nv = 1
        while tmp_nv == 1:
            print("Bạn không thể xóa bộ phận đang có nhân viên!")
            print("Lưu ý chọn các mã không có trong danh sách này: ", check_nv)
            print("Vui lòng chọn 1 trong các mã sau: ", check_bp)
            del_mbp = len_checking(input("Nhập mã bộ phận muốn xóa: "))
            if all(str(i) != str(del_mbp) for i in check_nv):
                tmp_nv = 0

        # Tao list moi sau khi xoa de ghi lai vao file json_BP
        after_del = list()
        for i in list_bp:
            if str(i["Mã bộ phận"]) != str(del_mbp):
                after_del.append(i)
        with open("json_BP.txt", "w", encoding="utf-8-sig") as new_info:
            json.dump(after_del, new_info, indent=4, ensure_ascii=False)
        print("Đã xóa thành công!")
        print("...")
    # 6. Hien thi bang luong
    elif int(param) == 6:
        print()
        print("Bảng lương của nhân viên:")
        print("...")
        # Lay danh sach nhan vien
        try:
            with open("json_NV.txt", "r", encoding="utf-8-sig") as read_info_NV:
                list_nv = json.load(read_info_NV)
                for i in list_nv:
                    i.update({"Hệ số lương": return_number(i["Hệ số lương"])})
                    i.update({"Thưởng": return_number(i["Thưởng"])})
        except FileNotFoundError:
            print("Chưa có dữ liệu của bất cứ nhân viên nào...")
            create_data_nv()
            with open("json_NV.txt", "r", encoding="utf-8-sig") as empty_info:
                list_nv = json.load(empty_info)

        # Lay danh sach bo phan
        try:
            with open("json_BP.txt", "r", encoding="utf-8-sig") as read_info_BP:
                list_bp = json.load(read_info_BP)
                for i in list_bp:
                    i.update({"Thưởng bộ phận": return_number(i["Thưởng bộ phận"])})
        except FileNotFoundError:
            create_data_bp()
            with open("json_BP.txt", "r", encoding="utf-8-sig") as empty_info:
                list_bp = json.load(empty_info)

        list_employees = list()
        list_managers = list()
        for nv in list_nv:
            if nv["Chức vụ"] == "NV":
                list_employees.append(nv)
            if nv["Chức vụ"] == "QL":
                list_managers.append(nv)

        for e in list_employees:
            info_emp = list()
            for v in e.values():
                if v != "NV":
                    info_emp.append(v)
            nv = Employee.return_info(info_emp)
            Employee.check_department(nv, list_bp)
            salary_nv = Employee.salary_cal(nv)
            print("Mã số:", e["Mã số"])
            print("Thu nhập thực nhận:", string_standardize(salary_nv))
            print("...")

        for e in list_managers:
            info_man = list()
            for v in e.values():
                if v != "QL":
                    info_man.append(v)
            ql = Manager.return_info(info_man)
            Manager.check_department(ql, list_bp)
            salary_ql = Manager.salary_cal(ql)
            print("Mã số:", e["Mã số"])
            print("Thu nhập thực nhận:", string_standardize(salary_ql))
            print("...")
    # 7. Chinh sua thong tin nhan vien
    elif int(param) == 7:
        print()
        print("Chỉnh sửa nhân viên:")
        print("...")
        try:
            with open("json_NV.txt", "r", encoding="utf-8-sig") as read_info_NV:
                list_nv = json.load(read_info_NV)
        # Neu file chua ton tai (chua co thong tin nhan vien nao)
        except FileNotFoundError:
            print("Chưa có dữ liệu của bất cứ nhân viên nào...")
            # Tao file json hien thi nhan vien chua co thong tin
            create_data_nv()
            # Mo file vua ghi de lay du lieu ve hien thi ra man hinh
            with open("json_NV.txt", "r", encoding="utf-8-sig") as empty_info:
                list_nv = json.load(empty_info)

        list_msnv = list()
        for j in list_nv:
            list_msnv.append(j["Mã số"])
        modify_id = len_checking(input("Nhập mã nhân viên: "))
        tmp_msnv = 0
        if all(str(i) != str(modify_id) for i in list_msnv):
            tmp_msnv = 1
        while tmp_msnv == 1:
            print("Mã nhân viên không tồn tại!")
            modify_id = len_checking(input("Nhập mã nhân viên: "))
            if any(str(i) == str(modify_id) for i in list_msnv):
                tmp_msnv = 0

        tmp = list()
        for nv in list_nv:
            if str(nv["Mã số"]) == str(modify_id):
                tmp.append(nv)
        tmp[0].update(
            {
                "Họ và tên": modify_returning(
                    tmp[0]["Họ và tên"], input("Nhập họ và tên: ")
                )
            }
        )

        position = modify_returning(
            tmp[0]["Chức vụ"], input("Nhập chức vụ (NV / QL): ")
        )
        while position != "NV" and position != "QL":
            print("Vui lòng nhập đúng chức vụ!")
            position = modify_returning(
                tmp[0]["Chức vụ"], input("Nhập chức vụ (NV / QL): ")
            )
        tmp[0].update({"Chức vụ": position})

        tmp[0].update(
            {
                "Hệ số lương": int(
                    modify_checking(
                        modify_returning(
                            return_number(tmp[0]["Hệ số lương"]),
                            input("Nhập hệ số lương: "),
                        )
                    )
                )
            }
        )
        tmp[0].update(
            {
                "Số ngày làm việc": int(
                    modify_checking(
                        modify_returning(
                            tmp[0]["Số ngày làm việc"],
                            input("Nhập số ngày làm việc: "),
                        )
                    )
                )
            }
        )
        tmp[0].update(
            {
                "Hệ số hiệu quả": float(
                    modify_checking(
                        modify_returning(
                            tmp[0]["Hệ số hiệu quả"],
                            input("Nhập hệ số hiệu quả: "),
                        )
                    )
                )
            }
        )
        tmp[0].update(
            {
                "Thưởng": int(
                    modify_checking(
                        modify_returning(
                            return_number(tmp[0]["Thưởng"]), input("Nhập thưởng: ")
                        )
                    )
                )
            }
        )
        tmp[0].update(
            {
                "Số ngày đi muộn": int(
                    modify_checking(
                        modify_returning(
                            tmp[0]["Số ngày đi muộn"],
                            input("Nhập số ngày đi muộn: "),
                        )
                    )
                )
            }
        )

        for i in list_nv:
            if i["Mã số"] == tmp[0]["Mã số"]:
                i.update({"Chức vụ": tmp[0]["Chức vụ"]})
                i.update({"Họ và tên": tmp[0]["Họ và tên"]})
                i.update({"Hệ số lương": string_standardize(tmp[0]["Hệ số lương"])})
                i.update({"Số ngày làm việc": tmp[0]["Số ngày làm việc"]})
                i.update({"Hệ số hiệu quả": tmp[0]["Hệ số hiệu quả"]})
                i.update({"Thưởng": string_standardize(tmp[0]["Thưởng"])})
                i.update({"Số ngày đi muộn": tmp[0]["Số ngày đi muộn"]})
        with open("json_NV.txt", "w", encoding="utf-8-sig") as new_info:
            json.dump(list_nv, new_info, indent=4, ensure_ascii=False)
        print("Đã hoàn tất chỉnh sửa!")
        print("...")


if __name__ == "__main__":
    print("_____Loading Data_____")
    Common.list_penalty = parse_penalty()
    Common.list_taxs = parse_tax()
    print("_________Menu_________")
    print(
        "1. Hiển thị danh sách nhân viên.",
        "\n" "2. Hiển thị danh sách bộ phận.",
        "\n" "3. Thêm nhân viên mới.",
        "\n" "4. Xóa nhân viên theo ID.",
        "\n" "5. Xóa bộ phân theo ID.",
        "\n" "6. Hiển thị bảng lương.",
        "\n" "7. Chỉnh sửa nhân viên.",
        "\n" "8. Thoát.",
    )
    user_choice = checking_request(input("Mời bạn nhập chức năng mong muốn: "))
    if int(user_choice) == 8:
        print()
        print("________Program is closed________")
    while int(user_choice) != 8:
        main(user_choice)
        print("_________________________________")
        print()
        print("             ~ MENU ~")
        print(
            "1. Hiển thị danh sách nhân viên.",
            "\n" "2. Hiển thị danh sách bộ phận.",
            "\n" "3. Thêm nhân viên mới.",
            "\n" "4. Xóa nhân viên theo ID.",
            "\n" "5. Xóa bộ phân theo ID.",
            "\n" "6. Hiển thị bảng lương.",
            "\n" "7. Chỉnh sửa nhân viên.",
            "\n" "8. Thoát.",
        )
        print()
        user_choice = checking_request(input("Mời bạn nhập các chức năng khác: "))
        os.system("CLS")
        if int(user_choice) == 8:
            print()
            print("________Program is closed________")
