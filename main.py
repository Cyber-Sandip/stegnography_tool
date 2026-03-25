
import os
import struct
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk  

MAGIC = b"STEGOv2"


def hide_files_in_jpg(cover_path, secret_files, output_path):
    with open(cover_path, "rb") as f:
        cover_data = f.read()

    header = bytearray()
    header += MAGIC
    header += struct.pack(">I", len(secret_files))

    payload = bytearray()
    for filepath in secret_files:
        with open(filepath, "rb") as f:
            filedata = f.read()

        filename = os.path.basename(filepath).encode("utf-8")
        header += struct.pack(">I", len(filename))
        header += filename
        header += struct.pack(">I", len(filedata))
        payload += filedata

    with open(output_path, "wb") as f:
        f.write(cover_data)
        f.write(header)
        f.write(payload)

    messagebox.showinfo("✅ Success", f"Hidden {len(secret_files)} files inside:\n{output_path}")


def extract_files_from_jpg(stego_path, output_dir="."):
    with open(stego_path, "rb") as f:
        data = f.read()

    marker = b"\xff\xd9"
    idx = data.find(marker)
    if idx == -1:
        messagebox.showerror("❌ Error", "Not a valid JPEG file!")
        return

    hidden = data[idx+2:]
    if not hidden.startswith(MAGIC):
        messagebox.showerror("❌ Error", "No hidden data found!")
        return

    pos = len(MAGIC)
    file_count = struct.unpack(">I", hidden[pos:pos+4])[0]
    pos += 4

    file_meta = []
    for _ in range(file_count):
        name_len = struct.unpack(">I", hidden[pos:pos+4])[0]
        pos += 4
        filename = hidden[pos:pos+name_len].decode("utf-8")
        pos += name_len
        file_len = struct.unpack(">I", hidden[pos:pos+4])[0]
        pos += 4
        file_meta.append((filename, file_len))


    extracted_files = []
    for filename, file_len in file_meta:
        filedata = hidden[pos:pos+file_len]
        pos += file_len
        out_path = os.path.join(output_dir, filename)
        with open(out_path, "wb") as f:
            f.write(filedata)
        extracted_files.append(out_path)

    messagebox.showinfo("✅ Success", f"Extracted {len(extracted_files)} files to:\n{output_dir}")


                                        # ==== GUI Part ====
def choose_cover_and_hide():
    cover = filedialog.askopenfilename(title="Select Cover JPG", filetypes=[("JPEG Images", "*.jpg;*.jpeg")])
    if not cover:
        return
    files = filedialog.askopenfilenames(title="Select Files to Hide")
    if not files:
        return
    output = filedialog.asksaveasfilename(title="Save Stego JPG As", defaultextension=".jpg",
                                          filetypes=[("JPEG Image", "*.jpg")])
    if not output:
        return
    hide_files_in_jpg(cover, files, output)


def choose_stego_and_extract():
    stego = filedialog.askopenfilename(title="Select Stego JPG", filetypes=[("JPEG Images", "*.jpg;*.jpeg")])
    if not stego:
        return
    out_dir = filedialog.askdirectory(title="Select Output Folder")
    if not out_dir:
        return
    extract_files_from_jpg(stego, out_dir)


def main():
    #dark mode
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("Stegnography Tool")
    root.geometry("450x280")
    root.configure(bg="black")

    # Title
    title = ctk.CTkLabel(root, text="Steganography Tool",
                         font=("Orbitron", 24, "bold"), text_color="#00ffcc", bg_color="black")
    title.pack(pady=20)

    # Stylish Buttons
    btn_hide = ctk.CTkButton(root, text="🔒 Hide Files in JPG", command=choose_cover_and_hide,
                             fg_color="#00ff99", hover_color="#00cc77", text_color="black",
                             corner_radius=20, width=280, height=55,
                             font=("Consolas", 16, "bold"))
    btn_hide.pack(pady=12)

    btn_extract = ctk.CTkButton(root, text="🔓 Extract Files from JPG", command=choose_stego_and_extract,
                                fg_color="#00aaff", hover_color="#0088cc", text_color="black",
                                corner_radius=20, width=280, height=55,
                                font=("Consolas", 16, "bold"))
    btn_extract.pack(pady=12)

    # Footer
    footer = ctk.CTkLabel(root, text="Made by Sandip Hazra",
                          font=("Consolas", 12), text_color="#E1DADA", bg_color="black")
    footer.pack(side="bottom", pady=12)

    root.mainloop()


if __name__ == "__main__":
    main()
