import qrcode
from PIL import Image

# Data you want in QR code
data = "9761872560"

# Generate QR code
qr = qrcode.make(data)

# Save the QR code
qr.save("qrcode.png")

# Open the QR code image
img = Image.open("qrcode.png")
img.show()

print("QR Code generated and displayed!")
