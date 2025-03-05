import qrcode

qr = qrcode.QRCode(
        version = 15 , #image 15 means the version of the qr code high the number bigger the code image and complicated picture
        box_size = 10 , # size of the box where qr code will be displayed
        border = 5  # it is the white part of image -- border in all 4 sides with white color
)

data = "https://www.youtube.com/watch?v=h6uMKtwI3Ro"
# as i have given the path of channel like the same way you can give anything
    # if you don't want to redicat and create for channel text that write text in the qr quotes
qr.add_data(data)
qr.make(fit = True )
img = qr.make_image( fill = "black" , back_color = "white")
img.save("ta7an.png")
