import pyqrcode
import png

from pyqrcode import QRCode

# String which represents the QR code
s ="""patient details
     Name:sridhar,age=21
     surgery=cardiac surgery
     height=175
     weight=70
     """
# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale=8)

# Create and save the png file naming "myqr.png"
url.png('patient details.png', scale=6)