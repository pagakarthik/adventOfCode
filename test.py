def get_two_digit_collections(value):
    successive_digits = [value%100]
    if value/10 < 1.0:
        print ("getting out, value/10 is: ", value/10)
        return successive_digits
    else:
        print ("entered else")
        # successive_digits.append(value%100)
        print (successive_digits)
        successive_digits.append(get_two_digit_collections(value//10))
        return successive_digits


def test_2(val):
    data = []
    if val < 9.0:
        return data
    else:
        # data.append(val%100)
        new_val = test_2(val//10)
        if len(new_val) != 0:
            data.append(new_val)
        data.append(val%100)

        return  data

if __name__ == "__main__":
    result = test_2(123456)
    print(result)
