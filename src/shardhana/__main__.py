import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Shardhana 0.0.1.post3")
    root.geometry("400x100")

    label = tk.Label(root, text="Hello Shardhana !!!")
    label.pack(padx=20, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()