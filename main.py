from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as font
import os
from tkinter.scrolledtext import ScrolledText


root = Tk()

def compile(solution, brute, generator):
	g = "g++ " + str(generator) + " -o " + "gen"
	os.system(g)
	t = "g++ " + str(solution)+" -o "+"sol"
	os.system(t)
	u = "g++ " + str(brute) + " -o " + "brt"
	os.system(u)

def run():
	os.system("./gen >ip1.txt")
	os.system("./sol <ip1.txt >ot1.txt")
	os.system("./brt <ip1.txt >ot2.txt")

def give_verdict():
	file1 = open('ot1.txt')
	file2 = open('ot2.txt')
	output1 = file1.read()
	output2 = file2.read()
	store = []
	global f1
	global f2
	f1 = ""
	f2 = ""
	for i in output1:
		if(i == ' ' or i=="\n"):
			store.append(i)
		else:
			for j in store:
				f1 += j
			store.clear()
			f1 += i

	store.clear()

	for i in output2:
		if(i == ' ' or i=="\n"):
			store.append(i)
		else:
			for j in store:
				f2 += j
			store.clear()
			f2 += i

def lowerBar():
	btnCancel = Button(root, text = "Cancel", command = cancel)
	btnCancel.configure(height = 1, width = 10, padx = 2.5, pady = 5, bg = "#ffffff", bd = 1)
	btnCancel.place(relx = 0.85, rely = 0.90)

	btnNext = Button(root, text = "Next", command = next_)
	btnNext.configure(height = 1, width = 10, padx = 2.5, pady = 5, bg = "#ffffff", bd = 1)
	btnNext.place(relx = 0.725, rely = 0.90)

def openSolution():
	solution = filedialog.askopenfilename(filetypes = (("Cpp File", "*.cpp"),))
	global soltutionfile
	soltutionfile = solution

def openBrute():
	brute = filedialog.askopenfilename(filetypes = (("Cpp File", "*.cpp"),))
	global brutefile
	brutefile = brute

def openGen():
	Gen = filedialog.askopenfilename(filetypes = (("Cpp File", "*.cpp"),))
	global genfile
	genfile = Gen

def cancel():
	root.destroy()

def next_():
	child = root.winfo_children()
	for _ in child:
		_.destroy()

	show_result = ScrolledText(root,wrap="none", bd=1, bg="#CAFFE5", fg="black")
	show_result.pack(expand = 1, fill = BOTH)
	compile(soltutionfile, brutefile, genfile)
	tc = 1
	while True:
		run()
		give_verdict()
		cmp = (f1 == f2)
		re = ""
		if cmp==1:
			re="Correct Answer"
		else:
			re = "Wrong Answer!!!"
		show_result.insert(END,"#TestCase :" + str(tc)+" \n" + "output1 : " + f1+" \n" + "output2 : " + f2+"\nVerdict: "+re+ "\n\n")
		tc = tc + 1
		if(cmp == 0 or tc > 100):
			break

def chooseFile():


	buttonFont = font.Font(family='Helvetica', size=12, weight='bold')

	openBtnImage = PhotoImage(file = "images/open1.png")

	"""
	mytext = Text(root, height = 15, width = 30, borderwidth = 2, relief = SUNKEN, bg = "#e8e8e8")
	mytext.place(relx = 0.084, rely = 0.28)
	"""

	btn = Button(root, image = openBtnImage, borderwidth = 0, bg = "white", command = openSolution)
	btn.place(relx = 0.7, rely = 0.15)


	divider = ttk.Separator(root, orient = 'horizontal')
	divider.place(relx=0.15, rely= 0.27, relwidth=0.725, relheight=0.001)

	label = Label(root, text = "open correct solution to test (.cpp only)", font = buttonFont, bg = "#CAFFE5", fg = "grey")
	label.place(relx = 0.15, rely = 0.2)

	btn1 = Button(root, image = openBtnImage, borderwidth = 0, bg = "white", command = openBrute)
	btn1.image = openBtnImage
	btn1.place(relx = 0.7, rely = 0.4)

	label = Label(root, text = "open  bruteforce solution to check (.cpp only)", font = buttonFont, bg = "#CAFFE5", fg = "grey")
	label.place(relx = 0.15, rely = 0.45)

	divider1 = ttk.Separator(root, orient = 'horizontal')
	divider1.place(relx=0.15, rely=0.52, relwidth=0.725, relheight=0.001)


	btn2 = Button(root, image = openBtnImage, borderwidth = 0, bg = "white", command = openGen)
	btn2.image = openBtnImage
	btn2.place(relx = 0.7, rely = 0.65)

	divider2 = ttk.Separator(root, orient = 'horizontal')
	divider2.place(relx=0.15, rely=0.77, relwidth=0.725, relheight=0.001)

	label2 = Label(root, text = "open test case generator(.cpp only)", font = buttonFont, bg = "#CAFFE5", fg = "grey")
	label2.place(relx = 0.15, rely = 0.70)

	"""
	mytext1 = Text(root, height = 15, width = 30, borderwidth = 2, relief = SUNKEN, bg = "#e8e8e8")
	mytext1.place(relx = 0.584, rely = 0.28)
	"""

def main2():
	root.geometry("750x450")
	root.title("Stress Tester")
	root.resizable(0,0)

	# openImage = PhotoImage(file = "images/roorbg.png")
	label = Label(root, bg = '#CAFFE5', width = 120, height = 80)
	label.place(relx = 0, rely = 0)
	root.configure(bg = "#ffffff")

	lowerBar()
	chooseFile()
	root.mainloop()

main2()