import csv

list_of_rows = []
with open('budget_data.csv', 'r') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    next(data)
    for row in data:
        list_of_rows.append(row)

total_months = len(list_of_rows)

profits = [int(row[1]) for row in list_of_rows]
total_profit = sum(profits)

sum_change = sum([profits[i + 1] - profits[i] for i in range(len(profits) - 1)])
avg_change = round(sum_change / (total_months - 1), 2)

max_increase = -1 * (2 ^ 31 - 1)
max_increase_month = ''
for i in range(len(list_of_rows) - 1):
    diff = int(list_of_rows[i + 1][1]) - int(list_of_rows[i][1])
    if diff > max_increase:
        max_increase = diff
        max_increase_month = list_of_rows[i + 1][0]


max_decrease = 1 * (2 ^ 31 - 1)
max_decrease_month = ''
for i in range(len(list_of_rows) - 1):
    diff = int(list_of_rows[i + 1][1]) - int(list_of_rows[i][1])
    if diff < max_decrease:
        max_decrease = diff
        max_decrease_month = list_of_rows[i + 1][0]

print('Financial Analysis')
print('---------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {max_increase_month} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})')

