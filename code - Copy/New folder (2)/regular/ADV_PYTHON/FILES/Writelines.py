#writelines(iterable)

f=open("data4.txt","w")

lst=["1.Have a nice day \n",
        "2.Have a good day \n",
        "3.Have a cool day \n",
        "4.Hava a wonderful day \n"]

f.writelines(lst)
f.close()
print("Data is Saved ")
