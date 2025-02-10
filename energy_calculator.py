import argparse

def calculate_unit_cost(units):
    """Calculate cost for given units based on slab rates"""
    cost = 0
    remaining_units = units
    
    # Slab 1: 0-100 units @ Rs 4.71
    slab_units = min(100, remaining_units)
    cost += slab_units * 4.71
    remaining_units -= slab_units
    
    # Slab 2: 101-300 units @ Rs 10.29
    if remaining_units > 0:
        slab_units = min(200, remaining_units)
        cost += slab_units * 10.29
        remaining_units -= slab_units
    
    # Slab 3: 301-500 units @ Rs 14.55
    if remaining_units > 0:
        slab_units = min(200, remaining_units)
        cost += slab_units * 14.55
        remaining_units -= slab_units
    
    # Slab 4 & 5: >500 units @ Rs 16.64
    if remaining_units > 0:
        cost += remaining_units * 16.64
    
    return cost

def main():
    try:
        units = int(input("Enter the number of units consumed: "))
        if units <= 0:
            print("Error: Units should be greater than 0")
            return
        
        total_cost = calculate_unit_cost(units)
        print(f"Total cost for {units} units: Rs {total_cost:.2f}")
    except ValueError:
        print("Error: Please enter a valid number")

if __name__ == "__main__":
    main()