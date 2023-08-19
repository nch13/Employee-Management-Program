import urllib.request
import xml.etree.ElementTree as Etree
import json


# Truy xuat du lieu tien phat di tre tu link url json
def parse_penalty():
    # open url by using urllib
    url_json = "https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de"
    open_json = urllib.request.urlopen(url_json)
    # decoding json, return list type
    list_penalty = json.load(open_json)
    return list_penalty


# Truy xuat du lieu thue tu link url xml
def parse_tax():
    # open url by using urllib
    url_xml = "https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7"
    open_xml = urllib.request.urlopen(url_xml)
    # reading data of xml file as a tree objects
    tree_xml = Etree.parse(open_xml)
    # root_xml is a root element, it has a tag <taxs>, sub-element is "tax",...
    root_xml = tree_xml.getroot()
    list_tax = list()
    # each item in root_xml, has sub-elements of "tax" element: min, max, value
    for item in root_xml:
        if len(item) == 3:
            min_tax = int(item[0].text)
            max_tax = int(item[1].text)
            value_tax = int(item[2].text)
            list_tax.append({"min": min_tax, "max": max_tax, "value": value_tax})
        # last item does not have element "max"
        else:
            min_tax = int(item[0].text)
            value_tax = int(item[1].text)
            list_tax.append({"min": min_tax, "value": value_tax})
    return list_tax


# Ghi thong tin none vao file nhan vien neu file chua tao
def create_data_nv():
    list_nv = [
        {
            "Mã số": "none",
            "Mã bộ phận": "none",
            "Chức vụ": "none",
            "Họ và tên": "none",
            "Hệ số lương": "0 (VND)",
            "Số ngày làm việc": 0,
            "Hệ số hiệu quả": 0,
            "Thưởng": "0 (VND)",
            "Số ngày đi muộn": 0,
        }
    ]
    # Ghi du lieu vao file json duoi dang unicode
    with open("json_NV.txt", "w", encoding="utf-8-sig") as info_NV:
        json.dump(list_nv, info_NV, indent=4, ensure_ascii=False)


# Ghi thong tin none vao file bo phan neu file chua tao
def create_data_bp():
    list_bp = [{"Mã bộ phận": "none", "Thưởng bộ phận": "0 (VND)"}]
    # Ghi du lieu vao file json duoi dang unicode
    with open("json_BP.txt", "w", encoding="utf-8-sig") as info_BP:
        json.dump(list_bp, info_BP, indent=4, ensure_ascii=False)
