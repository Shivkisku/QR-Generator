# QR-Generator

This Python code generates a simple GUI (graphical user interface) using the tkinter module, which allows the user to input text and then generates a corresponding QR code.

The GUI has a label and input field for the user to enter the text they want to encode. When the "Generate QR Code" button is clicked, the generate_qr_code() function is called. This function retrieves the text entered by the user, creates a QR code object using the pyqrcode module, and saves the QR code as a PNG file named "code.png" in the current directory.

The generated QR code is saved with a scale of 6, which determines the size of the code. The larger the scale, the larger the QR code will be. Once the QR code is generated, the user can view it in the saved PNG file.

The window's event loop is started using window.mainloop(), which keeps the window open and waits for user input until the user closes the window.



