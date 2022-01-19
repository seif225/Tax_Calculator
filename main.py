def adjust_tax_levels(tax_levels, min_range):
    for i in range(1, min_range):
        tax_levels[min_range]['difference'] += tax_levels[i]['difference']
    return tax_levels


def calc_tax(min_range, tax_scope):
    tax_levels = {1: {'percentage': 0 / 100, 'difference': 15000},
                  2: {'percentage': 2.5 / 100, 'difference': 15000},
                  3: {'percentage': 10 / 100, 'difference': 15000},
                  4: {'percentage': 15 / 100, 'difference': 15000},
                  5: {'percentage': 20 / 100, 'difference': 140000},
                  6: {'percentage': 22.5 / 100, 'difference': 200000},
                  7: {'percentage': 25 / 100, 'difference': 400000},
                  8: {'percentage': 25 / 100, 'difference': 10000000000}}
    reminder = tax_scope
    sum_tax = 0
    for i in range(min_range, 9):
        if min_range > 1:  # add all previous differences to the minimum
            tax_levels = adjust_tax_levels(tax_levels, min_range)
        reminder, sum_tax = apply_slice(tax_levels[i]['percentage'], tax_levels[i]['difference'], reminder, sum_tax)
    return reminder, sum_tax


def apply_slice(percentage, difference, reminder, sum_tax):
    if reminder > difference:
        sum_tax = sum_tax + (difference * percentage)
        reminder = reminder - difference
    else:
        sum_tax = sum_tax + (reminder * percentage)
        reminder = 0
    return reminder, sum_tax


# starting point of logic.
salary = 5000
tax_scope = salary * 12 - 9000
if tax_scope <= 600000:
    final_reminder, final_tax = calc_tax(1, tax_scope)
elif 600000 < tax_scope <= 700000:
    final_reminder, final_tax = calc_tax(2, tax_scope)
elif 700000 < tax_scope <= 800000:
    final_reminder, final_tax = calc_tax(3, tax_scope)
elif 800000 < tax_scope <= 900000:
    final_reminder, final_tax = calc_tax(4, tax_scope)
    print(final_reminder, final_tax)
elif 900000 < tax_scope <= 1000000:
    final_reminder, final_tax = calc_tax(5, tax_scope)
elif tax_scope > 1000000:
    final_reminder, final_tax = calc_tax(6, tax_scope)

print(final_reminder, final_tax)
# categories.GROSS  +categories.INSS
