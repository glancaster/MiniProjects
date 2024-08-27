import barcode
from barcode.writer import ImageWriter

CODE = 45616574456


barcode_class = barcode.get_barcode_class('upc')
barcode = barcode_class(str(CODE), writer=ImageWriter())
barcode.save('barcode')
