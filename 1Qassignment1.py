print("****Books******")
print("Introduction to Python Programming")
print("Python Libraries Cookbook")
print("Datascience in Python")
b1 = int(input("Enter the quantity of 'Introduction to Python Programming' book Rs.499.00 : "))
b2 = int(input("Enter the quantity of 'Python Libraries Cookbook' book Rs.855.00 : "))
b3 = int(input("Enter the quantity of 'Datascience in Python' book Rs.645.00 : "))
b1_amount = 499.00*b1
b2_amount = 855.00*b2
b3_amount = 645.00*b3
print("Invoice : ")
print("Introduction to Python ",end = " ")
print(b1," ->",end = " ")
print(b1_amount)
print("Python Libraries Cookbook ",end = " ")
print(b2," ->",end = " ")
print(b2_amount)
print("Datascienece in Python ",end = " ")
print(b3," ->",end = " ")
print(b3_amount)
print("Additional  charges : ")
print("GST = 12% + delivery charges = 250")
t_amount = b1_amount+b2_amount+b3_amount
final_amt = t_amount + t_amount*0.12 + 250
print("Total Amount : ",end = " ")
print(final_amt)





