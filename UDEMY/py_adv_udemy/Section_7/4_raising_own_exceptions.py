def ProcessInvoice(netto,brutto):
    if netto > brutto:
        raise ValueError("Netto should be lower or equel to brutto")
    else:
        print("Processing invoice: netto = {}, brutto = {}".format(netto,brutto))


def EndOfMonth():
    netto = 1230
    brutto = 10000

    try:
        ProcessInvoice(netto,brutto)
        1/0
    except ValueError as e:
        print("The values on invoice are incorrect: {}".format(e))
        raise ValueError('Error when processing invoice') from e
    except Exception as e:
        print("Error with processing invoice {}".format(e))
        raise Exception("General error when processing invoice")


EndOfMonth()