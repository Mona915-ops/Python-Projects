import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5 / 9
        kelvin = celsius + 273.15
        
        label_celsius_result.config(text=f"Celsius: {celsius:.2f} °C")
        label_kelvin_result.config(text=f"Kelvin: {kelvin:.2f} K")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value for Fahrenheit!")

# Create the main application window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
label_title = tk.Label(root, text="Fahrenheit to Celsius and Kelvin Converter", font=("Arial", 14))
label_title.pack(pady=10)

# Fahrenheit Input
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_fahrenheit = tk.Label(frame_input, text="Enter Fahrenheit: ", font=("Arial", 12))
label_fahrenheit.pack(side=tk.LEFT)

entry_fahrenheit = tk.Entry(frame_input, font=("Arial", 12), width=10)
entry_fahrenheit.pack(side=tk.LEFT)

# Convert Button
button_convert = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_temperature)
button_convert.pack(pady=10)

# Results Labels
label_celsius_result = tk.Label(root, text="Celsius: ", font=("Arial", 12))
label_celsius_result.pack(pady=5)

label_kelvin_result = tk.Label(root, text="Kelvin: ", font=("Arial", 12))
label_kelvin_result.pack(pady=5)

# Run the application
root.mainloop()
