import tkinter as tk 
from tkinter.filedialog import askopenfilename , asksaveasfilename
window = tk.Tk()
window.title("Texter")

window.rowconfigure([0,1],minsize=20 , weight=1)
window.columnconfigure([0,1] ,minsize=25,weight=1)

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Texter - {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Texter - {filepath}")
    
frame=tk.Frame(master=window)
but_open=tk.Button(master=frame ,text="Open" ,width=10 ,fg="white" ,bg="blue" , command=open_file)
but_save=tk.Button(master=frame ,text="Save As" ,width=10  ,fg="white" ,bg="green", command=save_file)

frame2=tk.Frame(master=window)
txt_edit=tk.Text(master=frame2)

but_open.grid(row=0, column=0, sticky="w" , padx=10 , pady=15)
but_save.grid(row=1, column=0, sticky="w" , padx=10 )
txt_edit.grid(row=0 , column=0 ,sticky="e" ,padx=5)
frame.grid(row=0, column=0, sticky="news")
frame2.grid(row=0, column=1, sticky="news")

window.mainloop()
