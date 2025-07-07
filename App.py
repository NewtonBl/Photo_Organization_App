import Sort
import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

directory = ""

        

class App(ctk.CTk):

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="Select Folder", initialdir="/")
        if folder_path:
            global directory
            directory = folder_path

    def sort_photos(self):
        global directory
        if directory:
            try:
                Sort.sort(directory)
                self.label3.configure(text="Photos sorted successfully!")
            except Exception as e:
                self.label3.configure(text=f"Error sorting photos.")
        else:
            self.label3.configure(text="Please select a folder first.")
    
    def __init__(self):
        super().__init__()

        w = 600
        h = 300
        padding = 5

        self.title("Photo Sorting App")
        self.geometry(f"{w}x{h}")
        self.grid_propagate(False)

        self.frame = ctk.CTkFrame(self, width=w-2*padding, height=h-2*padding)
        self.frame.grid(row=0, column=0, padx=padding, pady=padding)
        self.frame.columnconfigure((0,1), weight=1)
        self.frame.grid_propagate(False)

        self.label1 = ctk.CTkLabel(self.frame, text="Welcome to the photo sorting app.", font=("Roboto", 20))
        self.label1.grid(row=0, column=0, padx=10, pady=(20,10), sticky="ew", columnspan=2)

        self.label2 = ctk.CTkLabel(self.frame, text="First, choose a folder to sort photos:", font=("Roboto", 20))
        self.label2.grid(row=1, column=0, padx=10, pady=(30,10), sticky="w")

        self.folder_button = ctk.CTkButton(self.frame, text="Select Folder", command=self.select_folder)
        self.folder_button.grid(row=1, column=1, padx=10, pady=(30,10), sticky="ew")

        self.sort_button = ctk.CTkButton(self.frame, text="Sort Photos", command=self.sort_photos)
        self.sort_button.grid(row=2, column=0, columnspan=2, padx=10, pady=(30,10))

        self.label3 = ctk.CTkLabel(self.frame, text="Confirmation will appear once program completes.", font=("Roboto", 20))
        self.label3.grid(row=3, column=0, padx=10, pady=(30,10), columnspan=2)


if __name__ == "__main__":
    app = App()
    app.mainloop()