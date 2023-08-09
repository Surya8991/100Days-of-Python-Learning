# Program to find how much per person cost for food after adding tip
print("Welcome to the Sunshine Cafe \n Tip Calcluator")
bill=int(input("Enter the Bill Amount \n"))
people=int(input("Enter the No. of People to Split the bill \n"))
tip=int(input("Enter the tip: \n"))
per_person=round(((bill+tip)/people),2)
print(f"Amount to be paid by Per person is {per_person}")