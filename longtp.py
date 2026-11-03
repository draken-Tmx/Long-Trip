from backend import journey,trip_download,clear
while True:
    clear()
    print("1. Calculate time")
    print("2. Download traveling playlist")
    print("3. exit")
    op=input("> ")
    if op == "1":
        journey()
    elif op == "2":
        trip_download()
    elif op == "3":
        break
    else:
        print("incorrect")