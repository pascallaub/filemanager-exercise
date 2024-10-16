import os
import shutil
import tkinter as tk

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

def copy_file():
    source = entry1.get()
    destination = entry2.get()
    source = os.path.normpath(source)
    destination = os.path.normpath(destination)
    if directory.strip() == '':     #Homeverzeichnis, wenn keins angegeben wird
        directory = os.path.expanduser("~")
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
    source = entry3.get()
    destination = entry4.get()
    source = os.path.normpath(source)
    destination = os.path.normpath(destination)
    if directory.strip() == '':     #Homeverzeichnis, wenn keins angegeben wird
        directory = os.path.expanduser("~")
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
    old_name = entry5.get()
    new_name = entry6.get()
    try:
        os.rename(old_name, new_name)
        label19.config(text=f"Datei umbenannt: {old_name} -> {new_name}")
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

def search_file():
    directory = entry8.get()
    file = entry9.get()
    if directory.strip() == '':     #Homeverzeichnis, wenn keins angegeben wird
        directory = os.path.expanduser("~")

    directory = os.path.normpath(directory)

    found = False
    for root, dirs, files in os.walk(directory):
        if file in files:
            label16.config(text=f"Datei gefunden: {os.path.join(root, file)}")
            found = True
            break
    
    if not found:
        label16.config(text="Datei nicht gefunden!")

root = tk.Tk()
root.title("Filemanager!")
root.geometry("600x400")

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
frame6 = tk.Frame(container, bg='lightblue')

for frame in (frame1, frame2, frame3, frame4, frame5, frame6):
    frame.grid(row=0, column=0, sticky='nsew')

#Frame 1 Hauptmenü
label1 = tk.Label(frame1, text="Hauptmenü", font=('Helvetica', 20), width=30)
label1.pack(pady=25)

button1 = tk.Button(frame1, text="Kopieren", command=lambda: raise_frame(frame2), font=('Helvetica', 14), width=30)
button1.pack(pady=5)

button2 = tk.Button(frame1, text="Verschieben", command=lambda: raise_frame(frame3), font=('Helvetica', 14), width=30)
button2.pack(pady=5)

button3 = tk.Button(frame1, text="Umbenennen", command=lambda: raise_frame(frame4), font=('Helvetica', 14), width=30)
button3.pack(pady=5)

button4 = tk.Button(frame1, text="Löschen", command=lambda: raise_frame(frame5), font=('Helvetica', 14), width=30)
button4.pack(pady=5)

button5 = tk.Button(frame1, text="Suchen", command=lambda: raise_frame(frame6), font=('Helvetica', 14), width=30)
button5.pack(pady=5)

#Frame 2 Kopieren
label5 = tk.Label(frame2, text="Kopieren", font=('Helvetica', 20), width=30)
label5.pack(pady=25)

label2 = tk.Label(frame2, text="Gib den Quellpfad ein", font=('Helvetica', 14), width=30)
label2.pack(pady=5)

entry1 = tk.Entry(frame2, font=('Helvetica', 14), width=30)
entry1.pack(pady=5)

label3 = tk.Label(frame2, text="Gib den Zielpfad ein", font=('Helvetica', 14), width=30)
label3.pack(pady=5)

entry2 = tk.Entry(frame2, font=('Helvetica', 14), width=30)
entry2.pack(pady=5)

button6 = tk.Button(frame2, text="Kopieren", command=copy_file, font=('Helvetica', 14), width=30)
button6.pack(pady=10)

label17 = tk.Label(frame2, text="", font=('Helvetica', 14), width=30)
label17.pack(pady=5)
label17.output = True

button9 = tk.Button(frame2, text="Zurück", command=lambda: raise_frame(frame1), font=('Helvetica', 14), width=30)
button9.pack(pady=10)

#Frame 3 Verschieben
label4 = tk.Label(frame3, text="Verschieben", font=('Helvetica', 20), width=30)
label4.pack(pady=25)

label6 = tk.Label(frame3, text="Gib den Quellpfad ein", font=('Helvetica', 14), width=30)
label6.pack(pady=5)

entry3 = tk.Entry(frame3, font=('Helvetica', 14), width=30)
entry3.pack(pady=5)

label7 = tk.Label(frame3, text="Gib das Zielverzeichnis an", font=('Helvetica', 14), width=30)
label7.pack(pady=5)

entry4 = tk.Entry(frame3, font=('Helvetica', 14), width=30)
entry4.pack(pady=5)

button7 = tk.Button(frame3, text="Verschieben", command=move_file, font=('Helvetica', 14), width=30)
button7.pack(pady=10)

label18 = tk.Label(frame3, text="", font=('Helvetica', 14), width=30)
label18.pack(pady=5)
label18.output = True

button8 = tk.Button(frame3, text="Zurück", command=lambda: raise_frame(frame1), font=('Helvetica', 14), width=30)
button8.pack(pady=10)

#Frame 4 Umbenennen
label8 = tk.Label(frame4, text="Umbenennen", font=('Helvetica', 20), width=30)
label8.pack(pady=25)

label9 = tk.Label(frame4, text="Gib den alten Dateinamen mit Pfad an", font=('Helvetica', 14), width=30)
label9.pack(pady=5)

entry5 = tk.Entry(frame4, font=('Helvetica', 14), width=30)
entry5.pack(pady=5)

label10 = tk.Label(frame4, text="Gib den neuen Namen mit Pfad ein", font=('Helvetica', 14), width=30)
label10.pack(pady=5)

entry6 = tk.Entry(frame4, font=('Helvetica', 14), width=30)
entry6.pack(pady=5)

button10 = tk.Button(frame4, text="Umbenennen", command=change_name, font=('Helvetica', 14), width=30)
button10.pack(pady=10)

label19 = tk.Label(frame4, text="", font=('Helvetica', 14), width=30)
label19.pack(pady=5)
label19.output = True

button11 = tk.Button(frame4, text="Zurück", command=lambda: raise_frame(frame1), font=('Helvetica', 14), width=30)
button11.pack(pady=10)

#Frame 5 Löschen
label11 = tk.Label(frame5, text="Löschen", font=('Helvetica', 20), width=30)
label11.pack(pady=25)

label12 = tk.Label(frame5, text="Gib den Dateinamen mit Pfad ein", font=('Helvetica', 14), width=30)
label12.pack(pady=5)

entry7 = tk.Entry(frame5, font=('Helvetica', 14), width=30)
entry7.pack(pady=5)

button12 = tk.Button(frame5, text="Löschen", command=delete_file, font=('Helvetica', 14), width=30)
button12.pack(pady=10)

label20 = tk.Label(frame5, text="", font=('Helvetica', 14), width=30)
label20.pack(pady=5)
label20.output = True

button13 = tk.Button(frame5, text="Zurück", command=lambda: raise_frame(frame1), font=('Helvetica', 14), width=30)
button13.pack(pady=10)

#Frame 6 Suchen
label13 = tk.Label(frame6, text="Suchen", font=('Helvetica', 20), width=30)
label13.pack(pady=25)

label14 = tk.Label(frame6, text="Gib das Verzeichnis ein", font=('Helvetica', 14), width=30)
label14.pack(pady=5)

entry8 = tk.Entry(frame6, font=('Helvetica', 14), width=30)
entry8.pack(pady=5)

label15 = tk.Label(frame6, text="Gib den Dateinamen ein", font=('Helvetica', 14), width=30)
label15.pack(pady=5)

entry9 = tk.Entry(frame6, font=('Helvetica', 14), width=30)
entry9.pack(pady=10)

button14 = tk.Button(frame6, text="Suchen", command=search_file, font=('Helvetica', 14), width=30)
button14.pack(pady=5)

label16 = tk.Label(frame6, text="", font=('Helvetica', 14), width=30)
label16.pack(pady=5)
label16.output = True

button15 = tk.Button(frame6, text="Zurück", command=lambda: raise_frame(frame1), font=('Helvetica', 14), width=30)
button15.pack(pady=10)

raise_frame(frame1)

if __name__=='__main__':
    root.mainloop()
