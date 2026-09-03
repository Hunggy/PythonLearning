def append_record(date, item, amount):
    with open("ledger.txt", "a") as file:             # ①
        file.write(f"{date},{item},{amount}\n")

def read_records():
    with open("ledger.txt", "r") as file:                       # ②
        records = file.readlines()                            # ③
        for record in records:
            print(record, end="")
    
# 示例操作
append_record("2023-04-05", "Groceries", 35.20)
append_record("2023-04-06", "Internet Bill", 50)
read_records()                                                   # ④