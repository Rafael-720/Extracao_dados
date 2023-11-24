import tkinter as tk
from tkinter import ttk, messagebox
import database_connections as db_conn
import data_exporter as exporter

def connect_and_export():
    db_type = database_combobox.get()
    host = host_entry.get()
    port = port_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    db_name = db_entry.get()
    query = query_entry.get()

    try:
        if db_type == "Postgres":
            df = db_conn.connect_to_postgres(query, host, port, user, password, db_name)
        elif db_type == "MySQL":
            df = db_conn.connect_to_mysql(query, host, port, user, password, db_name)
        elif db_type == "Firebird":
            df = db_conn.connect_to_firebird(query, host, port, user, password, db_name)
       
        # Adicione condições para outros bancos de dados, passando a porta também

        filename = "exported_data.xlsx"  # Modifique conforme necessário
        exporter.export_to_excel(df, filename)
        messagebox.showinfo("Info", "Exportação Concluída!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def create_gui():
    app = tk.Tk()
    app.title("Exportador de Dados")

    frame = ttk.Frame(app, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Dropdown para escolher o banco de dados
    database_label = ttk.Label(frame, text="Escolha o Banco de Dados:")
    database_label.grid(row=0, column=0, sticky=tk.W)
    global database_combobox
    database_combobox = ttk.Combobox(frame, values=["Postgres", "Firebird", "SQL Server", "MySQL", "Oracle"])
    database_combobox.grid(row=0, column=1)

    # Campo para Host
    global host_entry, port_entry, user_entry, password_entry, db_entry, query_entry
    host_label = ttk.Label(frame, text="Host:")
    host_label.grid(row=1, column=0, sticky=tk.W)
    host_entry = ttk.Entry(frame, width=50)
    host_entry.grid(row=1, column=1)

    # Campo para Porta
    port_label = ttk.Label(frame, text="Porta:")
    port_label.grid(row=2, column=0, sticky=tk.W)
    port_entry = ttk.Entry(frame, width=50)
    port_entry.grid(row=2, column=1)

    # Campo para Usuário
    user_label = ttk.Label(frame, text="Usuário:")
    user_label.grid(row=3, column=0, sticky=tk.W)
    user_entry = ttk.Entry(frame, width=50)
    user_entry.grid(row=3, column=1)

    # Campo para Senha
    password_label = ttk.Label(frame, text="Senha:")
    password_label.grid(row=4, column=0, sticky=tk.W)
    password_entry = ttk.Entry(frame, width=50, show="*")
    password_entry.grid(row=4, column=1)

    # Campo para Nome do DB
    db_label = ttk.Label(frame, text="Nome do DB:")
    db_label.grid(row=5, column=0, sticky=tk.W)
    db_entry = ttk.Entry(frame, width=50)
    db_entry.grid(row=5, column=1)

    # Campo para Query SQL
    query_label = ttk.Label(frame, text="SQL Query:")
    query_label.grid(row=6, column=0, sticky=tk.W)
    query_entry = ttk.Entry(frame, width=50)
    query_entry.grid(row=6, column=1)

    # Botão para Exportar
    export_button = ttk.Button(frame, text="Exportar", command=connect_and_export)
    export_button.grid(row=7, column=1, sticky=tk.E)

    return app

if __name__ == "__main__":
    gui_app = create_gui()
    gui_app.mainloop()
