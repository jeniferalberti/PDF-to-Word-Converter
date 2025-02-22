import tkinter as tk
import threading 
from tkinter import filedialog, messagebox
from pdf2docx import Converter

# Função para selecionar um arquivo PDF
def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_entry.delete(0, tk.END)
        pdf_entry.insert(0, file_path)

# Função para converter PDF para Word
def pdf_to_word_ui():
    pdf_file = pdf_entry.get()
    if not pdf_file:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo PDF.")
        return
    
    word_file = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])

    if not word_file:
        return
    
    convert_button.config(state=tk.DISABLED)  # Desabilita o botão para evitar múltiplos cliques
    status_label.config(text="Convertendo... Aguarde...")
    root.update_idletasks()

    def conversion_thread():
        try:
            # Cria um conversor e realiza a conversão do PDF para Word
            cv = Converter(pdf_file)
            cv.convert(word_file, detect_rotation=True, rectify=True, analyze_tables=True)
            cv.close()
            status_label.config(text="Conversão concluída!")
            messagebox.showinfo("Sucesso", "PDF convertido para Word com sucesso!")

        except Exception as e:
            status_label.config(text="Falha na conversão")
            messagebox.showerror("Erro", f"Falha na conversão: {e}")
        
        finally:
            convert_button.config(state=tk.NORMAL)  # Reabilita o botão após a conversão

    threa = threading.Thread(target=conversion_thread)
    threa.start()

# Configuração da interface gráfica
root = tk.Tk()
root.iconbitmap('icone.ico')
root.title("Conversor PDF para Word")

# Elementos da interface gráfica
tk.Label(root, text="PDF para Word").grid(row=0, column=0, padx=10, pady=10)
pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Selecionar", command=select_pdf_file).grid(row=0, column=2, padx=10, pady=10)
convert_button = tk.Button(root, text="Converter", command=pdf_to_word_ui)
convert_button.grid(row=0, column=3, padx=10, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=1, column=0, columnspan=4, pady=10)

# Inicia a interface gráfica
root.mainloop()
