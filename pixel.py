from PIL import Image
import numpy as np

def image_cryptor(image_path, key, mode):
    img = Image.open(image_path)
    img_array = np.array(img)
    key = np.resize(key, img_array.shape)

    if mode == 'encrypt':
        crypted_array = np.bitwise_xor(img_array, key)
        crypted_img = Image.fromarray(crypted_array)
        crypted_img.save("encrypted_image.png")
        print("Image encrypted successfully.")
    elif mode == 'decrypt':
        decrypted_array = np.bitwise_xor(img_array, key)
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully.")
    else:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")


def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

    image_path = input("Enter Path Of Image File: ")
    key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)

    image_cryptor(image_path, key, 'encrypt')
    image_cryptor("encrypted_image.png", key, 'decrypt')


if __name__ == "__main__":
    main()
input("Press Enter to exit...")