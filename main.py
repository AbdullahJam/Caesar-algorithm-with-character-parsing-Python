import string
import matplotlib.pyplot as plt

CHARACTER_SET = string.ascii_uppercase + string.ascii_lowercase + "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ"

def caesar_encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char in CHARACTER_SET:
            char_index = (CHARACTER_SET.index(char) + key) % len(CHARACTER_SET)
            cipher_text += CHARACTER_SET[char_index]
        else:
            cipher_text += char
    return cipher_text

def caesar_decrypt(cipher_text, key):
    return caesar_encrypt(cipher_text, -key)

def character_frequency_analysis(cipher_text):
    char_frequency = {char: 0 for char in CHARACTER_SET}
    for char in cipher_text:
        if char in CHARACTER_SET:
            char_frequency[char] += 1
    return char_frequency

def plot_character_frequency(char_frequency):
    fig, ax = plt.subplots()
    ax.bar(char_frequency.keys(), char_frequency.values())
    ax.set_xlabel('Character')
    ax.set_ylabel('Frequency')
    ax.set_title('Character Frequency Analysis')
    plt.show()

def calculate_error_ratio(original_text, decoded_text):
    error_count = 0
    for i in range(len(original_text)):
        if original_text[i] != decoded_text[i]:
            error_count += 1
    return error_count / len(original_text)

def encrypt_text():
    plain_text = input_text.get("1.0", "end-1c")
    key = int(key_entry.get())
    cipher_text = caesar_encrypt(plain_text, key)
    cipher_textbox.delete("1.0", "end")
    cipher_textbox.insert("1.0", cipher_text)
    char_frequency = character_frequency_analysis(cipher_text)
    plot_character_frequency(char_frequency)

def decrypt_text():
    cipher_text = cipher_textbox.get("1.0", "end-1c")
    key = int(key_entry.get())
    plain_text = caesar_decrypt(cipher_text, key)
    plain_textbox.delete("1.0", "end")
    plain_textbox.insert("1.0", plain_text)
    error_ratio = calculate_error_ratio(input_text.get("1.0", "end-1c"), plain_text)
    error_label.config(text="Error Ratio: {:.2%}".format(error_ratio))

# GUI
import tkinter as tk

root = tk.Tk()
root.title("Caesar Cipher")

input_label = tk.Label(root, text="Enter text:")
input_label.grid(row=0, column=0, sticky="w")

input_text = tk.Text(root, height=10)
input_text.grid(row=1, column=0)

key_label = tk.Label(root, text="Enter key (an integer):")
key_label.grid(row=2, column=0, sticky="w")

key_entry = tk.Entry(root)
key_entry.grid(row=3, column=0)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=4, column=0)

cipher_label = tk.Label(root, text="Encrypted text:")
cipher_label.grid(row=5, column=0, sticky="w")

cipher_textbox = tk.Text(root, height=10)
cipher_textbox.grid(row=6, column=0)

analysis_button = tk.Button(root, text="Character Frequency Analysis", command=lambda: plot_character_frequency(character_frequency_analysis(cipher_textbox.get("1.0", "end-1c"))))
analysis_button.grid(row=7, column=0)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=8, column=0)

plain_label = tk.Label(root, text="Decrypted text:")
plain_label.grid(row=9, column=0, sticky="w")

plain_textbox = tk.Text(root, height=10)
plain_textbox.grid(row=10, column=0)

error_label = tk.Label(root, text="")
error_label.grid(row=11, column=0)

root.mainloop()