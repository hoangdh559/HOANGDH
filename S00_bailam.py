def tongtienmuahang(gia_truoc_thue):

  tien_thue = gia_truoc_thue * 0.1
  tien_thue = int(tien_thue)
  tong_tien = gia_truoc_thue + tien_thue
  return tong_tien


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

  gia_truoc_thue = input("Nhập giá trị trước thuế: ")
  if not isinstance(gia_truoc_thue, int):

    print("Giá trị nhập vào không phải là số nguyên!")
    print("Tổng tiền sau thuế: none")
  else:
    tong_tien = tongtienmuahang(gia_truoc_thue)
    print(f"Tổng tiền sau thuế: {tong_tien}")

