"A Desktop program where you can upload images and add a watermark"
#solution 
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        # Header
        header = tk.Label(root, text="Watermark App", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
        header.pack(pady=20)

        # Image frame
        self.image_frame = tk.Frame(root, bg="#f0f0f0")
        self.image_frame.pack(pady=10)

        # Create upload button
        self.upload_button = tk.Button(self.image_frame, text="Upload Image", command=self.upload_image, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.upload_button.pack()

        # Watermark input
        self.label = tk.Label(root, text="Enter Watermark Text:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
        self.text_entry.pack(pady=5)

        # Add and save buttons
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        self.add_button = tk.Button(button_frame, text="Add Watermark", command=self.add_watermark, font=("Helvetica", 12), bg="#008CBA", fg="white", padx=10, pady=5)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.save_button = tk.Button(button_frame, text="Save Image", command=self.save_image, font=("Helvetica", 12), bg="#f44336", fg="white", padx=10, pady=5)
        self.save_button.pack(side=tk.RIGHT, padx=10)

        self.image_label = tk.Label(self.image_frame, bg="#f0f0f0")
        self.image_label.pack(pady=10)

        self.image = None
        self.watermarked_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)
            messagebox.showinfo("Image Upload", "Image uploaded successfully!")

    def display_image(self, img):
        img.thumbnail((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def add_watermark(self):
        if self.image:
            watermark_text = self.text_entry.get()
            if watermark_text:
                self.watermarked_image = self.image.copy()
                draw = ImageDraw.Draw(self.watermarked_image)
                font = ImageFont.truetype("arial.ttf", 36)

                text_width, text_height = draw.textsize(watermark_text, font)
                width, height = self.watermarked_image.size

                x = width - text_width - 10
                y = height - text_height - 10

                draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
                self.display_image(self.watermarked_image)
                messagebox.showinfo("Watermark", "Watermark added successfully!")
            else:
                messagebox.showerror("Error", "Please enter a watermark text.")
        else:
            messagebox.showerror("Error", "Please upload an image first.")

    def save_image(self):
        if self.watermarked_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("BMP files", "*.bmp")])
            if file_path:
                self.watermarked_image.save(file_path)
                messagebox.showinfo("Save Image", "Image saved successfully!")
        else:
            messagebox.showerror("Error", "Please add a watermark before saving.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
