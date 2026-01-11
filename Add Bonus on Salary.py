#Add Bonus On Salary
#Bonus = 10% or 0.1

a = int(input("Enter Your Salary: "))

if a >= 50000:
    bonus = a*0.10
    total_Salary = a + bonus
    print("Salary With Bonus is:" ,int(total_Salary))
else:
    print("Try Again To get Bonus")
    
