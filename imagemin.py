from PIL import Image, ImageFilter
import os

image8 = Image.open('mike.jpeg')
image8.rotate(90).show('mike.jpeg')

image9 = Image.open('aaron.jpeg')
image9.rotate(90).show("aaron.jepg")

image10 = Image.open('hasbulla.jpeg')
image10.rotate(180).show('hasbulla.jpeg')

image11 = Image.open('lps.jpeg')
image11.rotate(90).show('lps.jpeg')

image12 = Image.open('chica.jpeg')
image12.filter(Imagefilter.GaussianBlur(15)).show('chica.jpeg')

image13 = Image.open('rock.jpeg')
image13 .show('rock.jpeg')

image14 = Image.open('tayloranded.jpeg')
image14 .show('tayloranded.jpeg')

image15 = Image.open('sal.jpeg')
image15 .show('sal.jpeg')

image16 = Image.open('icarly.jpeg')
image16 .show('icarly.jpeg')

image17 = Image.open('stormi.jpeg')
image17 .show('stormi.jpeg')

size_300 = (300,300)
size_700 = (700,700)

