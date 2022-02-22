print("BMI Calculator")
print("enter the weight in kg:")
weight = input()
weight2 = float(weight)
print("enter your height in cm: ")
height = input()
height2 = float(height) / 100
print("Your BMI is:")
BMI_result = weight2/height2 ** 2
print(BMI_result)
print("Analysis of your BMI:")

if (BMI_result < 16):
    print("Danger! You are starving!")
elif BMI_result >= 16 and BMI_result <= 16.99:
    print("Warning! You are too skinny!")
    print("Improve your diet!")
elif BMI_result >= 17 and BMI_result <= 18.49:
    print("You're underweight, take care of yourself!")
elif BMI_result >= 18.5 and BMI_result <= 24.99:
    print("You are lucky, your BMI is normal!")
elif BMI_result >= 25 and BMI_result <= 29.99:
    print("You are overweight, start to move more!")
elif BMI_result >= 30 and BMI_result <= 34.99:
    print("Attention! You have 1 st degree obesity, take care of your health!")
elif BMI_result >= 35 and BMI_result <= 39.99:
    print("Warning! You are obese in the second degree. Consult a dietitian ")
elif BMI_result > 40:
    print("Danger! You are extremely obese, take immediate action before it's too late!")




# Ranges of BMI values:

#    less than 16 - starvation
#    16 - 16.99 - emaciation
#    17 - 18.49 - less than the correct weight
#    18.5 - 24.99 - correct value
#    25 - 29.99 - overweight
#    30 - 34.99 - I degree of obesity
#    35 - 39.99 - 2nd degree of obesity
#    above 40 - extreme obesity


