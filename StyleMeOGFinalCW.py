#'''\\\\\\\\\\\\\\imports///////////////////'''
from tkinter import *
import sqlite3

#\\\\\\\Open app and main screen////////////
def open_app():
    main = Tk()
    back="main" #Used for when moving to other screens

    #\\\Does this even work?///
    conn = sqlite3.connect('styleme.db')
    cursor = conn.cursor()
    sql = "select * from items"
    results = cursor.execute(sql)
    all_items = results.fetchall()
    for items in all_items:
        print (items)
    cursor.close()
    
    consistency(main) #sets a style for all windows (size, bgcolour)
  
    #LISTS - UPDATE TO DATABASE
    wardrobeItems=["Blue Trousers","Dungarees", "Jumper"]
    outfitItems=["casual","hippy","crazy"]

    #WARDROBE ITEM DICTIONARY + IMAGE FILE VALUES
    #   - only .png - outifts will stay a list for now
    wardrobeItems2={"Blue Trousers":"Images\\bluetrousers.png","Dungarees":"Images\\dungarees.png", "Jumper":"Images\\jumper.png"}    

    #LOGO - UPDATE IMAGE TO LOGO
    photo = PhotoImage(file='Images/redcircle.png')
    photo = photo.subsample(3)          
    label = Label(image=photo)          
    label.image = photo                 
    label.pack(pady=10)

    #APPLICATION MAIN MENU
    Button(main, text ="Wardrobe", command =lambda: screen2screen(main,"Wardrobe",0),bg="red",fg="white").pack(pady=10)
    Button(main, text ="Outfits", command =lambda: screen2screen(main,"Outfits",0),bg="red",fg="white").pack(pady=10)
    Button(main, text ="Add", command =lambda: screen2screen(main,"Adding",0),bg="red",fg="white").pack(pady=10)

#\\\\\\\\Changing screens function/////////////////
    '''this function directs program to correct pages
        whilst also dealing with the previous pages'''
    
    def screen2screen(first, second, third):
        '''fisrt = where did you come from
            second = where are you going
             third = ONLY FOR ITEM PAGE - item reference
              '''
        
        global back

        #DEALING WITH PREVIOUS WINDOW
        if first == main:
            '''main screen has to be dealt with differently to the other screens
                else program may just close entirely
                 '''
            main.withdraw()
            back = "main"
            
        else:
            first.destroy()

        #WINDOW FUNCTION DIRECTORY
        if second == "Wardrobe":
            open_Wardrobe()
        elif second == "Outfits":
            open_Outfits()
        elif second == "ItemPage":
            open_ItemPage(first,third)
        elif second == "Adding":
            open_Adding(first)
        elif second == "main":
            main.deiconify()
        
#\\\\\\\\\\\\\\\\\Wardrobe page////////////////////////
            
    def open_Wardrobe():
        #When opening the screen...
        global back
        Wardrobe = Toplevel()
        consistency(Wardrobe)
        back="Wardrobe"

        #FRAMES FOR LAYOUT PURPOSES
        banner=Frame(Wardrobe, bg="red",pady=5, padx=5)
        banner.pack(fill=X)
        screen=Frame(Wardrobe)
        screen.pack(fill=BOTH)
        items1=Frame(screen)
        items1.pack(fill=BOTH,expand=TRUE,side=LEFT)
        items2=Frame(screen)
        items2.pack(fill=BOTH, expand=TRUE,side=LEFT)

        #BANNER CONTENT
        Button(banner, text = "Home", command= lambda: screen2screen(Wardrobe,"main",0), bg="red", fg="white").grid(row=0,column=0)
        Label(banner, text = "Wardrobe", bg="red", fg="white").grid(row=0,column=1,sticky="nsew")
        Button(banner, text = "Add", command= lambda: screen2screen(Wardrobe, "Adding",0), bg="red", fg="white",anchor="e").grid(row=0,column=6)

        #WARDROBE CONTENT
        for i in range (len(wardrobeItems)):
            '''for layout purposes
                I want two columns of wardrobe items
                - This if/else statement sorts all items
                   '''
            
            if i%2==0:
                Button(items1, text = wardrobeItems[i], command= lambda c=i: screen2screen(Wardrobe, "ItemPage",wardrobeItems[c]),
                       bg="white",height=15).pack(fill=X)
            else:
                Button(items2, text = wardrobeItems[i], command= lambda c=i: screen2screen(Wardrobe, "ItemPage",wardrobeItems[c]),
                       bg="white",height=15).pack(fill=X)

            #!!!TESTING!!! - ADDING IMAGES TO BUUTONS
            #I couldn't seem to get this to work
            '''
            if i%2==0:
                #I want the button to display the image & name of the item
                #imageloc = 'Images/redcircle.png'
                #photo = PhotoImage(file=imageloc)
                #photo = photo.subsample(5)                     
                Button(items1, text = wardrobeItems[i],
                          command= lambda c=i: screen2screen(Wardrobe, "ItemPage", wardrobeItems[c]),
                          bg="white",height=15).pack(fill=X)
                #b.image = photo
            else:
                #imageloc = 'Images/redcircle.png'
                #photo = PhotoImage(file=imageloc)
                #photo = photo.subsample(5)                     
                Button(items1, text = wardrobeItems[i],
                          command= lambda c=i: screen2screen(Wardrobe, "ItemPage", wardrobeItems[c]),
                          bg="white",height=15).pack(fill=X)
                #b.image = photo
            '''

#\\\\\\\\\\\\\\\\\\Outfits page/////////////////////////
    '''Wardrobe and outfit page has the same concept but different content
        The outfit page has all the working features of wardrobe
        whereas wardrobe may include some !!!TESTING!!! code snippets'''
    
    def open_Outfits():
        #When opening the screen...
        global back
        Outfits = Toplevel()
        consistency(Outfits)
        back="Outfits"
        
        #FRAMES FOR LAYOUT PURPOSES
        banner=Frame(Outfits, bg="red",pady=5, padx=5)
        banner.pack(fill=X)
        screen=Frame(Outfits)
        screen.pack(fill=BOTH)
        items1=Frame(screen)
        items1.pack(fill=BOTH,expand=TRUE,side=LEFT)
        items2=Frame(screen)
        items2.pack(fill=BOTH,expand=TRUE,side=LEFT)

        #BANNER CONTENT
        Button(banner, text = "Home", command= lambda: screen2screen(Outfits, "main",0),bg="red", fg="white").grid(row=0, column=0)
        Label(banner, text = "Welcome to Outfits", bg="red", fg="white").grid(row=0,column=1,sticky="nsew")
        Button(banner, text = "Add", command= lambda: screen2screen(Outfits, "Adding",0),bg="red", fg="white").grid(row=0,column=6)

        #OUTFITS CONTENT
        for i in range (len(outfitItems)):
            if i%2==0:
                Button(items1, text = outfitItems[i], command= lambda c=i: screen2screen(Outfits, "ItemPage",outfitItems[c]),
                       bg="white",height=15).pack(fill=X)
            else:
                Button(items2, text = outfitItems[i], command= lambda c=i: screen2screen(Outfits, "ItemPage",outfitItems[c]),
                       bg="white",height=15).pack(fill=X)
        
#\\\\\\\\\\\\\\\\\\\\\Item page//////////////////////////
    def open_ItemPage(origin,itemName):
        #When loading the screen...
        ItemPage = Toplevel()
        consistency(ItemPage)
        global back

        #FRAMES FOR LAYOUT PURPOSES
        banner=Frame(ItemPage, bg="red")
        banner.pack(fill=X)

        #BANNER CONTENT
        #Back button configuration
        if back=="Wardrobe":
            Button(banner, text = "<", command= lambda: screen2screen(ItemPage, "Wardrobe",0)).pack(side=LEFT)
        elif back=="Outfits":
            Button(banner, text = "<", command= lambda: screen2screen(ItemPage, "Outfits",0)).pack(side=LEFT)
        
        Label(banner, text = itemName,bg="red",fg="white").pack()
        '''insert photo here'''

        #DISPLAY ITEM IMAGE
        if back=="Wardrobe":
            imageloc = wardrobeItems2[itemName]
            photo = PhotoImage(file=imageloc)
            photo = photo.subsample(3)          
            label = Label(ItemPage,image=photo)          
            label.image = photo                 
            label.pack(pady=10)
        else:
            imageloc = 'Images/image.png'
            photo = PhotoImage(file=imageloc)
            photo = photo.subsample(3)          
            label = Label(ItemPage,image=photo)          
            label.image = photo                 
            label.pack(pady=10)

#\\\\\\\\\\\\\\\\\\\\\Adding page/////////////////////////
        
    def open_Adding(origin):
        global back
        global wardrobeItems
        global outfitItems
        Adding = Toplevel()
        consistency(Adding)

        #FRAMES FOR LAYOUT PURPOSES
        banner=Frame(Adding, bg="red")
        banner.pack(fill=X)
        values=Frame(Adding)
        values.pack(fill=BOTH)

        #BANNER CONTENT
        Button(banner, text = "Back", command= lambda: screen2screen(Adding, back,0)).pack(side=LEFT)
        Label(banner, text = "Welcome to Adding", bg="red",fg="white").pack()

        #ADDING FUNCTION
        def AddtoCollection():
            '''Here was my attempt to add items to collection
                this function only prints all information I would need when adding'''
            '''I commented out all the lines that gave me errors'''  
            
            #WHERE IM ADDING TO - DOESNT WORK
            global wardrobeItems
            global outfitItems

            #COLLECTING DATA
            destination =(d.get())
            name = (ItemName.get())

            #
            if destination == 1:
                #TESTING
                print ("Wardrobe")
                
                #wardrobeItems.append(ItemName)
                #print (wardrobeItems)
            elif destination == 2:
                #TESTING
                print ("Outfits")
                
                #outfitItems.append(ItemName)
                #print (outfitItems)
            else:
                #TESTING
                print ("Error")

            #TESTING
            print (name)
            

        #DESTINATION SECTION
        #Label
        destin= Label(values, text = "Destination")
        destin.grid(row=2,column=0)

        #Value input - RADIOBUTTONS
        d=IntVar()            
        wardrobe = Radiobutton(values, text="Wardrobe", variable = d, value=1)
        wardrobe.grid(row=2,column=1)
        outfits = Radiobutton(values, text="Outfits", variable = d, value=2)
        outfits.grid(row=2,column=2)

        #TESTING - DEFAULT SELECTION WHEN ADD OPENED THROUGH OTHER WINDOW
                #Doesn't work yet
        '''
        if back == "Wardrobe":
            select(wardrobe)
        elif back == "Outfits":
            select(outfits)
        '''
            
        #ITEM NAME SECTION
        #Label
        Label(values, text="Item Name").grid(row=3, column=0)
    
        #Textbox input
        ItemName = StringVar()
        e1 = Entry(values, textvariable=ItemName)
        e1.grid(row=3,column=1)
        Button(values, text="save", command= AddtoCollection).grid(row=6, column = 0)

#\\\\\\\\\\\\\\\\\\\\\END OF PAGES///////////////////
def consistency(wn):
    #wn.configure(background="white") - Frames ruin this
    wn.geometry("400x500")

    
open_app()
