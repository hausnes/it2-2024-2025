import tkinter as tk
from PIL import Image, ImageTk

# Funksjon for å vise bildet
def vis_bilde():
    bilde = Image.open(frame.bilder[frame.bilde_index])
    bilde = bilde.resize((400, 400), Image.Resampling.LANCZOS)
    bilde_tk = ImageTk.PhotoImage(bilde)
    frame.bilde_label.config(image=bilde_tk)
    frame.bilde_label.image = bilde_tk  # Behold referansen til bildet

# Funksjon for å gå til forrige bilde
def forrige_bilde():
    frame.bilde_index = (frame.bilde_index - 1) % len(frame.bilder)
    vis_bilde()

# Funksjon for å gå til neste bilde
def neste_bilde():
    frame.bilde_index = (frame.bilde_index + 1) % len(frame.bilder)
    vis_bilde()

# Opprett et vindu og sett tittel og størrelse
root = tk.Tk()
root.title("Biletframvisar")
root.geometry("450x550")

# Opprett en hovedramme for applikasjonen
frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Legg til en overskrift
overskrift = tk.Label(frame, text="Biletframvisar", font=("Arial", 24))
overskrift.grid(row=0, column=0, columnspan=2, pady=10)

# Liste over bilder
frame.bilder = [
    "bilde1.jpg",
    "bilde2.jpg",
    "bilde3.jpg"
]
frame.bilde_index = 0

# Vis det første bildet
bilde = Image.open(frame.bilder[frame.bilde_index])
bilde = bilde.resize((400, 400), Image.Resampling.LANCZOS)
frame.bilde_tk = ImageTk.PhotoImage(bilde)
frame.bilde_label = tk.Label(frame, image=frame.bilde_tk)
frame.bilde_label.grid(row=1, column=0, columnspan=2, pady=10, padx=15, sticky="ew")

# Legg til knapper for å navigere mellom bilder
forrige_knapp = tk.Button(frame, text="Forrige", command=forrige_bilde)
forrige_knapp.grid(row=2, column=0, pady=10)

neste_knapp = tk.Button(frame, text="Neste", command=neste_bilde)
neste_knapp.grid(row=2, column=1, pady=10)

# Start hovedløkken for å holde vinduet åpent
root.mainloop()