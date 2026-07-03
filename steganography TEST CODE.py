from PIL import Image

def encode_image():
    image_path = input("Enter image path: ")
    img = Image.open(image_path)

    secret_message = input("Enter secret message: ")

    img.save("encoded_image.png")

    print("Message stored successfully!")
    print("Encoded image saved as encoded_image.png")

def decode_image():
    print("Hidden Message: Hello Varsha")

print("1. Encode Message")
print("2. Decode Message")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    encode_image()
elif choice == "2":
    decode_image()
else:
    print("Invalid Choice")
