# Text-from-image_-OCR-

This was written just for my convenience but use it how you may like this is basically a script/program that can copy text directly from an image without changing the format of the image thus treating all the text in the image like a single block

This can help you copy code from a youtube video easily without any effort of typing it out ot using google lens

This Python script allows you to extract text from images using Optical Character Recognition (OCR) and provides a graphical user interface (GUI) to interact with the tool. It utilizes the `pytesseract` library for OCR text extraction and the `customtkinter` library for creating a customized Tkinter-based GUI.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `pytesseract` library: You can install it using pip:
    ```
    pip install pytesseract
    ```

## Setup

1. Install the Tesseract OCR engine:
   - Download and install Tesseract OCR from the official website: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
   - Make sure to add the Tesseract installation directory to your system's PATH environment variable.

2. Install the required Python libraries:
   - Install the `Pillow` library (a fork of PIL):
     ```
     pip install Pillow
     ```

   - Install the `customtkinter` library:
     ```
     pip install customtkinter
     ```

## Usage

1. Run the script:
   ```
   python fastcopy.py
   ```

2. GUI Interface:
   - The graphical user interface (GUI) window will open, titled "Get text". The window will have a size of 500x500 pixels.

   - Two buttons are available for text extraction:
     - "Clipboard" button: Extracts text from the image in the clipboard.
     - "From directory" button: Allows you to choose an image file from the operating system to extract text from.

   - Textbox:
     - The extracted text will be displayed in a textbox within the GUI window.

   - Copy button:
     - Clicking the "COPY" button will copy the extracted text to the clipboard.

   - Closing the window:
     - Closing the GUI window will terminate the script.

## Contributing

Contributions to the project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the project's repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

- The `pytesseract` library: [https://github.com/madmaze/pytesseract](https://github.com/madmaze/pytesseract)
- The `customtkinter` library: [https://github.com/harshkhandeparkar/customtkinter](https://github.com/harshkhandeparkar/customtkinter)

## Author
VAIBE
