from PIL import Image, ImageTk

class NewPokemon(tk.Toplevel):
    # ... (其他部分保持不变)

    def show_image(self, img_path):
        try:
            img = Image.open(img_path)
            # 调整图像大小为原始大小的50%
            width, height = img.size
            new_width = int(width * 0.5)
            new_height = int(height * 0.5)
            img = img.resize((new_width, new_height), Image.ANTIALIAS)

            tk_img = ImageTk.PhotoImage(img)

            x_pos = self.winfo_x() + self.winfo_width() + 10
            y_pos = self.winfo_y() + 200

            self.jpg = tk.Toplevel()
            self.jpg.title("樹果類型")
            self.jpg.geometry(f'+{x_pos}+{y_pos}')

            label = tk.Label(self.jpg, image=tk_img)
            label.image = tk_img
            label.pack()
        except FileNotFoundError:
            print("找不到图像")
