
recipients = ["b44 44 4rt", "W0u uuT3R", "4l 3x", "K 3 n 4n", "54R4h"]

for item in recipients:
    item_index = recipients.index(item)
    item = item.strip().lower()
    item = item.replace('0', 'o').replace('3', 'e').replace('4', 'a').replace('5', 's').replace(" ", "").title()
    recipients[item_index] = item
print(recipients)