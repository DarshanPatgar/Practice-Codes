import pyqrcode
import png
from pyqrcode import QRCode
s = "https://www.linkedin.com/in/darshan-patgar-36b135222/"
url = pyqrcode.create(s)
url.svg("mylr.svg", scale=8)
url.png('mylr.png', scale=6)


# # Import QRCode from pyqrcode
# import pyqrcode
# import png
# from pyqrcode import QRCode
#
#
# # String which represents the QR code
# s = "www.geeksforgeeks.org"
#
# # Generate QR code
# url = pyqrcode.create(s)
#
# # Create and save the svg file naming "myqr.svg"
# url.svg("myqr.svg", scale=8)
#
# # Create and save the png file naming "myqr.png"
# url.png('myqr.png', scale=6)
