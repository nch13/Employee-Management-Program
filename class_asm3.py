# Bo phan
class Department:
    def __init__(self, mbp, tbp):
        self.mbp = mbp  # Ma bo phan
        self.tbp = tbp  # Thuong bo phan

    def full_infomation(self):
        return f"{self.mbp}, {self.tbp}"

    @classmethod
    def infomation(cls, lst):
        mbp, tbp = lst
        return cls(mbp, tbp)


# Nhan vien
class Employee:
    # Constructor
    def __init__(
        self,
        msnv,
        department,
        name,
        salary_base,
        working_day,
        working_performance,
        bonus,
        late_comming_day,
    ):
        self.msnv = msnv  # Ma so nhan vien
        self.de = department  # Ma bo phan
        self.name = name  # Ho va ten
        self.sb = salary_base  # He so luong co ban
        self.wd = working_day  # So ngay lam viec trong thang
        self.wp = working_performance  # He so hieu qua
        self.bonus = bonus  # Thuong ca nhan
        self.lcd = late_comming_day  # So ngay di tre
        # Khai bao gia tri ban dau cho cac property
        self.s_without_tax = 0  # Tong thu nhap chua thue
        self.s_official = 0  # Luong thuc nhan
        self.bonus_de = 0  # Thuong theo bo phan

    def print_info(self):
        return f"{self.msnv}, {self.de}, {self.name}, {self.sb}, {self.wd}, {self.wp}, {self.bonus}, {self.lcd}"

    @classmethod
    def return_info(cls, lst):
        msnv, de, name, sb, wd, wp, bonus, lcd = lst
        return cls(msnv, de, name, sb, wd, wp, bonus, lcd)

    # Tinh tien phat di tre
    def penalty_cal(self):
        for i in Common.list_penalty:
            # Neu nv khong di tre, return 0
            if self.lcd == 0:
                return 0
            try:
                if i["min"] < self.lcd <= i["max"]:
                    return self.lcd * i["value"]
            except KeyError:
                if i["min"] < self.lcd:
                    return self.lcd * i["value"]

    # Tinh tien thue phai dong
    def tax_cal(self):
        s_not_bonus = (self.sb * self.wd) * self.wp
        s_total = s_not_bonus + self.bonus + self.bonus_de - Employee.penalty_cal(self)
        self.s_without_tax = s_total * 0.895
        for i in Common.list_taxs:
            # Khong can dong thue khi khong co luong
            if self.s_without_tax == 0:
                return 0
            try:
                if i["min"] * 1000000 < self.s_without_tax <= i["max"] * 1000000:
                    return self.s_without_tax * (i["value"] / 100)
            except KeyError:
                if i["min"] * 1000000 < self.s_without_tax:
                    return self.s_without_tax * (i["value"] / 100)

    # Kiem tra dung tien thuong cua tung bo phan
    def check_department(self, departments):
        for item in departments:
            if item["Mã bộ phận"] == self.de:
                self.bonus_de = item["Thưởng bộ phận"]
            else:
                continue
        return self.bonus_de

    # Tinh luong thuc nhan cua nhan vien
    def salary_cal(self):
        s_not_bonus = (self.sb * self.wd) * self.wp
        s_total = s_not_bonus + self.bonus + self.bonus_de - Employee.penalty_cal(self)
        self.s_without_tax = s_total * 0.895
        self.s_official = self.s_without_tax - Employee.tax_cal(self)
        return int(self.s_official)


# Quan ly
class Manager(Employee):
    # Tinh luong thuc nhan cua quan ly
    def salary_cal(self):
        s_not_bonus = (self.sb * self.wd) * self.wp
        s_total = (
            s_not_bonus + self.bonus + (self.bonus_de * 1.1) - Manager.penalty_cal(self)
        )
        self.s_without_tax = s_total * 0.895
        self.s_official = self.s_without_tax - Manager.tax_cal(self)
        return int(self.s_official)


# Luu du lieu lay duoc tu url thanh danh sach
# Class nay giup khong phai truyen tham so vao cac ham trong class Employee
class Common:
    list_penalty = list()
    list_taxs = list()
