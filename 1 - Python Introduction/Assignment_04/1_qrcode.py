import qrcode

text = input('Please Enter Text: ')
data = qrcode.make('eiliya')
data.save('qrcode.png')