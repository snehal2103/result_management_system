from tkinter import*
from PIL import Image, ImageTk, ImageDraw # pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
from datetime import*
import time
from math import*
import sqlite3
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1600x780+0+0") 
        self.root.config(bg="white")
        self.logo_dash=Image.open("image/edu.png")
        self.logo_dash=self.logo_dash.resize((70,50),Image.Resampling.LANCZOS)
        self.logo_dash=ImageTk.PhotoImage(self.logo_dash)
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1400,height=80)
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.exit_).place(x=1120,y=5,width=200,height=40)
        self.bg_img=Image.open("image/bg.png")
        self.bg_img=self.bg_img.resize((1000,450),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=1000,height=450)
        self.lbl=Label(self.root,text="Clock",font=("\nBook Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=170,height=450,width=310)
        self.total_courses = StringVar()
        self.total_students = StringVar()
        self.total_results = StringVar()

        total_course_btn = Button(self.root, textvariable=self.total_courses, font=("goudy old style", 15, "bold"), bg="#90EE90", fg="white", state=DISABLED)
        total_course_btn.place(x=600, y=650, width=150, height=40)

        total_student_btn = Button(self.root, textvariable=self.total_students, font=("goudy old style", 15, "bold"), bg="#ADD8E6", fg="white", state=DISABLED)
        total_student_btn.place(x=800, y=650, width=150, height=40)

        total_result_btn = Button(self.root, textvariable=self.total_results, font=("goudy old style", 15, "bold"), bg="#FFA500", fg="white", state=DISABLED)
        total_result_btn.place(x=1000, y=650, width=150, height=40)

        # Update the total counts
        self.update_total_counts()

        # ... (rest of your code remains u
        
        self.working()
        footer=Label(self.root,text="SRMS-Student Result Management System\nContact Us for any Technical Issue:99xxxxxx13\nDeveloped by Snehal Tripathi",padx=10,font=("goudy old style",12),bg="#033054",fg="white").pack(side=BOTTOM,fill=X)
        
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses[{str(len(cr))}]")
            self.lbl_course.after(200,self.update_details)

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students[{str(len(cr))}]")
            self.lbl_student.after(200,self.update_details)

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results[{str(len(cr))}]")
            self.lbl_result.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        # print(h,m,s)
        # print(hr,min_,sec_)

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="image/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)

        #***********For clock Image***********
        bg=Image.open("image/c.png")
        bg=bg.resize((300,300),Image.Resampling.LANCZOS)
        clock.paste(bg,(50,50))

        # Formula To Rotate the AntiClock
        # angle_in_radians = angle_in_degrees * math.pi / 180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)

        #***********Hour Line Image***********
        origin = 200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)

        #***********Min Line Image***********
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)

        #***********Sec Line Image***********
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("image/clock_new.png")
    

        # Update the total counts
        

        # ... (rest of your code remains unchanged)

    def update_total_counts(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        # Query to get total number of courses, students, and results
        cur.execute("SELECT COUNT(*) FROM course")
        total_courses = cur.fetchone()[0]
        self.total_courses.set(f"Total Courses: {total_courses}")

        cur.execute("SELECT COUNT(*) FROM student")
        total_students = cur.fetchone()[0]
        self.total_students.set(f"Total Students: {total_students}")

        cur.execute("SELECT COUNT(*) FROM result")
        total_results = cur.fetchone()[0]
        self.total_results.set(f"Total Results: {total_results}")

        con.close()

        # Update counts after 1 second (you can adjust the time interval if needed)
        self.root.after(1000, self.update_total_counts)
    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)
    def logout(self):
        op=messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
    def exit_(self):
        op=messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op==True:
            self.root.destroy()
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()