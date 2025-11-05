import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

df = pd.read_csv("birth_and_death_2017.csv")

df["Родилось"] = pd.to_numeric(df["Родилось"], errors="coerce")
df["Умерло"] = pd.to_numeric(df["Умерло"], errors="coerce")

years = sorted(df["Год"].unique())

root = tk.Tk()
root.title("Рождение и смертность (1950–2016)")
root.geometry("1100x700")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

check_frame = tk.LabelFrame(root, text="Выберите года", padx=10, pady=10)
check_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

plot_frame = tk.Frame(root)
plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(top_frame, text="Тип данных:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
type_combo = ttk.Combobox(top_frame, values=["Все", "Городское", "Сельское"], state="readonly", width=15)
type_combo.set("Все")
type_combo.pack(side=tk.LEFT, padx=5)

selected_years = {year: tk.BooleanVar(value=True) for year in years}
canvas = None  # для хранения текущего графика


def plot_graph():
    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()

    fig, ax = plt.subplots(figsize=(8, 5))

    selection = type_combo.get()
    active_years = [year for year, var in selected_years.items() if var.get()]

    if not active_years:
        ax.text(0.5, 0.5, "Нет выбранных годов", ha="center", va="center", fontsize=14)
        ax.axis("off")
    else:
        data = df[df["Год"].isin(active_years)]

        if selection == "Все":
            city = data[data["Тип"] == "Городское"]
            rural = data[data["Тип"] == "Сельское"]

            ax.plot(city["Год"], city["Родилось"], color="blue", label="Родилось (Городское)")
            ax.plot(city["Год"], city["Умерло"], color="orange", label="Умерло (Городское)")
            ax.plot(rural["Год"], rural["Родилось"], color="blue", linestyle="--", label="Родилось (Сельское)")
            ax.plot(rural["Год"], rural["Умерло"], color="orange", linestyle="--", label="Умерло (Сельское)")
        else:
            data = data[data["Тип"] == selection]
            ax.plot(data["Год"], data["Родилось"], color="blue", label="Родилось")
            ax.plot(data["Год"], data["Умерло"], color="orange", label="Умерло")

        ax.set_xlabel("Год")
        ax.set_ylabel("Человек")
        ax.set_title(f"Демографические данные: {selection.lower()}")
        ax.legend()
        ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def toggle_year(_=None):
    plot_graph()


for i, year in enumerate(years):
    cb = tk.Checkbutton(check_frame, text=str(year), variable=selected_years[year],
                        command=toggle_year)
    cb.grid(row=i // 3, column=i % 3, sticky="w")

btn = tk.Button(top_frame, text="Обновить график", command=plot_graph)
btn.pack(side=tk.LEFT, padx=10)

plot_graph()

root.mainloop()
