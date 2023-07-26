import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((250, 250), Image.ANTIALIAS)

    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# Create the main window
root = tk.Tk()
root.geometry("400x600")
root.title("QR Code Generator")

# Set background color to blue
root.configure(background="blue")

# Label for the top subheading
top_label = tk.Label(root, text=" QR Code Generator ", font=("Helvetica", 24), fg="black", bg="blue")
top_label.pack(pady=20)

# Input field for data
entry_label = tk.Label(root, text="Enter Text ....", font=("Helvetica", 14), fg="black", bg="blue")
entry_label.pack()
entry = tk.Entry(root)
entry.pack(pady=10)

# Button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Label to display the generated QR code
qr_label = tk.Label(root, bg="blue")
qr_label.pack(pady=20)

# Label for the bottom subheading
bottom_label = tk.Label(root, text="**  Made by Lakender Tyagi  **", font=("Helvetica", 16), fg="black", bg="blue")
bottom_label.pack(pady=5)

root.mainloop()
