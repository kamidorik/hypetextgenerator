from PIL import Image, ImageDraw, ImageFont

done = True

while done == True:
    text = input('Insert text: ')
    if text == "Stop":
        done = False
    else:
        img = Image.open("hype.jpg")
        w, h = img.size
        color = (0, 0, 0)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("ARICYRBI.TTF", 64)
        draw.text((160, 156),text,(216, 2, 178),font=font)
        draw.text((155, 154),text,(255, 255, 255), font=font)
        img.save('text2.png')
        img.show()