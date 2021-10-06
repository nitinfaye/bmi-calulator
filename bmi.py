import json
# JSON file
f = open ('data.json', "r")
 
# Reading from file
data = json.loads(f.read())
 
# Iterating through the json
# list
for i in data['bmi_details']:
    print(i)


# from user response for check the BMI condition
def bmicalculator():
    Genter = input("Enter the genter : ")
    HeightCM = int(input("Enter your Height in centimeters :"))
    WeightKg = int(input("Enter your Weight in kg : "))

    bmi = WeightKg / (HeightCM/10 ** 2)

    if bmi < 18.4:
        print(f"{Genter} is by {bmi} kg/m2 BMI")
        print("BMI Category : Underweight")
        print("Health risk : Malnutrition risk") 
    elif bmi == 18.5 - 24.9 :
        print(f"{Genter} is Normal weight & Low risk by {bmi} kg/m2 BMI")
        print("BMI Category : Overweight")
        print("Health risk : Enhanced risk") 
    elif bmi == 25 - 29.9:
        print(f"{Genter} is by {bmi} kg/m2 BMI")
        print("BMI Category : Overweight")
        print("Health risk : Enhanced risk") 
    elif bmi == 30 -34.0:
        print("f{Genter} is by{bmi} kg/m2 BMI")
        print("BMI Category :Moderately obese")
        print("Health risk : Medium risk") 
    elif bmi == 35 - 39.9:
        print("f{Genter} is by{bmi} kg/m2 BMI")
        print("BMI Category :Severely obese")
        print("Health risk : High risk")   
    else :
       print(f"{Genter} is by {bmi} kg/m2 BMI")
       print("BMI Category : Very severely obese")
       print("Health risk : Very High risk")  

if __name__=='__main__':
    bmicalculator()