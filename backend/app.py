# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template
import os

app = Flask(__name__)

# Define the path to the templates directory
template_dir = os.path.abspath('C:\Jeeva\DevOps Assignment\templates')
app.template_folder = template_dir

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




# from flask import Flask, render_template

# # Create a Flask application instance
# app = Flask(__name__)

# # Define a route to render the index.html template
# @app.route('/')
# def index():
#     # Render the index.html template located in the 'templates' directory
#     return render_template('index.html')

# # Run the Flask application
# if __name__ == '__main__':
#     # Run the Flask application on host '0.0.0.0' and port 5000
#     app.run(debug=True, host='0.0.0.0', port=5000)

