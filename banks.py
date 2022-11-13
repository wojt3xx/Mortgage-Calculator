# creating class Banks
class Banks:

# linking interest rates to banks
    available_banks = {
        "HSBC Holdings": 0.11,
        "Lloyds Banking Group": 0.12,
        "NatWest Group": 0.1,
        "Barclays": 0.09
    }

# creating a display table to show in application that displays intrest rates to banks
    def __repr__():
        print("{:<26} {:<15}".format('Bank','Interest Rate'))
        print('----------------------------------------')
        for key, value in Banks.available_banks.items():
            value = str(value) + '%'
            print("{:<26} {:<15}".format(key, value))