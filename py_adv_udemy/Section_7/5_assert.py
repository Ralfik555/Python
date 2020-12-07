import datetime
netto = 100
brutto = 120
# netto must be less or equel to brutto
assert netto <= brutto, "netto must be less or equel to brutto"


orderDate = datetime.date(2022,11,13)
deliveryDate = datetime.date(2022,10,18)
# order date should be earlier that the delivery date
assert orderDate <= deliveryDate, "Order date cannot be later that the delivery date"

