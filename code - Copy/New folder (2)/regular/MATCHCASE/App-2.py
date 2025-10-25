
ch=input("Enter any char ")

match ch:
    case 'm' | 'M':     # if ch=='m' or ch=='M':
        print("Male")
    case 'f' | 'F':        # if ch=='f' or ch=='F':
        print("Female")
    case default:     # case _:
        print("Third-Gender")
