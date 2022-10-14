import time
import tkinter as tk
import turtle
t = turtle.Turtle()

def set_color(word):
    brands_dict = ['gucci',
                'jordans',
                'nike',
                'birkin',
                'rolex', 
                'rollie',
                'louis',
                'vuitton',
                'goyard',
                'saint',
                'laurent',
                'dolce',
                'celine',
                'canada goose',
                'moncler',
                'bottega',
                'burberry',
                'loewe', 
                'dior', 
                'cartier', 
                'chanel', 
                'louboutin', 
                'prada', 
                'fendi', 
                'balenciaga', 
                'tiffany', 
                'versace', 
                'hermes',
                'yeezy',
                'pumas'
                ]
    
    articles_dict = ['t-shirt',
                    'towel',
                    'bra',
                    'bras',
                    'shirt',
                    'shirts',
                    'short',
                    'shorts',
                    'boot',
                    'dashiki',
                    'robe',
                    'pj',
                    'belt',
                    'bottoms',
                    'lingerie',
                    'buckles',
                    'pendant',
                    'bandana',
                    'bandanas',
                    'shoe',
                    'shoes',
                    'glove',
                    'gloves',
                    'underwear',
                    'pouches',
                    'jeans',
                    'sweater',
                    'helmet',
                    'collar',
                    'daisy dukes',
                    'bikini',
                    'black dress',
                    'red dress',
                    'dress',
                    'shades',
                    'sunglasses',
                    'sneakers',
                    'boots',
                    'bags',
                    'hat',
                    'caps',
                    'jacket',
                    'cardigan',
                    'suit',
                    'tie',
                    'pajama',
                    'pajamas',
                    'trousers',
                    'coat',
                    'overalls',
                    'skirt'
    ]

    textiles_dict = ['denim',
                    'silk',
                    'wool',
                    'cotton',
                    'velvet',
                    'chiffon',
                    'satin',
                    'velour',
                    'moleskin',
                    'flannel',
                    'corduroy',
                    'fleece',
                    'lace',
                    'mink',
                    'fur',
                    'sequin',
                    'jean'
    ]

    if word in brands_dict:
        return '#FB0000'
    elif word in articles_dict:
        return '#FFB800'
    elif word in textiles_dict:
        return '#00FFB3'
    else:
        return '#8E8D8D'

# opening the text file
with open('input3.txt','r') as file:
    # Initial starting position
    turtle.Screen().bgcolor("black")
    t.penup()
    x_pos = -600
    t.setx(x_pos)
    y_pos = 300
    t.sety(y_pos)
    margin = 5
    t.speed(50)
    for line in file:
        for word in line.split():
            width = (len(word))*10
            t.pendown()
            t.fillcolor(set_color(word))
            t.begin_fill()
            t.forward(width)
            t.right(90)
            t.forward(20)
            t.right(90)
            t.forward(width)
            t.right(90)
            t.forward(20)
            t.right(90)
            t.end_fill()
            t.penup()
            x_pos += width + margin

            # Start new line
            if (x_pos >= 750):
                x_pos=-600
                y_pos -= 30 
            t.setx(x_pos)
            t.sety(y_pos)
            print(t.xcor())

    time.sleep(10)
    ts = t.getscreen()
    ts.getcanvas().postscript(file="duck.eps")
