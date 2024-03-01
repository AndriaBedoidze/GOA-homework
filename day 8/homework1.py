required_weight = 50
required_height = 170

user_weight = int(input("enter your weight: "))
user_height = int(input("enter your height: "))

weight_check = user_weight == required_weight
height_check = user_height == required_height

weight_check = user_weight > required_weight
height_check = user_height > required_height

weight_check = user_weight < required_weight
height_check = user_height < required_height

weight_check = user_weight >= required_weight
height_check = user_height >= required_height

weight_check = user_weight <= required_weight
height_check = user_height <= required_height