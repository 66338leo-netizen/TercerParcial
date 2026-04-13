import customtkinter

def button_callback():
    print("Button Pressed")

app=customtkinter.CTk()
app.title("ay app")
app.geometry("400x150")
app.grid_columnconfigure((0),weight=1)

button=customtkinter.CTkButton(app,text="ay button",command=button_callback)
button.grid(row=0, column=0, padx=20,pady=20)
checkbox_1=customtkinter.CTkButton(app,text="ay button",command=button_callback)
checkbox_1.grid(row=0, column=0, padx=20,pady=20)
checkbox_2=customtkinter.CTkButton(app,text="ay button",command=button_callback)
checkbox_2.grid(row=1, column=1, padx=20,pady=20)

app.mainloop()
