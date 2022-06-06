from PIL import Image

def convert_to_array(photo):
    r, g, b = photo.split()
    pixels = {}

    pixels[0] = list(r.getdata())
    pixels[1] = list(g.getdata())
    pixels[2] = list(b.getdata())

    return pixels

def convert_to_B_and_W_single_treshold(photo, treshold):
    pixels = convert_to_array(photo)
    photo = photo.convert("L")
    width, height = photo.size
    pix_arr = []
    for n in range(height * width):
        if (pixels[0][n] + pixels[1][n] + pixels[2][n]) / 3 > treshold:
            pix_arr.append(255)
        else:
            pix_arr.append(0)
    photo.putdata(pix_arr)
    return photo

def convert_to_B_and_W_double_treshold(photo, treshold1, treshold2):
    pixels = convert_to_array(photo)
    photo = photo.convert("L")
    width, height = photo.size
    pix_arr = []
    for n in range(height * width):
        if treshold1 < (pixels[0][n] + pixels[1][n] + pixels[2][n]) / 3 < treshold2:
            pix_arr.append(255)
        else:
            pix_arr.append(0)
    photo.putdata(pix_arr)
    return photo


if __name__ == '__main__':
    # imagine location
    photo = Image.open("yoda.jpeg")

    choice = int(input("Entrer 1 for single treshold and 2 for double"))
    while choice != 1 and choice != 2:
        choice = int(input("Entrer 1 for single treshold and 2 for double"))

    treshold1 = int(input("Entrer the treshold"))
    while not 0 <= treshold1 <= 255:
        treshold1 = int(input("Entrer the treshold"))

    if choice == 1:
        new_img = convert_to_B_and_W_single_treshold(photo, treshold1)
    elif choice == 2:

        treshold2 = int(input("Entrer second treshold"))
        while not 0 <= treshold2 <= 255 or treshold2 < treshold1:
            treshold2 = int(input("Entrer second treshold"))

        new_img = convert_to_B_and_W_double_treshold(photo, treshold1, treshold2)

    new_img.show()