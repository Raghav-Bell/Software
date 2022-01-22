import tkinter as tk
window=tk.Tk()
window.title("Convertor")
window.rowconfigure(0, minsize=20)
window.columnconfigure([0,1,2 ,3,4] , minsize=5)

def con():
  p=float(ent.get())
  c=(5/9)*(p-32)
  label3["text"]=str(round(c ,2))+"\N{DEGREE CELSIUS}"
  label4["text"]=str(c+273.15)+" " +"K"
  
ent=tk.Entry( width=10)
label1=tk.Label(text="\N{DEGREE FAHRENHEIT}")
but=tk.Button(text="\N{RIGHTWARDS BLACK ARROW}" ,command=con)
label3=tk.Label(text="\N{DEGREE CELSIUS}" )
label4=tk.Label(text="K")

ent.grid(row=0, column=0 , sticky="we" , padx=10)
label1.grid(row=0, column=1 , sticky="we" ,pady=10)
but.grid(row=0, column=2 , sticky="we" , padx=10)
label3.grid(row=0, column=3 , sticky="we" , padx=10)
label4.grid(row=0,column=4,sticky="we", padx=10)

window.mainloop()
