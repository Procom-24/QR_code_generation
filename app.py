import pyqrcode
object = input("Enter your email: ")
qr=pyqrcode.create(object)
name=object+".png"
qr.png(name)