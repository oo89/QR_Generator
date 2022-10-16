import pyqrcode
import png 
from pyqrcode import QRCode

qr = 'www.oscarojeda.com'
url = pyqrcode.create(qr)
url.png('myqr.png', scale=6)