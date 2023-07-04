import tkinter as tk

def convert_weight():
    result_var.set("Your weight in pounds is: " + str(float(input_var.get()) * 2.20462))

window = tk.Tk()
window.title("Weight Converter")

input_var = tk.StringVar()
result_var = tk.StringVar()

instructions_label = tk.Label(window, text="Enter your weight in kilograms:")
input_entry = tk.Entry(window, textvariable=input_var)
convert_button = tk.Button(window, text="Convert", command=convert_weight)
result_label = tk.Label(window, textvariable=result_var)

instructions_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
convert_button.grid(row=1, columnspan=2)
result_label.grid(row=2, columnspan=2)

instructions_label.configure(font=("Arial", 10), fg="#333333")
input_entry.configure(font=("Arial", 10))
convert_button.configure(font=("Arial", 10), fg="#000000", bg="#4CAF50")

window.mainloop()