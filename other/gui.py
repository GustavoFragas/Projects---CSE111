import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    root = tk.Tk()
    root.option_add("*Font", "Arial 14")
    frm_main = Frame(root)
    frm_main.master.title("Simple calculator")
    frm_main.pack(padx=100, pady=3, fill=tk.BOTH, expand=True)
    setup_main(frm_main)
    frm_main.mainloop()

def setup_main(frm):
    lbl_first_number=Label(frm, text="Enter the first number:" )
    lbl_first_number.grid(row=0, column=0)
    ent_first_number=IntEntry(frm, width=10)
    ent_first_number.grid(row=0, column=1)

    lbl_second_number=Label(frm, text="Enter the second number:" )
    lbl_second_number.grid(row=1, column=0)
    ent_second_number=IntEntry(frm, width=10)
    ent_second_number.grid(row=1, column=1)

    lbl_result=Label(frm, text="Result:")
    lbl_result.grid(row=2, column=0)
    lbl_result_value=Label(frm, text="", width=10)
    lbl_result_value.grid(row=2, column=1)

    btn_calculate=Button(frm, text="Calculate Sum",command=lambda: calculate_sum(ent_first_number.get(),ent_second_number.get(),lbl_result_value))
    btn_calculate.grid(row=3, column=0, columnspan=2, pady=5)

    def calculate_sum(number1, number2, result_label):
        result = number1 + number2
        result_label.config(text=str(result))

if __name__ == "__main__":
    main()  