import tkinter as tk
from tkinter import ttk
from quickTKsql import *

#Window 1
login = tk.Tk()
login.title('Login screen')
login.geometry('1366x768')
login.config(bg = 'black')

title = tk.Label(login,text = 'Enter your credentials',font = ('Comic Sans MS',25),
                 fg = 'white',bg = 'black')
title.pack(padx = 2,pady = 2)

placeholder = tk.Button(login,text = 'Placeholder',height = 10,width = 10,)
placeholder.pack(padx = 2,pady = 2) #image of mall ig?

                                #Username
user = tk.Label(login,text = 'Enter Username:',font = ('Clear Sans',20),
                fg = 'white',bg = 'black',anchor = 'w') #Displays the word username
user.pack(fill = 'x',padx = 2,pady = 2)
cred_user = tk.Entry(login,font = ('Clear Sans',15),fg = 'black',justify = 'left',
                     width = 50) #Entry btn to fill username value
cred_user.pack(padx = 2,pady = 2,expand = True)

                                  #Password
Pass = tk.Label(login,text = 'Enter Password:',font = ('Clear Sans',20),
                fg = 'white',bg = 'black',anchor = 'w') #Displays the word passwd
Pass.pack(fill = 'x',padx = 2,pady = 2)
cred_pass = tk.Entry(login,fg = 'black',font = ('Clear Sans',15),width = 50,
                     justify = 'left',show = '*') #Entry btn to fill passwd value 
cred_pass.pack(padx = 2,pady = 2,expand = True)

                              #btn accepting values
obtain = tk.Button(login,text = 'Enter',font = ('Comic Sans MS',20),width = 20 ,
                   bg = 'black',fg = 'white',
                   command = lambda: cred(username = cred_user.get(),
                                          password = cred_pass.get(),
                                          widget_1 = db_options,
                                          widget_2 = wrong)) #btn accepting user credentials
obtain.pack(expand = True,padx = 2,pady = 2)

'''
Widget is displayed: -- bound to fn 2
    a. if credentials are wrong
    b. else not displayed
'''
wrong = tk.Label(login,text='Username/Password is wrong',
                         font = ('Comic Sans MS',20),fg = 'red',bg = 'black') 


#Creating a window where tables can be displayed
#Window 2 
db_options = tk.Toplevel(login,bg = 'black')
db_options.title('Database/Table selection screen')
db_options.geometry('1366x768')
db_options.withdraw()

#Creating a new window where sql operations can be done
#Window 3
sql = tk.Toplevel(db_options)
sql.geometry('1366x768')
sql.withdraw()

#Creating window to display sql errors
#Error window
error = tk.Toplevel(db_options)
error.title('Error window')
error.geometry('700x200')
error.withdraw()

                     #Return btn for db_options
back_button = tk.Button(db_options,text = '← Return',font = ('Clear Sans',15),
                        bg = 'black',fg = 'white',
                        command = lambda: leave(db_options))
back_button.pack(fill = 'x',padx = 2,pady = 2)

                     #List of tables via bunch of btn stored in dictionary
tables = tk.Label(db_options,text = 'Mall Management and Operations',
                  font = ('Comic Sans MS',20),relief = 'raised')
tables.pack(fill = 'x',padx = 2,pady = 2)

tables = display_tables(db_options,sql)

                     #Refresh btn to show if new table is created or not
refresh = tk.Button(db_options,text = '⟳',font = ('Clear Sans',20),
                    bg = 'black',fg = 'white',
                    command = lambda: re_display(db_options,refresh,new_btn,
                                                 tables,sql))
refresh.pack(fill = 'x',padx = 2,pady = 2)

                     #Btn allowing to create a new table
new_btn = tk.Button(db_options,text = '+',font = ('Comic Sans MS',20),
                    fg = 'white',bg = 'black',
                    command = lambda: create_win_setup(new,new_back_btn,
                                                       nf2_sub1,nf2_sub2,new_frame2,
                                                       new_add_field,send_values,
                                                       T_titlebox))
new_btn.pack(fill = 'x',padx = 2,pady = 2)

#Creating a window where tables creation can be done
#Window 3 alt
new = tk.Toplevel(db_options)
new.title('New MySQL table creation screen')
new.geometry('1366x768')
new.withdraw()

#Creating window to display sql errors during creation
#Error window alt
newerror = tk.Toplevel(db_options)
newerror.title('Error window')
newerror.geometry('700x200')
newerror.withdraw()

#Create window widgets
new_back_btn = tk.Button(new,text = '← Return',
                     font = ('Clear Sans',15),bg = 'black',fg = 'white',
                     command = lambda: leave(new))
new_back_btn.pack(side = 'top',fill = 'x',padx = 2,pady = 2)

send_values = tk.Button(new,text = 'Create New Table (MAX 5 Fields)',
                        font = ('Comic Sans MS',15),
                        fg = 'white',bg = 'black',
                        command = lambda: create(newerror))
send_values.pack(side = 'bottom',fill = 'x',padx = 2,pady = 2)

refresh_values = tk.Button(new,text = '⟳',font = ('Comic Sans MS',15),
                        fg = 'white',bg = 'black',command = refresh_entry_boxes)
refresh_values.pack(side = 'bottom',fill = 'x',padx = 2,pady = 2)
                     
new_frame1 = tk.Frame(new,bg = 'black')
new_frame1.pack(side = 'left',padx = 2,pady = 2,fill = 'both',expand = True)

new_frame2 = tk.Frame(new,bg = 'black')
new_frame2.pack(side = 'left',padx = 2,pady = 2,fill = 'both',expand = True)

                     #Labels on Frame 1
table_name = tk.Label(new_frame1,text = 'Enter Table Name:',
                      font = ('Comic Sans MS',15),
                      bg = '#20b2aa',fg = 'black',anchor = 'e')
table_name.pack(padx = 2,pady = 2,fill = 'x')

                     #Entry boxes and labels on frame 2
T_titlebox = tk.Entry(new_frame2,font = ('Clear Sans',20),fg = '#20b2aa',
                    justify = 'left')
T_titlebox.pack(padx = 2,pady = 2,fill = 'x')

div = tk.Label(new_frame2,text = '',font = ('Comic Sans MS',1),bg = 'black')
div.pack(padx = 2,pady = 2,fill = 'x')

new_add_field = tk.Button(new_frame2,text = '+',font = ('Comic Sans MS',15),
                          fg = 'white',bg = 'black',
                          command = lambda: add_field(nf2_sub1,nf2_sub2,
                                                      new_frame2,new_add_field))

                     #Sub-frames on Frame  1
nf2_sub1 = tk.Frame(new_frame1,bg = 'green')
nf2_sub1.pack(side = 'left',padx = 2,pady = 2,fill = 'both',expand = True)

nf2_sub2 = tk.Frame(new_frame1)
nf2_sub2.pack(side = 'left',padx = 2,pady = 2,fill = 'both',expand = True)

                     #Labels on frame 1 sub 1 (field no.)
rec_no_fr1 = tk.Label(nf2_sub1,text = 'Field No. 1: ',
                      font = ('Comic Sans MS',30),
                      bg = 'black',fg = 'white')
rec_no_fr1.pack(padx = 2,pady = 2,fill = 'both',expand = True)

login.mainloop()
