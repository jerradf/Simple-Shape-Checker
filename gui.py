# Teacher: Jerrad Flores
# Student: Thomas Wang
# School: Coding Minds Academy; 2021

# The GUI of the program.
# We call methods to draw shapes (sample and user-drawn) onto the display.
# Using the buttons.

import turtle
import tkinter
from tkinter import font
import shape_checker
import time
import file


class GUI:
  def __init__(self):
    self.homepage = turtle.Screen()

    self.homepage.bgcolor("light yellow")
    self.homepage.title("Pixel Processor")
    self.font = tkinter.font.Font(family="Times New Roman", size = 7, weight="normal")
    self.canvas=self.homepage.getcanvas()

    self.image_name = "Choose Your Image"
    turtle.clear()

  
  def reset_screen(self):
    self.homepage.clear()
    self.homepage.bgcolor("light yellow")
    self.homepage.title("Pixel Processor")


  def initialize_upload_check_buttons(self):
    upload_button= tkinter.Button(self.canvas.master,height=1, width=10, bg="white", command= self.image_upload,text=("upload image"))

    upload_button["font"] = self.font
    self.canvas.create_window(-80,-80,window=upload_button)

    check_button= tkinter.Button(self.canvas.master,height=1, width=10, bg="white", command= self.checker, text="check image")

    check_button["font"]= self.font
    self.canvas.create_window(-80,-55,window=check_button)


  def initialize_drawing_board(self):
    # fill the corner of the right of the screen (if we can get it)
    '''
    turtle.fillcolor("white")
    for i in range(4):
      turtle.right(90)
      turtle.forward(50)
    turtle.end_fill()
    '''


  def image_upload(self):
    root = tkinter.Tk()
    root.title = "Choose your Image"
    while True:
      images = file.image_files()
      variable = tkinter.StringVar(root)
      variable.set("Choose your image")

      def option_changed(*args):
        if str(variable.get()) != "Choose your image":
          self.image_name = str(variable.get())
          root.destroy()
        tkinter.messagebox.showinfo(title=
        "Upload Image", message="Image Uploaded.")
        self.reset_screen()
        self.initialize_upload_check_buttons()


      w = tkinter.OptionMenu(root, variable, *images, command=option_changed)
      w.pack()

      root.mainloop()


  def checker(self):
    if self.image_name == "Choose Your Image":
      tkinter.messagebox.showwarning(title="Check Image", message="Please choose an image.")
      return 0 # (the return value does not mean anything, simply prevents program from quitting unexpectedly)

    shape1 = shape_checker.ShapeChecker(self.image_name)
    shape1.is_closing_shape() # adds the data for our Label
    
    if shape1.closed_shape == False:
      shape1.draw_shape()
      tkinter.messagebox.showerror(title="An error occured", message="The image is not closed.")

      def fill_shape(*args):
        shape1.complete_open_shape()
        time.sleep(5)
        tkinter.messagebox.showinfo(title="Closed!", message="Congrats! The shape is now closed.")

        turtle.clear()
        individual_info_button.destroy()

      individual_info_button = tkinter.Button(self.canvas.master, height=1, width=20, bg="green", command= fill_shape, text="Close the Open Shape!")
      individual_info_button["font"]= self.font
      self.canvas.create_window(50, 80, window=individual_info_button)
      turtle.hideturtle()
      
    else:
      text_label = tkinter.Label(self.canvas.master, text="Image Drawn Below", height=3, width=20, bg="white", borderwidth=2, relief="ridge")
      text_label["font"] = self.font
      self.canvas.create_window(50, -80, window=text_label)

      shape1.draw_shape()

      tkinter.messagebox.showinfo(title="Success", message="Drawing Complete. (See image before clicking \"OK\")")
      

      def show_info(*args):
        # reset executes only when the "Individual Pixel Information Window"
        # closes. This only occurs when we close the window.
        text_label.destroy()
        turtle.clear()
        individual_info_button.destroy()
        def reset(*args):
          self.image_name = "Choose Your Image"
          side_window.destroy()
          turtle.clear()

        side_window = tkinter.Tk()
        side_window.title("Individual Pixel Information")
        side_window.geometry("350x350")
        side_window.protocol("WM_DELETE_WINDOW", reset)

        t = tkinter.Label(side_window, text = [i for i in shape1.closing_shape_data])
        t.pack()

      individual_info_button = tkinter.Button(self.canvas.master, height=1, width=20, bg="green", command= show_info, text="Show additional Information!")
      individual_info_button["font"]= self.font
      self.canvas.create_window(50, 80, window=individual_info_button)


  def main(self):
    turtle.hideturtle()
    self.initialize_drawing_board()
    self.initialize_upload_check_buttons()