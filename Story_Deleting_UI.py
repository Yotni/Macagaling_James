import tkinter as tk
from tkinter import messagebox
from Dictionary_of_Stories import Personal_load_data
from Story_Deleting import Story_Deleting


def Del_Popup_Container(right_panel, parent_tab):
    # ===== BUTTON =====
    Del_button = tk.Button(
        right_panel,
        text="Delete",
        bg="#8A2BE2",
        fg="white",
        activebackground="#D6B3FF",
        activeforeground="white",
        relief="groove",
        font=("Courier", 18, "bold")
    )
    Del_button.pack(side="left", expand=True, fill="x", padx=10)

    # popup frame
    Del_box = tk.Frame(parent_tab, bg="#8A2BE2")

    # CONTENT FRAME (directly inside popup)
    content_frame = tk.Frame(Del_box, bg="#8A2BE2")
    content_frame.pack(fill="both", expand=True)

    # POPUP TOGGLE
    box_visible = False

    def toggle_popup():
        nonlocal box_visible

        if box_visible:
            Del_box.place_forget()
            Del_button.config(bg="#8A2BE2")
            box_visible = False
        else:
            Del_box.place(relx=0.635, rely=0.23, relwidth=0.35, relheight=0.4)
            Del_button.config(bg="#D6B3FF")
            box_visible = True

    Del_button.config(command=toggle_popup)

    return content_frame

def deleting_Story_Box(content_frame):
    inner_box_line = tk.Frame(
        content_frame,
        bg="#8A2BE2",
        highlightbackground="white",
        highlightthickness=1
    )
    inner_box_line.pack(anchor="center", padx=20, pady=20, fill="x")

    DeleteBox(inner_box_line)
    return inner_box_line

class DeleteBox:
    def __init__(self, parent):
        self.parent = parent
        self.personal_library = Personal_load_data()

        self.Story_Deleting()

    def Story_Deleting(self):

        self.delete_container = tk.Frame(self.parent, bg="#8A2BE2", highlightcolor="#FFFFFF" )
        self.delete_container.pack(padx=20, pady=20, fill="both")

        def Infos_Containers():
            frame = tk.Frame(self.delete_container, bg="#8A2BE2", highlightthickness=1, highlightbackground="white", padx=5, pady=5
            )
            frame.pack(fill="both", pady=5)
            return frame

        # for label waht do to delet
        tk.Label(
            self.delete_container,
            text="Which Story ID do you want to delete:",
            font=("Courier", 15, "bold"),
            bg="#8A2BE2",
            fg="white"
        ).pack(side="top")

        # for inputting numbers ID
        story_select = Infos_Containers()

        tk.Label(
            story_select,
            text="Story:",
            font=("Courier", 15, "bold"),
            bg="#8A2BE2",
            
            fg="white"
        ).pack(anchor="sw")

        self.story_number_entry = tk.Entry(
            story_select,
            font=("Arial", 15),
            bg="#D6B3FF"
        )
        self.story_number_entry.pack(fill="x")

        # button for deleting
        DEL_STORY = tk.Button(self.delete_container, text="DELETE STORY", bg="#D6B3FF", 
                              fg="White", font=("Arial", 12, "bold"), relief="groove", 
                              command=self.run_delete
        )
        DEL_STORY.pack(pady=10)

    
    def run_delete(self):

        story_number = self.story_number_entry.get().strip()
        id_key = f"Story {story_number}"

        # refresh latest data
        self.personal_library = Personal_load_data()

        # SAFETY CHECK (IMPORTANT)
        if not story_number:
            messagebox.showwarning("Input Error", "Please enter a story number or ID.")
            return
        
        if id_key not in self.personal_library:
            messagebox.showerror("Error", F"Story ID [{id_key}] does not exist!")
            return

        story_title = self.personal_library[id_key].get("Title", "Unknown")

        # CONFIRM POPUP
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Do you want to delete Story: {story_title}?"
        )

        if not confirm:
            messagebox.showinfo("Cancelled", "Deletion Cancelled")
            return

        # CALL BACKEND
        result = Story_Deleting(
            self.personal_library,
            story_number,
            Confirm="Y",
            Delete_Another="N"
        )

        # ERROR HANDLING
        if isinstance(result, str):
            messagebox.showerror("Error", result)
            return

        # SUCCESS
        messagebox.showinfo("Success", result["result"])

        # refresh memory
        self.personal_library = result["library"]

        # clear input
        self.story_number_entry.delete(0, tk.END)