import model 
import view

def button_click():
    t = view.start_selection()
    cont = model.extract_txt()
    if t == 1:
        view.search_name(cont)
    elif t == 2:
        view.search_surname(cont)
    elif t == 3:
        view.search_number(cont)
    elif t == 4:
        view.show_all(cont)    
    else:
        print('попробуйте снова')        

    
