# retruning tax amount based on billed amount using terinary operator
# if amount is more than 50000 the tax is 10%, if it less the tax is 5% 
def tax_amount(amount):
    return int((amount/100)*10) if amount>50000 else int((amount/100)*5)

