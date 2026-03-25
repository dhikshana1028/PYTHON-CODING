import qrcode
x=qrcode.QRCode()
msg="CKCET students are very very SMART !!!"
x.add_data(msg)
x.make(fit=True)
res=x.make_image(fill_color="black",back_color="white")
res.save("news.png")
print("created successfully !")