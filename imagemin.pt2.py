from PIL import Image, ImageFilter
import os

size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir('.'):
    if f.endswith(' .jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn, fext))

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))


while True:
    user_choice = input("Which image would you like to modify? ")
    usershow = Image.open(user_choice + ".jpeg")
    usershow.show()
    user_confirmation = input("Is this the correct image (yes/no): ")
    if user_confirmation == 'yes':
        break

choice = input(" How would you like to modify your image(resize, black and white, rotate, blur) ")


if choice == "rotate":
    image1 = Image.open(user_choice + '.jpeg')
    image1.rotate(90).save('rotate/'+ user_choice+'rotate.jpeg')
    image2 = Image.open('rotate/'+ user_choice+'rotate.jpeg')
    image2.show()
    

if choice == "black and white":
    image1 = Image.open(user_choice + '.jpeg')
    image1.convert(mode='L').save('black and white/' + user_choice + 'black and white.jpeg')
    image2 = Image.open('black and white/' + user_choice + 'black and white.jpeg')
    image2.show()

if choice == "blur":
    image1 = Image.open(user_choice + '.jpeg')
    image1.filter(ImageFilter.GaussianBlur(5)).save('blur/' + user_choice + 'blur.jpeg')
    image2 = Image.open('blur/' + user_choice + 'blur.jpeg')
    image2.show()


if choice == "resize":
    image1 = Image.open(user_choice + ".jpeg")
    print(image1.size)

    x = int(input("Enter a new size 1: "))
    y = int(input("Enter a new size 2: "))
    new_size = image1.resize((x,y))
    new_size.show()

    if x and y == 300:
        new_size.save("300/" + user_choice + '.jpeg')
        
    elif x and y == 450:
        new_size.save("450/" + user_choice + '.jpeg')
        
    elif x and y == 600:
        new_size.save("600/" + user_choice + '.jpeg')
        
    else:
        new_size.save("other_size/" + user_choice + '.jpeg')
