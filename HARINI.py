from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
db_connect= pymysql.connect(
    host='localhost',
    user='root;',
    password='HARINI GS',
    database='lead'
)
my_data=db_connect.cursor()
print("sucessfully connected***")

admin_list=[]
lead_list=[]
root=Tk()
root.title('CRM')
root.geometry("1200x800")
root.configure(background='#1A276')
def admin_sigin():
    def save_admin():
        name=name_entry.get()
        mobile=mobile_entry.get()
        password=password_entry.get()
        if not name or not mobile or not password:
            messagebox.showerror("ERROR","Please fill out all the fields")
            return
        else:
            sql_statement="INSERT INTO admin register name(name,mobile,password) values"
            values=(name,mobile,password)
            my_data.execute(sql_statement,values)
            bd_connection.commit()
            admin_list.append({'name':name,'mobile':mobile,'password':password})
            messagebox.showinfo("SUCCESS","you registered successfully GOOD JOB")
            signin_frame.destroy()
signin_frame=Frame(root,bg='#1A5276',width=500,height=700)
signin_frame.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    
