import requests
import customtkinter
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("300x300")
root.title("Population Data Fetcher")

countries_input = []
with open("countries.text", "r") as countries:
    for country in countries:
        countries_input.append(country.strip())

def Optionmenu_Callback(choice):
    name = choice
    country_name = name.capitalize()
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    country_data = response.json()[0]

    population = country_data["population"]
    capital = country_data["capital"][0]
    area = country_data["area"]

    messagebox.showinfo(title=f"{country_name}", message=f" Capital: {capital}, Population: {population}, Area: {area} km²")
def Country_Result():
    name = entry.get()

    if len(name) == 0:
            messagebox.showerror(title="Error!", message="Please enter all information.")
    else:
        try:
            country_name = name.capitalize()
            response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
            country_data = response.json()[0]

            population = country_data["population"]
            capital = country_data["capital"][0]
            area = country_data["area"]
            messagebox.showinfo(title=f"{country_name}", message=f" Capital: {capital}, Population: {population}, Area: {area} km²")
        except KeyError:
            messagebox.showerror(title="Error!", message="Please make sure that the information entered is correct.")
        finally:
            entry.delete(0, "end")

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=15,padx=20,fill="both",expand=True)

lable=customtkinter.CTkLabel(master=frame,text="Population Data Fetcher")
lable.pack(pady=15,padx=5)

entry=customtkinter.CTkEntry(master=frame)
entry.pack(pady=5,padx=20)

check=customtkinter.CTkButton(master=frame,text="Results",command=Country_Result)
check.pack(pady=10,padx=20,side="top")

option_menu=customtkinter.CTkOptionMenu(frame,values=countries_input,command=Optionmenu_Callback)
option_menu.pack(pady=10,padx=10)
option_menu.set("Countries")


root.mainloop()