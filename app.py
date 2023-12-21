from tkinter import Tk, Label, Button, filedialog, Canvas, StringVar
from PIL import Image, ImageTk
from image_processing.core import resize_and_compress

class ImageProcessor:
    def __init__(self):
        self.input_path = ""
        self.output_path = ""

    def upload_image(self):
        self.input_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        return self.input_path

    def convert_and_save(self, default_name_var):
        if self.input_path:
            self.output_path = filedialog.asksaveasfilename(
                initialfile=default_name_var.get(),
                defaultextension=".jpg",
                filetypes=[("JPEG files", "*.jpg")]
            )
            if self.output_path:
                resize_and_compress(self.input_path, self.output_path)

class DarkThemeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Resizer")
        self.master.minsize(400, 600)
        self.master.configure(bg="#2E2E2E")

        # Center the window on the screen
        window_width = 400
        window_height = 600
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 4  # Adding some margin to the top
        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.image_processor = ImageProcessor()

        self.label = Label(master, text="Select an image:", bg="#2E2E2E", fg="white")
        self.label.pack()

        self.upload_button = Button(master, text="Upload Image", command=self.upload_image, bg="#454545", fg="white")
        self.upload_button.pack()

        self.canvas = Canvas(master, bg="#2E2E2E", width=300, height=300)
        self.canvas.pack()

        self.default_name_var = StringVar(value="resized-image")  # Default name for the saved image

        self.convert_button = Button(master, text="Convert and Save", command=self.convert_and_save, bg="#454545", fg="white")
        self.convert_button.pack()

    def upload_image(self):
        input_path = self.image_processor.upload_image()
        if input_path:
            self.show_image(input_path)

    def convert_and_save(self):
        if self.image_processor.input_path:
            self.image_processor.convert_and_save(self.default_name_var)

    def show_image(self, input_path):
        image = Image.open(input_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)

        self.canvas.delete("all")
        self.canvas.create_image(150, 150, image=photo)
        self.canvas.image = photo

if __name__ == "__main__":
    root = Tk()
    app = DarkThemeApp(root)
    root.mainloop()
