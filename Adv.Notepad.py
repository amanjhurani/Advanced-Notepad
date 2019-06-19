from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os
from googletrans import Translator


class Notepad:
    root = Tk()
    # root.wm_iconbitmap("math.ico")
    root.title("Aman_notepad")
    root.geometry("700x400")
    TextArea = Text(root,font = ("arial", 15))

    menubar = Menu(root)
    FileMenu = Menu(menubar,tearoff = 0)
    EditMenu = Menu(menubar,tearoff = 0)
    HelpMenu = Menu(menubar,tearoff = 0)
    LangMenu = Menu(menubar,tearoff = 0)
    CalcMenu = Menu(menubar,tearoff = 0)
    Scrollbar = Scrollbar(TextArea)
    file = None

    def __init__(self):
        # text area resizeable
        self.root.grid_rowconfigure(0,weight = 1)
        self.root.grid_columnconfigure(0,weight = 1)
        self.TextArea.grid(sticky=N+S+E+W)
        # file menu
        self.FileMenu.add_command(label = "New",activebackground="green",command = self.NewFile)
        self.FileMenu.add_command(label = "Save",command = self.savefile)
        self.FileMenu.add_command(label = "Open",command = self.openFile)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label = "Exit", activebackground="red",command = self.quitApplication)
        self.menubar.add_cascade(label = "File", menu = self.FileMenu)
        # Edit Menu Functions
        self.EditMenu.add_command(label="Select all    (Ctrl+A)",command = self.selectAll)
        self.EditMenu.add_command(label="Cut             (Ctrl+X)",command = self.cut)
        self.EditMenu.add_command(label="Copy          (Ctrl+C)",command = self.copy)
        self.EditMenu.add_command(label="Paste          (Ctrl+V)",command = self.paste)
        self.menubar.add_cascade(label = "Help", menu = self.EditMenu)
        # help menu
        self.HelpMenu.add_command(label="About Notepad",command = self.showabout)
        self.menubar.add_cascade(label = "About", menu = self.HelpMenu)

        # language menu
        self.LangMenu.add_command(label="Hindi",command= lambda: self.OnButton("hi"))
        self.LangMenu.add_command(label="Gujarati", command=lambda: self.OnButton("gu"))
        self.LangMenu.add_command(label="Sindhi", command=self.calculate)
        self.menubar.add_cascade(label="Language", menu=self.LangMenu)

        #Calculate
        self.menubar.add_cascade(label="Calculate",command=self.calculate)


        self.root.config(menu = self.menubar)
        self.Scrollbar.pack(side = RIGHT, fill = Y)
        self.Scrollbar.config(command = self.TextArea.yview)
        self.TextArea.config(yscrollcommand = self.Scrollbar.set)
        # all methods

    def openFile(self):
        self.file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files","*.*"),
                                                                            ("text document","*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file)+"-Notepad")
            self.TextArea.delete(1.0,END)
            file = open(self.file,"r")
            self.TextArea.insert(1.0,file.read())
            file.close()
    def NewFile(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.TextArea.delete(1.0,END)
    def savefile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile = "Untitled.txt",
                                          defaultextension = ".txt",
                                          filetypes=[("All Files", "*.*"),("text document", "*.txt")])
            if self.file == "":
                self.file = None
            else:
                file = open(self.file,"w")
                file.write(self.TextArea.get(1.0,END))
                file.close()

                self.root.title(os.path.basename(self.file + "- Notepad"))
        else:
            file = open(self.file,"w")
            file.write(self.TextArea.get(1.0,END))
            file.close()

    def quitApplication(self):
        self.root.destroy()

        #edit menu
    def cut(self):
        self.TextArea.event_generate("<<Cut>>")
    def selectAll(self):
        self.TextArea.event_generate("<<SelectAll>>")
    def copy(self):
        self.TextArea.event_generate("<<Copy>>")
    def paste(self):
        self.TextArea.event_generate("<<Paste>>")

    def showabout(self):
        showerror("Notepad","This is Notepad App")
    def calculate(self):
        a = self.TextArea.get(SEL_FIRST, SEL_LAST)
        ans = eval(a)
        showinfo("Calculated Answer", ans)

    def OnButton(self,lang):
        a = self.TextArea.get(SEL_FIRST, SEL_LAST)
        translator = Translator()
        translated = translator.translate(a, dest=lang)
    #     self.TextArea.config(bg = e,fg = x)
    #     showinfo("Translation : ", translated.text)
        trans = Tk()
        # root.wm_iconbitmap("math.ico")
        trans.title("Translated Text")

        label = Label(trans,text=translated.text)
        label.pack()

        trans.mainloop()


    def run(self):
        self.root.mainloop()
notepad = Notepad()
notepad.run()