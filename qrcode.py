import qrcode


data = "https://www.google.com"

# Create QR code
qr = qrcode.QRCode(
    version=1,  # controls size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save as file
img.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'")