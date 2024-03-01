required_pushup = 50
required_squats = 100

pushup = int(input("enter pushup: "))
squats = int(input("enter squats: "))

check_pushup = pushup == required_pushup
check_squats = squats == required_squats

print(check_pushup)
print(check_squats)