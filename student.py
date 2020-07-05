#database--- stm, table---students
from tkinter import *
from tkinter import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x750+0+0")
        title=Label(self.root,text="Student Management System",bd=10,relief=SUNKEN,font="consolas 40 bold", bg="orange", fg="red")
        title.pack(side=TOP,fill=X)

#=================================All  Variables=========================================================================

        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        

#=================================Management Form Frame==================================================================

        Mgmt_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="yellow")
        Mgmt_Frame.place(x=20,y=100,width=450,height=580)

        mg_title=Label(Mgmt_Frame,text="Manage Students",bg="yellow",fg="black",font="consolas 30 bold")
        mg_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Mgmt_Frame,text="Roll No.",bg="yellow",fg="black",font="consolas 20 bold")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Mgmt_Frame,textvariable=self.roll_no_var,font="consolas 15 bold",bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Mgmt_Frame,text="Name",bg="yellow",fg="black",font="consolas 20 bold")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Mgmt_Frame,textvariable=self.name_var,font="consolas 15 bold",bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Mgmt_Frame,text="Email",bg="yellow",fg="black",font="consolas 20 bold")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Mgmt_Frame,textvariable=self.email_var,font="consolas 15 bold",bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Mgmt_Frame,text="Gender",bg="yellow",fg="black",font="consolas 20 bold")
        lbl_email.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Mgmt_Frame,textvariable=self.gender_var,font="consolas 13 bold",state='readonly')
        combo_gender['values']=("male","female")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact=Label(Mgmt_Frame,text="Contact",bg="yellow",fg="black",font="consolas 20 bold")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Mgmt_Frame,textvariable=self.contact_var,font="consolas 15 bold",bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_Dob=Label(Mgmt_Frame,text="DoB",bg="yellow",fg="black",font="consolas 20 bold")
        lbl_Dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_Dob=Entry(Mgmt_Frame,textvariable=self.dob_var,font="consolas 15 bold",bd=5,relief=GROOVE)
        txt_Dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Address=Label(Mgmt_Frame,text="Address",bg="yellow",fg="black",font="consolas 20 bold")
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_Address=Text(Mgmt_Frame,width=30,height=4,font="consolas 10")
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

#=================================Management Form Frame==================================================================

        btn_Frame=Frame(Mgmt_Frame,bd=4,relief=RIDGE,bg="yellow")
        btn_Frame.place(x=15,y=520,width=420)

        Addbtn=Button(btn_Frame,text="ADD",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


#=================================Detail Form Frame==================================================================

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="yellow")
        Detail_Frame.place(x=500,y=100,width=825,height=580)


#============================Table Frame=================================================================================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="yellow")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","DoB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        
        self.Student_table.heading("Roll",text="Roll No.")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DoB",text="DoB")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']="headings"
        self.Student_table.column("Roll",width=50)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("DoB",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)      #expand adjusts according to frame
        self.Student_table.bind("<Button-1>",self.get_cursor)

        self.fetch_data()
    def add_students(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get('1.0',END)))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,event):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get('1.0',END),self.roll_no_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
        
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        

root=Tk()
ob=Student(root)
root.mainloop()
