from PIL import Image

END_MARKER = "#####"

def encode():
    image_path = input("Enter image path: ")

    try:
        img = Image.open(image_path).convert("RGB")
    except Exception:
        print("Unable to open image.")
        return

    message = input("Enter secret message: ") + END_MARKER

    binary = ''.join(format(ord(c), '08b') for c in message)

    pixels = img.load()
    width, height = img.size

    if len(binary) > width * height:
        print("Message is too long for this image.")
        return

    index = 0

    for y in range(height):
        for x in range(width):
            if index >= len(binary):
                break

            r, g, b = pixels[x, y]

            r = (r & 254) | int(binary[index])

            pixels[x, y] = (r, g, b)

            index += 1

        if index >= len(binary):
            break

    output = "encoded_image.png"
    img.save(output)

    print("\nMessage hidden successfully!")
    print("Encoded image saved as:", output)


def decode():
    image_path = input("Enter encoded image path: ")

    try:
        img = Image.open(image_path).convert("RGB")
    except Exception:
        print("Unable to open image.")
        return

    pixels = img.load()
    width, height = img.size

    binary = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary += str(r & 1)

    message = ""

    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]

        if len(byte) < 8:
            break

        char = chr(int(byte, 2))
        message += char

        if message.endswith(END_MARKER):
            break

    if END_MARKER in message:
        print("\nHidden Message:")
        print(message.replace(END_MARKER, ""))
    else:
        print("No hidden message found.")


while True:

    print("\n===== IMAGE STEGANOGRAPHY TOOL =====")
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        encode()

    elif choice == "2":
        decode()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
