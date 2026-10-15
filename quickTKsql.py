import mysql.connector as msc
import tkinter as tk

db = msc.connect(host = 'localhost',user = 'root',
                 password = 'ADMIN',autocommit = True,
                 database = 'Mall_Management_and_Operations')
cur = db.cursor()

table_col = []
table_rec = []
entry_box_list_create = []

#1
def leave(window,table_widget = None,tab_holder = None,return_btn = None,
          table_col = None,table_rec = None):
    window.withdraw()
    window.grab_release() #Releases that focus

    if table_widget != None and tab_holder != None:
        return_btn.destroy()
        table_widget.destroy()
        tab_holder.destroy()
        table_col.clear()
        table_rec.clear()

#2
def cred(username,password,widget_1,widget_2):
    '''
    Here:
    widget_1 = db_options #toplevel window
    widget_2 = wrong #label to display if wrong values are entered
    '''
    try:
        db = msc.connect(host = 'localhost',user = 'root',
                         password = 'ADMIN' ,autocommit = True,
                         database = 'Mall_Management_and_Operations')
        #replace user and passwd rhs by parameter variables
        cur = db.cursor()
        widget_1.deiconify() #so it is visible again
        widget_1.grab_set() #Grabs the focus from the main screen to the new screen so that old screen cannot be used
        widget_2.destroy()
            
    except msc.ProgrammingError:
        widget_2.pack(expand = True,fill = 'x')

#3
def oprn_window(sql,table_name):
    from Mall_interface_branch import main

    table_col.clear()
    sql.deiconify()
    sql.grab_set()
    sql.title('Operations on ' + table_name)
    
    cur.execute('desc %s' % (table_name))
    res = cur.fetchall()
    for r in res:
       table_col.append(r[0])
       
    cur.execute('select * from %s' % (table_name))
    res = cur.fetchall()
    for r in res:
        table_rec.append(r)
    
    main(sql,table_col,table_rec,table_name)
    

#4
def display_tables(db_options,sql):
    cur.execute('show tables')
    tables  = []
    
    for r in cur.fetchall():
        table_btn = tk.Button(db_options,text = r[0],font = ('Comic Sans MS',20),
                        bg = 'black',fg = 'white',
                        command = lambda tn = r[0]: oprn_window(sql,tn))
        '''Since after each iteration the value inside oprn_window changes
           and after the loop finishes its final value ramains the final element
           of the iteration therefore we use a variable inside lambda so it
           captures the value then and there and whenever the btn is  cicked
           it passes on the captured value onto the function'''
        table_btn.pack(fill = 'x',padx = 2,pady = 2)
        tables.append(table_btn)

    return tables

#5
def re_display(db_options,refresh,new_btn,tables,sql):
    refresh.pack_forget()  #Unpacks the widget
    new_btn.pack_forget()
    for r in tables:
        r.destroy()
    tables.clear()
  
    cur.execute('show tables')

    for r in cur.fetchall():
        btn = tk.Button(db_options,text = r[0],font = ('Comic Sans MS',20),
                        bg = 'black',fg = 'white',
                        command = lambda tn = r[0]: oprn_window(sql,tn))
        '''Since after each iteration the value inside oprn_window changes
           and after the loop finishes its final value ramains the final element
           of the iteration therefore we use a variable inside lambda so it
           captures the value then and there and whenever the btn is  cicked
           it passes on the captured value onto the function''' 
        btn.pack(fill = 'x',padx = 2,pady = 2)
        tables.append(btn)

    refresh.pack(fill = 'x',padx = 2,pady = 2)
    new_btn.pack(fill = 'x',padx = 2,pady = 2)

#6
def create_win_setup(new,new_back_btn,nf2_sub1,nf2_sub2,new_frame2,
                     new_add_field,send_values,T_titlebox):
    new.title('Creating new table')
    new.deiconify()
    new.grab_set()
    entry_box_list_create.clear()
    entry_box_list_create.append(T_titlebox)

    #Labels on frame 1 sub 2

    field1 = tk.Label(nf2_sub2,text = 'Enter field: ',
                      font = ('Comic Sans MS',15),
                      bg = 'black',fg = 'white',anchor = 'e')
    field1.pack(padx = 2,pady = 2,fill = 'x')

    field_datatype = tk.Label(nf2_sub2,text = 'Enter datatype: ',
                                font = ('Comic Sans MS',15),
                                bg = 'black',fg = 'white',anchor = 'e')
    field_datatype.pack(padx = 2,pady = 2,fill = 'x')

    field_constraint = tk.Label(nf2_sub2,
                                text = 'Enter Constraint (leave empty if not req.): ',
                                font = ('Comic Sans MS',15),
                                bg = 'black',fg = 'white',anchor = 'e')
    field_constraint.pack(padx = 2,pady = 2,fill = 'x')
    
    for r in range(3):
        enterbox = tk.Entry(new_frame2,font = ('Clear Sans',16),fg = 'black',
                            justify = 'left')
        entry_box_list_create.append(enterbox)
        enterbox.pack(padx = 2,pady = 2,fill = 'x')

    new_add_field.pack(fill = 'x',padx = 2,pady = 2)

total_field_widgets_on_screen = 1

#7
def add_field(nf2_sub1,nf2_sub2,new_frame2,new_add_field):
    new_add_field.pack_forget() 

    global total_field_widgets_on_screen
    total_field_widgets_on_screen += 1

    #Labels on frame 1 sub 1 (field no.)
    rec_no_fr1 = tk.Label(nf2_sub1,text = 'Field No. %s: ' % (total_field_widgets_on_screen),
                          font = ('Comic Sans MS',30),
                          bg = 'black',fg = 'white')
    rec_no_fr1.pack(padx = 2,pady = 2,fill = 'both',expand = True)

    #Labels on frame 1 sub 2

    field1 = tk.Label(nf2_sub2,text = 'Enter field: ',
                      font = ('Comic Sans MS',15),
                      bg = 'black',fg = 'white',anchor = 'e')
    field1.pack(padx = 2,pady = 2,fill = 'x')

    field_datatype = tk.Label(nf2_sub2,text = 'Enter datatype: ',
                                font = ('Comic Sans MS',15),
                                bg = 'black',fg = 'white',anchor = 'e')
    field_datatype.pack(padx = 2,pady = 2,fill = 'x')

    field_constraint = tk.Label(nf2_sub2,
                                text = 'Enter Constraint (leave empty if not req.): ',
                                font = ('Comic Sans MS',15),
                                bg = 'black',fg = 'white',anchor = 'e')
    field_constraint.pack(padx = 2,pady = 2,fill = 'x')

    #Entry boxes and labels on frame 2

    div = tk.Label(new_frame2,text = '',font = ('Comic Sans MS',1),
                   bg = 'black')
    div.pack(padx = 2,pady = 2,fill = 'x')
    
    for r in range(3):
        enterbox = tk.Entry(new_frame2,font = ('Clear Sans',16),fg = 'black',
                            justify = 'left')
        entry_box_list_create.append(enterbox)
        enterbox.pack(padx = 2,pady = 2,fill = 'x')

    new_add_field.pack(fill = 'x',padx = 2,pady = 2)

    if total_field_widgets_on_screen == 5:
        new_add_field.destroy()

#8
def create(newerror):

    try:
        tabme = entry_box_list_create[0].get()
        
        columns = []
        for i in range(1,len(entry_box_list_create),3):
            col_name = entry_box_list_create[i].get()
            col_type = entry_box_list_create[i + 1].get()
            col_con = entry_box_list_create[i + 2].get()
            columns.append(f'{col_name} {col_type} {col_con}')

        query = (f'CREATE TABLE {tabme} ({", ".join(columns)})')
        cur.execute(query)

        newerror.deiconify()
        newerror.grab_set()

        success = tk.Label(newerror,text = 'Table created successfully!',
                           font = ('Courier New',15),fg = 'red')
        success.pack(padx = 2,pady = 2,fill = 'both',expand = True)

        ok_btn = tk.Button(newerror,text = 'OK',font = ('Clear Sans',10),
                           bg = 'grey',command = lambda: leave(newerror))
        ok_btn.pack(padx = 2,pady = 2,fill = 'both',expand = True)

    except msc.Error:
        newerror.deiconify()
        newerror.grab_set()
        
        error = tk.Label(newerror,text = 'Field(s) either left empty or wrong values entered \n Try using valid names/datatypes/constraints',
                         font = ('Courier New',15),fg = 'red')
        error.pack(padx = 2,pady = 2,fill = 'both',expand = True)

        ok_btn = tk.Button(newerror,text = 'OK',font = ('Clear Sans',10),
                           bg = 'grey',command = lambda: leave(newerror))
        ok_btn.pack(padx = 2,pady = 2,fill = 'both',expand = True)

#9
def refresh_entry_boxes():
    for r in entry_box_list:
        r.delete(0,tk.END)

#10
def insert(entry_box_list_insert,table_name):
    values = ''
    for r in entry_box_list_insert:
        if r.get() == '':
            values += 'NULL,'
            continue
        values += "'" + r.get() + ',' + "'"

    values.rstrip(',')

    query = 'INSERT INTO %s VALUES(%s)' % (table_name,values)
    print(query)
    #cur.execute(query)























    








       
    
