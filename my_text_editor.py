import tkinter as tk
from tkinter import Button, Grid, Menu, ttk
from tkinter import font, colorchooser, messagebox,filedialog
import os
from tkinter.constants import UNDERLINE

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.minsize(400,400)
main_application.title("MY TEXT EDITOR")
main_application.wm_iconbitmap('icon.ico')

############################# main menu #######################################
main_menu = tk.Menu()

#---------------------------------------------------------------------

# file 
# file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file = tk.Menu(main_menu,tearoff=False)



#------------------------------------------------------------------

# edit 
# edit icons
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu,tearoff=False)



# -----------------------------------------------------------------------------------

# view 
# view icon 
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu,tearoff=False)



#---------------------------------------------------------------------------------

# color theme 
# add color themes
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menu,tearoff=False)
theme_choice = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict = {
    'Light Default': ('#000000','#ffffff'),
    'Light Plus': ('#474747','#e0e0e0'),
    'Dark': ('#c4c4c4','#2d2d2d'),
    'Red': ('#2d2d2d','#ffe8e8'),
    'Monokai': ('#d3b774','#474747'),
    'Night Blue': ('#ededed','#6b9dc2'),
}


# cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Themes',menu=color_theme)

# ---------------------------$$$$$$ End main Menu $$$$$$ -------------------------


############################# tool bar #######################################~

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# font box 
font_tuple = tk.font.families()
font_family_var =tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=20,textvariable=font_family_var, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5,pady=5)
#-----------------------------------------------------------------------------------

# size_box
font_size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=15,textvariable=font_size_var,state='readonly')
font_size['values']=tuple(range(12,96,2))
font_size.current(1)
font_size.grid(row=0,column=1,padx=5,pady=5)
#----------------------------------------------------------------------------------------
# bold button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_button=ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=5,pady=5)

# italic button
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_button=ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5,pady=5)

# underline button
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_button=ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5,pady=5)

# font_color buttonn
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_button=ttk.Button(tool_bar,image=font_color_icon)
font_color_button.grid(row=0,column=5,padx=5,pady=5)

# align left buttonn
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_button=ttk.Button(tool_bar,image=align_left_icon)
align_left_button.grid(row=0,column=6,padx=5,pady=5)

# align center buttonn
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_button=ttk.Button(tool_bar,image=align_center_icon)
align_center_button.grid(row=0,column=7,padx=5,pady=5)

# align right buttonn
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_button=ttk.Button(tool_bar,image=align_right_icon)
align_right_button.grid(row=0,column=8,padx=5,pady=5)



# ---------------------------$$$$$$ End tool bar $$$$$$ -------------------------


############################# text editor #######################################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and  font size functionality
current_font_family = 'Arial'
current_font_size=14


def change_font_family(main_application):
    global current_font_family
    current_font_family = font_family_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(main_application):
    global current_font_size
    current_font_size = font_size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font_family)
font_size.bind("<<ComboboxSelected>>",change_font_size)

# buttons functionlity
# bold Button fuinctionality 
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_button.configure(command=change_bold)

# italic button functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

italic_button.configure(command=change_italic)


# underline button functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size,UNDERLINE))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_button.configure(command=change_underline)        

# change text color 
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_button.configure(command=change_font_color)    

# align functionality

# left 
def align_left():
    text_contant=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_contant,'left')

align_left_button.configure(command=align_left)    

# right 
def align_right():
    text_contant=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_contant,'right')

align_right_button.configure(command=align_right)    

# center 
def align_center():
    text_contant=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_contant,'center')

align_center_button.configure(command=align_center)    



text_editor.configure(font=('Arial',14))

# ---------------------------$$$$$$ End text editor $$$$$$ -------------------------


############################# status bar #######################################

status_bar = ttk.Label(main_application,text='status bar')
status_bar.pack(side=tk.BOTTOM,)

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'characters :{characters} words :{words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)        

# ---------------------------$$$$$$ End status bar $$$$$$ -------------------------


########################## main menu functinality#################################
####################### file menu #########################
# variable
url =""

# new file 
def new_file(event=None):
    global url
    url=""
    text_editor.delete(1.0,tk.END)

# open file 
def open_file(evebt=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All File','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))   

# save file 

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))             
            with open(url,'w',encoding='uft-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All File','*.*'))) 
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return         

# save as file 
def save_as_file(event=None ):
    global url
    try:
        content2=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All File','*.*'))) 
        url.write(content2)
        url.close() 
    except:
        return

# exit functionality
def exit_func(event=None):
    global url ,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel("Warning",'Do you want to save the File ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='uft-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All File','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return   

# add options in file menu 
file.add_command(label='New',image=new_icon,compound=tk.LEFT, accelerator='Ctrl+N',command=new_file)
file.add_command(label='Open',image=open_icon,compound=tk.LEFT, accelerator='Ctrl+O',command=open_file)
file.add_command(label='Save',image=save_icon,compound=tk.LEFT, accelerator='Ctrl+S',command=save_file)
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT, accelerator='Ctrl+Shift+S',command=save_as_file)
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT, accelerator='Ctrl+Q',command=exit_func)

#######################====================================########################

####################### edit menu #########################
# find functionality 
def find_func(event=None):
    
    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word = find_input.get()
        replace_word = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        text_editor.delete(1.0,tk.END)
        new_content = content.replace(word,replace_word) 
        text_editor.insert(1.0,new_content)              
         
    find_replace = tk.Toplevel()
    find_replace.title("Find") 
    find_replace.geometry('500x250+500+500') 
    find_replace.resizable(0,0)

    # add find frame 
    find_frame = ttk.LabelFrame(find_replace,text='Find/Replace')
    find_frame.pack(padx=20)        

    # label 
    text_find_label = ttk.Label(find_frame,text="Find : ")
    text_replace_label = ttk.Label(find_frame,text='Replace : ')

    # entry box 
    find_input = ttk.Entry(find_frame,width=30)
    replace_input = ttk.Entry(find_frame,width=30)

    # Button
    find_button = ttk.Button(find_frame,text="Find",command=find)
    replace_button = ttk.Button(find_frame,text="Replace",command=replace)

    # label grid 
    text_find_label.grid(row=0,column=0,padx=5,pady=5)
    text_replace_label.grid(row=1,column=0,padx=5,pady=5)

    # entry grid 
    find_input.grid(row=0,column=1,padx=5,pady=5)
    replace_input.grid(row=1,column=1,padx=5,pady=5)

    # button Grid
    find_button.grid(row=2,column=0,padx=5,pady=5)
    replace_button.grid(row=2,column=1,padx=5,pady=5)

    find_replace.mainloop()




# add options in edit menu 

edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT, accelerator='Ctrl+C',command=lambda : text_editor.event_generate('<Control C>'))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT, accelerator='Ctrl+V',command=lambda : text_editor.event_generate('<Control v>'))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT, accelerator='Ctrl+X',command=lambda : text_editor.event_generate('<Control x>'))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT, accelerator='Ctrl+Alt+C',command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT, accelerator='Ctrl+F',command=find_func)


#######################====================================########################



####################### view menu #########################




# add options in view Menu
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()   
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)  
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM,)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM,)
        show_statusbar = True





view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label="Status Bar",onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)


#######################====================================########################



####################### color themes menu #########################

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color,bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(bg=bg_color,fg=fg_color)

# add options in color thems

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1


# --------------------$$$$$$ End main Menu functinality $$$$$$ ---------------------


main_application.config(menu = main_menu)

#### bind shortcut keys
main_application.bind('<Control-n>',new_file)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Control-Alt-s>',save_as_file)
main_application.bind('<Control-q>',exit_func)
main_application.bind('<Control-f>',find_func)
main_application.mainloop()