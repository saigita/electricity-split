import argparse

def calculate_unit_cost(units):
    """Calculate cost for given units based on slab rates"""
    # For equal distribution of slab benefits, units are calculated per person
    cost = 0
    remaining_units = units
    
    # Each person gets equal share of first slab (33.33 units each for first 100 units)
    first_slab_share = min(33.33, remaining_units)
    cost += first_slab_share * 4.71
    remaining_units -= first_slab_share
    
    # Each person gets equal share of second slab (66.67 units each for next 200 units)
    if remaining_units > 0:
        second_slab_share = min(66.67, remaining_units)
        cost += second_slab_share * 10.29
        remaining_units -= second_slab_share
    
    # Each person gets equal share of third slab (66.67 units each for next 200 units)
    if remaining_units > 0:
        third_slab_share = min(66.67, remaining_units)
        cost += third_slab_share * 14.55
        remaining_units -= third_slab_share
    
    # Remaining units at highest slab
    if remaining_units > 0:
        cost += remaining_units * 16.64
    
    return cost

def main():
    # Get inputs interactively
    print("\nElectricity Bill Split Calculator")
    print("-" * 50)
    
    # Get person names
    print("\nEnter names of three people:")
    person1_name = input("Person 1 name: ")
    person2_name = input("Person 2 name: ")
    person3_name = input("Person 3 name: ")
    
    total_units = float(input("\nEnter total units consumed: "))
    total_bill = float(input("Enter total bill amount (Rs): "))
    print("\nEnter individual unit consumption:")
    person1_units = float(input(f"{person1_name}'s units: "))
    person2_units = float(input(f"{person2_name}'s units: "))
    person3_units = float(input(f"{person3_name}'s units: "))
    
    # Calculate common units
    individual_units = person1_units + person2_units + person3_units
    common_units = total_units - individual_units
    
    if common_units < 0:
        print("Error: Individual units sum is greater than total units!")
        return
    
    # Calculate common units per person
    common_units_per_person = common_units / 3
    
    # Calculate total units per person (individual + common share)
    person1_total_units = person1_units + common_units_per_person
    person2_total_units = person2_units + common_units_per_person
    person3_total_units = person3_units + common_units_per_person
    
    # Calculate costs based on total units per person
    person1_total_cost = calculate_unit_cost(person1_total_units)
    person2_total_cost = calculate_unit_cost(person2_total_units)
    person3_total_cost = calculate_unit_cost(person3_total_units)
    
    # Calculate other charges
    units_cost = person1_total_cost + person2_total_cost + person3_total_cost
    other_charges = total_bill - units_cost
    other_charges_per_person = other_charges / 3
    
    # Calculate final shares
    person1_share = person1_total_cost + other_charges_per_person
    person2_share = person2_total_cost + other_charges_per_person
    person3_share = person3_total_cost + other_charges_per_person
    
    # Print results
    print("\nBill Split Summary:")
    print("-" * 50)
    print(f"Total Units: {total_units:.2f}")
    print(f"Common Units: {common_units:.2f}")
    print(f"Common Units per person: {common_units_per_person:.2f}")
    print(f"Total Bill Amount: Rs {total_bill:.2f}")
    print(f"Total Units Amount: Rs {units_cost:.2f}")
    print(f"Other Charges: Rs {other_charges:.2f}")
    print("\nPer Person Break-up:")
    print("-" * 50)
    print(f"{person1_name}:")
    print(f"Individual Units: {person1_units:.2f}")
    print(f"Total Units (including common {common_units_per_person:.2f}): {person1_total_units:.2f}")
    print(f"Units Cost: Rs {person1_total_cost:.2f}")
    print(f"Other Charges Share: Rs {other_charges_per_person:.2f}")
    print(f"Total Share: Rs {person1_share:.2f}")
    print(f"\n{person2_name}:")
    print(f"Individual Units: {person2_units:.2f}")
    print(f"Total Units (including common {common_units_per_person:.2f}): {person2_total_units:.2f}")
    print(f"Units Cost: Rs {person2_total_cost:.2f}")
    print(f"Other Charges Share: Rs {other_charges_per_person:.2f}")
    print(f"Total Share: Rs {person2_share:.2f}")
    print(f"\n{person3_name}:")
    print(f"Individual Units: {person3_units:.2f}")
    print(f"Total Units (including common {common_units_per_person:.2f}): {person3_total_units:.2f}")
    print(f"Units Cost: Rs {person3_total_cost:.2f}")
    print(f"Other Charges Share: Rs {other_charges_per_person:.2f}")
    print(f"Total Share: Rs {person3_share:.2f}")

if __name__ == "__main__":
    main()
