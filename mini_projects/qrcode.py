import qrcode
url=input("entre your url:- ")
name= input("entre your file name ")
img = qrcode.make(url)
type(img)  # qrcode.image.pil.PilImage
img.save("qr_code.png")