gram_in_lot=13.3
lot_in_pound=32
pound_in_talent= 20
talent_str=input("Mass of object in talent:")
pound_str=input("Mass of object in pound:")
lot_str=input("Mass of object in lot:")
talent=int(talent_str)
pound=int(pound_str)
lot=int(lot_str)
Mass_in_gram= talent*pound_in_talent*lot_in_pound*gram_in_lot+pound*lot_in_pound*gram_in_lot+lot*gram_in_lot
Mass_in_Kilogram=Mass_in_gram/1000

print(f"The mass of object are {Mass_in_Kilogram:.1f}kg,and {Mass_in_gram:.2f}g")
