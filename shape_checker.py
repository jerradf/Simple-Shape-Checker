# Teacher: Jerrad Flores
# Student: Thomas Wang
# School: Coding Minds Academy; 2021

from PIL import Image
import turtle
import time


class ShapeChecker:
  # We can initialize our ShapeChecker to have specific attributes that we don't need to do in a program
  def __init__(self, image_name: str):
    # We want a Image attribute in our class to store the name of the image, along with the actual Image
    self.closing_shape_data = []
    self.image_name = image_name
    self.image = Image.open(image_name)
    # For our ShapeChecker, we want a list to store all the coordinates of every single pixel
    self.pixels = self.image.load()
    # For our ShapeChecker, we want a list to store all the coordinates that contain the shape ONLY (starts empty)
    self.shape_pixels = []
    # For our ShapeChecker, we need a width and a height
    self.width, self.height = self.image.size #(width, height)
    # We want an attribute to determine if the shape on the image is closed or not
    self.closed_shape = bool #this will be updated later based on the image (this doesn't matter right now)


  def pixels_that_make_up_shape(self):
    for x in range(self.width):
      for y in range(self.height):
        if (self.pixels[x,y] != (0,0,0,0)) and ((x,y) not in self.shape_pixels):
          self.shape_pixels.append((x,y))
    # Why don't we need to return anything?
    # Because we are simply updating our class attributes, MUCH simpler!


  def pixels_that_make_up_shape(self):
    for x in range(self.width):
      for y in range(self.height):
        if (self.pixels[x,y] == (0,0,0,255)) and ((x,y) not in self.shape_pixels):
          self.shape_pixels.append((x,y))
    # Why don't we need to return anything?
    # Because we are simply updating our class attributes, MUCH simpler!


  def is_closing_shape(self):
    # Rather than having to call this function in the program, I can simply do it here.
    # Makes the program much simpler!
    self.pixels_that_make_up_shape()
    self.closing_shape_data = []
    
    for i, j in enumerate(self.shape_pixels):
      count = 0
      # pixel to the left
      if(((self.shape_pixels[i][0])-1, self.shape_pixels[i][1]) in self.shape_pixels):
        count += 1

      # pixel to the right
      if(((self.shape_pixels[i][0])+1, self.shape_pixels[i][1]) in self.shape_pixels):
        count += 1

      # pixel up
      if((self.shape_pixels[i][0], (self.shape_pixels[i][1])+1) in self.shape_pixels):
        count += 1

      # pixel down
      if((self.shape_pixels[i][0], (self.shape_pixels[i][1])-1) in self.shape_pixels):
        count += 1
      
      # pixel up-left
      if(((self.shape_pixels[i][0])-1, (self.shape_pixels[i][1])+1) in self.shape_pixels):
        count += 1

      # pixel up-right
      if(((self.shape_pixels[i][0])+1, (self.shape_pixels[i][1])+1) in self.shape_pixels):
        count += 1
      
      # pixel down-left
      if(((self.shape_pixels[i][0])-1, (self.shape_pixels[i][1])-1) in self.shape_pixels):
        count += 1

      # pixel down-right
      if(((self.shape_pixels[i][0])+1, (self.shape_pixels[i][1])-1) in self.shape_pixels):
        count += 1

      # If the count is < 2 (i.e. there is not enough adjacent pixels, this image is NOT closed).
      else:
        if(count < 2):
          self.closing_shape_data.append(f'{self.shape_pixels[i]} 2 Pixels Adjacent? NO. # of pixels adjacent: {count}\n')
          self.closed_shape = False
          self.closing_shape_data.append(f'{self.image_name} is NOT a closed shape.\n')
          # We are only returning so that the function can end (we don't want to check anything else)
          # Notice how I don't return anything?
          # This is because the value that is returned does NOT matter! (We don't use it anywhere)
          return 0

        self.closing_shape_data.append(f'{self.shape_pixels[i]} 2 Pixels Adjacent? YES\n')
    
    # We have checked all the pixels without returning False
    # Therefore, we can update our self.closed_shape to be True
    # REMEMBER: We don't need to return anything, because the function ends right here anyway!
    self.closed_shape = True
    self.closing_shape_data.append(f'{self.image_name} is a closed shape.\n\n')

  
  def draw_shape(self):
    turtle.clear()
    self.is_closing_shape()
    if 0 == 0:#self.closed_shape == True:
      list_of_pixels_already_drawn = []
      coordinate = self.shape_pixels[0] #coordinate = (x, y); coordinate[0] = x; coordinate[1] = y
      
      turtle.penup()
      turtle.goto((coordinate[0], coordinate[1]))
      turtle.pendown()
      # 1.) Check if the adjacent pixel FROM OUR COORDINATE is in our shape_pixels (in)
      # 2.) Check if the adjacent pixel FROM OUR COORDINATE has already been drawn (not in our list_of_pixels_already_drawn) (not in)
      # 3.) If Step 1 and Step 2 Qualifications are met, Step 3 consists of three parts:
      #         3.1): Move the turtle to that adjacent pixel
      #         3.2): (To make sure that we never go to this pixel again) we append this pixel to our list_of_pixels_already_drawn
      #         3.3): Update coordinate to be the adjacent pixel
      for i, j in enumerate(self.shape_pixels):
        # pixel to the left
        if((((coordinate[0])-1, coordinate[1]) in self.shape_pixels) and (((coordinate[0])-1, coordinate[1]) not in list_of_pixels_already_drawn)):
          turtle.goto(((coordinate[0])-1, coordinate[1]))
          list_of_pixels_already_drawn.append(((coordinate[0])-1, coordinate[1]))
          coordinate = ((coordinate[0])-1, coordinate[1])

        # pixel to the right
        elif((((coordinate[0])+1, coordinate[1]) in self.shape_pixels) and (((coordinate[0])+1, coordinate[1]) not in list_of_pixels_already_drawn)):
          turtle.goto(((coordinate[0])+1, coordinate[1]))
          list_of_pixels_already_drawn.append(((coordinate[0])+1, coordinate[1]))
          coordinate = ((coordinate[0])+1, coordinate[1])

        # pixel up
        elif(((coordinate[0], (coordinate[1])+1) in self.shape_pixels) and ((coordinate[0], (coordinate[1])+1) not in list_of_pixels_already_drawn)):
          turtle.goto((coordinate[0], (coordinate[1])+1))
          list_of_pixels_already_drawn.append((coordinate[0], (coordinate[1])+1))
          coordinate = (coordinate[0], (coordinate[1])+1)


        # pixel down
        elif(((coordinate[0], (coordinate[1])-1) in self.shape_pixels) and ((coordinate[0], (coordinate[1])-1) not in list_of_pixels_already_drawn)):
          turtle.goto((coordinate[0], (coordinate[1])-1))
          list_of_pixels_already_drawn.append((coordinate[0], (coordinate[1])-1))
          coordinate = (coordinate[0], (coordinate[1])-1)
        
        # pixel up-left
        elif((((coordinate[0])-1, (coordinate[1])+1) in self.shape_pixels) and (((coordinate[0])-1, (coordinate[1])+1) not in list_of_pixels_already_drawn)):
          turtle.goto(((coordinate[0])-1, (coordinate[1])+1))
          list_of_pixels_already_drawn.append(((coordinate[0])-1, (coordinate[1])+1))
          coordinate = ((coordinate[0])-1, (coordinate[1])+1)

        # pixel up-right
        elif((((coordinate[0])+1, (coordinate[1])+1) in self.shape_pixels) and (((coordinate[0])+1, (coordinate[1])+1) not in list_of_pixels_already_drawn)):
          turtle.goto(((coordinate[0])+1, (coordinate[1])+1))
          list_of_pixels_already_drawn.append(((coordinate[0])+1, (coordinate[1])+1))
          coordinate = ((coordinate[0])+1, (coordinate[1])+1)
        
        # pixel down-left
        elif((((coordinate[0])-1, (coordinate[1])-1) in self.shape_pixels) and (((coordinate[0])-1, (coordinate[1])-1) not in list_of_pixels_already_drawn)):
          turtle.goto(((coordinate[0])-1, (coordinate[1])-1))
          list_of_pixels_already_drawn.append(((coordinate[0])-1, (coordinate[1])-1))
          coordinate = ((coordinate[0])-1, (coordinate[1])-1)

        # pixel down-right
        elif((((coordinate[0])+1, (coordinate[1])-1) in self.shape_pixels) and (((coordinate[0])+1, (coordinate[1])-1) not in list_of_pixels_already_drawn)):
          turtle.goto(((coordinate[0])+1, (coordinate[1])-1))
          list_of_pixels_already_drawn.append(((coordinate[0])+1, (coordinate[1])-1))
          coordinate = ((coordinate[0])+1, (coordinate[1])-1)


  def complete_open_shape(self):
    open_pixels = []
    for i, j in enumerate(self.shape_pixels):
      count = 0
      # pixel to the left
      if(((self.shape_pixels[i][0])-1, self.shape_pixels[i][1]) in self.shape_pixels):
        count += 1
      # pixel to the right
      if(((self.shape_pixels[i][0])+1, self.shape_pixels[i][1]) in self.shape_pixels):
        count += 1
      # pixel up
      if((self.shape_pixels[i][0], (self.shape_pixels[i][1])+1) in self.shape_pixels):
        count += 1
      # pixel down
      if((self.shape_pixels[i][0], (self.shape_pixels[i][1])-1) in self.shape_pixels):
        count += 1
      # pixel up-left
      if(((self.shape_pixels[i][0])-1, (self.shape_pixels[i][1])+1) in self.shape_pixels):
        count += 1
      # pixel up-right
      if(((self.shape_pixels[i][0])+1, (self.shape_pixels[i][1])+1) in self.shape_pixels):
        count += 1
      # pixel down-left
      if(((self.shape_pixels[i][0])-1, (self.shape_pixels[i][1])-1) in self.shape_pixels):
        count += 1
      # pixel down-right
      if(((self.shape_pixels[i][0])+1, (self.shape_pixels[i][1])-1) in self.shape_pixels):
        count += 1
      # If the count is < 2 (i.e. there is not enough adjacent pixels, this image is NOT closed).
      else:
        if (count < 2):
          turtle.goto(self.shape_pixels[i])
          open_pixels.append(self.shape_pixels[i])
    
    turtle.penup()
    turtle.goto(self.shape_pixels[0])
    turtle.pendown()
    turtle.goto(open_pixels[-1])
    turtle.hideturtle()