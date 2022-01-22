import tkinter as tk
win3 =tk.Tk()
win3.title("Collatz Conjecture ")
win3.rowconfigure(0, minsize=20 ,weight=1)
win3.columnconfigure([0,1,2], minsize=30,weight=1)


def collatz_cyc(): 
        
    k=0
    m=label2["text"]
    p=ent.get()
    n=int(p)          
    while n!=1:
        
        if(n%2==0):
            n=n/2
            #print(n)
            
        else:
            n=(3*n+1)/2
            #print(n)
        k=k+1
   
    label2["text"]="Cycles:" +" "+ str(k)
    

def collatz_print(): 
        
    
    
    p=ent.get()
    n=int(p)          
    while n!=1:
        
        if(n%2==0):
            n=n/2
            print(n)
            
        else:
            n=(3*n+1)/2
            print(n)
        
   
    
 
frame=tk.Frame(master=win3)
label=tk.Label(master=frame ,text="Enter a natural number: ")
ent=tk.Entry(master=frame  , width=10)

frame2=tk.Frame(master=win3)
label2=tk.Label(master=frame2 , text="Cycles: ")
but1=tk.Button(master=frame2 , text="Calculate", fg="white", bg="green", command=collatz_cyc)
but2=tk.Button(master=frame2, text="Print", fg="white",bg="blue" ,command=collatz_print)

frame.grid(row=0,column=0 , sticky="news")
label.grid(row=0,column=0 , sticky="w")
ent.grid(row=0, column=1, sticky="we")

frame2.grid(row=1,column=0 , sticky="news")
label2.grid(row=0,column=0,sticky="w", padx=20)
but1.grid(row=1,column=1,sticky="e", padx=5)
but2.grid(row=1,column=2,sticky="e", padx=5)



win3.mainloop()
