# Generate Barcode

# Description
Given a code, generate a png of a barcode for the code.


Tags: Python, Barcode
Libraries: barcode

# Quick Glance


[1] import barcode
[1] from barcode.writer import ImageWriter

[2] CODE = 45616574456


[3] barcode_class = barcode.get_barcode_class('upc')
[4] barcode = barcode_class(str(CODE), writer=ImageWriter())
[5] barcode.save('barcode')


1. Necessary imports from barcode library.
2. 11 digit code being used for the barcode.
3. Define the barcode class type. You can get all the class types with `barcode.PROVIDED_BARCODES`
4. Assign the code to the class object.
5. Generate the image which will be saved as `barcode.png` to your cwd.

The Python barcode library has many great examples to get you started. Check out [barcode](https://python-barcode.readthedocs.io/en/stable/getting-started.html) library.

