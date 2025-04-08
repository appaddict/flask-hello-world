from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

    my_html =  '''
    
    <body style="font-size: 20em;">
        <h1 style="color:  #0000ff;">Hello World</h1>
        <p>This is a message from Ku, hahaha</p>
    </body>
    
    ''' 
    return my_html
