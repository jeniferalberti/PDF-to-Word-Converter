import tkinter as tk
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
    if word_file:
        try:
            # Cria um conversor e realiza a conversão do PDF para Word
            cv = Converter(pdf_file)
            cv.convert(word_file, detect_rotation=True, rectify=True, analyze_tables=True)
            cv.close()
            messagebox.showinfo("Sucesso", "PDF convertido para Word com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na conversão: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversor PDF para Word")

# Elementos da interface gráfica
tk.Label(root, text="PDF para Word").grid(row=0, column=0, padx=10, pady=10)
pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Selecionar", command=select_pdf_file).grid(row=0, column=2, padx=10, pady=10)
tk.Button(root, text="Converter", command=pdf_to_word_ui).grid(row=0, column=3, padx=10, pady=10)

# Inicia a interface gráfica
root.mainloop()
