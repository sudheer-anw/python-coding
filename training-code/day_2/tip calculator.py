print('wellcome to tip calculator!')
bill = float(input('what was the total amount?: ' ))
tip = int(input('how much tip would you like to give?: '))
people = int(input('how many people to split this bill: '))
tip_as_persentage = tip/100
total_tip_amount = bill + tip_as_persentage
total_bill = total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
print(f'for each person need to pay :{final_amount}')

