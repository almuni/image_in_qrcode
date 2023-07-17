import qrcode
from PIL import Image
# taking image which user wants
# in the QR code center
Logo_link = '' # Here you insert the images path
logo = Image.open(Logo_link)

basewidth = 100  # taking base width

wpercent = (basewidth/float(logo.size[0])) # adjust image size
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H)

text_in_qr = '' # Here you can add your text that will be inserted into the qr code

QRcode.add_data(text_in_qr) # adding text_in_qr or text to QRcode

QRcode.make() # generating QR code

QRcolor = 'Green' # taking color name from user

QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB') # adding color to QR code

pos = ((QRimg.size[0] - logo.size[0]) // 2, # set size of QR code
	(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

QRimg.save('gfg_QR.png')
print('QR code generated!') # save the QR code generated
