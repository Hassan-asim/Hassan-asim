import tkinter as tk

# Constants to store item information
components = {
    "Case": ["Compact case ($75.00)", "Tower case ($150.00)"],
    "RAM": ["8 GB RAM ($79.99)", "16 GB RAM ($149.99)", "32 GB RAM ($299.99)"],
    "Main Hard Disk Drive": ["1 TB HDD ($49.99)", "2 TB HDD ($89.99)", "4 TB HDD ($129.99)"],
    "Additional Items": [
        "240 GB SSD ($59.99)", "480 GB SSD ($119.99)",
        "1 TB HDD ($49.99)", "2 TB HDD ($89.99)", "4 TB HDD ($129.99)",
        "DVD/Blu-Ray Player ($50.00)", "DVD/Blu-Ray Re-writer ($100.00)",
        "Standard Version ($100.00)", "Professional Version ($175.00)"
    ]
}

class ComputerShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Shop")
        
        self.selected_case = tk.StringVar()
        self.selected_ram = tk.StringVar()
        self.selected_hdd = tk.StringVar()
        self.additional_items = []

        self.create_main_items_frame()
        self.create_bill_frame()
        self.create_additional_items_frame()
        self.create_discount_frame()

    def create_main_items_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()
        tk.Label(frame, text="Select a Case:").grid(row=0, column=0)
        tk.Label(frame, text="Select RAM:").grid(row=1, column=0)
        tk.Label(frame, text="Select HDD:").grid(row=2, column=0)

        # Dropdowns for main items
        case_options = components["Case"]
        tk.OptionMenu(frame, self.selected_case, *case_options).grid(row=0, column=1)
        ram_options = components["RAM"]
        tk.OptionMenu(frame, self.selected_ram, *ram_options).grid(row=1, column=1)
        hdd_options = components["Main Hard Disk Drive"]
        tk.OptionMenu(frame, self.selected_hdd, *hdd_options).grid(row=2, column=1)

        tk.Button(frame, text="Bill", command=self.calculate_price).grid(row=3, column=0)
        tk.Button(frame, text="Additional Items", command=self.open_additional_items_window).grid(row=3, column=1)

    def create_bill_frame(self):
        self.bill_frame = tk.Frame(self.root)

    def create_additional_items_frame(self):
        self.additional_items_frame = tk.Toplevel(self.root)
        self.additional_items_frame.withdraw()
        tk.Label(self.additional_items_frame, text="Select Additional Items:").pack()
        additional_options = components["Additional Items"]
        self.additional_item_vars = []
        for item in additional_options:
            var = tk.BooleanVar()
            item_checkbox = tk.Checkbutton(self.additional_items_frame, text=item, variable=var)
            item_checkbox.pack()
            self.additional_item_vars.append(var)
        tk.Button(self.additional_items_frame, text="Bill", command=self.calculate_price).pack()

    def create_discount_frame(self):
        self.discount_frame = tk.Frame(self.root)
        self.discount_frame.pack()

    def calculate_price(self):
        if not self.selected_case.get() or not self.selected_ram.get() or not self.selected_hdd.get():
            tk.messagebox.showerror("Error", "Please select all mandatory items.")
            return

        selected_case_price = float(self.selected_case.get().split("($")[1].split(")")[0])
        selected_ram_price = float(self.selected_ram.get().split("($")[1].split(")")[0])
        selected_hdd_price = float(self.selected_hdd.get().split("($")[1].split(")")[0])
        
        total_price = 200 + selected_case_price + selected_ram_price + selected_hdd_price

        for i, item in enumerate(self.additional_items):
            item_price = float(item.split("($")[1].split(")")[0])
            total_price += item_price

        discount = 0
        if len(self.additional_items) == 1:
            discount = total_price * 0.05
        elif len(self.additional_items) >= 2:
            discount = total_price * 0.10

        discounted_price = total_price - discount

        self.update_bill(f"Basic Component Cost: $200.00", f"Total Price: ${total_price:.2f}", f"Discount: ${discount:.2f}", f"Discounted Price: ${discounted_price:.2f}")

    def open_additional_items_window(self):
        if not self.selected_case.get() or not self.selected_ram.get() or not self.selected_hdd.get():
            tk.messagebox.showerror("Error", "Please select all mandatory items before adding additional items.")
        else:
            self.additional_items_frame.deiconify()

    def update_bill(self, *bill_items):
        self.bill_frame.destroy()
        self.bill_frame = tk.Frame(self.root)
        self.bill_frame.pack()
        for item in bill_items:
            tk.Label(self.bill_frame, text=item).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ComputerShopApp(root)
    root.mainloop()
