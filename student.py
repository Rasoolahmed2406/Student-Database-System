from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql



class Window1:
    def __init__(self,root):
        self.root = root
        self.root.title("Student managment Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightgrey")
        self.frame = Frame(self.root,bg="lightgrey")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame,text="Student Management system",font=("areal",30,"bold"),bg="lightgrey",fg="black")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)

        #============================================================================================================
        self.LoginFrame1 = LabelFrame(self.frame,width=1350,height=600,font=("areal",30,"bold"),relief="ridge",bg="lightgrey",bd=22,fg="black")
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = LabelFrame(self.frame,width=1350,height=600,font=("areal",30,"bold"),relief="ridge",bg="lightgrey",bd=22,fg="black")
        self.LoginFrame2.grid(row=2,column=0)

        #=================================Label and Entry========================================================
        self.lblUsername = Label(self.LoginFrame1, text="Username",font=("areal",20,"bold"),bg="lightgrey")
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername = Entry(self.LoginFrame1,font=("areal",20,"bold"),textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1,padx=8,pady=4)

        self.lblPassword= Label(self.LoginFrame1, text="Password",font=("areal",20,"bold"),bg="lightgrey")
        self.lblPassword.grid(row=1,column=0)
        self.txPassword = Entry(self.LoginFrame1,font=("areal",20,"bold"),show="*",textvariable=self.Password)
        self.txPassword.grid(row=1,column=1,padx=8,pady=8)

    #=============================================Buttons========================================================================

        self.BtnLogin = Button(self.LoginFrame2,text="Login",width=17,bd=8,command=self.Login_System)
        self.BtnLogin.grid(row=3,column=0,padx=8,pady=20)

        self.BtnRset = Button(self.LoginFrame2,text="Reset",width=17,bd=8,command=self.Reset)
        self.BtnRset.grid(row=3,column=1,padx=8,pady=20)


        self.BtnExit = Button(self.LoginFrame2,text="Exit",width=17,bd=8,command=self.iExit)
        self.BtnExit.grid(row=3,column=2,padx=8,pady=20)

#=========================================================================================================

    def Login_System(self):
        u = self.Username.get()
        p = self.Password.get()

        if u == str("Rasool") and p == str("Rasool"):
            self.newWindow = Toplevel(self.root)
            self.app = Student(self.newWindow)
        else:
            messagebox.showerror("Error!","Invalid Uesrname or Password")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        

    def iExit(self):
        self.iExit = messagebox.askyesno("Error!","Do you want to Exit")
        if self.iExit>0:
            self.root.destroy()
        else:
            command = self.new_window
            return
        
        
    def new_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = Student(self.newWindow)



class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="Student Mangement System",font=("Arial",30,"bold"),border=12,relief=GROOVE,bg="blue",foreground="yellow")
        title.pack(side=TOP,fill=X)

        #==============Variables names  Start ===========================

        self.USN = StringVar()
        self.First_Name = StringVar()
        self.Middle_Name = StringVar()
        self.Last_Name = StringVar()
        self.Depatment = StringVar()
        self.Section = StringVar()
        self.Gender =StringVar()
        self.Sem = StringVar()
        self.Email_id = StringVar()
        self.Cell_No = StringVar()
        self.Advisor = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        #==============Variables names  Ends ===========================

        detail_frame = LabelFrame(self.root,text="Enter Details",font=("Arial",20),bd=12,relief=GROOVE,bg="lightgrey")
        detail_frame.place(x=20,y=90,width=435,height=700)

        deta_frame = Frame(self.root,bd=12,bg="lightgrey",relief=GROOVE)
        deta_frame.place(x=470,y=90,width=1060,height=700)



        rollno_lbl = Label(detail_frame,text="USN",bd=7,font=("arial",13),bg="lightgrey")
        rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

        rollno_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.USN)
        rollno_ent.grid(row=0,column=1,padx=2,pady=2)

        f_name_lbl = Label(detail_frame,text="First Name",bd=7,font=("arial",13),bg="lightgrey")
        f_name_lbl.grid(row=1,column=0,padx=2,pady=2)

        f_name_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.First_Name)
        f_name_ent.grid(row=1,column=1,padx=2,pady=2)

        m_name_lbl = Label(detail_frame,text="Middle Name",bd=7,font=("arial",13),bg="lightgrey")
        m_name_lbl.grid(row=2,column=0,padx=2,pady=2)

        m_name_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.Middle_Name)
        m_name_ent.grid(row=2,column=1,padx=2,pady=2)

        l_name_lbl = Label(detail_frame,text="Last Name",bd=7,font=("arial",13),bg="lightgrey")
        l_name_lbl.grid(row=3,column=0,padx=2,pady=2)

        l_name_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.Last_Name)
        l_name_ent.grid(row=3,column=1,padx=2,pady=2)

        depatment_lbl = Label(detail_frame,text="Department",bd=7,font=("arial",13),bg="lightgrey")
        depatment_lbl.grid(row=4,column=0,padx=2,pady=2)

        depatment_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.Depatment)
        depatment_ent.grid(row=4,column=1,padx=2,pady=2)

        section_lbl = Label(detail_frame,text="Section",bd=7,font=("arial",13),bg="lightgrey")
        section_lbl.grid(row=5,column=0,padx=2,pady=2)

        section_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.Section)
        section_ent.grid(row=5,column=1,padx=2,pady=2)

        gender_lbl = Label(detail_frame,text="Gender",bd=6,font=("arial",12),bg="lightgrey")
        gender_lbl.grid(row=6,column=0,padx=2,pady=2)

        gender_ent = ttk.Combobox(detail_frame,font=("arial",17),state="readonly",textvariable=self.Gender)
        gender_ent['values']=("Male","Female","Others")
        gender_ent.grid(row=6,column=1,padx=2,pady=2)

        sem_lbl = Label(detail_frame,text="Sem",bd=7,font=("arial",13),bg="lightgrey")
        sem_lbl.grid(row=7,column=0,padx=2,pady=2)

        sem_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.Sem)
        sem_ent.grid(row=7,column=1,padx=2,pady=2)

        email_lbl = Label(detail_frame,text="Email id",bd=7,font=("arial",13),bg="lightgrey")
        email_lbl.grid(row=8,column=0,padx=2,pady=2)

        email_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.Email_id)
        email_ent.grid(row=8,column=1,padx=2,pady=2)

        cell_lbl = Label(detail_frame,text="Cell No",bd=7,font=("arial",13),bg="lightgrey")
        cell_lbl.grid(row=9,column=0,padx=2,pady=2)

        cell_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.Cell_No)
        cell_ent.grid(row=9,column=1,padx=2,pady=2)

        advisor_lbl =Label(detail_frame,text="Advisor",bd=7,font=("arial",13),bg="lightgrey")
        advisor_lbl.grid(row=10,column=0,padx=2,pady=2)

        advisor_ent = Entry(detail_frame,bd=7,font=("arial",17),textvariable=self.Advisor)
        advisor_ent.grid(row=10,column=1,padx=2,pady=2)

#==============Entry Details Frame Ends ============================

#==============Button Frame Statrs =================================

        btn_frame =Frame(detail_frame,bg="lightgrey",bd=10,relief=GROOVE)
        btn_frame.place(x=30,y=520,width=360,height=120)

        add_btn = Button(btn_frame,bg="lightgrey",text="Add",bd=8,font=("arial",13),width=16,command=self.add_student)
        add_btn.grid(row=0,column=0,padx=2,pady=2)

        update_btn = Button(btn_frame,bg="lightgrey",text="Update",bd=8,font=("arial",13),width=16,command=self.update_data)
        update_btn.grid(row=0,column=1,padx=2,pady=2)

        delete_btn = Button(btn_frame,bg="lightgrey",text="Delete",bd=8,font=("arial",13),width=16,command=self.delete_data)
        delete_btn.grid(row=1,column=0,padx=2,pady=2)

        clear_btn = Button(btn_frame,bg="lightgrey",text="Clear",bd=8,font=("arial",13),width=16,command=self.clear)
        clear_btn.grid(row=1,column=1,padx=2,pady=2)

#==============Button Frame Ends =================================

#==============Search Frame Starts =================================

        search_frame = Frame(deta_frame,bg="lightgrey",bd=10,relief=GROOVE)
        search_frame.pack(side=TOP,fill=X)

        search_lbl = Label(search_frame,text="Search",bg="lightgrey",font=("arial",14))
        search_lbl.grid(row=0,column=0,padx=2,pady=2)

        search_in = ttk.Combobox(search_frame,font=("arial",14),state="readonly",textvariable=self.Search_by)
        search_in['values'] = ("USN","First Name","Last Name","Cell NO","Email id")
        search_in.grid(row=0,column=1,padx=12,pady=2)

        search_ent = Entry(search_frame,bd=7,font=("arial",17),textvariable=self.Search_txt)
        search_ent.grid(row=0,column=2,padx=2,pady=2)

        search_btn = Button(search_frame,text="Search",command=self.search_data,font=("arial",13),bd=9,width=14,bg="lightgrey")
        search_btn.grid(row=0,column=3,padx=12,pady=2)

        show_btn = Button(search_frame,text="Show all",command=self.fetch_data,font=("arial",13),bd=9,width=14,bg="lightgrey")
        show_btn.grid(row=0,column=4,padx=12,pady=2)

#==============Search Frame End=================================
#==============Data Frame Starts =================================

        main_frame =Frame(deta_frame,bg="lightgrey",bd=11,relief=GROOVE)
        main_frame.pack(fill=BOTH,expand=True)

        y_scroll = Scrollbar(main_frame,orient=VERTICAL)
        x_scroll =Scrollbar(main_frame,orient=HORIZONTAL)

        self.student_table = ttk.Treeview(main_frame,columns=("USN","First Name","Middle Name","Last Name","Department","Section","Gender","Sem","Email id","Cell No","Advisor"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

        y_scroll.config(command=self.student_table.yview)
        x_scroll.config(command=self.student_table.xview)

        y_scroll.pack(side=RIGHT,fill=Y)
        x_scroll.pack(side=BOTTOM,fill=X)

        self.student_table.heading("USN",text="USN")
        self.student_table.heading("First Name",text="First Name")
        self.student_table.heading("Middle Name",text="Middle Name")
        self.student_table.heading("Last Name",text="Last Name")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Sem",text="Sem")
        self.student_table.heading("Email id",text="Email id")
        self.student_table.heading("Cell No",text="Cell No")
        self.student_table.heading("Advisor",text="Advisor")

        self.student_table['show'] ='headings'

        self.student_table.column("USN",width=100)
        self.student_table.column("First Name",width=100)
        self.student_table.column("Middle Name",width=100)
        self.student_table.column("Last Name",width=100)
        self.student_table.column("Department",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Email id",width=100)
        self.student_table.column("Cell No",width=100)
        self.student_table.column("Advisor",width=100)
        self.student_table.pack(fill=BOTH,expand=True)

        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_student(self):
        if self.USN =="" or self.First_Name=="" or self.Middle_Name=="" or self.Last_Name=="" or self.Depatment=="" or self.Section == "" or self.Gender=="" or self.Sem=="" or self.Email_id =="" or self.Cell_No=="" or self.Advisor=="":
            messagebox.showerror("Error!","Please Fill All details")
        

        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="studentsdb")
            curr = conn.cursor()
            curr.execute("INSERT INTO studentsdb VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.USN.get(),
                                                                                            self.First_Name.get(),
                                                                                            self.Middle_Name.get(),
                                                                                            self.Last_Name.get(),
                                                                                            self.Depatment.get(),
                                                                                            self.Section.get(),
                                                                                            self.Gender.get(),
                                                                                            self.Sem.get(),
                                                                                            self.Email_id.get(),
                                                                                            self.Cell_No.get(),
                                                                                            self.Advisor.get()))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()

    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="studentsdb")
        cur = con.cursor()
        cur.execute("select * from studentsdb")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
            
    def clear(self):
        self.USN.set("")
        self.First_Name.set("")
        self.Middle_Name.set("")
        self.Last_Name.set("")
        self.Depatment.set("")
        self.Section.set("")
        self.Gender.set("")       
        self.Sem.set("")
        self.Email_id.set("")
        self.Cell_No.set("")
        self.Advisor.set("")

    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.USN.set(row[0])
        self.First_Name.set(row[1])
        self.Middle_Name.set(row[2])
        self.Last_Name.set(row[3])
        self.Depatment.set(row[4])
        self.Section.set(row[5])
        self.Gender.set(row[6])        
        self.Sem.set(row[7])
        self.Email_id.set(row[8])
        self.Cell_No.set(row[9])
        self.Advisor.set(row[10])

    def update_data(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="studentsdb")
        cur = conn.cursor()
        cur.execute("update studentsdb set First_Name=%s,Middle_Name=%s,Last_Name=%s,Depatment=%s,Section=%s,Gender=%s,sem=%s,Email_id=%s,Cell_No=%s,Advisor=%s where USN=%s",
                                                                                                                                                    (   self.First_Name.get(),
                                                                                                                                                        self.Middle_Name.get(),
                                                                                                                                                        self.Last_Name.get(),
                                                                                                                                                        self.Depatment.get(),
                                                                                                                                                        self.Section.get(),
                                                                                                                                                        self.Gender.get(),
                                                                                                                                                        self.Sem.get(),
                                                                                                                                                        self.Email_id.get(),
                                                                                                                                                        self.Cell_No.get(),
                                                                                                                                                        self.Advisor.get(),
                                                                                                                                                        self.USN.get()
                                                                                                                                                        ))

        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("SMS","Record updated Successfully")


    def delete_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="studentsdb")
        cur = con.cursor()
        cur.execute("delete  from studentsdb where USN=%s",self.USN.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("SMS","Record Dleted Sucssefull")


    def search_data(self):
            con = pymysql.connect(host="localhost",user="root",password="",database="studentsdb")
            cur = con.cursor()
            cur.execute("select  from studentsdb where"+str(self.Search_by.get())+" % LIKE "+str(self.Search_txt.get())+"%")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
                con.commit()
            con.close()



root = Tk()
obj = Window1(root)
root.mainloop()