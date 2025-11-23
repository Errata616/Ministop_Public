#Food list (List is chosen so that things can be changed easier
main_food = ["Bánh tacos", "Pizza", "Mì lẩu", "Bánh bao", "Xíu mại"]
light_snack = ["Bò lá lốt", "Phô mai que", "Cá viên", "Tôm chiên", "Lạp xưởng nướng đá"]
drink = ["Nước suối", "Coca", "Pepsi", "Strongbold", "Fanta", "Soda"]

#Pricing (Dictionary is used to help with the calculation)
price = {"Bánh tacos" : 30000, "Pizza" : 30000, "Mì lẩu" : 32000, "Bánh bao" : 25000, "Xíu mại" : 23000,
         "Bò lá lốt" : 10000, "Phô mai que" : 12000, "Cá viên" : 8000, "Tôm chiên" : 12000, "Lạp xưởng nướng đá" : 15000,
         "Nước suối" : 6000, "Coca" : 9000, "Pepsi" : 9000, "Strongbold" : 15000, "Fanta" : 9000, "Soda" : 11000}

#Bill with Dictionary type to print out bill format
bill = {}

#Handling food
def food_handler():
    cost = 0
    while True:
        print("Hãy nhập lựa chọn của quý khách:")
        for i in main_food:
            print(f"{main_food.index(i) + 1}: {i}[{main_food.index(i) + 1}]")
        try:
            choice = int(input("Nhập phím từ [1] -> [5] để lựa chọn, phím [0] để thoát: "))
            #Kiểm tra hợp lệ
            if choice < 0 or choice > 5:
               print("Lựa chọn không hợp lệ ! Vui lòng chọn lại !")
            elif choice == 0:
                decide = str(input("Quý khách có chắc chắn với lựa chọn này không ? [Nhập phím [Y] để xác nhận là có]: "))
                print('-' * 100)
                if decide == "y" or decide == "Y":
                    break   
            else:
                for i in range(1, 6):
                    if choice == i:
                        while True:
                            decide = str(input("Quý khách có chắc chắn muốn mua món hàng này không ? [Nhập Y/N để xác nhận]: "))
                            print('-' * 100)
                            if decide == "Y" or decide == "y":    
                                print(f"Giá tiền của {main_food[i - 1]} là {price[main_food[i - 1]]} VNĐ")
                                cost = price[main_food[i - 1]]
                                #Đơn hàng đã mua sẽ được thêm vào hóa đơn
                                #Trường hợp ta mua nhiều hàng giống nhau thì món hàng sẽ x2 x3 ...
                                if main_food[i - 1] in bill:
                                    bill.update({main_food[i - 1] : cost + bill[main_food[i - 1]]})
                                else:
                                    bill.update({main_food[i - 1] : cost})
                                break
                            elif decide == "N" or decide == "n":
                                break
                            else:
                                print("Lựa chọn không hợp lê ! Vui lòng chọn lại !")    
                decide = str(input("Quý khách có muốn mua thêm món hàng nào không ? [Nhập phím [Y] để xác nhận là có]: "))
                print('-' * 100)
                if decide != "y" and decide != "Y":
                    break   
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng chọn lại !")  

#Handling beverage
def drink_handler():
    cost = 0
    while True:
        print("Hãy nhập lựa chọn của quý khách:")
        for i in drink:
            print(f"{drink.index(i) + 1}: {i}[{drink.index(i) + 1}]")
        try:
            choice = int(input("Nhập phím từ [1] -> [6] để lựa chọn, phím [0] để thoát: "))
            #Kiểm tra hợp lệ
            if choice < 0 or choice > 6:
               print("Lựa chọn không hợp lệ ! Vui lòng chọn lại !")
            elif choice == 0:
                decide = str(input("Quý khách có chắc chắn với lựa chọn này không ? [Nhập phím [Y] để xác nhận là có]: "))
                print('-' * 100)
                if decide == "y" or decide == "Y":
                    break   
            else:
                for i in range(1, 7):
                    if choice == i:
                        while True:
                            decide = str(input("Quý khách có chắc chắn muốn mua món hàng này không ? [Nhập Y/N để xác nhận]: "))
                            print('-' * 100)
                            if decide == "Y" or decide == "y":    
                                print(f"Giá tiền của {drink[i - 1]} là {price[drink[i - 1]]} VNĐ")
                                cost = price[drink[i - 1]]
                                #Như trên
                                if drink[i - 1] in bill:
                                    bill.update({drink[i - 1] : cost + bill[drink[i - 1]]})
                                else:
                                    bill.update({drink[i - 1] : cost})
                                break
                            elif decide == "N" or decide == "n":
                                break
                            else:
                                print("Lựa chọn không hợp lê ! Vui lòng chọn lại !")    
                decide = str(input("Quý khách có muốn mua thêm món hàng nào không ? [Nhập phím [Y] để xác nhận là có]: "))
                print('-' * 100)
                if decide != "y" and decide != "Y":
                    break   
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng chọn lại !") 

#Handling snack
def snack_handler():
    cost = 0
    while True:
        print("Hãy nhập lựa chọn của quý khách:")
        for i in light_snack:
            print(f"{light_snack.index(i) + 1}: {i}[{light_snack.index(i) + 1}]")
        try:
            choice = int(input("Nhập phím từ [1] -> [5] để lựa chọn, phím [0] để thoát: "))
            #Kiểm tra hợp lệ
            if choice < 0 or choice > 5:
               print("Lựa chọn không hợp lệ ! Vui lòng chọn lại !")
            elif choice == 0:
                decide = str(input("Quý khách có chắc chắn với lựa chọn này không ? [Nhập phím [Y] để xác nhận là có]: "))
                print('-' * 100)
                if decide == "y" or decide == "Y":
                    break   
            else:
                for i in range(1, 6):
                    if choice == i:
                        while True:
                            decide = str(input("Quý khách có chắc chắn muốn mua món hàng này không ? [Nhập Y/N để xác nhận]: "))
                            print('-' * 100)
                            if decide == "Y" or decide == "y":    
                                print(f"Giá tiền của {light_snack[i - 1]} là {price[light_snack[i - 1]]} VNĐ")
                                cost = price[light_snack[i - 1]]
                                #Cũng như trên
                                if light_snack[i - 1] in bill:
                                    bill.update({light_snack[i - 1] : cost + bill[light_snack[i - 1]]})
                                else:
                                    bill.update({light_snack[i - 1] : cost})
                                break
                            elif decide == "N" or decide == "n":
                                break
                            else:
                                print("Lựa chọn không hợp lê ! Vui lòng chọn lại !")    
                decide = str(input("Quý khách có muốn mua thêm món hàng nào không ? [Nhập phím [Y] để xác nhận là có]: "))
                print('-' * 100)
                if decide != "y" and decide != "Y":
                    break   
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng chọn lại !")

#Hàm Formatting (I have to ask AI for this one because Python string formatting is something new to me)
def bill_format():
    # --- Configuration ---
    W_ITEM = 35    # Width for Item Name + Quantity column
    W_PRICE = 16   # Width for Price + Currency column
    W_LINE = W_ITEM + W_PRICE # Total width for separators
    
    subtotal = 0
    
    # --- Header ---
    print("\n" + " HÓA ĐƠN ".center(W_LINE, '='))
    
    # Print Column Headers
    print(f"{'Đơn Hàng':<{W_ITEM}}{'Giá Tiền':>{W_PRICE}}")
    print("".center(W_LINE, '-'))
    
    # --- Item Rows ---
    for k, v in bill.items():
        # 1. Calculate the quantity (since v is the total price for the item)
        # Note: We must ensure the item exists in the 'price' dictionary.
        unit_price = price.get(k)
        if unit_price is None or unit_price == 0:
            quantity = 0
        else:
            quantity = int(v / unit_price)
        
        # 2. Prepare the item string (Left-aligned)
        item_and_qty = f"{k} x{quantity}"

        # 3. Prepare the price string (Right-aligned, with comma separators)
        price_str = f"{v:,} VNĐ" 

        # Print the row using fixed-width f-string alignment
        # {item_and_qty:<{W_ITEM}} -> Left-align within W_ITEM
        # {price_str:>{W_PRICE}} -> Right-align within W_PRICE
        print(f"{item_and_qty:<{W_ITEM}}{price_str:>{W_PRICE}}")
        
        subtotal += v

    # --- Footer and Total Calculation ---
    print("".center(W_LINE, '-'))

    # VAT Calculation (assuming 10%)
    tax_rate = 0.1
    tax_amount = int(subtotal * tax_rate)
    final_total = subtotal + tax_amount

    # Print Subtotal
    subtotal_str = f"{subtotal:,} VNĐ"
    print(f"{'TỔNG TIỀN HÀNG:':<{W_ITEM}}{subtotal_str:>{W_PRICE}}")

    # Print Tax
    tax_str = f"{tax_amount:,} VNĐ"
    print(f"{'THUẾ VAT 10%:':<{W_ITEM}}{tax_str:>{W_PRICE}}")

    print("".center(W_LINE, '='))

    # Print Final Total
    total_str = f"{final_total:,} VNĐ"
    print(f"{'TỔNG CỘNG THANH TOÁN:':<{W_ITEM}}{total_str:>{W_PRICE}}")
    print("".center(W_LINE, '='))

#Main        
def main():
    print("==================Cửa hàng tiện lợi xin chào quý khách !==================")
    while True:
        print("Quý khách muốn mua gì:\n-----------------\n 1.Đồ ăn[1]\n 2.Đồ ăn nhẹ[2]\n 3.Đồ uống[3]\n-----------------")
        n = int(input("Nhấn phím [1], [2], [3] để lựa chọn, Nhấn phím [0] để thoát: "))
        if n == 1:
            food_handler()
        elif n == 2:
            snack_handler()
        elif n == 3:
            drink_handler()
        elif n == 0:
            break
        else:
            print("Lựa chọn không hợp lệ ! Vui lòng chọn lại !")
    bill_format()
    print("Cảm ơn quý khách !")

main()
