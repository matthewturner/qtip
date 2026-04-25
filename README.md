# QTip - Manual QR Code Fixup

Manually fix a corrupt or damaged QR code.

## Features
* Load image as a background and fill in the cells
* Save and load current state if you want to come back to it
* Automatically infer cells from the specified threshold of dark pixels
* Include a border on download
* Change the colour of the overlay
* Double-click to clear a cell

## Usage

1. Fix the perspective of your image using an online tool such as [FixPic](https://picfix.pro/) or [Image Online](https://imageonline.io/perspective-tool/)
2. Clone this repository locally
3. Open the index.html
4. Select your fixed image
5. Fill in the squares
6. Download the fixed up image

## Reverse Usage

Sometimes you have the data and want to see if it's what is contained in the QR Code.

**NB** Outputs version 7 (45x45) QR Codes by default

1. Install the qrcode dependency `pip install qrcode`
2. Add the data to a new file called `input.txt`
3. Run `python ./create.py`
4. Compare the newly generated `version7_qr.jpg` with the original