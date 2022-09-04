from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename

root=Tk()
root.title("myPDF")
root.geometry("1280x720")
root.configure(bg="black")
root.resizable(True,False)

file_path = ''

def set_file_path(path):
    global file_path
    file_path=path

def open_file():
    path = askopenfilename(filetypes=[('TXT Files','*.txt')])
    with open(path, 'r') as file:
        code = file.read()
        srccode.delete('1.0', END)
        srccode.insert('1.0', code)
        set_file_path(path)

def save():
    if file_path=='':
        path = asksaveasfilename(filetypes=[('TXT Files','*.txt')])
    else:
        path=file_path

    with open(path, 'w') as file:
        code= srccode.get('1.0', END)
        file.write(code)
        set_file_path(path)


#icon
#logo=PhotoImage(file="logo.png")
#root.iconphoto(False, logo)

#code input pane
srccode = Text(root,font="cosolas 18")
srccode.place(x=160,y=0,width=1100,height=700)

#button
Open=PhotoImage(file="C:/Users/Shivam/AppDev/mypdf/open.png")
Save=PhotoImage(file="C:/Users/Shivam/AppDev/mypdf/Save.png")


Button(root, image=Open,bg="#323846",bd=0,command=open_file).place(x=30,y=30)
Button(root, image=Save,bg="#323846",bd=0,command=save).place(x=30,y=130)


root.mainloop()


