import qrcode
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result


comadan_color = (int(54*0.8), int(93*0.8), int(123))
device_id = "COMA867997034737030"
device_type = "NB09-02-01"
device_id_short = device_id[4:]
device_id_readable = " ".join(device_id_short[i:i+2] for i in range(0, len(device_id_short), 2))

print(device_id_readable)

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
qr.add_data("https://config.senti.cloud/onboard/" + device_id + "/" + device_type)


qr.make(fit=True)

img = add_margin(qr.make_image(fill_color=comadan_color, back_color="white"), 0, 0, 100, 0, "white")

draw = ImageDraw.Draw(img)
font_type = ImageFont.truetype("Roboto-Medium.ttf", 61)
font_id = ImageFont.truetype("Roboto-Medium.ttf", 37)
draw.text((4, qr.box_size*38), device_id_short, fill=comadan_color, font=font_id, )
draw.text((00, qr.box_size*32.5), device_type, fill=comadan_color, font=font_type)
img.show()
img.save("image.png")
print(qr.version)
