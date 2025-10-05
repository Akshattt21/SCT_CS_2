from PIL import Image

img = Image.open("input.png")
pixels = img.load()

key = 123
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b = pixels[i, j]
        pixels[i, j] = (r ^ key, g ^ key, b ^ key)

img.save("encrypted.png")
print("✅ Encrypted image saved as encrypted.png")
