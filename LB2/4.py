persons = input().split(' ')
n = len(persons)
q = int(input())

purchases = {}
for i in persons:
    purchases[i] = 0


for i in range(q):
    name, amount = input().split()
    purchases[name] += int(amount)


summ = 0
for i in purchases:
    summ += purchases[i]
summ /= 3

balances = []
for person in persons:
    diff = purchases[person] - summ
    balances.append((person, diff))

balances.sort(key=lambda x: x[1])
transfers = []
i, j = 0, n - 1

while i < j:
    debtor, debt = balances[i]
    creditor, credit = balances[j]
    
    if abs(debt) < 1e-9:
        i += 1
        continue
    if abs(credit) < 1e-9:
        j -= 1
        continue
    
    amount = min(-debt, credit)
    transfers.append((debtor, creditor, amount))
    
    balances[i] = (debtor, debt + amount)
    balances[j] = (creditor, credit - amount)

print(len(transfers))
for from_person, to_person, amount in transfers:
    print(f"{from_person} {to_person} {amount:.2f}")
    