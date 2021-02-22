from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple #we have made it global bcoz we as fn get_Seletced_row is having arg so its mandtatory to pass while calling it and doing so gives us a error,so we stored the index in globsal var and used t in delete btton 
        index=list1.curselection()[0]
        selected_tuple=list1.get(index) #from the listbox get the tuple wtih index x
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1]) #this is for inserting  title at the selected row and END tells us that where v have to insert new value.bcoz of END the row v hve selected gets displayed int the four boxes titlenauthor,year,isbn
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])#inserting author ay selected row
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3]) #inserting year at selected row
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4]) #inserting isbn at selected row
    except IndexError:
        pass     



def view_command():
    list1.delete(0,END) #this line tells that after pressing view all for the second time it the content doesnt get repeated again
    for rows in backend.view():
        list1.insert(END,rows)

    
    
def search_command():
    list1.delete(0,END)
    for rows in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,rows)

def insert_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()) #if we keep insert fn till this line it doesnt show the entry on the screen directly but it shows after clicking view all
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))



def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
   backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())#seleted tuple[0] is for the id
    

window=Tk()

window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

b1=Button(window,text="Viewall",command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,command=insert_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update entry",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete entry",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)


list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row) #for selection of row

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)  #yscrollcommand is for y axis
sb1.configure(command=list1.yview)

window.mainloop()