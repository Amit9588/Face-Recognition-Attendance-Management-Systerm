from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Student Details")

        ### variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        #first
        img = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\imgorig.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # Second
        img1 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\sample.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        # Third Image
        img2 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\smart-attendance.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # Bg ImGGE
        img3 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\bg1.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bG_image = Label(self.root, image=self.photoimg3)
        bG_image.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bG_image, text="STUDENT MANAGEMENT SYSTEM ", font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=-100, y=0, width=1530, height=45)

        main_frame = Frame(bG_image,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1350,height=550)

        #left label frame

        left_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=0,width=660,height=520)

        img_left = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 110), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=4, y=0, width=650, height=110)

        #current course
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",font=("times new roman", 12, "bold"))
        current_course_frame.place(x=4, y=105, width=650, height=110)

        #Department
        dept_label = Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=20)


        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman",12,"bold"), width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Mechanical","Electronics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10)

        #Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=30,sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,font=("times new roman", 12, "bold"), width=17,
                                 state="read only")
        course_combo["values"] = ("Select Courses", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=22, pady=10,sticky=W)

        # Year
        year_label = Label(current_course_frame,text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=30, pady=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), width=17,
                                    state="read only")
        year_combo["values"] = ("Select Year", "2018-19", "2019-20", "2020-21", "2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=12, pady=10, sticky=W)

        # Semester
        Semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        Semester_label.grid(row=1, column=2, padx=30, pady=10, sticky=W)

        Semester_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), width=17,
                                  state="read only")
        Semester_combo["values"] = ("Select Semester", "First", "Second", "Third", "Fourth","Fifth","Sixth","Seventh","Eight")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=22, pady=10, sticky=W)

        # Class Student course
        Class_Student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                         font=("times new roman", 12, "bold"))
        Class_Student_frame.place(x=4, y=215, width=650, height=280)

        # Student Id
        Student_ID_label = Label(Class_Student_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        Student_ID_label.grid(row=0, column=0, padx=20,pady=3, sticky=W)

        Student_ID_entry= ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=19,font=("times new roman",13,"bold"))
        Student_ID_entry.grid(row=0,column=1,padx=0,pady=3,sticky=W)

        #Student Name
        Student_Name_label = Label(Class_Student_frame, text="Student Name:", font=("times new roman", 12, "bold"),
                                 bg="white")
        Student_Name_label.grid(row=0, column=2, padx=5,pady=3 ,sticky=W)

        Student_Name_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_std_name, width=19, font=("times new roman", 13, "bold"))
        Student_Name_entry.grid(row=0, column=3, padx=8,pady=3 ,sticky=W)

        # class Division
        class_div_label = Label(Class_Student_frame, text="Class Division:", font=("times new roman", 12, "bold"),
                                   bg="white")
        class_div_label.grid(row=1, column=0, padx=20,pady=3, sticky=W)

        #class div combobox
        class_div_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_div,
                                    font=("times new roman", 13, "bold"),
                                    width=17, state="read only")
        class_div_combo["values"] = ("A", "B", "C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=0, pady=3)

        # Roll NO
        roll_no_label = Label(Class_Student_frame, text="Roll No:", font=("times new roman", 12, "bold"),
                                   bg="white")
        roll_no_label.grid(row=1, column=2, padx=5, pady=3,sticky=W)

        roll_no_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_roll, width=19, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3,padx=8,pady=3,  sticky=W)

        # Gender
        gender_label = Label(Class_Student_frame, text="Gender:", font=("times new roman", 12, "bold"),
                              bg="white")
        gender_label.grid(row=2, column=0, padx=20,pady=3, sticky=W)

        #gender combobox

        gender_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"),
                                 width=17, state="read only")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=0, pady=3)

        # Roll NO
        dob_label = Label(Class_Student_frame, text="DOB:", font=("times new roman", 12, "bold"),
                              bg="white")
        dob_label.grid(row=2, column=2, padx=5,pady=3 ,sticky=W)

        dob_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_dob, width=19, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=8,pady=3 ,sticky=W)

        # Email
        email_label = Label(Class_Student_frame,text="Email:", font=("times new roman", 12, "bold"),
                             bg="white")
        email_label.grid(row=3, column=0, padx=20,pady=3 ,sticky=W)

        email_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_email, width=19, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=0, pady=3,sticky=W)

        # Phone No
        phone_label = Label(Class_Student_frame, text="Phone No:", font=("times new roman", 12, "bold"),
                          bg="white")
        phone_label.grid(row=3, column=2, padx=5, pady=3,sticky=W)

        phone_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_phone,width=19, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=8,pady=3, sticky=W)

        # Teacher
        teacher_label = Label(Class_Student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"),
                             bg="white")
        teacher_label.grid(row=4, column=0, padx=20,pady=3, sticky=W)

        teacher_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_teacher,width=19, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=1, padx=0, pady=3,sticky=W)

        # Adress
        adress_label = Label(Class_Student_frame, text="Address:", font=("times new roman", 12, "bold"),
                            bg="white")
        adress_label.grid(row=4, column=2, padx=5, pady=3,sticky=W)

        adress_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_address, width=19, font=("times new roman", 13, "bold"))
        adress_entry.grid(row=4, column=3, padx=8,pady=3, sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radio_button1= ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="YES")
        radio_button1.grid(row=5,column=0,pady=5)

        # radio buttons
        self.var_radio2 =StringVar()
        radio_button2 = ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1 ,text="No Photo Sample", value="NO")
        radio_button2.grid(row=5, column=1,pady=5)

        #Button frames
        btn_frame=Frame(Class_Student_frame,bd =2,relief=RIDGE)
        btn_frame.place(x=0,y=195,width=645,height=30)

        save_btn= Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,)

        update_btn = Button(btn_frame, text="Update", width=15, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=15, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=15, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        reset_btn.grid(row=0, column=3)

###### button frame 2

        btn_frame1 = Frame(Class_Student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=228, width=645, height=30)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", width=31, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=31, font=("times new roman", 13, "bold"),bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

















        # right label frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        right_frame.place(x=675, y=0, width=660, height=520)

        img_right = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\student.jpg")
        img_right = img_right.resize((720, 110), Image.ANTIALIAS)
        self.img_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.img_right)
        f_lbl.place(x=4, y=0, width=650, height=110)

        ################# SEARCH SYSTEM ####################

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                         font=("times new roman", 12, "bold"))
        search_frame.place(x=4, y=110, width=650, height=70)

        #LABEL
        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"),
                              bg="white")
        search_label.grid(row=0, column=0, padx=0, pady=3, sticky=W)


        #combo bar
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=17,
                                      state="read only")
        search_combo["values"] = (
        "Select", "First", "Roll No:", "Phone NO:", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #Entry

        search_entry = ttk.Entry(search_frame,width=14, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10,pady=3, sticky=W)

        #button

        search_btn = Button(search_frame,text="Search",width=10,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=10)

        showall_btn = Button(search_frame,text="Show All",width=9,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=6)

        ####Frame
        table_frame = Frame(right_frame, bd=2,bg="White",relief=RIDGE)
        table_frame.place(x=4, y=185, width=645, height=305)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)

        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table= ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId ")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

################## function declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department"  or self.var_std_name.get() =="" or self.var_std_id.get() == "":
            messagebox.showerror("Error","All fields are required",parent= self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Amit@9588",database="face_recognizerr")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                self.var_dep.get(),
                                                                                self.var_course.get(),
                                                                                self.var_year.get(),
                                                                                self.var_semester.get(),
                                                                                self.var_std_id.get(),
                                                                                self.var_std_name.get(),
                                                                                self.var_div.get(),
                                                                                self.var_roll.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_email.get(),
                                                                                self.var_phone.get(),
                                                                                self.var_address.get(),
                                                                                self.var_teacher.get(),
                                                                                self.var_radio1.get()



                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully")
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)



################## Fetch Data ##############

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Amit@9588",
                                       database="face_recognizerr")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    ### ******************** get cursor *************

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

# ************update function

    def update_data(self):
        if self.var_dep.get() == "Select Department"  or self.var_std_name.get() =="" or self.var_std_id.get() == "":
            messagebox.showerror("Error","All fields are required",parent= self.root)

        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update details",parent=self.root)
                if update>0:

                    conn = mysql.connector.connect(host="localhost", username="root", password="Amit@9588",
                                                       database="face_recognizerr")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep = %s ,Course = %S ,Year = %s ,Semester = %s, Division = %s,"
                                      "Roll=%s , Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s"
                                      "where Student_id=%s",(

                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get()

                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details updated succesfully")















if __name__=="__main__":
    root = Tk()
    obj = Student(root)

    root.mainloop()