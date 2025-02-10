# Electricity Bill Split Calculator

A Python-based calculator that helps roommates split their electricity bill fairly based on MSEDCL (Maharashtra State Electricity Distribution Co. Ltd.) slab rates. The calculator takes into account individual consumption and common area usage to provide an equitable split of the total electricity bill.

## Features

- Calculates individual shares based on MSEDCL slab rates
- Handles common area electricity consumption
- Splits additional charges equally
- Supports 3 people sharing accommodation
- Provides detailed break-up of charges

## Slab Rates Used

| Units Consumed   | Rate (Rs/unit) |
| ---------------- | -------------- |
| 0-100 units      | 4.71           |
| 101-300 units    | 10.29          |
| 301-500 units    | 14.55          |
| 501-1000 units   | 16.64          |
| Above 1000 units | 16.64          |

## How to Use

1. Run the script:

   ```bash
   python customizable_electricity_bill_calculator.py
   ```

2. Enter the required information when prompted:

   - Names of three people
   - Total units consumed
   - Total bill amount
   - Individual unit consumption for each person

3. The calculator will display:
   - Bill split summary
   - Common units distribution
   - Individual break-up for each person including:
     - Individual units consumed
     - Share of common units
     - Units cost
     - Share of other charges
     - Total amount to be paid

## Requirements

- Python 3.x
- No additional packages required

## Note

This calculator is specifically designed for MSEDCL electricity bills in Maharashtra, India. The slab rates are based on MSEDCL tariffs and may need to be updated if rates change.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.
