import tkinter as tk
root=tk.Tk()

root.title('Adrian')


x=['Paul','Kamash','Bolo']

def names(): 
    for names in x:
     print (names)
button=tk.Button(root,text="names",command=names)
button.pack()
root.mainloop()
    