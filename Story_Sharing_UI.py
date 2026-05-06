import tkinter as tk
from tkinter import messagebox
from Dictionary_of_Stories import Personal_load_data
from Story_Sharing import Share_Personal_list

    
def Share_Popup_Container(right_panel, parent_tab):
    Share_button = tk.Button(right_panel, text="Share", bg="#8A2BE2", fg="white", activebackground="#D6B3FF",
        activeforeground="white", relief="groove", font=("Courier", 18, "bold")
    )
    Share_button.pack(side="left", expand=True, fill="x", padx=10)

    Share_box = tk.Frame(parent_tab, bg="#8A2BE2")

    content_frame = tk.Frame(Share_box, bg="#8A2BE2")
    content_frame.pack(fill="both", expand=True)

    box_visible = False

    def toggle_popup():
        nonlocal box_visible
        if box_visible:
            Share_box.place_forget()
            Share_button.config(bg="#8A2BE2")
            box_visible = False
        else:
            Share_box.place(relx=0.635, rely=0.23, relwidth=0.35, relheight=0.4)
            Share_button.config(bg="#D6B3FF")
            box_visible = True

    Share_button.config(command=toggle_popup)

    return content_frame

def Share_Story_Box(content_frame):
    inner_box_line = tk.Frame(
        content_frame,
        bg="#8A2BE2",
        highlightbackground="#ffffff",
        highlightthickness=1
    )
    inner_box_line.pack(anchor="center", padx=20, pady=20, fill="x")

    ShareBox(inner_box_line)
    return inner_box_line

class ShareBox:
    def __init__(self, parent):
        self.parent = parent
        self.Story_Sharing()

    def Story_Sharing(self):
        title = tk.Label(
            self.parent,
            text="Share Story by Number or ID",
            bg="#8A2BE2",
            fg="#ffffff",
            font=("courier", 18, "bold")
        )
        def Infos_Containers():
            Infos_Container = tk.Frame(self.parent, bg="#8A2BE2", 
                                       highlightthickness=1, highlightcolor="#ffffff", padx=5, pady=5)
            Infos_Container.pack(fill="both", pady=5, padx=20)

            return Infos_Container
        
        # story id title
        title.pack(pady=15)
        Share_Box = Infos_Containers()
        instruction = tk.Label(
            Share_Box,
            text="Enter story ID:",
            bg="#8A2BE2",
            fg="white",
            font=("courier", 12)
        )
        instruction.pack(pady=10,)

        # typing of story id
        self.entry = tk.Entry(
            Share_Box,
            font=("courier", 14),
            justify="center",
            bg="#D6B3FF"
        )
        self.entry.pack(fill="x", pady=10, ipady=5)
        
        # share burron
        share_btn = tk.Button(
            self.parent,
            text="Share",
            bg="#D6B3FF",
            fg="white",
            font=("courier", 14, "bold"),
            relief="groove",
            command=self.share_story
        )
        share_btn.pack(pady=10)

    def share_story(self):
        user_input = self.entry.get().strip()

        if not user_input:
            messagebox.showwarning("Input Error", "Please enter a story number or ID.")
            return

        # Allow both "3" and "Story 3"
        if user_input.lower().startswith("story"):
            story_number = user_input.split(" ")[1]
        else:
            story_number = user_input

        Personal_Library = Personal_load_data()
        Story_ID = f"Story {story_number}"

        if Story_ID not in Personal_Library:
            messagebox.showerror("Not Found", f"{Story_ID} not found in Personal Library.")
            return

        Share_Personal_list(story_number)
        messagebox.showinfo("Success", f"{Story_ID} shared to Public Library!")
        self.entry.delete(0, tk.END)