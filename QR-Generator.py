import pyqrcode
import png
import tkinter as tk

def generate_qr_code():
    # Retrieve data from the input field
    data = data_entry.get()
    
    # Create a QR code object from the data and save it to a PNG file
    qr_code = pyqrcode.create(data)
    qr_code.png('code.png', scale=6)

# Create a Tkinter window
window = tk.Tk()
window.geometry("400x200")
window.title("QR Code Generator")

# Create a label and input field for the data
data_label = tk.Label(window, text="Enter text to encode:")
data_label.place(x=20, y=50)
data_entry = tk.Entry(window, width=30)
data_entry.place(x=150, y=50)

# Create a button to generate the QR code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.place(x=150, y=100)

# Start the window's event loop
window.mainloop()
