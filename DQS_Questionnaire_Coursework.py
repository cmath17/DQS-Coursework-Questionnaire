# Written by : Calum Mather - Class Four(Questionnaire) and class system to put individual code together
#              Conor Jones - Class One(Home Page) and file store/retrieve
#              Athanasios Gkavalis - Class Three(Logic Test)
#              Dimitri Georgakis - Class Two(Practice Test)

from Tkinter import *
import Tkinter as tk
import tkMessageBox
#from PIL import ImageTk, Image
import tkFont

class One(Frame):
    def __init__(self, root):
        Frame.__init__(self,root)
        self.root = root
        top = tk.Toplevel(root)
        top.title("Cardiff University Logic Test Application")
        
        self.fent = StringVar()
        self.sent = StringVar()
        self.eent = StringVar()

################################## Tkinter labels ################################################
        self.filePath = "CardiffUniLogo.gif"
        self.img = PhotoImage(file=self.filePath)
        panel = tk.Label(top, image = self.img).grid(row=3, column=0)

        label1  = tk.Label(top,text="Welcome to Cardiff University's Interactive Logic Test & Questionnaire!\n",  fg = 'Red').grid(row=2, column=0, sticky=N)
        label20 = tk.Label(top,text=" ").grid(row=3, column=0,  sticky=W)
        label8  = tk.Label(top,text="\nThis application will provide you with a series of logic").grid(row=4, column=0, sticky=N)
        label9  = tk.Label(top,text="questions which will test your ability to problem solve and ").grid(row=5, column=0, sticky=N)
        label10 = tk.Label(top,text="provide immediate feedback on how you did.").grid(row=6, column=0, sticky=N)
        label11 = tk.Label(top,text="Don't worry- you will get a practice run before the official test to demonstrate the").grid(row=7, column=0, sticky=N)
        label12 = tk.Label(top,text="types of questions that you will be answering.").grid(row=8, column=0, sticky=N)
        label18 = tk.Label(top,text=" ").grid(row=9, column=0,  sticky=W)
        label13 = tk.Label(top,text="Following the logic test is a questionnaire. It's purpose is to").grid(row=10, column=0, sticky=N)
        label14 = tk.Label(top,text="suggest a Computer Science course at Cardiff University").grid(row=11, column=0, sticky=N)
        label15 = tk.Label(top,text="that will best suit you based on your answers.").grid(row=12, column=0, sticky=N)
        label19 = tk.Label(top,text=" ").grid(row=12, column=0,  sticky=W)
        label16 = tk.Label(top,text="Before we start, please can you enter your details below and").grid(row=13, column=0, sticky=N)
        label17 = tk.Label(top,text="click 'SUBMIT' to save your details to our database.").grid(row=14, column=0, sticky=N)
        label17 = tk.Label(top,text="After the details have successfully saved, you must click each button as they are ordered.").grid(row=16, column=0, sticky=N)
        label21 = tk.Label(top,text="\nFor help, select the 'Help' tab on the file bar at the top of this window.").grid(row=17, column=0, sticky=N)
        label19 = tk.Label(top,text=" ").grid(row=18, column=0,  sticky=W)
        label5  = tk.Label(top,text="Firstname: ").grid(row=19, column=0,  sticky=W)
        label6  = tk.Label(top,text="Surname: ").grid(row=20, column=0,  sticky=W)
        label7  = tk.Label(top,text="Email: ").grid(row=21, column=0,  sticky=W)

        ################################## Tkinter User input #############################################
    
        # CALUM, need to enter the command name as the function title here for practice, logic & Questionnaire
        adminButton = tk.Button(top,text="Admin Tools", command=self.Retrieve).grid(row=0, column=0, sticky=NE)
        AboutButton = tk.Button(top,text="About", command=self.About).grid(row=0, column=0, sticky=N)
        logHelpButton = tk.Button(top,text="Home Page Help", command=self.HomePageGuide).grid(row=0, column=0, sticky=NW) 
        SubmitButton = tk.Button(top,text="SUBMIT", command=self.inputtofile).grid(row=23, column=0, sticky=N) # submit button
        #nameOnlyButton = tk.Button(top,text="DON'T TAKE TEST/QUESTIONNAIRE", command = self.nameOnly).grid(row=24, column = 0, sticky = N)#No test button
        PracticeButton = tk.Button(top,text="1. Practice Test", command=self.openPrac).grid(row=25, column=0, sticky=W) # next button
        quitButton = tk.Button(top,text="QUIT - Admin Only", command=self.CloseApplication).grid(row=1, column=0, sticky=NE)
        LogicTestButton = tk.Button(top,text="2. Take Logic Test", command=self.openTest).grid(row=25, column=0, sticky=N) # next button
        QuestionnaireButton = tk.Button(top,text="3. Take Questionnaire", command=self.openQuest).grid(row=25, column=0, sticky=E) # next button



        fEnt = tk.Entry(top,textvariable=self.fent, width=40).grid(row=19, column=0, columnspan=2, sticky=N) # firstname
        sEnt = tk.Entry(top,textvariable=self.sent, width=40).grid(row=20, column=0, columnspan=2, sticky=N) # surname
        eEnt = tk.Entry(top,textvariable=self.eent, width=40).grid(row=21, column=0, columnspan=2, sticky=N) # email


        ################################## Tkinter Menu ####################################################

    def CloseApplication(self):
        root.destroy()

    def inputtofile(self):
        strMsg=""
        if (self.fent.get() == "") or ( self.eent.get() == "") or  (self.sent.get() == ""):
            strMsg = strMsg + "You need to fill all entries."

        my_file = open("Test.txt", "a")
        my_file.write("\n\n------- START STUDENT FILE -------")
        my_file.write("\nStudent firstname: " + self.fent.get() + "\n")
        my_file.write("Student surname: " + self.sent.get()  + "\n")
        my_file.write("Student email: " + self.eent.get()  + "\n")
        my_file.write("\n")
        tkMessageBox.showinfo(title="Details Submitted!", 
        message="Details have been saved.")
        self.clearResponse()
        return
    # need to sort this out
    def Retrieve(self):
    	confirm = tkMessageBox.askyesno("Confirm", "View student details?")
        if confirm is False:
        	return
        else:
        	from subprocess import call
        	call("notepad Test.txt")
    def About(self):
        tkMessageBox.showinfo("About the software", "This program was created as part of a year 1 COMSC assessment under the module 'Developing Quality Software'. The program was created by four team members who individually created each aspect of this software program which was assembled at the end of the implementation stage of the developing software project. \n \nThe software was created to be used at careers fayres to run alongside the computer science stall in order to test potential computer scientist's ability in problem solving and to harvest student's emails who can be contacted at a later date about studying at cardiff. \n\nTeam members:\nCalum Mather \nConor Jones \nDimitris Georgakis \nThanasis Gavalis")

    def HomePageGuide(self):
        tkMessageBox.showinfo("Home Page Help", "Here you are required to enter your details in the entry boxes below before proceeding to the next window so that we can keep track of each person's score which we will use to contact you in the near future about studying at Cardiff University. \n\nTo proceed:\n\n- Enter your name and email address below,\n- Click 'submit'.\n- Then follow the order of the buttons beneath (1-3).\n- As each button is pressed a new window will appear which will contain the contents of each heading the buttons indicate.")

    # def nameOnly(self):
    #     tkMessageBox.showinfo("No Test/Questionnaire", "Thank you for your time.")
    # 	my_file = open("Test.txt", "a")
    #     my_file.write("\n------- END STUDENT FILE TEST NOT TAKEN -------\n")
    #     my_file.close
    #     self.fent.set("")
    #     self.sent.set("")
    #     self.eent.set("")

    def clearResponse(self):
        
        self.fent.set("")
        self.sent.set("")
        self.eent.set("")    
        
     # create a function that will reset/reload/refresh the program
    def refresh(self):
       reload(root)
       root.destroy()
       root.Tk()
        
    def OnButton(self):
            clickNext = tkMessageBox.askyesno(title="Next...", 
                                           message="Would you like to proceed to the logic test? If not, your details have been saved and the application will reset.")
            if clickNext is True:
                self.openit()
                print "Here is where the new window needs to be opened ro re-direct the page" # redirect the user to new window
            else:
                command = refresh # doesnt work, sort out
    def openPrac(self):
        two = Two(self.root)

    def openTest(self):
        three = Three(self.root)

    def openQuest(self):
        four = Four(self.root)

class Two():
    def __init__(self, root):
        self.root = root
        top = tk.Toplevel(root)
        
        top.geometry("700x400")  
        titleStuff= tk.Label(top, bg = "grey88", height = "5", fg = 'RoyalBlue1',text = "Logic Question Number 1: A=5, B=3, C=15: Please Select the Result for [(A+C)/B(C-A)]B", width = "100")
        titleStuff.grid()

        i= Label(top, bg = "gray91", height = "5", fg = 'RoyalBlue1', text = "Please Select Your Answer:", width = "100")
        i.grid()


        top.title('Practice Questions-Logic Test')
                
            
        def Right(): 
            print "Right Answer!"
            tkMessageBox.showinfo(title="Correct", message="Correct answer")
                
        def Wrong():
            print "Wrong Answer"
                
            M=0 #user answer wrong so takes 0 marks
            tkMessageBox.showinfo(title="Wrong answer", message="Wrong answer!")
            NextQuestion()
        def NextQuestion():
            print"Next Question"
            print"Thanasis Gkavalis Practise Logic Test"
                
            M=1 #1 point the user takes, providing the right answer
        def PreviousQuestion():
            print"Previous Question"
                


        w = tk.Button(top,bg = "lavender blush",height = "5",width = "13", fg = 'RoyalBlue1', text ="200", command = Wrong)
        w.place(x = "150", y = "250")

        w = tk.Button(top,bg = "lavender blush",height = "5",width = "13",fg = 'RoyalBlue1', text ="15", command = Wrong)
        w.place(x = "250", y = "250")

        r = tk.Button(top, bg = "lavender blush",height = "5",width = "13",fg = 'RoyalBlue1', text ="2", command = Right)
        r.place(x = "350", y = "250")

        w = tk.Button(top,bg = "lavender blush", height = "5",width = "13",fg = 'RoyalBlue1',text ="25", command = Wrong)
        w.place(x = "450", y = "250")

        w = tk.Button(top,bg = "indian red", height = "5",width = "13",fg = 'white',text ="Close Test", command=lambda:top.destroy())
        w.place(x = "580", y = "300")
            
    
class Three(Frame):
    def __init__(self,master):
        # Initialise Questionnaire Class
        Frame.__init__(self,master)
        self.grid()

        #root = Tk()
        top = tk.Toplevel(root)
        dFont=tkFont.Font(family="bold", size=50)
        top.geometry("700x800")

        titleStuff= Label(top, bg = "grey88", height = "5", fg = 'RoyalBlue1',text = "[x] is one quarter of [y],[q] is twice [x] and [p] is one third of [q].", width = "100")
        titleStuff.grid()

        i= Label(top, bg = "grey91", height = "5", fg = 'RoyalBlue1', text = "Please Select Your Answer:", width = "100")
        i.grid()


        top.title(' Questions-Logic Test')
        def quit():
            
            lambda:top.destroy()
        def quit2():
            tkMessageBox.showinfo(title="Correct", message="YOU ANSWERED BOTH QUESTIONS WRONG!YOU FAILED IN THE EXAMS")
            
            lambda:top.destroy()
        def quit3():
            tkMessageBox.showinfo(title="Correct", message="YOU ANSWERED ONE QUESTION WRONG!YOU FAILED IN THE EXAMS")
            
            lambda:top.destroy()
        def quit4():
            tkMessageBox.showinfo(title="Correct", message="YOU ANSWERED ALL QUESTIONS RIGHT! YOU PASSED THE EXAMS")
            
            lambda:top.destroy()
            
        def resultButtonRight2():
            w = Button(top,bg = "RoyalBlue1", height = "5",width = "13",fg = 'white',text ="Results", command =congratulations2 )
            w.place(x = "25", y = "700")
            top.mainloop()
        def resultButtonRight():
            w = Button(top,bg = "RoyalBlue1", height = "5",width = "13",fg = 'white',text ="Results", command =congratulations )
            w.place(x = "25", y = "700")
            top.mainloop()
        def resultButtonWrong2():
             w = Button(top,bg = "RoyalBlue1", height = "5",width = "13",fg = 'white',text ="Results", command =sorry2 )
             w.place(x = "25", y = "700")
        def resultButtonWrong():
             w = Button(top,bg = "RoyalBlue1", height = "5",width = "13",fg = 'white',text ="Results", command =sorry1 )
             w.place(x = "25", y = "700")
            
        def congratulations2():

            top = Tk()  
            top.geometry("700x400")    

            
            w = Button(top,bg = "indian red", height = "12",width = "70",fg = 'white',text ="Look Your Answer Here", command = quit4)
            w.place(x = "120", y = "85")
            w = Button(top,bg = "RoyalBlue1", height = "5",width = "70",fg = 'white',text ="Close Window", command = lambda:top.destroy())
            w.place(x = "120", y = "250")

        def sorry1():

            top = Tk()  
            top.geometry("700x400")    
            
            w = Button(top,bg = "indian red", height = "12",width = "70",fg = 'white',text ="LOOK AND SEE YOUR RESULTS HERE", command = quit3)
            w.place(x = "120", y = "85")
            w = Button(top,bg = "RoyalBlue1", height = "5",width = "70",fg = 'white',text ="Close Window", command = lambda:top.destroy())
            w.place(x = "120", y = "250")
        def sorry2():

            top = Tk()  
            top.geometry("700x400")    


            titleStuff.grid()
            w = Button(top,bg = "indian red", height = "12",width = "70",fg = 'white',text ="Look Your Answer Here", command = quit2)
            w.place(x = "120", y = "85")
            w = Button(top,bg = "RoyalBlue1", height = "5",width = "70",fg = 'white',text ="Close Window", command = lambda:top.destroy())
            w.place(x = "120", y = "250")
            

        def question1RIGHT():
            print"d"
            titleStuff= Label(top, bg = "grey88", height = "5", fg = 'RoyalBlue1',text = "[a+b]=8. [c]=[a]+3. [d]=[b]+[e]. [e]=-[c]. Please find [d]", width = "100")
            titleStuff.grid()
            titleStuff.place(x="0",y="400")

            i= Label(top, bg = "grey91", height = "5", fg = 'RoyalBlue1', text = "Please Select Your Answer:", width = "100")
            i.grid()
            i.place(x="0",y="480")

            w = Button(top,bg = "lavender blush",height = "5",width = "13", fg = 'RoyalBlue1', text =" A:11", command = resultButtonRight2)
            w.place(x = "150", y = "600")

            w = Button(top,bg = "lavender blush",height = "5",width = "13",fg = 'RoyalBlue1', text =" B:4", command = resultButtonWrong)
            w.place(x = "250", y = "600")

            r = Button(top, bg = "lavender blush",height = "5",width = "13",fg = 'RoyalBlue1', text =" C:12", command =resultButtonWrong)
            r.place(x = "350", y = "600")
             
            w = Button(top,bg = "lavender blush", height = "5",width = "13",fg = 'RoyalBlue1',text ="D: [b]", command = resultButtonWrong)
            w.place(x = "450", y = "600")

            


            top.mainloop()
        def questionWrong():
            
            print"d"
            titleStuff= Label(top, bg = "grey88", height = "5", fg = 'RoyalBlue1',text = "[a+b]=8. [c]=[a]+3. [d]=[b]+[e]. [e]=-[c]. Please find [d]", width = "100")
            titleStuff.grid()
            titleStuff.place(x="0",y="400")

            i= Label(top, bg = "grey91", height = "5", fg = 'RoyalBlue1', text = "Please Select Your Answer:", width = "100")
            i.grid()
            i.place(x="0",y="480")

            w = Button(top,bg = "lavender blush",height = "5",width = "13", fg = 'RoyalBlue1', text =" A:11", command = resultButtonWrong)
            w.place(x = "150", y = "600")

            w = Button(top,bg = "lavender blush",height = "5",width = "13",fg = 'RoyalBlue1', text =" B:4", command = resultButtonWrong2)
            w.place(x = "250", y = "600")

            r = Button(top, bg = "lavender blush",height = "5",width = "13",fg = 'RoyalBlue1', text =" C:12", command =resultButtonWrong2)
            r.place(x = "350", y = "600")
             
            w = Button(top,bg = "lavender blush", height = "5",width = "13",fg = 'RoyalBlue1',text ="D: [b]", command = resultButtonWrong2)
            w.place(x = "450", y = "600")

           
            

            
            
        def question1():
            print "Test Begin"
            
        w = Button(top,bg = "lavender blush",height = "5",width = "13", fg = 'RoyalBlue1', text ="A: 3[p]=2[y]", command = questionWrong)
        w.place(x = "150", y = "250")

        w = Button(top,bg = "lavender blush",height = "5",width = "13",fg = 'RoyalBlue1', text ="B: 5[y]=[p]", command = questionWrong)
        w.place(x = "250", y = "250")

        r = Button(top, bg = "lavender blush",height = "5",width = "13",fg = 'RoyalBlue1', text ="C: [y]=2[p]", command = question1RIGHT)
        r.place(x = "350", y = "250")

        w = Button(top,bg = "lavender blush", height = "5",width = "13",fg = 'RoyalBlue1',text ="D: 6[p]=[y]", command = questionWrong)
        w.place(x = "450", y = "250")

        w = Button(top,bg = "indian red", height = "5",width = "19",fg = 'white',text ="EXIT", command = lambda:top.destroy())
        w.place(x = "500", y = "700")
        top.mainloop()
        


class Four():
    def __init__(self, root):
        self.root = root
        top = tk.Toplevel(root)
        top.title("Questionnaire")

        #Create widgets to ask team experience questions

        lblStrAgr = tk.Label(top, text = "Strongly \n Agree", font = ("MS", 8, "bold"))
        lblStrAgr.grid(row = 3, column = 4, rowspan = 2)

        lblParAgr = tk.Label(top, text = "Partly \n Agree", font = ("MS", 8, "bold"))
        lblParAgr.grid(row = 3, column = 5, rowspan = 2)

        lblNeu = tk.Label(top, text = "No \n Opinion", font = ("MS", 8, "bold"))
        lblNeu.grid(row = 3, column = 6, rowspan = 2)

        lblParDis = tk.Label(top, text = "Partly \n Disagree", font = ("MS", 8, "bold"))
        lblParDis.grid(row = 3, column = 7, rowspan = 2)

        lblStrDis = tk.Label(top, text = "Strongly \n Disagree", font = ("MS", 8, "bold"))
        lblStrDis.grid(row = 3, column = 8, rowspan = 2)

        lblQT = tk.Label(top, text = "Course Questionnaire:", font = ("MS", 8, "bold"))
        lblQT.grid(row = 4, column = 0, columnspan = 2, sticky = W)

        #Question One

        lblQ1 = tk.Label(top, text = "1. I enjoy mathematics.", font = ("MS", 8, "bold"))
        lblQ1.grid(row = 5, column = 0, columnspan = 4, sticky = W)

        #Question Two

        lblQ2 = tk.Label(top, text = "2. I have an interest in business.", font = ("MS", 8, "bold"))
        lblQ2.grid(row = 6, column = 0, columnspan = 4, sticky = W)

        #Question Three

        lblQ3 = tk.Label(top, text = "3. I have experience with coding.", font = ("MS", 8, "bold"))
        lblQ3.grid(row = 7, column = 0, columnspan = 4, sticky = W)

        #Question Four

        lblQ4 = tk.Label(top, text = "4. I have an interest with computer security.", font = ("MS", 8, "bold"))
        lblQ4.grid(row = 8, column = 0, columnspan = 4, sticky = W)

        #Question Five

        lblQ5 = tk.Label(top, text = "5. I have an interest in graphics and design.", font = ("MS", 8, "bold"))
        lblQ5.grid(row = 9, column = 0, columnspan = 4, sticky = W)

        #Question Six

        lblQ6 = tk.Label(top, text = "6. I have an interest in learning whilst working in industry.", font = ("MS", 8, "bold"))
        lblQ6.grid(row = 10, column = 0, columnspan = 4, sticky = W)

        #Question Seven

        lblQ7 = tk.Label(top, text = "7. I would like to focus on developing software.", font = ("MS", 8, "bold"))
        lblQ7.grid(row = 11, column = 0, columnspan = 4, sticky = W)

        #Question Eight

        lblQ8 = tk.Label(top, text = "8. I would like to study a different subject, but still do some computing.", font = ("MS", 8, "bold"))
        lblQ8.grid(row = 12, column = 0, columnspan = 4, sticky = W)

        #Question Nine

        lblQ9 = tk.Label(top, text = "9. I have an interest in creating video games.", font = ("MS", 8, "bold"))
        lblQ9.grid(row = 13, column = 0, columnspan = 4, sticky = W)

        #Question Ten

        lblQ10 = tk.Label(top, text = "10. I would like to keep my options as open as possible.", font = ("MS", 8, "bold"))
        lblQ10.grid(row = 14, column = 0, columnspan = 4, sticky = W)

        self.varQ1 = IntVar()
        self.varQ2 = IntVar()
        self.varQ3 = IntVar()
        self.varQ4 = IntVar()
        self.varQ5 = IntVar()
        self.varQ6 = IntVar()
        self.varQ7 = IntVar()
        self.varQ8 = IntVar()
        self.varQ9 = IntVar()
        self.varQ10 = IntVar()


        #Q1 Radios

        R1Q1 = tk.Radiobutton(top, variable = self.varQ1, value = 5)
        R1Q1.grid(row = 5, column = 4)

        R2Q1 = tk.Radiobutton(top, variable = self.varQ1, value = 4)
        R2Q1.grid(row = 5, column = 5)

        R3Q1 = tk.Radiobutton(top, variable = self.varQ1, value = 3)
        R3Q1.grid(row = 5, column = 6)

        R4Q1 = tk.Radiobutton(top, variable = self.varQ1, value = 2)
        R4Q1.grid(row = 5, column = 7)      

        R5Q1 = tk.Radiobutton(top, variable = self.varQ1, value = 1)
        R5Q1.grid(row = 5, column = 8)

        #Q2 Radios

        R1Q2 = tk.Radiobutton(top, variable = self.varQ2, value = 5)
        R1Q2.grid(row = 6, column = 4)

        R2Q2 = tk.Radiobutton(top, variable = self.varQ2, value = 4)
        R2Q2.grid(row = 6, column = 5)

        R3Q2 = tk.Radiobutton(top, variable = self.varQ2, value = 3)
        R3Q2.grid(row = 6, column = 6)

        R4Q2 = tk.Radiobutton(top, variable = self.varQ2, value = 2)
        R4Q2.grid(row = 6, column = 7)

        R5Q1 = tk.Radiobutton(top, variable = self.varQ2, value = 1)
        R5Q1.grid(row = 6, column = 8)

        #Q3 Radios

        R1Q3 = tk.Radiobutton(top, variable = self.varQ3, value = 5)
        R1Q3.grid(row = 7, column = 4)

        R2Q3 = tk.Radiobutton(top, variable = self.varQ3, value = 4)
        R2Q3.grid(row = 7, column = 5)

        R3Q3 = tk.Radiobutton(top, variable = self.varQ3, value = 3)
        R3Q3.grid(row = 7, column = 6)

        R4Q3 = tk.Radiobutton(top, variable = self.varQ3, value = 2)
        R4Q3.grid(row = 7, column = 7)

        R5Q3 = tk.Radiobutton(top, variable = self.varQ3, value = 1)
        R5Q3.grid(row = 7, column = 8)

                #Q4 Radios

        R1Q4 = tk.Radiobutton(top, variable = self.varQ4, value = 5)
        R1Q4.grid(row = 8, column = 4)

        R2Q4 = tk.Radiobutton(top, variable = self.varQ4, value = 4)
        R2Q4.grid(row = 8, column = 5)

        R3Q4 = tk.Radiobutton(top, variable = self.varQ4, value = 3)
        R3Q4.grid(row = 8, column = 6)

        R4Q4 = tk.Radiobutton(top, variable = self.varQ4, value = 2)
        R4Q4.grid(row = 8, column = 7)

        R5Q4 = tk.Radiobutton(top, variable = self.varQ4, value = 1)
        R5Q4.grid(row = 8, column = 8)

                #Q5 Radios

        R1Q5 = tk.Radiobutton(top, variable = self.varQ5, value = 5)
        R1Q5.grid(row = 9, column = 4)

        R2Q5 = tk.Radiobutton(top, variable = self.varQ5, value = 4)
        R2Q5.grid(row = 9, column = 5)

        R3Q5 = tk.Radiobutton(top, variable = self.varQ5, value = 3)
        R3Q5.grid(row = 9, column = 6)

        R4Q5 = tk.Radiobutton(top, variable = self.varQ5, value = 2)
        R4Q5.grid(row = 9, column = 7)

        R5Q5 = tk.Radiobutton(top, variable = self.varQ5, value = 1)
        R5Q5.grid(row = 9, column = 8)

                #Q6 Radios

        R1Q6 = tk.Radiobutton(top, variable = self.varQ6, value = 5)
        R1Q6.grid(row = 10, column = 4)

        R2Q6 = tk.Radiobutton(top, variable = self.varQ6, value = 4)
        R2Q6.grid(row = 10, column = 5)

        R3Q6 = tk.Radiobutton(top, variable = self.varQ6, value = 3)
        R3Q6.grid(row = 10, column = 6)

        R4Q6 = tk.Radiobutton(top, variable = self.varQ6, value = 2)
        R4Q6.grid(row = 10, column = 7)

        R5Q6 = tk.Radiobutton(top, variable = self.varQ6, value = 1)
        R5Q6.grid(row = 10, column = 8)


                #Q7 Radios

        R1Q7 = tk.Radiobutton(top, variable = self.varQ7, value = 5)
        R1Q7.grid(row = 11, column = 4)

        R2Q7 = tk.Radiobutton(top, variable = self.varQ7, value = 4)
        R2Q7.grid(row = 11, column = 5)

        R3Q7 = tk.Radiobutton(top, variable = self.varQ7, value = 3)
        R3Q7.grid(row = 11, column = 6)

        R4Q7 = tk.Radiobutton(top, variable = self.varQ7, value = 2)
        R4Q7.grid(row = 11, column = 7)

        R5Q7 = tk.Radiobutton(top, variable = self.varQ7, value = 1)
        R5Q7.grid(row = 11, column = 8)

                #Q8 Radios

        R1Q8 = tk.Radiobutton(top, variable = self.varQ8, value = 5)
        R1Q8.grid(row = 12, column = 4)

        R2Q8 = tk.Radiobutton(top, variable = self.varQ8, value = 4)
        R2Q8.grid(row = 12, column = 5)

        R3Q8 = tk.Radiobutton(top, variable = self.varQ8, value = 3)
        R3Q8.grid(row = 12, column = 6)

        R4Q8 = tk.Radiobutton(top, variable = self.varQ8, value = 2)
        R4Q8.grid(row = 12, column = 7)

        R5Q8 = tk.Radiobutton(top, variable = self.varQ8, value = 1)
        R5Q8.grid(row = 12, column = 8)

                #Q9 Radios

        R1Q9 = tk.Radiobutton(top, variable = self.varQ9, value = 5)
        R1Q9.grid(row = 13, column = 4)

        R2Q9 = tk.Radiobutton(top, variable = self.varQ9, value = 4)
        R2Q9.grid(row = 13, column = 5)

        R3Q9 = tk.Radiobutton(top, variable = self.varQ9, value = 3)
        R3Q9.grid(row = 13, column = 6)

        R4Q9 = tk.Radiobutton(top, variable = self.varQ9, value = 2)
        R4Q9.grid(row = 13, column = 7)

        R5Q9 = tk.Radiobutton(top, variable = self.varQ9, value = 1)
        R5Q9.grid(row = 13, column = 8)

                #Q10 Radios

        R1Q10 = Radiobutton(top, variable = self.varQ10, value = 5)
        R1Q10.grid(row = 14, column = 4)

        R2Q10 = Radiobutton(top, variable = self.varQ10, value = 4)
        R2Q10.grid(row = 14, column = 5)

        R3Q10 = Radiobutton(top, variable = self.varQ10, value = 3)
        R3Q10.grid(row = 14, column = 6)

        R4Q10 = Radiobutton(top, variable = self.varQ10, value = 2)
        R4Q10.grid(row = 14, column = 7)

        R5Q10 = Radiobutton(top, variable = self.varQ10, value = 1)
        R5Q10.grid(row = 14, column = 8)

        ####Buttons#####

        butSubmit = Button(top, text='Submit',font=('MS', 8,'bold'), command=self.storeResponse)
        butSubmit.grid(row=16, column=2, columnspan=2, sticky=W)

        butClear = Button(top, text='Clear',font=('MS', 8,'bold'), command=self.clearResponse)
        butClear.grid(row=16, column=4, columnspan=1, sticky=S)

        butQuit = Button(top, text='Close Questionnaire',font=('MS', 8,'bold'),command=lambda:top.destroy())
        butQuit.grid(row=1, column=8, columnspan=1, sticky=E)

        butHelp = Button(top,text='Questionnaire Help',font=('MS', 8,'bold'), command=self.questHelp)
        butHelp.grid(row=1, column=0, columnspan=1, sticky=W)


    def questHelp(self):
        tkMessageBox.showinfo("Questionnaire Help","Here you need to select the response that you believe is most appropriate for yourself for each question.\nThe program will then tell give you a score for each course. \nThe course(s) with the highest score is recommended for you.\n\nTo Proceed:\n\n -Select each answer as applicable.\n -Click 'Submit'.\n -Your results will be displayed.\n -Click 'Return to home.'")

    def clearResponse(top):
        
        top.varQ1.set(0)
        top.varQ2.set(0)
        top.varQ3.set(0)
        top.varQ4.set(0)
        top.varQ5.set(0)
        top.varQ6.set(0)
        top.varQ7.set(0)
        top.varQ8.set(0)
        top.varQ9.set(0)
        top.varQ10.set(0)

    def storeResponse(top):

        comSci = 0
        comVisCom = 0
        comSecFor = 0
        comHiPerf = 0
        comSysEng = 0
        softEng = 0
        mathCom = 0
        bis = 0 


        strMsg=""

        if (top.varQ1.get()== 0) or (top.varQ2.get() == 0) or (top.varQ3.get() == 0) or (top.varQ4.get() == 0) or (top.varQ5.get() == 0) or (top.varQ6.get() == 0) or (top.varQ7.get() == 0) or (top.varQ8.get() == 0) or (top.varQ9.get() == 0) or (top.varQ10.get() == 0):
            strMsg = strMsg + "You need to answer all Questions"

        

        comSci = comSci + top.varQ3.get() + top.varQ6.get() + top.varQ9.get() + top.varQ10.get()
        comVisCom = comVisCom + top.varQ5.get() + top.varQ6.get() + top.varQ9.get()
        comSecFor = comSecFor + top.varQ4.get() + top.varQ6.get()
        comHiPerf = comHiPerf + top.varQ3.get() + top.varQ6.get() + top.varQ9.get()
        comSysEng = comSysEng + top.varQ3.get() + top.varQ7.get() + top.varQ9.get()
        softEng = softEng + top.varQ3.get() + top.varQ6.get() + top.varQ7.get() + top.varQ9.get()
        mathCom = mathCom + top.varQ1.get() + top.varQ6.get() + top.varQ8.get() + top.varQ10.get()
        bis = bis + top.varQ2.get() + top.varQ6.get() + top.varQ8.get() + top.varQ10.get()

        
        

        if strMsg == "":

            tkMessageBox.showinfo("Questionnaire", "Questionnaire Submitted")
            tkMessageBox.showinfo("Results", " Your Course Scores Are: " + "\n Computer Science: " + str(comSci) + "\n Computer Science with Visual Computing: " + str(comVisCom) + "\n Computer Science with Security and Forensics: " + str(comSecFor) + "\n Computer Science with High Performance Computing: " + str(comHiPerf) + "\n Computer Systems Engineering: " + str(comSysEng) + "\n Software Engineering: " + str(softEng) + "\n Maths and Computing: " + str(mathCom) + "\n Business Information Systems: " + str(bis))
            file=open("Test.txt", "a")
            file.write("\n Student's Course Scores: " + "\n Computer Science: " + str(comSci) + "\n Computer Science with Visual Computing: " + str(comVisCom) + "\n Computer Science with Security and Forensics: " + str(comSecFor) + "\n Computer Science with High Performance Computing: " + str(comHiPerf) + "\n Computer Systems Engineering: " + str(comSysEng) + "\n Software Engineering: " + str(softEng) + "\n Maths and Computing: " + str(mathCom) + "\n Business Information Systems: " + str(bis))
            file.write("\n------- END STUDENT FILE -------")
            file.close()
            top.clearResponse()
        
        else:  
            tkMessageBox.showwarning("Entry Error", strMsg)

root = tk.Tk()
one=One(root)
root.withdraw()
root.mainloop()

