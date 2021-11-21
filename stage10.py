import time
import os
import ctypes, sys
from tkinter import *
from PIL import *
from PIL import Image
import pytesseract
from tkinter import filedialog
from pdf2image import convert_from_path
from pdf2image import *

i = 1
file_path = " "
folder_path = " "
out_path = " "
root = Tk()

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '/usr/share/tesseract-ocr/4.00/tessdata'
#poppler_path=r'C:\Program Files\poppler-21.09.0\bin'

root.title("PDF Scrapper")

def browse(): #this function is called when the first browse button is clicked
    global file_path
    root.filename = filedialog.askopenfilename(initialdir="C:\ ", title="Select A File", filetypes=(("pdf files", "*.pdf"),("all files", "*.*"))) #this will return the file path in string
    file_path = root.filename

def browse1(): #this function is called when the second browse button is clicked
    global folder_path
    root.foldername = filedialog.askdirectory(initialdir="C:\ ") #this will return the folder path in string
    folder_path = root.foldername

def creation():
    p1 = folder_path+"/tmp"
    d1 = p1+"/1"
    d2 = p1+"/2"
    d3 = p1+"/3"
    os.mkdir(p1)
    os.mkdir(d1)
    os.mkdir(d2)
    os.mkdir(d3)

def convert():
    global out_path
    out_path = folder_path+"/tmp/1/"
    images = convert_from_path(file_path, output_folder=out_path, fmt='PNG', thread_count=3, output_file="output")
    global i
    i = 1
    for image in images:
        image.save('output'+str(i)+'.png', 'PNG')
        i += 1
def renm():
    a = 0
    for count, filename in enumerate(os.listdir(out_path)):
        dst ="p2i" + str(a) + ".png"
        src = out_path+ filename
        dst = out_path+ dst
        a = a+1
        # rename() function will
        # rename all the files
        os.rename(src, dst)
def crop():
    z = 0
    for z in range(0, i-1):
        infile = str(out_path)+'p2i'+str(z)+'.png'
        outfile = folder_path+"/tmp/2/"+str(z)+".png"
        img = Image.open(infile)
        w, h = img.size
        x = 1
        rw = int(w/2)
        for x in range(1,2):
            if(x == 1):
                cropped = img.crop((0, 0, w-rw, h))
                outfile = folder_path+"/tmp/2/"+str(z+z)+".png"
                cropped.save(outfile)
            x = x + 1
            if( x == 2):
                cropped = img.crop((rw, 0, w, h))
                outfile = folder_path+"/tmp/2/"+str(z+z+1)+".png"
                cropped.save(outfile)
        z = z + 1

def recon():
    p = 0
    y = i+i-2
    req = folder_path+"/tmp/3/"
    for p in range(0, y):
        infile = folder_path+"/tmp/2/"+str(p)+".png"
        img = Image.open(infile)
        text = pytesseract.image_to_string(img)
        mf = open(req+str(p)+".txt", "w")
        mf.write(text)
        mf.close()
        p = p + 1

def ad_detection():
    d = 0
    for d in range(0, 53):
        path1 = folder_path+'/tmp/3/'+str(d)+'.txt'
        size = os.path.getsize(path1)
        if (size < 1000):
            os.remove(path1)
def renm1():
    p = 54
    of = folder_path+'/tmp/3/'
    for count, filename in enumerate(os.listdir(of)):
        dst = str(p) + ".txt"
        src = of+ filename
        dst = of+ dst
        p = p+1
        # rename() function will
        # rename all the files
        os.rename(src, dst)

def dlt():
    dir1 = folder_path+"/tmp/1"
    dir2 = folder_path+"/tmp/2"
    dir3 = folder_path+"/tmp/3"
    dir4 = folder_path+"/tmp"
    dir5 = folder_path+"/tmp"
    dir6 = "C:/Users/User/Downloads/PYTHON PDF SCRAPPER/dist"

    for f in os.listdir(dir1):
        os.remove(os.path.join(dir1, f))
    for g in os.listdir(dir2):
        os.remove(os.path.join(dir2, g))
    for h in os.listdir(dir3):
        os.remove(os.path.join(dir3, h))
    for k in os.listdir(dir4):
        os.rmdir(os.path.join(dir4, k))
    os.rmdir(dir5)
    for abcd in range(1, i):
        os.remove(dir6+"/output"+str(abcd)+".png")

def arrange():
    dir1 = folder_path+"/tmp/3"
    for f in os.listdir(dir1):
        fileObj = open(dir1+"/"+f, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        l = len(words)
        w = 0
        j = 0
        k = 0
        m = 0
        n = 0
        bc = [ "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", ":",  ";",  "<",  ">",  "?",  "/", "\\", "'", "»"]
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        c5 = []
        for w in range(0,len(words)-1):
            x = str(words[w])
            x = x.strip()
            for z in bc:
                x = x.replace(z,'')
            x = x.strip()
            l1 = len(x)
            a1 = 0
            a2 = 5
            division = int(l1/5)
            if (division > 0):
                for itr in range(0,len(x)):
                    check = str(x[a1:a2])
                    check.strip()
                    a1 = a1 + 1
                    a2 = a2 + 1
                    if check.isdigit():
                        c1.append(check)
                    if (a2 > len(x)):
                        a2 = len(x)
                    if (a2 - a1 != 5):
                        break
                    itr = itr + 1
            w = w + 1


        for j in range(0,len(words)-1):
            x = str(words[j])
            x = x.strip()
            for z in bc:
                x = x.replace(z,'')
            x = x.strip()
            for z in c1:
                x = x.replace(z,'')
            x = x.strip()
            l1 = len(x)
            a1 = 0
            a2 = 4
            division = int(l1/4)
            if (division > 0):
                for itr in range(0,len(x)):
                    check = str(x[a1:a2])
                    check.strip()
                    a1 = a1 + 1
                    a2 = a2 + 1
                    if check.isdigit():
                        c5.append(check)
                    if (a2 > len(x)):
                        a2 = len(x)
                    if (a2 - a1 != 4):
                        break
                    itr = itr + 1
            j = j + 1

        for k in range(0,len(words)-1):
            x = str(words[k])
            x = x.strip()
            len1 = len(x) - 1
            bc1 = [ "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", ":",  ";",  "<",  ">",  "?",  "/", "\\", "'", "»", "D.K.W."]
            for z in bc1:
                x = x.replace(z,'')
            for z in c1:
                x = x.replace(z,'')
            for z in c5:
                x = x.replace(z,'')
            if (x.count(".",len1-3,len1+1) == 2):
                if (len(x) > 4):
                    x = x[len1-3:len1+1]
                    c3.append(x)

                c3.append(x)
        k = k + 1


        for m in range(0,len(words)-1):
            x = str(words[m])
            x = x.strip()
            len1 = len(x) - 1
            bc1 = [ "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", ":",  ";",  "<",  ">",  "?",  "/", "\\", "'", "»", "P.b.", "L.b.", "V.b.", "Lb.", "Pb.", "Vb.", "St.v"]
            for z in bc1:
                x = x.replace(z,'')
            x = x.strip()
            for z in c1:
                x = x.replace(z,'')
            for z in c5:
                x = x.replace(z,'')
            for z in c3:
                x = x.replace(z,'')
            if (len(x) < 11 and len(x) > 1):
                #print(x)
                c4.append(x)
            m = m + 1

        for n in range(0, l-1):
            x = str(words[n])
            x = x.strip()
            len1 = len(x) - 1
            for z in bc:
                x = x.replace(z,'')
            x = x.strip()
            bc1 = [ "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", ":",  ";",  "<",  ">",  "?",  "/", "\\", "'", "»", "P.b.", "L.b.", "V.b.", "Lb.", "Pb.", "Vb.", "St.v"]
            for z in bc1:
                x = x.replace(z,'')
            for z in c1:
                x = x.replace(z,'')
            x = x.strip()
            for z in c3:
                x = x.replace(z,'')
            x = x.strip()
            for z in c4:
                x = x.replace(z,'')
            x = x.strip()
            for z in c5:
                x = x.replace(z,'')
            x = x.strip()
            if(len(x) > 3):
                c2.append(x)
            n = n + 1
        p = 1
        acd = max(len(c1), len(c2), len(c3), len(c4), len(c5))
        for abc in range(len(c1), acd):
            c1.append("     ")
            abc = abc+1
        acd = max(len(c1), len(c2), len(c3), len(c4), len(c5))
        for abc in range(len(c2), acd):
            c2.append("                   ")
            abc = abc+1
        acd = max(len(c1), len(c2), len(c3), len(c4), len(c5))
        for abc in range(len(c3), acd):
            c3.append("    ")
            abc = abc+1
        acd = max(len(c1), len(c2), len(c3), len(c4), len(c5))
        for abc in range(len(c4), acd):
            c4.append("          ")
            abc = abc+1
        acd = max(len(c1), len(c2), len(c3), len(c4), len(c5))
        for abc in range(len(c5), acd):
            c5.append("    ")
            abc = abc+1
        acd = max(len(c1), len(c2), len(c3), len(c4), len(c5))
        for ac in range(0,acd-1):
            ad = ac
            ae = ac
            af = ac
            ag = ac
            ah = ac
            text = str(c1[ad])+"    "+str(c2[ae])+"    "+str(c3[af])+"    "+str(c4[ag])+"    "+str(c5[ah])+'\n'

            mf = open(folder_path+"/"+str(p)+".txt", "a")
            mf.write(text)
            ac = ac + 1
        mf.close()
        p = p + 1

def start():
    time.sleep(1)
    creation()
    time.sleep(1)
    convert()
    time.sleep(1)
    renm()
    time.sleep(1)
    crop()
    time.sleep(1)
    recon()
    time.sleep(1)
    ad_detection()
    time.sleep(1)
    renm1()
    time.sleep(2)
    arrange()
    time.sleep(1)
    dlt()


clicked = StringVar() #the dropdown menu is defined
clicked.set(".txt")

label1 = Label(root, text="Upload PDF")
label2 = Label(root, text="No. Of PDFs")
label3 = Label(root, text="Output Format")
label4 = Label(root, text="Output Location")

button1 = Button(root, text="Browse", command=browse) #to specify the file to be input
button2 = OptionMenu(root, clicked, ".txt", ".xml") #to select the output format
button3 = Button(root, text="Browse", command=browse1) #To specify the output location
button4 = Button(root, text="START", command=start) #to start the program

input1 = Entry(root) #to input the no of files

output_format = clicked.get() #the selected output format is saved

#spaceisdefined
spaces = Label(root, text="     ")
spaces1 = Label(root, text="        ")
#space starts
spaces.grid(row=0, column=0)
spaces.grid(row=1, column=0)
spaces.grid(row=2, column=0)
spaces.grid(row=3, column=0)
spaces.grid(row=4, column=0)
spaces.grid(row=5, column=0)
spaces.grid(row=6, column=0)
spaces.grid(row=7, column=0)
spaces.grid(row=8, column=0)
spaces.grid(row=9, column=0)
spaces.grid(row=10, column=0)
spaces.grid(row=11, column=0)
spaces.grid(row=12, column=0)
spaces.grid(row=13, column=0)
spaces.grid(row=14, column=0)
spaces.grid(row=15, column=0)
spaces.grid(row=0, column=1)
spaces.grid(row=1, column=1)
spaces.grid(row=2, column=1)
spaces.grid(row=3, column=1)
spaces.grid(row=4, column=1)
spaces.grid(row=5, column=1)
spaces.grid(row=6, column=1)
spaces.grid(row=7, column=1)
spaces.grid(row=8, column=1)
spaces.grid(row=9, column=1)
spaces.grid(row=10, column=1)
spaces.grid(row=11, column=1)
spaces.grid(row=12, column=1)
spaces.grid(row=13, column=1)
spaces.grid(row=14, column=1)
spaces.grid(row=15, column=1)
spaces.grid(row=0, column=2)
spaces.grid(row=1, column=2)
spaces.grid(row=2, column=2)
spaces.grid(row=4, column=2)
spaces.grid(row=5, column=2)
spaces.grid(row=7, column=2)
spaces.grid(row=8, column=2)
spaces.grid(row=10, column=2)
spaces.grid(row=11, column=2)
spaces.grid(row=13, column=2)
spaces.grid(row=14, column=2)
spaces.grid(row=0, column=3)
spaces.grid(row=1, column=3)
spaces.grid(row=2, column=3)
spaces.grid(row=3, column=3)
spaces.grid(row=4, column=3)
spaces.grid(row=5, column=3)
spaces.grid(row=6, column=3)
spaces.grid(row=7, column=3)
spaces.grid(row=8, column=3)
spaces.grid(row=9, column=3)
spaces.grid(row=10, column=3)
spaces.grid(row=11, column=3)
spaces.grid(row=12, column=3)
spaces.grid(row=13, column=3)
spaces.grid(row=14, column=3)
spaces1.grid(row=15, column=3)
spaces.grid(row=0, column=4)
spaces.grid(row=1, column=4)
spaces.grid(row=2, column=4)
spaces.grid(row=3, column=4)
spaces.grid(row=4, column=4)
spaces.grid(row=5, column=4)
spaces.grid(row=6, column=4)
spaces.grid(row=7, column=4)
spaces.grid(row=8, column=4)
spaces.grid(row=9, column=4)
spaces.grid(row=10, column=4)
spaces.grid(row=11, column=4)
spaces.grid(row=12, column=4)
spaces.grid(row=13, column=4)
spaces.grid(row=14, column=4)
spaces.grid(row=15, column=4)
spaces.grid(row=0, column=5)
spaces.grid(row=1, column=5)
spaces.grid(row=2, column=5)
spaces.grid(row=4, column=5)
spaces.grid(row=5, column=5)
spaces.grid(row=7, column=5)
spaces.grid(row=8, column=5)
spaces.grid(row=10, column=5)
spaces.grid(row=11, column=5)
spaces.grid(row=13, column=5)
spaces.grid(row=14, column=5)
#space ends

#Label diplay
label1.grid(row=3, column=2)
label2.grid(row=6, column=2)
label3.grid(row=9, column=2)
label4.grid(row=12, column=2)

#Input box/field display
input1.grid(row=6, column=5)

#Button display
button1.grid(row=3, column=5)
button2.grid(row=9, column=5)
button3.grid(row=12, column=5)
button4.grid(row=15, column=4)

root.mainloop()
