from market import app

# we can import app because it recognizes it from __init__ file

# this checks if run.py file is executed directly, not imported
if __name__ == '__main__':
    app.run(debug=True)
