from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

    my_html =  '''
    
    <body style="font-size:10vw">
    
    
        <h1 style="color:  #002aff;">Hello World</h1>
    
    </body>
    
    ''' 
    return my_html
