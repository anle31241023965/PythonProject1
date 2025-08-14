"""
Bài tập:
1/ Kiểm tra version python = Command Prompt
    -> python --version
2/ In dòng chữ Hello world dùng cmd
    -> print('Hello world')
3/ Dùng Google Colab in dòng Hello world
    -> Tạo tài khoản, hạn chế dùng AI
4/ Dùng Pycharm tạo project in dòng chữ Hello world
    -> Lưu ý!!! python path: python313/python.exe
     -> Tạo 2 directories: src và resources
      -> Vào Files -> Settings -> Project: Python project -> Project Structure -> Nối (directory) src với resources.
       -> Quay lại, nhấn chuột phải vào src chọn New -> Python file
"""
print('Hello world!')

#    *Dùng thử breakpoint (dấu tròn màu đỏ) và Debug. Nhấn F8 (Step Over) để xem từng dòng lệnh được thực thi như thế nào.
#    *Tô một vùng rồi nhấn Ctrl + / để biến thành Ghi chú/Bỏ ghi chú

# VARIABLES EXERCISE
#1/ Create a variable named car_name and assign the value Volvo to it.
car_name = "Volvo"
print(f"This {car_name} car is the oldest at our store!")
        #Our car Volvo is the best!

#2/ Create a variable named x and assign the value 50 to it.
x = 50
print(f"It's already {x} years old.")
        #It's already 50 years old.

#3/ Display the sum of 5 + 10, using two variables: x and y
x,y = 5.205,10.881
result = x + y
print("Amount: ${:.2f}".format(result))
        #Amount: $16.09

#4/ Create a variable called z, assign x + y to it, and display the result.
z = x + y
print(f"The sum is {z:.2f}")
        #The sum is 16.09

#5/ Insert the correct syntax to assign values to multiple variables in one line: x? y? z? = "Orange", "Banana", "Cherry"
x,y,z = "Orange", "Banana", "Cherry"
print(x,y,z, sep='_')

#6/ Check the data type of all your variables using type() built-in function
print(type(car_name))
print(type(x))
print(type(y))
print(type(z))

#7/ Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')