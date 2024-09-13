from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import sqlite3
from hashlib import sha256

def create_frame1(frame):

    

    # Connexion à la base de données
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Requête pour récupérer le dernier utilisateur
    cursor.execute("SELECT * FROM connexion ORDER BY id DESC LIMIT 1")
    dernier_utilisateur = cursor.fetchone()

    conn.close()

    def show(user_id):

        def valider():

            item_id = dernier_utilisateur[0]

            _user_username = user_username_entry.get()
            _user_nom = user_nom_entry.get()
        
            _user_type = user_type_entry.get()
            _user_ville = user_ville_entry.get()
            _user_phone = user_phone_spingbox.get()
            _user_password = user_password_entry.get()

            
                
            if _user_username and _user_type:

                try:
                    conn = sqlite3.connect('data.db')

                    data_insert_query = '''UPDATE utilisateurs
                                        SET username = ?, nom = ?,
                                          role = ?,password = ?,ville = ?,phone = ?
                                        WHERE id = ?'''
                    
                    hashed_password = sha256(_user_password.encode()).hexdigest()
                    if not _user_password:
                        hashed_password = user[4]

                    data_insert_tuple = (_user_username,_user_nom,_user_type,hashed_password,_user_ville,_user_phone,user_id,)

                    cursor = conn.cursor()

                    cursor.execute(data_insert_query,data_insert_tuple)

                    conn.commit()
                
                    conn.close()
                    messagebox.showinfo("Succès", "Modifier avec succès ! Deconnecter vous pour prendre en compte les nouvelles modifications")

                    # username_entry.delete(0,frame.END)
                    # password_entry.delete(0,frame.END)

                except Exception as e:
                    messagebox.showerror("Erreur", str(e))
                finally:
                    # Fermer la connexion
                    conn.close()

                
            else: 
                messagebox.showwarning(title="Error", message="Remplissez les champs vides.")

        print(user_id)
        # Connexion à la base de données
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        try:
        # Requête pour récupérer l'utilisateur
            cursor.execute("SELECT * FROM utilisateurs WHERE id = ?", (user_id,))
            user = cursor.fetchone()

            if user is not None:
                print("Utilisateur trouvé :", user)
            else:
                print("Aucun utilisateur trouvé avec cet ID.")
        except sqlite3.Error as e:
            print("Erreur lors de la récupération de l'utilisateur :", e)
        finally:
            conn.close()

        user_info_frame = LabelFrame(frame,text="Mettre a jour votre profil")
        user_info_frame.grid(row=0,column=0,padx=20,pady=10)
        #####
        user_username_label = Label(user_info_frame,text="Username")
        user_username_label.grid(row=0,column=0)
        

        user_username_entry = Entry(user_info_frame)
        user_username_entry.grid(row=1,column=0)
        user_username_entry.insert(0,user[1])
        

        #######
        user_type_label = Label(user_info_frame,text="Role")
        user_type_label.grid(row=0,column=1)

        user_type_entry = ttk.Combobox(user_info_frame,values=["Administrateur","Client"])
        user_type_entry.grid(row=1,column=1)
        user_type_entry.insert(0,user[3])

        ############
        user_nom_label = Label(user_info_frame,text="Nom")
        user_nom_label.grid(row=0,column=3)

        user_nom_entry = Entry(user_info_frame)
        user_nom_entry.grid(row=1,column=3)
        user_nom_entry.insert(0,user[2])

        ############
        user_phone_label = Label(user_info_frame,text="Telephone")
        user_phone_label.grid(row=0,column=4)

        user_phone_spingbox = ttk.Spinbox(user_info_frame,from_=0)
        user_phone_spingbox.grid(row=1,column=4)
        user_phone_spingbox.set(user[6])

        ############
        user_ville_label = Label(user_info_frame,text="Ville")
        user_ville_label.grid(row=2,column=0)

        user_ville_entry = Entry(user_info_frame)
        user_ville_entry.grid(row=3,column=0)
        user_ville_entry.insert(0,user[5])

        ############
        user_password_label = Label(user_info_frame,text="Mot de passe")
        user_password_label.grid(row=2,column=1)

        user_password_entry = Entry(user_info_frame,show="*")
        user_password_entry.grid(row=3,column=1)
        
        ######
        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10,pady=5)

        # Button
        button = tkinter.Button(frame, text="Enregistrer",command=valider)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    #####################
    show(dernier_utilisateur[1])


    

