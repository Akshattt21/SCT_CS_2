from PIL import Image

img = Image.open("encrypted.png")
pixels = img.load()

key = 50
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b = pixels[i, j]
        pixels[i, j] = (r ^ key, g ^ key, b ^ key)

img.save("decrypted.png")
print("✅ Decrypted image saved as decrypted.png")
