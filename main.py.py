from PIL import Image
import os
import numpy as np
import pygame, sys
import queue

text_file = open("Output.txt", "w")


# this method calculates the average of the ints in an array
def avg(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    num = sum / len(a)

    return num


# this method creates an array consisiting of n numbers of a barcode
#
# by taking the projections arrays and thier averages to solve for the projection values
# add them together to get their barcode
def barcode_generator(c1, c2, c3, c4):
    # creating array that stores barcode
    barcode_size = len(c1) + len(c2) + len(c3) + len(c4)
    barcode = [0 for i in range(barcode_size)]

    code_generations = queue.Queue()

    # code generations for all projection
    code_generations.put(idv_code_gen(c1, avg(c1)))
    code_generations.put(idv_code_gen(c2, avg(c2)))
    code_generations.put(idv_code_gen(c3, avg(c3)))
    code_generations.put(idv_code_gen(c4, avg(c4)))

    index = 0
    # for the projection arrays, sum all of them to create the barcode array
    while (code_generations.empty() == False):
        arr = code_generations.get()
        for i in range(len(arr)):
            barcode[index] = arr[i]
        index += 1

    return barcode

# generates a code for an individual projection array
# 
# using the average of the projection angle array, the numbers in the array greater than the average
# will turn into one
def idv_code_gen(a, a_avg):
    code_arr = [0 for i in range(len(a))]
    for i in range(len(a)):
        if a[i] > a_avg:
            code_arr[i] = 1
    return code_arr

# this method initializes and gathers all pre-requisites for creating and barcode and returns the value of one
# 
# initializes projection arrays and retrieves their proper values, then creates a bar code
def barcode_main_function(a):
    size = 28  # the length of the images

    # initializing projection arrays
    p1 = [0 for i in range(size)]
    p2 = [0 for i in range(size + 1)]
    p3 = [0 for i in range(size)]
    p4 = [0 for i in range(size + 1)]

    # calculating the projections horizontally and vertically
    for i in range(size):
        for j in range(size):
            p1[i] += a[i][j]  # everything will be added from left to right
            p3[i] += a[j][i]  # everything will be added from up to down

    # calculating 45 degrees
    initial_i = (int)(size / 2)  # starting at the bottom left
    initial_j = 0
    index = 0
    sum = 0

    # find the sum of each diagonal moving down right until the condition is met
    while initial_j < (size / 2) + 1:
        if initial_i > 0:  # first half
            n = 0
            while (initial_i + n < size) and (initial_j + n < size):  # # down right
                sum += a[initial_i + n][initial_j + n]
                n = n + 1
            p2[index] = sum
            sum = 0
            index += 1
            initial_i = initial_i - 1
        else:  # second half
            n = 0
            while (initial_i + n < size) and (initial_j + n < size):  # # down right
                sum += a[initial_i + n][initial_j + n]
                n = n + 1
            p2[index] = sum
            sum = 0
            index += 1
            initial_j = initial_j + 1

    # calculating 135 degrees
    initial_i = 0
    initial_j = (int)(size / 2) - 1  # start at top left
    index = 0
    sum = 0

    # find the sum of each diagonal moving down left until the condition is met to create a projection array
    while initial_i < (size / 2) + 1:
        if initial_j < size - 1:  # iterate first half until initial_j reaches the size-1
            n = 0
            while (initial_i + n < size) and (initial_j - n >= 0):  # # down left
                sum += a[initial_i + n][initial_j - n]
                n = n + 1
            p4[index] = sum
            sum = 0
            index += 1
            initial_j = initial_j + 1
        else:  # iterate the rest until initial_i reaches size/2 + 1
            n = 0
            while (initial_i + n < size) and (initial_j - n >= 0):  # # down left
                sum += a[initial_i + n][initial_j - n]
                n = n + 1
            p4[index] = sum
            sum = 0
            index += 1
            initial_i = initial_i + 1

    #after all projection numbers are calculated create the barcode
    code = barcode_generator(p1,p2,p3,p4)

    return code

# This method iterates throughout a selected folder and turns all the images within into 2d numpy array with grayscale values
def get_images(folders, image_names, index, arr):
    for x in range(10):
        img = Image.open('MNIST_DS/' + folders[index] + '/' + image_names[x])
        arr[index*10 + x] = np.asarray(img)

# this method compares two barcode ids and sums up and returns thier differences
def hamming_distance(user_code, code):
    amt_ones = 0
    for i in range(len(user_code)):
        # add up amount of different binary numbers
        if user_code[i] != code[i]:
            amt_ones += 1
    return amt_ones

#To display the numpy array into a single line
np.set_printoptions(linewidth=np.inf)
img_arr = [0 for i in range(100)]


folders = os.listdir('MNIST_DS')

for i in range(10):
	image_names = os.listdir('MNIST_DS/' + folders[i])
	get_images(folders, image_names, i, img_arr)

# First instance of pygame to ask user for input
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([760,460])
pygame.display.set_caption('Data Structures Final')
base_font = pygame.font.Font(None, 50)
user_input = ''

while True:
    screen.fill((25.5, 41.2, 88.2))
    
    for event in pygame.event.get():

        directions = 'Enter the image name:'
        direction_surface = base_font.render(directions,True,(255,255,255))
        screen.blit(direction_surface, (200,150))
        text_surface = base_font.render(user_input,True,(255,255,255))
        screen.blit(text_surface,(285,210))

        pygame.display.flip()
        clock.tick(60)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[0:-1]
            else:
                user_input += event.unicode
        pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # to ask user to input an image
                size = len(user_input)
                new_input = user_input[:size - 1]
                user_img = Image.open(new_input + '.jpg')

                # Second instance of pygame to display the output to the user
                pygame.init()
                clock = pygame.time.Clock()
                display_surface = pygame.display.set_mode((760, 460))
                        
                pygame.display.set_caption('Data Structures Final')
                        
                image = pygame.image.load(new_input + '.jpg')
                image = pygame.transform.scale(image, (280, 280))
                display_surface.fill((25.5, 41.2, 88.2))
                display_surface.blit(image, (60, 80))

                user_image_name = str(new_input)
                text_surface = base_font.render(user_image_name,True,(255,255,255))
                screen.blit(text_surface,(120,40))


                while True:
                    
                    for event in pygame.event.get():


                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        user_arr_img = np.asarray(user_img)

                        user_barcode = barcode_main_function(user_arr_img)


                        #initializing hamming distance holder
                        smallest_hamming_distance = 28*4 + 2
                        index_of_closest_img = 0

                        #Main 
                        for t in range(len(img_arr)):
                            size = 28

                            barcode = barcode_main_function(img_arr[t])

                            barcode_num = 0

                            #if barcode@img_arr[t] clost to hamming sitance of barcode:
                                #closest num = t
                            if hamming_distance(user_barcode, barcode) < smallest_hamming_distance:
                                smallest_hamming_distance = hamming_distance(user_barcode, barcode)
                                index_of_closest_img = t


                        # finding the folder of the smallest hamming distance
                        output_folder_index = int(index_of_closest_img/10)
                        output_image_name_index = index_of_closest_img % 2
                        
                        retrieved_images = os.listdir('MNIST_DS/' + folders[output_folder_index])
                        new_image = pygame.image.load('MNIST_DS/' + folders[output_folder_index] + '/' + retrieved_images[output_image_name_index])
                        new_image = pygame.transform.scale(new_image, (280, 280))
                        display_surface.blit(new_image, (420, 80))

                        #displaying the images onto the GUI
                        loading = 'Image retrieved!'
                        text_surface = base_font.render(loading,True,(255,255,255))
                        screen.blit(text_surface,(220,400))

                        new_image_name = str(retrieved_images[output_image_name_index]).replace('.jpg','')
                        text_surface = base_font.render(new_image_name,True,(255,255,255))
                        screen.blit(text_surface,(460,40))

                    pygame.display.flip()
                    clock.tick(60)