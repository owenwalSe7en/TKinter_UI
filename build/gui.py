import tkinter as tk
from tkinter import ttk, filedialog

class LabelMaintenanceWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Label Creator")

        # Set window size and make it not resizable
        self.master.geometry("320x250")
        self.master.resizable(False, False)

        # Input File
        self.label_input_file = ttk.Label(master, text="Input File:")
        self.label_input_file.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_input_file = ttk.Entry(master)
        self.entry_input_file.grid(row=0, column=1, padx=5, pady=5)
        self.browse_input_button = ttk.Button(master, text="Browse", command=self.browse_input)
        self.browse_input_button.grid(row=0, column=2, padx=3, pady=5)

        # Output File
        self.label_output_file = ttk.Label(master, text="Output File:")
        self.label_output_file.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_output_file = ttk.Entry(master)
        self.entry_output_file.grid(row=1, column=1, padx=5, pady=5)
        self.browse_output_button = ttk.Button(master, text="Browse", command=self.browse_output)
        self.browse_output_button.grid(row=1, column=2, padx=3, pady=5)

        # Sheet Name
        self.label_sheet_name = ttk.Label(master, text="Sheet Name:")
        self.label_sheet_name.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_sheet_name = ttk.Entry(master)
        self.entry_sheet_name.grid(row=2, column=1, padx=5, pady=5)

        # Column Letter
        self.label_column_letter = ttk.Label(master, text="Column Letter:")
        self.label_column_letter.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_column_letter = ttk.Entry(master)
        self.entry_column_letter.grid(row=3, column=1, padx=5, pady=5)

        # First Row
        self.label_first_row = ttk.Label(master, text="First Row:")
        self.label_first_row.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_first_row = ttk.Entry(master)
        self.entry_first_row.grid(row=4, column=1, padx=5, pady=5)

        # Last Row
        self.label_last_row = ttk.Label(master, text="Last Row:")
        self.label_last_row.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_last_row = ttk.Entry(master)
        self.entry_last_row.grid(row=5, column=1, padx=5, pady=5)

        # Submit Button
        self.submit_button = ttk.Button(master, text="Submit", command=self.collect_data)
        self.submit_button.grid(row=6, column=0, columnspan=3, pady=10)

    def browse_input(self):
        file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("All Files", "*.*")])
        self.entry_input_file.delete(0, tk.END)
        self.entry_input_file.insert(0, file_path)

    def browse_output(self):
        dir_path = filedialog.askdirectory(title="Select Output Directory")
        self.entry_output_file.delete(0, tk.END)
        self.entry_output_file.insert(0, dir_path)

    def collect_data(self):
        # Retrieve data from entry widgets
        input_file = self.entry_input_file.get()
        output_file = self.entry_output_file.get()
        sheet_name = self.entry_sheet_name.get()
        column_letter = self.entry_column_letter.get()
        first_row = self.entry_first_row.get()
        last_row = self.entry_last_row.get()

        user_data = [input_file, output_file, sheet_name, column_letter, first_row, last_row]
        print(user_data)
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LabelMaintenanceWindow(root)
    root.mainloop()