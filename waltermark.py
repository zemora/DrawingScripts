from PIL import Image, ImageFont, ImageDraw

def add_water_mark(fname, text):
    img = Image.open(fname)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("QumpellkaNo12.otf", 40)
    w, h = font.getsize(text)
    W, H = img.size
    xy = (W-100-w, H-80-h//2)
    draw.text(xy, text, "yellow", font)
    img.save("watermarked" + fname)
