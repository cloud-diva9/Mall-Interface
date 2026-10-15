import tkinter as tk
from tkinter import ttk
from quickTKsql import *

entry_box_list_insert = []
entry_box_list_del = []
entry_box_list_upd = []

#File which manages the widgets on operations window
def main(sql,table_col,table_rec,table_name):
    return_btn = tk.Button(sql,text = '← Return',font = ('Clear Sans',15),
                        bg = 'black',fg = 'white',
                           command = lambda: leave(sql,table_widget,tab_holder,
                                                   return_btn,table_col,table_rec))
    return_btn.pack(fill = 'x',padx = 2,pady = 2)

    table_frame = tk.Frame(sql,bg = 'black')
    table_frame.pack(fill = 'both',padx = 2,pady = 2)

#Making table to display records 
    #Making column ids
    for r in range(len(table_col)):
        table_col[r] = table_col[r].lower()
        
    table_widget = ttk.Treeview(table_frame,column = table_col,
                                show = 'headings',selectmode  = 'none')

    #Adding header text to columns and adjusting the column width
    for r in range(len(table_col)):
        table_widget.heading(column = table_col[r],text = table_col[r].upper())
        table_widget.column(column = table_col[r],width = 110,minwidth = 90,
                            stretch = False)

    #Inserting table records
    for r in range(len(table_rec)):
        table_widget.insert('',index = r,values = table_rec[r])

        #table_widget.delete(*table_widget.get_children()) to delete all records from visible table
        

    table_widget.pack(fill = 'both',padx = 2,pady = 2)

    #Adding tabs for various operations
    tab_holder = ttk.Notebook(sql)
    tab_holder.pack(fill = 'both',expand = True,padx = 2,pady = 2)

    #Creating tabs(frames) for the notebook widget
    insert_oprn = tk.Frame(tab_holder,bg = 'black')
    insert_oprn.pack(fill = 'both',expand = True,padx = 2,pady = 2)
    
    del_oprn = tk.Frame(tab_holder,bg = 'black')
    del_oprn.pack(side = 'left',fill = 'both',expand = True,padx = 2,pady = 2)

    upd_oprn = tk.Frame(tab_holder,bg = 'black')
    upd_oprn.pack(side = 'left',fill = 'both',expand = True,padx = 2,pady = 2)

    #Adding tabs(frames) to the notebook widget
    tab_holder.add(insert_oprn,text = 'Insert Operation')
    tab_holder.add(del_oprn,text = 'Delete Operation')
    tab_holder.add(upd_oprn,text = 'Update Operation')

    #Adding labels and entry boxes to insert operation frame
    rowno = 0
    colno = 0
    for r in range(len(table_col)):
        lbl = tk.Label(insert_oprn,text = table_col[r],font = ('Comic Sans MS',15),
                       fg = 'white',bg = 'black')
        lbl.grid(column = colno,row = rowno + 1,sticky = 'nsew',
                 padx = 2,pady = 2)

        entry = tk.Entry(insert_oprn,font = ('Comic Sans MS',15),
                         fg = 'black',bg = 'light grey',justify = 'left')
        entry.grid(column = colno + 1,row = rowno + 1,sticky = 'nsew',
                   padx = 2,pady = 2)

        entry_box_list_insert.append(entry)

        rowno +=1

        if rowno % 4 == 0:
            colno += 2
            rowno = 0

    if rowno % 4 != 0:
        while rowno % 4 != 0:
            lbl = tk.Label(insert_oprn,text = '',font = ('Comic Sans MS',15),
                           fg = 'white',bg = 'black')
            lbl.grid(column = colno,row = rowno + 1,sticky = 'nsew',
                     padx = 2,pady = 2)

            lbl = tk.Label(insert_oprn,text = '',font = ('Comic Sans MS',15),
                           fg = 'white',bg = 'black')
            lbl.grid(column = colno + 1,row = rowno + 1,sticky = 'nsew',
                     padx = 2,pady = 2)

            rowno += 1

        colno += 2

    insert_title = tk.Label(insert_oprn,text = 'Insert new records for the \
following fields (leave any entry box blank if not req.):',
                            font = ('Comic Sans MS',20),fg = 'white',bg = 'black')

    send_insert_values = tk.Button(insert_oprn,text = 'Insert records',
                                   font = ('Clear Sans',20),fg = 'white',bg = 'black',
                                   command = lambda: insert(entry_box_list_insert,
                                                            table_name))

    if colno == 0:
        insert_title.grid(column = 0,row = 0,columnspan = 2,sticky = 'nsew',
                          padx = 2,pady = 2)
        send_insert_values.grid(column = 0,row = 6,columnspan = 2,sticky = 'nsew',
                                padx = 2,pady = 2)

    else:
        insert_title.grid(column = 0,row = 0,columnspan = colno,
                      sticky = 'nsew',padx = 2,pady = 2)
        send_insert_values.grid(column = 0,row = 6,columnspan = colno,
                            sticky = 'nsew',padx = 2,pady = 2)

    #Adding labels and entry boxes to delete operation frame
    del_title = tk.Label(del_oprn,text = 'Delete any existing record(s):',
                            font = ('Comic Sans MS',20),fg = 'white',bg = 'black')
    del_title.pack(fill = 'x',padx = 2,pady = 2)

    del_field_lbl = tk.Label(del_oprn,text = 'Enter field name to delete:',
                       font = ('Comic Sans MS',20),fg = 'white',bg = 'black',
                       anchor = 'w')
    del_field_lbl.pack(fill = 'x',padx = 2,pady = 2)

    del_field_entry = tk.Entry(del_oprn,font = ('Comic Sans MS',15),
                         fg = 'black',bg = 'light grey',justify = 'left',width = 50)
    del_field_entry.pack(padx = 2,pady = 2)
    entry_box_list_del.append(del_field_entry)

    rec_lbl = tk.Label(del_oprn,text = 'Enter value to be deleted:' ,
                       font = ('Comic Sans MS',20),fg = 'white',bg = 'black',
                       anchor = 'w')
    rec_lbl.pack(fill = 'x',padx = 2,pady = 2)

    rec_del_entry = tk.Entry(del_oprn,font = ('Comic Sans MS',15),
                         fg = 'black',bg = 'light grey',justify = 'left',width = 50)
    rec_del_entry.pack(padx = 2,pady = 2)
    entry_box_list_del.append(rec_del_entry)

    send_del_values = tk.Button(del_oprn,text = 'Delete records',
                                font = ('Comic Sans MS',15),
                                fg = 'white',bg = 'black')
    send_del_values.pack(fill = 'x',padx = 2,pady = 2)

#command = delete()
    
    #Adding labels and entry boxes to delete operation frame
    upd_title = tk.Label(upd_oprn,text = 'Update any existing record(s):',
                            font = ('Comic Sans MS',20),fg = 'white',bg = 'black')
    upd_title.pack(fill = 'x',padx = 2,pady = 2)

    upd_field_lbl = tk.Label(upd_oprn,text = 'Enter field name to update:',
                       font = ('Comic Sans MS',20),fg = 'white',bg = 'black',
                       anchor = 'w')
    upd_field_lbl.pack(fill = 'x',padx = 2,pady = 2)

    upd_field_entry = tk.Entry(upd_oprn,font = ('Comic Sans MS',15),
                         fg = 'black',bg = 'light grey',justify = 'left',width = 50)
    upd_field_entry.pack(padx = 2,pady = 2)
    entry_box_list_upd.append(upd_field_entry)

    rec_lbl = tk.Label(upd_oprn,text = 'Enter value to be updated:' ,
                       font = ('Comic Sans MS',20),fg = 'white',bg = 'black',
                       anchor = 'w')
    rec_lbl.pack(fill = 'x',padx = 2,pady = 2)

    rec_upd_lbl = tk.Entry(upd_oprn,font = ('Comic Sans MS',15),
                         fg = 'black',bg = 'light grey',justify = 'left',width = 50)
    rec_upd_lbl.pack(padx = 2,pady = 2)
    entry_box_list_upd.append(rec_upd_lbl)

    send_upd_values = tk.Button(upd_oprn,text = 'Update records',
                                font = ('Comic Sans MS',15),
                                fg = 'white',bg = 'black')
    send_upd_values.pack(fill = 'x',padx = 2,pady = 2)

#command = update()








    
