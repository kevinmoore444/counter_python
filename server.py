from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

app.secret_key = "secret"



@app.route('/')          # The "@" decorator associates this route with the function immediately following
def direct_to_homepage():
    # need to check if there is an existing session 
    if "click_count" not in session:
    #if there is not a session, need to start a session
        session['click_count'] = 1
    # if there is a session need to increment one.
    else:
        session['click_count'] = session['click_count'] + 1
    return render_template("root.html")
 



@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

