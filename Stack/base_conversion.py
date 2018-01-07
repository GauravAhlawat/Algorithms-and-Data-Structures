import stack

# creating a function which can convert any number to binary conversion or to any other base also using Stack
def base_conversion(number, base):
    digits = '0123456789ABCDEF'

    st = stack()

    while number > 0:
        remainder = number % base
        st.push(remainder)
        number = number // base

    converted_num = ""
    while not st.isEmpty():
        converted_num = converted_num + str(digits[st.pop])

    return converted_num

def main():
    num = int(input("The number you want to convert"))
    base = int(input("The base in which you want to convert"))

    ret_num = base_conversion(num, base)
    print("the returned number is: %d" %ret_num)

if __name__ == '__main__':
    main()
