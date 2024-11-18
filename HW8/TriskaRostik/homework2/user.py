import passvalid

print("""
    ******************************************
    *                                        *
    *            ₵ⱧɆ₵₭ A̺͆N̺͆D̺͆ ฿ⱤɄ₮E             *
    *               PASSWORDS                *
    *                                        *
    *                              by H̳̿͟͞I̳̿͟͞D̳̿͟͞E̳̿͟͞   *
    ******************************************\n
    """)

human_pass = input("Write your password for check: ")

res = passvalid.check(human_pass)
print(res)

if res == "Valid password":
    while True:
        answer = input("You need to check brute for your password? (Yes or No)\n: ")
        if answer.lower() == "yes":
            print(passvalid.brute(human_pass))
            break
        elif answer.lower() == "no":
            print("Okey, Good Luck =)")
            break
        else:
            print("Incorrect choice, please enter 'Yes' or 'No'")