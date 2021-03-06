import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
import math
import re
import tkinter.scrolledtext as st
from tkinter import ttk
import functools
from PIL import ImageTk, Image
import webbrowser




root = tk.Tk()
root.title('AVS')
#This is for fitting the image to the size of the GUI
def on_resize(event):
    image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)

root.geometry('1200x800')

bgimg = Image.open('mountain.jpg')
l = tk.Label(root)
l.place(x=0, y=0, relwidth=1, relheight=1)
l.bind('<Configure>', on_resize)
#This enables the output box to update, but prevents the user from typing stuff into it (read only)
class ReadOnlyText(st.ScrolledText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(state=tk.DISABLED)

        self.insert = self._unlock(super().insert)
        self.delete = self._unlock(super().delete)

    def _unlock(self, f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            self.config(state=tk.NORMAL)
            r = f(*args, **kwargs)
            self.config(state=tk.DISABLED)
            return r
        return wrap


ttk.Label(root,text = "Program Output",font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 15)

text_area = ReadOnlyText(root,width = 40,height = 10,font = ("Times New Roman",12))

text_area.grid(column = 0,columnspan=2,sticky=W+E,pady = 10, padx = 10)

tk.Label(root, text="Sparta File").grid(row=0)
tk.Label(root, text="Sequence File").grid(row=1)
tk.Label(root, text="NHSQC Peaklist").grid(row=2)
tk.Label(root, text="HNCA  Peaklist").grid(row=3)
tk.Label(root, text="HNCACB  Peaklist").grid(row=4)
tk.Label(root, text="HNCO  Peaklist").grid(row=5)
tk.Label(root, text="Save Sparta Filename").grid(row=6)
tk.Label(root, text="Save Peaklist Filename").grid(row=7)
tk.Label(root, text="Mutations (enter what amino acid was mutated E.G.if mutation was R133A, type 133R)\n If multiple mutations, seperate with space.\n Hit enter when done").grid(row=8)
tk.Label(root, text="Mutations (enter what it was mutated to E.G. if mutation was R133A, type 133A)\n If multiple mutations, seperate with space.\n Hit enter when done").grid(row=9)
tk.Label(root, text="Please type in what residue number the first amino acid in the sequence file is\nI.E. if the first amino acid in the sequence file is 20, type in 20\n Click enter when done").grid(row=10)
tk.Label(root, text="Set RMSD Threshold (Recommended 2-3). Click enter when done").grid(row=11)
tk.Label(root, text="NMR_STAR V2 or V3").grid(row=12)


e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e4 = tk.Entry(root)
e5 = tk.Entry(root)
e6 = tk.Entry(root)
e7 = tk.Entry(root)
e8 = tk.Entry(root)
e9 = tk.Entry(root)
e10 = tk.Entry(root)
e11 = tk.Entry(root)
e12 = tk.Entry(root)
e13 = tk.Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
e9.grid(row=8, column=1)
e10.grid(row=9, column=1)
e11.grid(row=10, column=1)
e12.grid(row=11, column=1)
e13.grid(row=12, column=1)

#These global values are what is entered by the user, and use within the script
sparta_file=()
sparta_directory=()
seq_file=()
seq_directory=()
save_file_sparta=()
save_file_peaklist=()
save_directory=()
NHSQC_file=()
NHSQC_directory=()
HNCA_file=()
HNCA_directory=()
HNCACB_file=()
HNCACB_directory=()
HNCO_file=()
HNCA_directory=()
mutation_list1=()
mutation_list2=()
seq_start=()
set_threshold=()
nmrstarfile=()
nmrstarfile_directory=()

#These functions define the function of the buttons
def input_file():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global sparta_directory
    global sparta_file
    sparta_directory=os.path.dirname(fullpath)
    sparta_file= os.path.basename(fullpath)
    label2=Label(root,text=fullpath).grid(row=0,column=1)

def input_seq():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global seq_file
    global seq_directory
    seq_directory=os.path.dirname(fullpath)
    seq_file= os.path.basename(fullpath)
    label3=Label(root,text=fullpath).grid(row=1,column=1)

def NHSQC():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global NHSQC_file
    global NHSQC_directory
    NHSQC_directory=os.path.dirname(fullpath)
    NHSQC_file= os.path.basename(fullpath)
    label4=Label(root,text=fullpath).grid(row=2,column=1)

def HNCA():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global HNCA_file
    global HNCA_directory
    HNCA_directory=os.path.dirname(fullpath)
    HNCA_file= os.path.basename(fullpath)
    label5=Label(root,text=fullpath).grid(row=3,column=1)

def HNCACB():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global HNCACB_file
    global HNCACB_directory
    HNCACB_directory=os.path.dirname(fullpath)
    HNCACB_file= os.path.basename(fullpath)
    label6=Label(root,text=fullpath).grid(row=4,column=1)

def HNCO():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global HNCO_file
    global HNCO_directory
    HNCO_directory=os.path.dirname(fullpath)
    HNCO_file= os.path.basename(fullpath)
    label7=Label(root,text=fullpath).grid(row=5,column=1)


def save_file():
    myFormats = [('Text File','*.txt'),]
    fullpath = tk.filedialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save file as...")
    global save_file_sparta
    global save_directory
    save_directory=os.path.dirname(fullpath)
    save_file_sparta=os.path.basename(fullpath)
    label2=Label(root,text=fullpath).grid(row=6,column=1)

def save_file2():
    myFormats = [('Text File','*.txt'),]
    fullpath = tk.filedialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save the image as...")
    global save_file_peaklist
    global save_directory
    save_directory=os.path.dirname(fullpath)
    save_file_peaklist=os.path.basename(fullpath)
    label8=Label(root,text=fullpath).grid(row=7,column=1)

def mutation_input():
    mutation1_input=e9.get()
    split_mutation=mutation1_input.split()
    global mutation_list1
    mutation_list1=split_mutation
    text_area.insert(tk.INSERT,f'mutation entered: {mutation1_input} \n')


def mutation_input2():
    mutation2_input=e10.get()
    split_mutation2=mutation2_input.split()
    global mutation_list2
    mutation_list2=split_mutation2
    text_area.insert(tk.INSERT,f'mutation entered: {mutation2_input} \n')

def seq_number():
    seq_input=e11.get()
    global seq_start
    seq_start=int(seq_input)
    text_area.insert(tk.INSERT,f'number entered: {seq_input} \n')

def threshold():
    threshold_input=e12.get()
    global set_threshold
    set_threshold=float(threshold_input)
    text_area.insert(tk.INSERT,f'RMSD Threshold set: {threshold_input} \n')

def help():
    webbrowser.open('https://github.com/sam-mahdi/Peaklist_Assignment_Library/blob/master/AVS/HELP/AVS_Manual.md')

def nmrstar():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global nmrstarfile
    global nmrstarfile_directory
    nmrstarfile_directory=os.path.dirname(fullpath)
    nmrstarfile= os.path.basename(fullpath)
    label8=Label(root,text=fullpath).grid(row=12,column=1)

def sparta_gen_only():
    text_area.delete(1.0,END)
    if sparta_file == ():
        text_area.insert(tk.INSERT,'please upload your sparta file (make sure to use browse)\n')
    if seq_file == ():
        text_area.insert(tk.INSERT,'please upload your seq file (make sure to use browse)\n')
    if save_file_sparta == ():
        text_area.insert(tk.INSERT,'please indicate sparta save file (make sure to use browse)\n')
    if seq_start == ():
        text_area.insert(tk.INSERT,'please enter a seq number (make sure to hit enter)\n')
    else:
        text_area.insert(tk.INSERT,'Starting Program\n')
#Determines the number of amino acids, used for filling in the missing data
        amino_acid_count=(0+seq_start)-1
        os.chdir(seq_directory)
        sequence_list=[]
        with open(seq_file) as sequence_file:
            for amino_acid in sequence_file:
                stripped_amino_acid=amino_acid.strip().upper()
                for word in stripped_amino_acid:
                    amino_acid_count+=1
                    sequence_list.append(str(amino_acid_count)+word)
#Extracts and combines the amino acid number, type, and its chemical shift and error from SPARTA+ pred.tab
#Since prolines lack the amide nitrogen and hydrogen, they are added in
        os.chdir(sparta_directory)
        text_area.insert(tk.INSERT,'Creating Sparta File\n')
        text_area.update_idletasks()
        y=0
        sparta_file_list1=[]
        sparta_file_list2=[]
        proline_counter=0
        with open(sparta_file) as sparta_predictions:
            for line in sparta_predictions:
                modifier=line.strip().upper()
                if re.findall('^\d+',modifier):
                    A=modifier.split()
                    del A[5:8]
                    del A[3]
                    A[0:3]=["".join(A[0:3])]
                    joined=" ".join(A)
                    proline_searcher=re.search('\BP',joined)
                    if proline_searcher != None:
                        proline_counter+=1
                        if proline_counter<2:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PN'+' 1000'+' 1000')
                    sparta_file_list1.append(joined)
                    if proline_searcher != None:
                        y+=1
                        if y==4:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PHN'+' 1000'+' 1000')
                            y=0
                            proline_counter=0
#Mutations that deviate from the crystal structure used for SPARTA+ are replaced with the appropriate amino acid type, and values replaced by 1000
#Designed to go through multiple mutation inputs (if doule or triple mutant)
        if mutation_list1==() or mutation_list2==():
            for amino_acids in sparta_file_list1:
                sparta_file_list2.append(amino_acids)
        else:
            for mutations,mutations2 in zip(mutation_list1,mutation_list2):
                for amino_acids in sparta_file_list1:
                    if re.findall(mutations,amino_acids):
                        splitting=amino_acids.split()
                        mutation=re.sub(mutations,mutations2,splitting[0])
                        mutation_value=re.sub('\d+.\d+',' 1000',splitting[1])
                        mutation_value2=re.sub('\d+.\d+',' 1000',splitting[2])
                        mutation_replacement=mutation+mutation_value+mutation_value2
                        sparta_file_list2.append(mutation_replacement)
                    else:
                        sparta_file_list2.append(amino_acids)
#Only appends amino acids that are within your sequence list. If crystal structure is truncated, or has more amino acids than you are looking at, they are ignored.
        sparta_file_list3=[]
        for aa in sparta_file_list2:
            modifiers=aa.strip()
            splitter=modifiers.split()
            searcher=re.search('^\d+[A-Z]',splitter[0])
            compiler=re.compile(searcher.group(0))
            sparta_sequence_comparison=list(filter(compiler.match,sequence_list))
            if sparta_sequence_comparison != []:
                sparta_file_list3.append(aa)

#The first amino acid will only lack the amide nitrogen and hydrogen.
#This goes through the first 5 entires, if the 5th entry does not equal the 4th, then the first 4 entires (the first amino acid) is removed.
        temp_list=[]
        temp_counter=0
        for checker in sparta_file_list3:
            temp_modifier=checker.strip()
            temp_split=temp_modifier.split()
            temp_finder=re.search('^\d+',temp_split[0])
            temp_list.append(temp_finder.group(0))
            temp_counter+=1
            if temp_counter==5:
                if int(temp_finder.group(0))==int(temp_list[0]):
                    break
                else:
                    del sparta_file_list3[0:4]
                    break
#The last amino acid will be missing the carbonyl
#At this point, every amino acids should have 6 entries, if the file is not divisible by 6, the last 5 (the last amino acid) is removed
        if len(sparta_file_list3)%6 != 0:
            del sparta_file_list3[-5:-1]
        os.chdir(save_directory)
        with open(save_file_sparta,'w') as file:
            for stuff_to_write in sparta_file_list3:
                file.write(stuff_to_write+'\n')
        text_area.insert(tk.INSERT,'Sparta file written\n')

def fun():
    text_area.delete(1.0,END)
    if sparta_file == ():
        text_area.insert(tk.INSERT,'please upload your sparta file (make sure to use browse)\n')
    if seq_file == ():
        text_area.insert(tk.INSERT,'please upload your seq file (make sure to use browse)\n')
    if save_file_sparta == ():
        text_area.insert(tk.INSERT,'please indicate sparta save file (make sure to use browse)\n')
    if save_file_peaklist == ():
        text_area.insert(tk.INSERT,'please indicate peaklist save file (make sure to use browse)\n')
    if NHSQC_file == ():
        text_area.insert(tk.INSERT,'please upload NHSQC peaklist (make sure to use browse)\n')
    if HNCA_file == ():
        text_area.insert(tk.INSERT,'please upload HNCO file (make sure to use browse)\n')
    if HNCACB_file == ():
        text_area.insert(tk.INSERT,'please upload HNCACB file (make sure to use browse)\n')
    if HNCO_file == ():
        text_area.insert(tk.INSERT,'please upload HNCO file (make sure to use browse)\n')
    if set_threshold == ():
        text_area.insert(tk.INSERT,'please enter a threshold (make sure to hit enter)\n')
    if seq_start == ():
        text_area.insert(tk.INSERT,'please enter a seq number (make sure to hit enter)\n')
    else:
        text_area.insert(tk.INSERT,'Starting Program\n')
#Determines the number of amino acids, used for filling in the missing data
        amino_acid_count=(0+seq_start)-1
        os.chdir(seq_directory)
        sequence_list=[]
        with open(seq_file) as sequence_file:
            for amino_acid in sequence_file:
                stripped_amino_acid=amino_acid.strip().upper()
                for word in stripped_amino_acid:
                    amino_acid_count+=1
                    sequence_list.append(str(amino_acid_count)+word)
#Extracts and combines the amino acid number, type, and its chemical shift and error from SPARTA+ pred.tab
#Since prolines lack the amide nitrogen and hydrogen, they are added in
        os.chdir(sparta_directory)
        text_area.insert(tk.INSERT,'Creating Sparta File\n')
        text_area.update_idletasks()
        y=0
        sparta_file_list1=[]
        sparta_file_list2=[]
        proline_counter=0
        with open(sparta_file) as sparta_predictions:
            for line in sparta_predictions:
                modifier=line.strip().upper()
                if re.findall('^\d+',modifier):
                    A=modifier.split()
                    del A[5:8]
                    del A[3]
                    A[0:3]=["".join(A[0:3])]
                    joined=" ".join(A)
                    proline_searcher=re.search('\BP',joined)
                    if proline_searcher != None:
                        proline_counter+=1
                        if proline_counter<2:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PN'+' 1000'+' 1000')
                    sparta_file_list1.append(joined)
                    if proline_searcher != None:
                        y+=1
                        if y==4:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PHN'+' 1000'+' 1000')
                            y=0
                            proline_counter=0
#Mutations that deviate from the crystal structure used for SPARTA+ are replaced with the appropriate amino acid type, and values replaced by 1000
#Designed to go through multiple mutation inputs (if doule or triple mutant)
        if mutation_list1==() or mutation_list2==():
            for amino_acids in sparta_file_list1:
                sparta_file_list2.append(amino_acids)
        else:
            for mutations,mutations2 in zip(mutation_list1,mutation_list2):
                for amino_acids in sparta_file_list1:
                    if re.findall(mutations,amino_acids):
                        splitting=amino_acids.split()
                        mutation=re.sub(mutations,mutations2,splitting[0])
                        mutation_value=re.sub('\d+.\d+',' 1000',splitting[1])
                        mutation_value2=re.sub('\d+.\d+',' 1000',splitting[2])
                        mutation_replacement=mutation+mutation_value+mutation_value2
                        sparta_file_list2.append(mutation_replacement)
                    else:
                        sparta_file_list2.append(amino_acids)
#Only appends amino acids that are within your sequence list. If crystal structure is truncated, or has more amino acids than you are looking at, they are ignored.
        sparta_file_list3=[]
        for aa in sparta_file_list2:
            modifiers=aa.strip()
            splitter=modifiers.split()
            searcher=re.search('^\d+[A-Z]',splitter[0])
            compiler=re.compile(searcher.group(0))
            sparta_sequence_comparison=list(filter(compiler.match,sequence_list))
            if sparta_sequence_comparison != []:
                sparta_file_list3.append(aa)

#The first amino acid will only lack the amide nitrogen and hydrogen.
#This goes through the first 5 entires, if the 5th entry does not equal the 4th, then the first 4 entires (the first amino acid) is removed.
        temp_list=[]
        temp_counter=0
        for checker in sparta_file_list3:
            temp_modifier=checker.strip()
            temp_split=temp_modifier.split()
            temp_finder=re.search('^\d+',temp_split[0])
            temp_list.append(temp_finder.group(0))
            temp_counter+=1
            if temp_counter==5:
                if int(temp_finder.group(0))==int(temp_list[0]):
                    break
                else:
                    del sparta_file_list3[0:4]
                    break
#The last amino acid will be missing the carbonyl
#At this point, every amino acids should have 6 entries, if the file is not divisible by 6, the last 5 (the last amino acid) is removed
        if len(sparta_file_list3)%6 != 0:
            del sparta_file_list3[-5:-1]

        text_area.insert(tk.INSERT,'Creating Peaklist File\n')
        text_area.update_idletasks()

        #This portion creates a list to be used later, the size of the list determines how many data points should be there
        os.chdir(seq_directory)
        list2=[]
        x=(0+seq_start)-1
        dict={}
        with open(seq_file) as sequence_file:
            for line in sequence_file:
                B=line.strip().upper()
                for word in B:
                    x+=1
                    dict[x]=word
                    list2.append(x)
        #This portion compiles data from various data files into 1 list.
        os.chdir(NHSQC_directory)
        list5=[]
        with open(NHSQC_file) as NHSQC:
            for line in NHSQC:
                modifications=line.strip().upper()
                if re.findall('^[A-Z]-*\d+[A-Z]',modifications):
        #This portion fills in any gaps in the data
                    C=re.search(r'-*\d+',modifications)
                    for a in list2:
                        if a == int(C.group(0)):
                            break
                        elif a>int(C.group(0)):
                            break
                        else:
                            for z in list5:
                                if re.findall(f'^[A-Z]{a}N',z):
                                    break
                            else:
                                list5.append(f'{dict[a]}{a}N-HN' + ' 1000' + '\n')
                                list5.append(f'{dict[a]}{a}N-HA' + ' 1000' +'\n')
                                list5.append(f'{dict[a]}{a}N-C' + ' 1000' +'\n')
                                list5.append(f'{dict[a]}{a}N-CA' + ' 1000' +'\n')
                                list5.append(f'{dict[a]}{a}N-CB' + ' 1000' +'\n')
                                list5.append(f'{dict[a]}{a}N-HN' + ' 1000' +'\n')
                    splitting1=modifications.split()
                    list5.append(splitting1[0]+ ' '+ splitting1[1] + '\n')
                    A=re.search(r'[A-Z]-*\d+',modifications)
                    list5.append(f'{A.group(0)}N-HA'+ ' 1000' + '\n')
                    glycine_search=re.search(r'^G',modifications)
                    if glycine_search != None:
                        list5.append(f'{A.group(0)}N-HA2'+ ' 1000' + '\n')
                    with open(HNCA_file) as HNCA,open(HNCO_file) as HNCO, open (HNCACB_file) as HNCACB:
                        for line3 in HNCO:
                            modifications3=line3.strip().upper()
                            if re.findall(f'{A.group(0)}C',modifications3):
                                splitting3=modifications3.split()
                                list5.append(f'{A.group(0)}C' + ' '+  splitting3[2]+'\n')
                                break
                        else:
                            list5.append(f'{A.group(0)}C-HN'+ ' 1000' +'\n')
                        for line2 in HNCA:
                            modifications2=line2.strip().upper()
                            if re.findall(f'{A.group(0)}N-CA',modifications2):
                                splitting2=modifications2.split()
                                list5.append(splitting2[0] + ' ' + splitting2[2]+ '\n')
                                break
                        else:
                            list5.append(f'{A.group(0)}N-CA'+ ' 1000' +'\n')
                        for line4 in HNCACB:
                            modifications4=line4.strip().upper()
                            splitting4=modifications4.split()
                            if glycine_search != None:
                                break
                            if re.findall(f'{A.group(0)}N-CB',modifications4):
                                list5.append(splitting4[0] + ' '+splitting4[2]+'\n')
                                break
                        else:
                            list5.append(f'{A.group(0)}N-CB'+ ' 1000' +'\n')
                    list5.append(splitting1[0]+ ' '+ splitting1[2] + '\n')
#This part compares the peaklist to the SPARTA file, and only appens amino acids that are in both SPARTA and the Peaklist file
        text_area.insert(tk.INSERT,'Converting Peaklist to match Sparta\n')
        text_area.update_idletasks()
        list3=[]
        count=0
        for lines in list5:
            modify=lines.strip()
            splitting5=modify.split()
            number_search=re.search('\d+',splitting5[0])
            amino_acid_search=re.search('^[A-Z]',splitting5[0])
            string_to_be_searched=number_search.group(0)+amino_acid_search.group(0)+'N'
            r=re.compile(string_to_be_searched)
            comparison_to_sparta=list(filter(r.match,sparta_file_list3))
            if comparison_to_sparta != []:
                list3.append(modify)
            else:
                count+=1
                if count==6:
                    #if any amino acid is the peaklist, but not SPARTA file, it will be excluded and printed out here
                    count=0
                    text_area.insert(tk.INSERT,f'{splitting5[0]} was excluded\n')
#This portion calculates the RMSD. First calculates the square deviations of each amino acid with its SPARTA counterpart
#Then it sums up these deviations (once you've done all 6 atoms), if the RMSD is above the set threshold, it prints it out
        list4=[]
        number=0
        for experimental,predictions in zip(list3,sparta_file_list3):
            number+=1
            splitting6=experimental.split()
            splitting7=predictions.split()
            square_deviation=((float(splitting7[1])-float(splitting6[1]))**2)/((float(splitting7[2]))**2)
            if square_deviation>100:
                square_deviation=0
            else:
                list4.append(square_deviation)
            if number%6 ==0:
                if len(list4)==0:
                    continue
                else:
                    rmsd=math.sqrt((1/int(len(list4)))*sum(list4))
                    list4.clear()
                    if rmsd>float(set_threshold):
                        text_area.insert(tk.INSERT,f'{splitting6[0]} had a rmsd of {rmsd}\n')
                    #text_area.insert(tk.INSERT,f'rmsd={rmsd}\n')
#The compiled files can be useful to use for other SPARTA comparisons (such as determing unknowns), so they are saved for later use
        os.chdir(save_directory)
        with open(save_file_sparta,'w') as file, open(save_file_peaklist,'w') as file2:
            for stuff_to_write in sparta_file_list3:
                file.write(stuff_to_write+'\n')
            for stuff_to_write2 in list3:
                    file2.write(stuff_to_write2+'\n')

def nmrstarrun3():
    text_area.delete(1.0,END)
    if sparta_file == ():
        text_area.insert(tk.INSERT,'please upload your sparta file (make sure to use browse)\n')
    if seq_file == ():
        text_area.insert(tk.INSERT,'please upload your seq file (make sure to use browse)\n')
    if save_file_sparta == ():
        text_area.insert(tk.INSERT,'please indicate sparta save file (make sure to use browse)\n')
    if save_file_peaklist == ():
        text_area.insert(tk.INSERT,'please indicate peaklist save file (make sure to use browse)\n')
    if set_threshold == ():
        text_area.insert(tk.INSERT,'please enter a threshold (make sure to hit enter)\n')
    if seq_start == ():
        text_area.insert(tk.INSERT,'please enter a seq number (make sure to hit enter)\n')
    if nmrstarfile == ():
        text_area.insert(tk.INSERT,'please upload your nmrstar file (make sure to use browse)\n')
    else:
        text_area.insert(tk.INSERT,'Starting Program\n')
        amino_acid_count=(0+seq_start)-1
        os.chdir(seq_directory)
        sequence_list=[]
        with open(seq_file) as sequence_file:
            for amino_acid in sequence_file:
                stripped_amino_acid=amino_acid.strip().upper()
                for word in stripped_amino_acid:
                    amino_acid_count+=1
                    sequence_list.append(str(amino_acid_count)+word)
        #Extracts and combines the amino acid number, type, and its chemical shift and error from SPARTA+ pred.tab
        #Since prolines lack the amide nitrogen and hydrogen, they are added in
        os.chdir(sparta_directory)
        text_area.insert(tk.INSERT,'Creating Sparta File\n')
        text_area.update_idletasks()
        y=0
        sparta_file_list1=[]
        sparta_file_list2=[]
        proline_counter=0
        with open(sparta_file) as sparta_predictions:
            for line in sparta_predictions:
                modifier=line.strip().upper()
                if re.findall('^\d+',modifier):
                    A=modifier.split()
                    del A[5:8]
                    del A[3]
                    A[0:3]=["".join(A[0:3])]
                    joined=" ".join(A)
                    proline_searcher=re.search('\BP',joined)
                    if proline_searcher != None:
                        proline_counter+=1
                        if proline_counter<2:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PN'+' 1000'+' 1000')
                    sparta_file_list1.append(joined)
                    if proline_searcher != None:
                        y+=1
                        if y==4:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PHN'+' 1000'+' 1000')
                            y=0
                            proline_counter=0
        #Mutations that deviate from the crystal structure used for SPARTA+ are replaced with the appropriate amino acid type, and values replaced by 1000
        #Designed to go through multiple mutation inputs (if doule or triple mutant)
        if mutation_list1==() or mutation_list2==():
            for amino_acids in sparta_file_list1:
                sparta_file_list2.append(amino_acids)
        else:
            for mutations,mutations2 in zip(mutation_list1,mutation_list2):
                for amino_acids in sparta_file_list1:
                    if re.findall(mutations,amino_acids):
                        splitting=amino_acids.split()
                        mutation=re.sub(mutations,mutations2,splitting[0])
                        mutation_value=re.sub('\d+.\d+',' 1000',splitting[1])
                        mutation_value2=re.sub('\d+.\d+',' 1000',splitting[2])
                        mutation_replacement=mutation+mutation_value+mutation_value2
                        sparta_file_list2.append(mutation_replacement)
                    else:
                        sparta_file_list2.append(amino_acids)
        #Only appends amino acids that are within your sequence list. If crystal structure is truncated, or has more amino acids than you are looking at, they are ignored.
        sparta_file_list3=[]
        for aa in sparta_file_list2:
            modifiers=aa.strip()
            splitter=modifiers.split()
            searcher=re.search('^\d+[A-Z]',splitter[0])
            compiler=re.compile(searcher.group(0))
            sparta_sequence_comparison=list(filter(compiler.match,sequence_list))
            if sparta_sequence_comparison != []:
                sparta_file_list3.append(aa)
        #The first amino acid will only lack the amide nitrogen and hydrogen.
        #This goes through the first 5 entires, if the 5th entry does not equal the 4th, then the first 4 entires (the first amino acid) is removed.
        temp_list=[]
        temp_counter=0
        for checker in sparta_file_list3:
            temp_modifier=checker.strip()
            temp_split=temp_modifier.split()
            temp_finder=re.search('^\d+',temp_split[0])
            temp_list.append(temp_finder.group(0))
            temp_counter+=1
            if temp_counter==5:
                if int(temp_finder.group(0))==int(temp_list[0]):
                    break
                else:
                    del sparta_file_list3[0:4]
                    break
        if len(sparta_file_list3)%6 != 0:
            del sparta_file_list3[-5:-1]

        acid_map = {
              'ASP':'D', 'THR':'T', 'SER':'S', 'GLU':'E',
              'PRO':'P', 'GLY':'G', 'ALA':'A', 'CYS':'C',
              'VAL':'V', 'MET':'M', 'ILE':'I', 'LEU':'L',
              'TYR':'Y', 'PHE':'F', 'HIS':'H', 'LYS':'K',
              'ARG':'R', 'TRP':'W', 'GLN':'Q', 'ASN':'N'
            }
        os.chdir(nmrstarfile_directory)
        final_list=[]
        x=0
        with open(nmrstarfile) as file:
          for lines in file:
            modifier=lines.strip()
            A=re.search(r'\b\d+\s+[A-Z]{3}\s+\w+\s+\w+\s+\d+\s+\d+',modifier)
            if A != None:
                atom_search=A.string
                C=atom_search.split()
                amino_acid_number=str(int(C[5])+int(seq_start)-1)
                residue_type=C[6]
                atom_type=C[7]
                converted=acid_map[residue_type]
                chemical_shift=C[10]
                G=[amino_acid_number]+[converted]+[atom_type]+[chemical_shift]
                if atom_type == 'N' or atom_type == 'HA' or atom_type =='CA' or atom_type == 'CB' or atom_type=='H' or atom_type=='C':
                    joined=' '.join(G)
                    final_list.append(joined)

        final_list2=[]
        atom_number_list=[]
        temp_list=[]
        temp_list2=[]
        temp_list3=[]
        for amino_acids in final_list:
            splitter2=amino_acids.split()
            x+=1
            if x >= 2:
                if splitter2[0] != atom_number_list[0]:
                    list_compiler=temp_list2+temp_list3+temp_list
                    final_list2.append(list_compiler)
                    atom_number_list.clear()
                    temp_list.clear()
                    temp_list2.clear()
                    temp_list3.clear()
                    atom_number_list.append(splitter2[0])
                    if splitter2[2] == 'H':
                        temp_list.append(amino_acids)
                    elif splitter2[2] == 'N':
                        temp_list2.append(amino_acids)
                    else:
                        temp_list3.append(amino_acids)
                else:
                    if splitter2[2] == 'H':
                        temp_list.append(amino_acids)
                    elif splitter2[2] == 'N':
                        temp_list2.append(amino_acids)
                    else:
                        temp_list3.append(amino_acids)
            else:
                atom_number_list.append(splitter2[0])
                if splitter2[2] == 'H':
                    temp_list.append(amino_acids)
                elif splitter2[2] == 'N':
                    temp_list2.append(amino_acids)
                else:
                    temp_list3.append(amino_acids)

        final_list3=[]
        for lists in final_list2:
            for elements in lists:
                splitting=elements.split()
                joined=''.join(splitting[0:2])
                final_list3.append(joined+'-'+splitting[2]+ ' ' + splitting[3])

        list2=[]
        x=(0+seq_start)-1
        dict={}
        with open(seq_file) as sequence_file:
            for line in sequence_file:
                B=line.strip().upper()
                for word in B:
                    x+=1
                    dict[x]=word
                    list2.append(x)

        final_list4=[]
        temp_list=[]
        count=0
        for values in final_list3:
            atom_find=re.search('^-*\d+[A-Z]',values)
            count+=1
            temp_list.append(atom_find.group(0))
            if count == 1:
                if re.findall('-N',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-N'+' 1000'+'\n')
                    count+=1
            if count == 2:
                if re.findall('-HA',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-HA'+' 1000'+'\n')
                    count+=1
            if count == 3:
                if re.findall('-C\s',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-C'+' 1000'+'\n')
                    count+=1
            if count == 4:
                if re.findall('-CA',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-CA'+' 1000'+'\n')
                    count+=1
            if count == 5:
                if re.findall('-CB',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-CB'+' 1000'+'\n')
                    count+=1
            if count == 6:
                if re.findall('-H\s',values) != []:
                    final_list4.append(values+'\n')
                    count=0
                    temp_list.clear()
                else:
                    final_list4.append(temp_list[0]+'-H'+' 1000'+'\n')
                    temp_list.clear()
                    if re.findall('-N',values) != []:
                        final_list4.append(values+'\n')
                        count=1
                    if re.findall('-HA',values) != []:
                        final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                        final_list4.append(values+'\n')
                        count=2
                    if re.findall('-C',values) != []:
                        final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-HA'+' 1000'+'\n')
                        final_list4.append(values+'\n')
                        count=3
                    if re.findall('-CA',values) != []:
                        final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-HA'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-C'+' 1000'+'\n')
                        final_list4.append(values+'\n')
                        count=4
                    if re.findall('-CB',values) != []:
                        final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-HA'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-C'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-CA'+' 1000'+'\n')
                        final_list4.append(values+'\n')
                        count=5

        glycine_search_list=[]
        for stuff in final_list4:
            if re.findall('\BG-HA',stuff) != []:
                splitting=stuff.split()
                glycine_search_list.append(stuff)
                glycine_search_list.append(splitting[0]+'2'+' 1000'+'\n')
            elif re.findall('\BG-CB',stuff) != []:
                pass
            else:
                glycine_search_list.append(stuff)

        outskirts_added=[]
        temp_outskirt_list=[]
        x=0
        y=0
        for atoms in glycine_search_list:
            A=re.search('^-*\d+',atoms)
            outskirts_added.append(atoms)
            x+=1
            y+=1
            if x == 6:
                if len(temp_outskirt_list)>0:
                    if int(A.group(0)) == (int(temp_outskirt_list[0])+1):
                        x=0
                        temp_outskirt_list.clear()
                        temp_outskirt_list.append(A.group(0))
                        pass
                    else:
                        z=int(temp_outskirt_list[0])+1
                        offset=0
                        while z != int(A.group(0)):
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-H' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-CB' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-CA' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-C' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-HA' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-HN' + ' 1000' + '\n')
                            z+=1
                            offset+=6
                        x=0
                        y+=offset
                        temp_outskirt_list.clear()
                        temp_outskirt_list.append(A.group(0))
                else:
                    temp_outskirt_list.append(A.group(0))
                    x=0
        list3=[]
        count=0
        for lines in outskirts_added:
            modify=lines.strip()
            splitting5=modify.split()
            number_search=re.search('^-*\d+[A-Z]',splitting5[0])
            r=re.compile(number_search.group(0))
            comparison_to_sparta=list(filter(r.match,sparta_file_list3))
            if comparison_to_sparta != []:
                list3.append(modify)
            else:
                count+=1
                if count==6:
                    #if any amino acid is the peaklist, but not SPARTA file, it will be excluded and printed out here
                    count=0
                    text_area.insert(tk.INSERT,f'{splitting5[0]} was excluded\n')

        list4=[]
        number=0
        for experimental,predictions in zip(list3,sparta_file_list3):
            number+=1
            splitting6=experimental.split()
            splitting7=predictions.split()
            square_deviation=((float(splitting7[1])-float(splitting6[1]))**2)/((float(splitting7[2]))**2)
            if square_deviation>100:
                square_deviation=0
            else:
                list4.append(square_deviation)
            if number%6 ==0:
                if len(list4)==0:
                    continue
                else:
                    rmsd=math.sqrt((1/int(len(list4)))*sum(list4))
                    list4.clear()
                    if rmsd>float(set_threshold):
                        text_area.insert(tk.INSERT,f'{splitting6[0]} had a rmsd of {rmsd}\n')
        os.chdir(save_directory)
        with open(save_file_sparta,'w') as file, open(save_file_peaklist,'w') as file2:
            for stuff_to_write in sparta_file_list3:
                file.write(stuff_to_write+'\n')
            for stuff_to_write2 in list3:
                    file2.write(stuff_to_write2+'\n')

def nmrstarrun2():
    text_area.delete(1.0,END)
    if sparta_file == ():
        text_area.insert(tk.INSERT,'please upload your sparta file (make sure to use browse)\n')
    if seq_file == ():
        text_area.insert(tk.INSERT,'please upload your seq file (make sure to use browse)\n')
    if save_file_sparta == ():
        text_area.insert(tk.INSERT,'please indicate sparta save file (make sure to use browse)\n')
    if save_file_peaklist == ():
        text_area.insert(tk.INSERT,'please indicate peaklist save file (make sure to use browse)\n')
    if set_threshold == ():
        text_area.insert(tk.INSERT,'please enter a threshold (make sure to hit enter)\n')
    if seq_start == ():
        text_area.insert(tk.INSERT,'please enter a seq number (make sure to hit enter)\n')
    if nmrstarfile == ():
        text_area.insert(tk.INSERT,'please upload your nmrstar file (make sure to use browse)\n')
    else:
        text_area.insert(tk.INSERT,'Starting Program\n')
        amino_acid_count=(0+seq_start)-1
        os.chdir(seq_directory)
        sequence_list=[]
        with open(seq_file) as sequence_file:
            for amino_acid in sequence_file:
                stripped_amino_acid=amino_acid.strip().upper()
                for word in stripped_amino_acid:
                    amino_acid_count+=1
                    sequence_list.append(str(amino_acid_count)+word)
        #Extracts and combines the amino acid number, type, and its chemical shift and error from SPARTA+ pred.tab
        #Since prolines lack the amide nitrogen and hydrogen, they are added in
        os.chdir(sparta_directory)
        text_area.insert(tk.INSERT,'Creating Sparta File\n')
        text_area.update_idletasks()
        y=0
        sparta_file_list1=[]
        sparta_file_list2=[]
        proline_counter=0
        with open(sparta_file) as sparta_predictions:
            for line in sparta_predictions:
                modifier=line.strip().upper()
                if re.findall('^\d+',modifier):
                    A=modifier.split()
                    del A[5:8]
                    del A[3]
                    A[0:3]=["".join(A[0:3])]
                    joined=" ".join(A)
                    proline_searcher=re.search('\BP',joined)
                    if proline_searcher != None:
                        proline_counter+=1
                        if proline_counter<2:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PN'+' 1000'+' 1000')
                    sparta_file_list1.append(joined)
                    if proline_searcher != None:
                        y+=1
                        if y==4:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PHN'+' 1000'+' 1000')
                            y=0
                            proline_counter=0
        #Mutations that deviate from the crystal structure used for SPARTA+ are replaced with the appropriate amino acid type, and values replaced by 1000
        #Designed to go through multiple mutation inputs (if doule or triple mutant)
        if mutation_list1==() or mutation_list2==():
            for amino_acids in sparta_file_list1:
                sparta_file_list2.append(amino_acids)
        else:
            for mutations,mutations2 in zip(mutation_list1,mutation_list2):
                for amino_acids in sparta_file_list1:
                    if re.findall(mutations,amino_acids):
                        splitting=amino_acids.split()
                        mutation=re.sub(mutations,mutations2,splitting[0])
                        mutation_value=re.sub('\d+.\d+',' 1000',splitting[1])
                        mutation_value2=re.sub('\d+.\d+',' 1000',splitting[2])
                        mutation_replacement=mutation+mutation_value+mutation_value2
                        sparta_file_list2.append(mutation_replacement)
                    else:
                        sparta_file_list2.append(amino_acids)
        #Only appends amino acids that are within your sequence list. If crystal structure is truncated, or has more amino acids than you are looking at, they are ignored.
        sparta_file_list3=[]
        for aa in sparta_file_list2:
            modifiers=aa.strip()
            splitter=modifiers.split()
            searcher=re.search('^\d+[A-Z]',splitter[0])
            compiler=re.compile(searcher.group(0))
            sparta_sequence_comparison=list(filter(compiler.match,sequence_list))
            if sparta_sequence_comparison != []:
                sparta_file_list3.append(aa)

        #The first amino acid will only lack the amide nitrogen and hydrogen.
        #This goes through the first 5 entires, if the 5th entry does not equal the 4th, then the first 4 entires (the first amino acid) is removed.
        temp_list=[]
        temp_counter=0
        for checker in sparta_file_list3:
            temp_modifier=checker.strip()
            temp_split=temp_modifier.split()
            temp_finder=re.search('^\d+',temp_split[0])
            temp_list.append(temp_finder.group(0))
            temp_counter+=1
            if temp_counter==5:
                if int(temp_finder.group(0))==int(temp_list[0]):
                    break
                else:
                    del sparta_file_list3[0:4]
                    break
        if len(sparta_file_list3)%6 != 0:
            del sparta_file_list3[-5:-1]
#NMRSTAR files are stored as 3 letter abbreviatons, SPARTA+ files use single letter, thus this dict will conver the 3 letter, into 1 letter
        acid_map = {
              'ASP':'D', 'THR':'T', 'SER':'S', 'GLU':'E',
              'PRO':'P', 'GLY':'G', 'ALA':'A', 'CYS':'C',
              'VAL':'V', 'MET':'M', 'ILE':'I', 'LEU':'L',
              'TYR':'Y', 'PHE':'F', 'HIS':'H', 'LYS':'K',
              'ARG':'R', 'TRP':'W', 'GLN':'Q', 'ASN':'N'
            }

        os.chdir(nmrstarfile_directory)
        final_list=[]
        x=0
#NMRSTAR files contain a lot of into, and may have multiple formats. However all formats contain atom number, followed by amino acid type, and atom type
#If protein contains tag, it will be missing in the SPARTA+ file. However, NMRSTAR includes tags into its atom_number ocunt. Thus, the offset will take this into account.
        with open(nmrstarfile) as file:
          for lines in file:
            modifier=lines.strip()
            A=re.search(r'\d+\s+[A-Z]{3}\s+\w+\s+\w+\s+\d+',modifier)
            if A != None:
                atom_search=A.string
                C=atom_search.split()
                amino_acid_number=str(int(C[2])+int(seq_start)-1)
                residue_type=C[3]
                atom_type=C[4]
                converted=acid_map[residue_type]
                chemical_shift=C[6]
#NMSTAR sorta atom number and atom types in different format. This converts it into the SPARTA+ format
                G=[amino_acid_number]+[converted]+[atom_type]+[chemical_shift]
#NMRSTAR files can contain carbon/hydrogen info from side chain assignment. This is used to remove them and focus exlclusively on backbone.
#As a result of this formatting tho, backbone atoms must use this nomenclature (i.e. H cannot be HN)
                if atom_type == 'N' or atom_type == 'HA' or atom_type =='CA' or atom_type == 'CB' or atom_type=='H' or atom_type=='C':
                    joined=' '.join(G)
                    final_list.append(joined)

        final_list2=[]
        atom_number_list=[]
        temp_list=[]
        temp_list2=[]
        temp_list3=[]
#NMRSTAR sorts atoms in various ways. NMRSTAR 2 and 3 sort H,C,CA,CB,N whereas SPARKY converted NMRSTAR3 sorts C,CA,CB,N,HN this sorts them into the SPARTA+ order
        for amino_acids in final_list:
            splitter2=amino_acids.split()
            x+=1
#This line states you start with the first amino acid, and then compare it to the 2nd. If they the same, then store the hydrogen, and nitrogen in different lists.
#When you reach the end of the amino acid (splitter2[0]!=atom_number_list[0]) then combine everythin gin the proper format. I.E. N=temp_list2, C,CA,CB=temp_list3, H=temp_list
            if x >= 2:
                if splitter2[0] != atom_number_list[0]:
                    list_compiler=temp_list2+temp_list3+temp_list
                    final_list2.append(list_compiler)
                    atom_number_list.clear()
                    temp_list.clear()
                    temp_list2.clear()
                    temp_list3.clear()
                    atom_number_list.append(splitter2[0])
                    if splitter2[2] == 'H':
                        temp_list.append(amino_acids)
                    elif splitter2[2] == 'N':
                        temp_list2.append(amino_acids)
                    else:
                        temp_list3.append(amino_acids)
                else:
                    if splitter2[2] == 'H':
                        temp_list.append(amino_acids)
                    elif splitter2[2] == 'N':
                        temp_list2.append(amino_acids)
                    else:
                        temp_list3.append(amino_acids)
            else:
                atom_number_list.append(splitter2[0])
                if splitter2[2] == 'H':
                    temp_list.append(amino_acids)
                elif splitter2[2] == 'N':
                    temp_list2.append(amino_acids)
                else:
                    temp_list3.append(amino_acids)
#The above makes a list of lists. This joinst he list, then joines them. Then you convert it back into a list, and add the -.
        final_list3=[]
        for lists in final_list2:
            for elements in lists:
                splitting=elements.split()
                joined=''.join(splitting[0:2])
                final_list3.append(joined+'-'+splitting[2]+ ' ' + splitting[3])
#This creates the dictionary for adding in the blanks
        list2=[]
        x=(0+seq_start)-1
        dict={}
        with open(seq_file) as sequence_file:
            for line in sequence_file:
                B=line.strip().upper()
                for word in B:
                    x+=1
                    dict[x]=word
                    list2.append(x)
#This will search through every amino acid, if it is msising any of the atoms. It will fill it in with the value of 1000.
#At this point, we know the order will be N, HA, C, CA, CB, H due to the previous loops. Thus, we can go through each value, and if it isn't there, fill it in.
        final_list4=[]
        temp_list=[]
        count=0
        for values in final_list3:
            atom_find=re.search('^-*\d+[A-Z]',values)
            count+=1
            temp_list.append(atom_find.group(0))
            if count == 1:
                if re.findall('-N',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-N'+' 1000'+'\n')
                    count+=1
            if count == 2:
                if re.findall('-HA',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-HA'+' 1000'+'\n')
                    count+=1
            if count == 3:
                if re.findall('-C\s',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-C'+' 1000'+'\n')
                    count+=1
            if count == 4:
                if re.findall('-CA',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-CA'+' 1000'+'\n')
                    count+=1
            if count == 5:
                if re.findall('-CB',values) != []:
                    final_list4.append(values+'\n')
                else:
                    final_list4.append(temp_list[0]+'-CB'+' 1000'+'\n')
                    count+=1
            if count == 6:
                if re.findall('-H\s',values) != []:
                    final_list4.append(values+'\n')
                    count=0
                    temp_list.clear()
                else:
#Sometimes, the last value might not be a hydrogen. Sometimes one amino acid may only have one chemical shift, and will be missing everything else.
#To keep those chemical shifts, but compensate for the missing ones, this goes through every value it should have, and if it doesn't have it, adds it in.
                    final_list4.append(temp_list[0]+'-H'+' 1000'+'\n')
                    temp_list.clear()
                    if re.findall('-N',values) != []:
                        final_list4.append(values+'\n')
                        count=1
                    if re.findall('-HA',values) != []:
                        final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                        final_list4.append(values+'\n')
                        count=2
                    if re.findall('-C',values) != []:
                        final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-HA'+' 1000'+'\n')
                        final_list4.append(values+'\n')
                        count=3
                    if re.findall('-CA',values) != []:
                        final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-HA'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-C'+' 1000'+'\n')
                        final_list4.append(values+'\n')
                        count=4
                    if re.findall('-CB',values) != []:
                        final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-HA'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-C'+' 1000'+'\n')
                        final_list4.append(atom_find.group(0)+'-CA'+' 1000'+'\n')
                        final_list4.append(values+'\n')
                        count=5
#The above scripts will add a CB value for Glycines. Additionally, our first loop does not transfer HA2 values. This will add an HA2, and eliminate the added CB
        glycine_search_list=[]
        for stuff in final_list4:
            if re.findall('\BG-HA',stuff) != []:
                splitting=stuff.split()
                glycine_search_list.append(stuff)
                glycine_search_list.append(splitting[0]+'2'+' 1000'+'\n')
            elif re.findall('\BG-CB',stuff) != []:
                pass
            else:
                glycine_search_list.append(stuff)

#The previous loops added 6 values for every amino acid. However, there are some amino acids with no values. This portion will fill in those gaps.
#It will search and extract the number, and store that into a temp_outskirt_list. When it has gone through it 6 times (one amino acid), it will go to the next amino acid (i+1)
#If the int(A.group(0)), the atom number of the amino acid we are looking at, is equivalent to its i-1 atom_number +1, then it will add the values and continue on
#If not, it will go through and add the 6 values as needed. To index properly we will simply use a value y, which counts how many atoms we have gone through so far. Since we are at the end of the new amino acids
#we need to add -6. It will do this, until the next amino acid is equal to the i-1 amino acids i+1.

        outskirts_added=[]
        temp_outskirt_list=[]
        x=0
        y=0
        for atoms in glycine_search_list:
            A=re.search('^-*\d+',atoms)
            outskirts_added.append(atoms)
            x+=1
            y+=1
            if x == 6:
                if len(temp_outskirt_list)>0:
                    if int(A.group(0)) == (int(temp_outskirt_list[0])+1):
                        x=0
                        temp_outskirt_list.clear()
                        temp_outskirt_list.append(A.group(0))
                        pass
                    else:
                        z=int(temp_outskirt_list[0])+1
                        offset=0
                        while z != int(A.group(0)):
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-H' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-CB' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-CA' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-C' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-HA' + ' 1000' +'\n')
                            outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-HN' + ' 1000' + '\n')
                            z+=1
                            offset+=6
                        x=0
                        y+=offset
                        temp_outskirt_list.clear()
                        temp_outskirt_list.append(A.group(0))
                else:
                    temp_outskirt_list.append(A.group(0))
                    x=0
        list3=[]
        count=0
        for lines in outskirts_added:
            modify=lines.strip()
            splitting5=modify.split()
            number_search=re.search('^-*\d+[A-Z]',splitting5[0])
            r=re.compile(number_search.group(0))
            comparison_to_sparta=list(filter(r.match,sparta_file_list3))
            if comparison_to_sparta != []:
                list3.append(modify)
            else:
                count+=1
                if count==6:
                    #if any amino acid is the peaklist, but not SPARTA file, it will be excluded and printed out here
                    count=0
                    text_area.insert(tk.INSERT,f'{splitting5[0]} was excluded\n')

        list4=[]
        number=0
        for experimental,predictions in zip(list3,sparta_file_list3):
            number+=1
            splitting6=experimental.split()
            splitting7=predictions.split()
            square_deviation=((float(splitting7[1])-float(splitting6[1]))**2)/((float(splitting7[2]))**2)
            if square_deviation>100:
                square_deviation=0
            else:
                list4.append(square_deviation)
            if number%6 ==0:
                if len(list4)==0:
                    continue
                else:
                    rmsd=math.sqrt((1/int(len(list4)))*sum(list4))
                    list4.clear()
                    if rmsd>float(set_threshold):
                        text_area.insert(tk.INSERT,f'{splitting6[0]} had a rmsd of {rmsd}\n')
        os.chdir(save_directory)
        with open(save_file_sparta,'w') as file, open(save_file_peaklist,'w') as file2:
            for stuff_to_write in sparta_file_list3:
                file.write(stuff_to_write+'\n')
            for stuff_to_write2 in list3:
                    file2.write(stuff_to_write2+'\n')

def sparky_to_nmrstar():
    text_area.delete(1.0,END)
    if sparta_file == ():
        text_area.insert(tk.INSERT,'please upload your sparta file (make sure to use browse)\n')
    if seq_file == ():
        text_area.insert(tk.INSERT,'please upload your seq file (make sure to use browse)\n')
    if save_file_sparta == ():
        text_area.insert(tk.INSERT,'please indicate sparta save file (make sure to use browse)\n')
    if save_file_peaklist == ():
        text_area.insert(tk.INSERT,'please indicate peaklist save file (make sure to use browse)\n')
    if set_threshold == ():
        text_area.insert(tk.INSERT,'please enter a threshold (make sure to hit enter)\n')
    if seq_start == ():
        text_area.insert(tk.INSERT,'please enter a seq number (make sure to hit enter)\n')
    if nmrstarfile == ():
        text_area.insert(tk.INSERT,'please upload your nmrstar file (make sure to use browse)\n')
    else:
        text_area.insert(tk.INSERT,'Starting Program\n')
        amino_acid_count=(0+seq_start)-1
        os.chdir(seq_directory)
        sequence_list=[]
        with open(seq_file) as sequence_file:
            for amino_acid in sequence_file:
                stripped_amino_acid=amino_acid.strip().upper()
                for word in stripped_amino_acid:
                    amino_acid_count+=1
                    sequence_list.append(str(amino_acid_count)+word)
        #Extracts and combines the amino acid number, type, and its chemical shift and error from SPARTA+ pred.tab
        #Since prolines lack the amide nitrogen and hydrogen, they are added in
        os.chdir(sparta_directory)
        text_area.insert(tk.INSERT,'Creating Sparta File\n')
        text_area.update_idletasks()
        y=0
        sparta_file_list1=[]
        sparta_file_list2=[]
        proline_counter=0
        with open(sparta_file) as sparta_predictions:
            for line in sparta_predictions:
                modifier=line.strip().upper()
                if re.findall('^\d+',modifier):
                    A=modifier.split()
                    del A[5:8]
                    del A[3]
                    A[0:3]=["".join(A[0:3])]
                    joined=" ".join(A)
                    proline_searcher=re.search('\BP',joined)
                    if proline_searcher != None:
                        proline_counter+=1
                        if proline_counter<2:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PN'+' 1000'+' 1000')
                    sparta_file_list1.append(joined)
                    if proline_searcher != None:
                        y+=1
                        if y==4:
                            proline_count=re.search('^\d+',joined)
                            sparta_file_list1.append(f'{proline_count.group(0)}PHN'+' 1000'+' 1000')
                            y=0
                            proline_counter=0
        #Mutations that deviate from the crystal structure used for SPARTA+ are replaced with the appropriate amino acid type, and values replaced by 1000
        #Designed to go through multiple mutation inputs (if doule or triple mutant)
        if mutation_list1==() or mutation_list2==():
            for amino_acids in sparta_file_list1:
                sparta_file_list2.append(amino_acids)
        else:
            for mutations,mutations2 in zip(mutation_list1,mutation_list2):
                for amino_acids in sparta_file_list1:
                    if re.findall(mutations,amino_acids):
                        splitting=amino_acids.split()
                        mutation=re.sub(mutations,mutations2,splitting[0])
                        mutation_value=re.sub('\d+.\d+',' 1000',splitting[1])
                        mutation_value2=re.sub('\d+.\d+',' 1000',splitting[2])
                        mutation_replacement=mutation+mutation_value+mutation_value2
                        sparta_file_list2.append(mutation_replacement)
                    else:
                        sparta_file_list2.append(amino_acids)
        #Only appends amino acids that are within your sequence list. If crystal structure is truncated, or has more amino acids than you are looking at, they are ignored.
        sparta_file_list3=[]
        for aa in sparta_file_list2:
            modifiers=aa.strip()
            splitter=modifiers.split()
            searcher=re.search('^\d+[A-Z]',splitter[0])
            compiler=re.compile(searcher.group(0))
            sparta_sequence_comparison=list(filter(compiler.match,sequence_list))
            if sparta_sequence_comparison != []:
                sparta_file_list3.append(aa)

        #The first amino acid will only lack the amide nitrogen and hydrogen.
        #This goes through the first 5 entires, if the 5th entry does not equal the 4th, then the first 4 entires (the first amino acid) is removed.
        temp_list=[]
        temp_counter=0
        for checker in sparta_file_list3:
            temp_modifier=checker.strip()
            temp_split=temp_modifier.split()
            temp_finder=re.search('^\d+',temp_split[0])
            temp_list.append(temp_finder.group(0))
            temp_counter+=1
            if temp_counter==5:
                if int(temp_finder.group(0))==int(temp_list[0]):
                    break
                else:
                    del sparta_file_list3[0:4]
                    break
        if len(sparta_file_list3)%6 != 0:
            del sparta_file_list3[-5:-1]

        acid_map = {
              'ASP':'D', 'THR':'T', 'SER':'S', 'GLU':'E',
              'PRO':'P', 'GLY':'G', 'ALA':'A', 'CYS':'C',
              'VAL':'V', 'MET':'M', 'ILE':'I', 'LEU':'L',
              'TYR':'Y', 'PHE':'F', 'HIS':'H', 'LYS':'K',
              'ARG':'R', 'TRP':'W', 'GLN':'Q', 'ASN':'N'
            }
    os.chdir(nmrstarfile_directory)
    final_list=[]
    x=0
    with open(nmrstarfile) as file:
      for lines in file:
        modifier=lines.strip()
        A=re.search(r'\d+\s+[A-Z]{3}\s+\w+\s+\w+\s+\d+',modifier)
        if A != None:
            atom_search=A.string
            C=atom_search.split()
            amino_acid_number=C[2]
            amino_acid_number=str(int(C[2])+int(seq_start)-1)
            residue_type=C[3]
            atom_type=C[4]
            converted=acid_map[residue_type]
            chemical_shift=C[7]
            G=[amino_acid_number]+[converted]+[atom_type]+[chemical_shift]
            if atom_type == 'N' or atom_type == 'HA' or atom_type =='CA' or atom_type == 'CB' or atom_type=='H' or atom_type=='C':
                joined=' '.join(G)
                final_list.append(joined)
    final_list2=[]
    atom_number_list=[]
    temp_list=[]
    temp_list2=[]
    temp_list3=[]
    for amino_acids in final_list:
        splitter2=amino_acids.split()
        x+=1
        if x >= 2:
            if splitter2[0] != atom_number_list[0]:
                list_compiler=temp_list2+temp_list3+temp_list
                final_list2.append(list_compiler)
                atom_number_list.clear()
                temp_list.clear()
                temp_list2.clear()
                temp_list3.clear()
                atom_number_list.append(splitter2[0])
                if splitter2[2] == 'H':
                    temp_list.append(amino_acids)
                elif splitter2[2] == 'N':
                    temp_list2.append(amino_acids)
                else:
                    temp_list3.append(amino_acids)
            else:
                if splitter2[2] == 'H':
                    temp_list.append(amino_acids)
                elif splitter2[2] == 'N':
                    temp_list2.append(amino_acids)
                else:
                    temp_list3.append(amino_acids)
        else:
            atom_number_list.append(splitter2[0])
            if splitter2[2] == 'H':
                temp_list.append(amino_acids)
            elif splitter2[2] == 'N':
                temp_list2.append(amino_acids)
            else:
                temp_list3.append(amino_acids)

    final_list3=[]
    for lists in final_list2:
        for elements in lists:
            splitting=elements.split()
            joined=''.join(splitting[0:2])
            final_list3.append(joined+'-'+splitting[2]+ ' ' + splitting[3])

    list2=[]
    x=(0+seq_start)-1
    dict={}
    os.chdir(seq_directory)
    with open(seq_file) as sequence_file:
        for line in sequence_file:
            B=line.strip().upper()
            for word in B:
                x+=1
                dict[x]=word
                list2.append(x)
    final_list4=[]
    temp_list=[]
    count=0
    i=0
    os.chdir(nmrstarfile_directory)
    for values in final_list3:
        atom_find=re.search('^-*\d+[A-Z]',values)
        count+=1
        temp_list.append(atom_find.group(0))
        if count == 1:
            if re.findall('-N',values) != []:
                final_list4.append(values+'\n')
            else:
                final_list4.append(temp_list[0]+'-N'+' 1000'+'\n')
                count+=1
        if count == 2:
            if re.findall('-HA',values) != []:
                final_list4.append(values+'\n')
            else:
                final_list4.append(temp_list[0]+'-HA'+' 1000'+'\n')
                count+=1
        if count == 3:
            if re.findall('-C\s',values) != []:
                final_list4.append(values+'\n')
            else:
                final_list4.append(temp_list[0]+'-C'+' 1000'+'\n')
                count+=1
        if count == 4:
            if re.findall('-CA',values) != []:
                final_list4.append(values+'\n')
            else:
                final_list4.append(temp_list[0]+'-CA'+' 1000'+'\n')
                count+=1
        if count == 5:
            if re.findall('-CB',values) != []:
                final_list4.append(values+'\n')
            else:
                final_list4.append(temp_list[0]+'-CB'+' 1000'+'\n')
                count+=1
        if count == 6:
            if re.findall('-H\s',values) != []:
                final_list4.append(values+'\n')
                count=0
                temp_list.clear()
            else:
                final_list4.append(temp_list[0]+'-H'+' 1000'+'\n')
                temp_list.clear()
                if re.findall('-N',values) != []:
                    final_list4.append(values+'\n')
                    count=1
                if re.findall('-HA',values) != []:
                    final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                    final_list4.append(values+'\n')
                    count=2
                if re.findall('-C\s',values) != []:
                    final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                    final_list4.append(atom_find.group(0)+'-HA'+' 1000'+'\n')
                    final_list4.append(values+'\n')
                    count=3
                if re.findall('-CA',values) != []:
                    final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                    final_list4.append(atom_find.group(0)+'-HA'+' 1000'+'\n')
                    final_list4.append(atom_find.group(0)+'-C'+' 1000'+'\n')
                    final_list4.append(values+'\n')
                    count=4
                if re.findall('-CB',values) != []:
                    final_list4.append(atom_find.group(0)+'-N'+' 1000'+'\n')
                    final_list4.append(atom_find.group(0)+'-HA'+' 1000'+'\n')
                    final_list4.append(atom_find.group(0)+'-C'+' 1000'+'\n')
                    final_list4.append(atom_find.group(0)+'-CA'+' 1000'+'\n')
                    final_list4.append(values+'\n')
                    count=5


    glycine_search_list=[]
    for stuff in final_list4:
        if re.findall('\BG-HA',stuff) != []:
            splitting=stuff.split()
            glycine_search_list.append(stuff)
            glycine_search_list.append(splitting[0]+'2'+' 1000'+'\n')
        elif re.findall('\BG-CB',stuff) != []:
            pass
        else:
            glycine_search_list.append(stuff)

    outskirts_added=[]
    temp_outskirt_list=[]
    x=0
    y=0
    for atoms in glycine_search_list:
        A=re.search('^-*\d+',atoms)
        outskirts_added.append(atoms)
        x+=1
        y+=1
        if x == 6:
            if len(temp_outskirt_list)>0:
                if int(A.group(0)) == (int(temp_outskirt_list[0])+1):
                    x=0
                    temp_outskirt_list.clear()
                    temp_outskirt_list.append(A.group(0))
                    pass
                else:
                    z=int(temp_outskirt_list[0])+1
                    offset=0
                    while z != int(A.group(0)):
                        outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-H' + ' 1000' +'\n')
                        outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-CB' + ' 1000' +'\n')
                        outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-CA' + ' 1000' +'\n')
                        outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-C' + ' 1000' +'\n')
                        outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-HA' + ' 1000' +'\n')
                        outskirts_added.insert((y+offset-6),f'{z}{dict[z]}N-N' + ' 1000' + '\n')
                        z+=1
                        offset+=6
                    x=0
                    y+=offset
                    temp_outskirt_list.clear()
                    temp_outskirt_list.append(A.group(0))
            else:
                temp_outskirt_list.append(A.group(0))
                x=0

    list3=[]
    count=0
    for lines in outskirts_added:
        modify=lines.strip()
        splitting5=modify.split()
        number_search=re.search('^-*\d+[A-Z]',splitting5[0])
        r=re.compile(number_search.group(0))
        comparison_to_sparta=list(filter(r.match,sparta_file_list3))
        if comparison_to_sparta != []:
            list3.append(modify)
        else:
            count+=1
            if count==6:
                #if any amino acid is the peaklist, but not SPARTA file, it will be excluded and printed out here
                count=0
                text_area.insert(tk.INSERT,f'{splitting5[0]} was excluded\n')

    list4=[]
    number=0
    for experimental,predictions in zip(list3,sparta_file_list3):
        number+=1
        splitting6=experimental.split()
        splitting7=predictions.split()
        square_deviation=((float(splitting7[1])-float(splitting6[1]))**2)/((float(splitting7[2]))**2)
        if square_deviation>100:
            square_deviation=0
        else:
            list4.append(square_deviation)
        if number%6 ==0:
            if len(list4)==0:
                continue
            else:
                rmsd=math.sqrt((1/int(len(list4)))*sum(list4))
                list4.clear()
                if rmsd>float(set_threshold):
                    text_area.insert(tk.INSERT,f'{splitting6[0]} had a rmsd of {rmsd}\n')
        os.chdir(save_directory)
        with open(save_file_sparta,'w') as file, open(save_file_peaklist,'w') as file2:
            for stuff_to_write in sparta_file_list3:
                file.write(stuff_to_write+'\n')
            for stuff_to_write2 in list3:
                    file2.write(stuff_to_write2+'\n')




tk.Button(root,text='browse',command=input_file).grid(row=0,column=2)
tk.Button(root,text='browse',command=input_seq).grid(row=1,column=2)
tk.Button(root,text='browse',command=NHSQC).grid(row=2,column=2)
tk.Button(root,text='browse',command=HNCA).grid(row=3,column=2)
tk.Button(root,text='browse',command=HNCACB).grid(row=4,column=2)
tk.Button(root,text='browse',command=HNCO).grid(row=5,column=2)
tk.Button(root,text='browse',command=save_file).grid(row=6,column=2)
tk.Button(root,text='browse',command=save_file2).grid(row=7,column=2)
tk.Button(root,text='enter',command=mutation_input).grid(row=8,column=2)
tk.Button(root,text='enter',command=mutation_input2).grid(row=9,column=2)
tk.Button(root,text='enter',command=seq_number).grid(row=10,column=2)
tk.Button(root,text='enter',command=threshold).grid(row=11,column=2)
tk.Button(root,text='browse',command=nmrstar).grid(row=12,column=2)
tk.Button(root,text='Quit',command=root.quit).grid(row=15,column=1)
tk.Button(root,text='Run using SPARKY files',command=fun).grid(row=13,column=0)
tk.Button(root,text='Run using NMRSTAR V3 file',command=nmrstarrun3).grid(row=13,column=1)
tk.Button(root,text='Run using NMRSTAR V2 file',command=nmrstarrun2).grid(row=13,column=2)
tk.Button(root,text='Run using SPARKY converted NMRSTAR V3 file',command=sparky_to_nmrstar).grid(row=14,column=2)
tk.Button(root,text='Help',command=help).grid(row=14,column=0)
tk.Button(root,text='Generate SPARTA file only (for APS)',command=sparta_gen_only).grid(row=14,column=1)

root.mainloop()
#tk.mainloop()
