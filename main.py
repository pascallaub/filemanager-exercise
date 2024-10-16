import os
import shutil
import tkinter as tk
from tkinter import filedialog

def raise_frame(frame):
    clear_entries(frame)
    frame.tkraise()

def clear_entries(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        elif isinstance(widget, tk.Label) and getattr(widget, 'output', False):
            widget.config(text="")

# def main_menu():
#     while True:
#         choice = input("1. Datei kopieren\n2. Datei verschieben\n3. Datei umbenennen\n4. Datei löschen\n5. Datei suchen\n6. Beenden\nAuswahl: ")
#         try:
#             if choice == '1':
#                 copy_file()
#             elif choice == '2':
#                 move_file()
#             elif choice == '3':
#                 change_name()
#             elif choice == '4':
#                 delete_file()
#             elif choice == '5':
#                 search_file()
#             elif choice == '6':
#                 quit()
#         except ValueError:
#             print("Gib eine Zahl von 1 - 5 ein!")

source = ""
destination = ""

def choose_file(entry):
    global source
    source = filedialog.askopenfilename()
    if source:
        entry.insert(0, source)

def choose_directory(entry):
    global destination
    destination = filedialog.askdirectory()
    if destination:
        entry.insert(0, destination)

def copy_file():
    global source, destination
    if not source or not destination:
        label17.config(text="Bitte Quelle und Ziel auswählen!")
        return

    try:
        shutil.copy(source, destination)
        label17.config(text=f"Datei kopiert: {source} -> {destination}")
    except FileNotFoundError:
        label17.config(text="Datei nicht gefunden!")
    except PermissionError:
        label17.config(text="Fehlende Berechtigung")
    except Exception as e:
        label17.config(text=f"Fehler: {e}")

def move_file():
    global source, destination
    try:
        shutil.move(source, destination)
        label18.config(text=f"Datei verschoben: {source} -> {destination}")
    except FileNotFoundError:
        label18.config(text="Datei nicht gefunden!")
    except PermissionError:
        label18.config(text="Fehlende Berechtigung!")
    except Exception as e:
        label18.config(text=f"Fehler: {e}")

def change_name():
    global source
    directory = os.path.dirname(source)
    new_name = entry6.get()
    new_name = os.path.join(directory, new_name)
    try:
        os.rename(source, new_name)
        label19.config(text=f"Datei umbenannt: {source} -> {new_name}")
    except FileNotFoundError:
        label19.config(text="Datei nicht gefunden!")
    except PermissionError:
        label19.config(text="Fehlende Berechtigung!")
    except Exception as e:
        label19.config(text=f"Fehler: {e}")

def delete_file():
    filepath = entry7.get()
    filepath = os.path.normpath(filepath)
    try:
        os.remove(filepath)
        label20.config(text=f"Datei gelöscht: {filepath}")
    except FileNotFoundError:
        label20.config(text="Datei nicht gefunden!")
    except PermissionError:
        label20.config(text="Fehlende Berechtigung!")
    except Exception as e:
        label20.config(text="Fehler: {e}")


root = tk.Tk()
root.title("Filemanager!")
root.geometry("950x450")

#Erstellt Container für alle Frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

frame1 = tk.Frame(container, bg='lightblue')
frame2 = tk.Frame(container, bg='lightblue')
frame3 = tk.Frame(container, bg='lightblue')
frame4 = tk.Frame(container, bg='lightblue')
frame5 = tk.Frame(container, bg='lightblue')

for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0, column=0, sticky='nsew')

#Frame 1 Hauptmenü
label1 = tk.Label(frame1, text="Hauptmenü", font=('Helvetica', 20), width=30)
label1.grid(row=0, column=2, columnspan=3, padx=200, pady=25, sticky='')

button1 = tk.Button(frame1, text="Kopieren", command=lambda: raise_frame(frame2), font=('Helvetica', 14), width=30)
button1.grid(row=1, column=2, padx=250, pady=5, sticky='')

button2 = tk.Button(frame1, text="Verschieben", command=lambda: raise_frame(frame3), font=('Helvetica', 14), width=30)
button2.grid(row=2, column=2, padx=250, pady=5, sticky='')

button3 = tk.Button(frame1, text="Umbenennen", command=lambda: raise_frame(frame4), font=('Helvetica', 14), width=30)
button3.grid(row=3, column=2, padx=250, pady=5, sticky='')

button4 = tk.Button(frame1, text="Löschen", command=lambda: raise_frame(frame5), font=('Helvetica', 14), width=30)
button4.grid(row=4, column=2, padx=250, pady=5, sticky='')


#Frame 2 Kopieren
label5 = tk.Label(frame2, text="Kopieren", font=('Helvetica', 20), width=30)
label5.grid(row=0, column=0, columnspan=3, pady=25)

label2 = tk.Label(frame2, text="Quellverzeichnis: ", font=('Helvetica', 14), width=30)
label2.grid(row=1, column=0, pady=5,)

entry1 = tk.Entry(frame2, font=('Helvetica', 14), width=30)
entry1.grid(row=1, column=1, padx=5, pady=5)

button16 = tk.Button(frame2, text="Quelldatei auswählen", command=lambda: choose_file(entry1), width=30)
button16.grid(row=1, column=2, padx=5, pady=5)

label3 = tk.Label(frame2, text="Gib den Zielpfad ein", font=('Helvetica', 14), width=30)
label3.grid(row=2, column=0, pady=5,)

entry2 = tk.Entry(frame2, font=('Helvetica', 14), width=30)
entry2.grid(row=2, column=1, padx=5, pady=5)

button17 = tk.Button(frame2, text="Zielverzeichnis auswählen", command=lambda: choose_directory(entry2), width=30)
button17.grid(row=2, column=2, padx=5, pady=5)

button6 = tk.Button(frame2, text="Kopieren", command=copy_file, font=('Helvetica', 14), width=30)
button6.grid(row=3, column=0, columnspan=3, pady=10)

label17 = tk.Label(frame2, text="", width=60, height=4, wraplength=400, anchor='w', justify='left', font=('Helvetica', 14))
label17.grid(row=4, column=0, columnspan=3, pady=5)
label17.output = True

button9 = tk.Button(frame2, text="Zurück", command=lambda: raise_frame(frame1), font=('Helvetica', 14), width=30)
button9.grid(row=5, column=0, columnspan=3, pady=10)

#Frame 3 Verschieben
label4 = tk.Label(frame3, text="Verschieben", font=('Helvetica', 20), width=30)
label4.grid(row=0, column=0, columnspan=3, pady=25)

label6 = tk.Label(frame3, text="Gib den Quellpfad ein", font=('Helvetica', 14), width=30)
label6.grid(row=1, column=0, pady=5)

entry3 = tk.Entry(frame3, font=('Helvetica', 14), width=30)
entry3.grid(row=1, column=1, padx=5, pady=5)

button18 = tk.Button(frame3, text="Quelldatei auswählen", command=lambda: choose_file(entry3), width=30)
button18.grid(row=1, column=2, padx=5, pady=5)

label7 = tk.Label(frame3, text="Gib das Zielverzeichnis an", font=('Helvetica', 14), width=30)
label7.grid(row=2, column=0, pady=5)

entry4 = tk.Entry(frame3, font=('Helvetica', 14), width=30)
entry4.grid(row=2, column=1, padx=5, pady=5)

button19 = tk.Button(frame3, text="Zielpfad auswählen", command=lambda: choose_directory(entry4), width=30)
button19.grid(row=2, column=2, padx=5, pady=5)

button7 = tk.Button(frame3, text="Verschieben", command=move_file, font=('Helvetica', 14), width=30)
button7.grid(row=3, column=0, columnspan=3, pady=10)

label18 = tk.Label(frame3, text="", width=60, height=4, wraplength=400, anchor='w', justify='left', font=('Helvetica', 14))
label18.grid(row=4, column=0, columnspan=3, pady=5)
label18.output = True

button8 = tk.Button(frame3, text="Zurück", command=lambda: raise_frame(frame1), font=('Helvetica', 14), width=30)
button8.grid(row=5, column=0, columnspan=3, pady=10)

#Frame 4 Umbenennen
label8 = tk.Label(frame4, text="Umbenennen", font=('Helvetica', 20), width=30)
label8.grid(row=0, column=0, columnspan=3, pady=25)

label9 = tk.Label(frame4, text="Wähle die alte Datei aus", font=('Helvetica', 14), width=30)
label9.grid(row=1, column=0, pady=5)

entry5 = tk.Entry(frame4, font=('Helvetica', 14), width=30)
entry5.grid(row=1, column=1, pady=5)

button20 = tk.Button(frame4, text="Durchsuchen", command=lambda: choose_file(entry5))
button20.grid(row=1, column=2, pady=5, sticky='w')

label10 = tk.Label(frame4, text="Gib den neuen Namen ein", font=('Helvetica', 14), width=30)
label10.grid(row=2, column=0, padx=5, pady=5)

entry6 = tk.Entry(frame4, font=('Helvetica', 14), width=30)
entry6.grid(row=2, column=1, padx=5, pady=5)

button10 = tk.Button(frame4, text="Umbenennen", command=change_name, font=('Helvetica', 14), width=30)
button10.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

label19 = tk.Label(frame4, text="", width=60, height=4, wraplength=400, anchor='w', justify='left', font=('Helvetica', 14))
label19.grid(row=4, column=0, columnspan=3, pady=5)
label19.output = True

button11 = tk.Button(frame4, text="Zurück", command=lambda: raise_frame(frame1), font=('Helvetica', 14), width=30)
button11.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

#Frame 5 Löschen
label11 = tk.Label(frame5, text="Löschen", font=('Helvetica', 20), width=30)
label11.grid(row=0, column=0, columnspan=3, pady=25)

label12 = tk.Label(frame5, text="Wähle eine Datei aus", font=('Helvetica', 14), width=30)
label12.grid(row=1, column=0, pady=5)

entry7 = tk.Entry(frame5, font=('Helvetica', 14), width=30)
entry7.grid(row=1, column=1, pady=5)

button21 = tk.Button(frame5, text="Datei auswählen", command=lambda: choose_file(entry7))
button21.grid(row=1, column=2, padx=5, pady=5)

button12 = tk.Button(frame5, text="Löschen", command=delete_file, font=('Helvetica', 14), width=30)
button12.grid(row=2, column=0, columnspan=3, padx= 10, pady=10)

label20 = tk.Label(frame5, text="", width=60, height=4, wraplength=400, anchor='w', justify='left', font=('Helvetica', 14))
label20.grid(row=3, column=0, columnspan=3, pady=5)
label20.output = True

button13 = tk.Button(frame5, text="Zurück", command=lambda: raise_frame(frame1), font=('Helvetica', 14), width=30)
button13.grid(row=4, column=0, columnspan=3, pady=10)


raise_frame(frame1)

if __name__=='__main__':
    root.mainloop()
