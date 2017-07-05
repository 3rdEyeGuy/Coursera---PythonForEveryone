score = input("Enter Score: ")
try:
    score = float(score)
    if 0 <= score < 0.6:
        print('F')
    elif 0.6 <= score < 0.7:
        print('D')
    elif 0.7 <= score < 0.8:
        print('C')
    elif 0.8 <= score < 0.9:
        print('B')
    elif 0.9 <= score <= 1.0:
        print('A')
except:
    print("Not within range or invalid input!")
