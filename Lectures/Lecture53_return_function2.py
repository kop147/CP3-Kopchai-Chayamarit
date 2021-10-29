def vatcalculate(totalprice, vat):
    result = totalprice + totalprice * vat / 100
    return result


totalprice = int(input("Total Price :"))
vat = int(input("Vat (%) :"))
print(vatcalculate(totalprice, vat))


