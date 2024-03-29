from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

# Mock data storage (replace this with a database in a real application)
customers = []
accounts = []

def encrypt(data):
    # Implement your encryption logic here
    return data

def decrypt(data):
    # Implement your decryption logic here
    return data

def add_customer(name, address, phone, email, password):
    new_customer = {
        'name': name,
        'address': address,
        'phone': phone,
        'email': email,
        'password': encrypt(password)
    }
    customers.append(new_customer)
    return len(customers)

def execute_c_program(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_customer', methods=['POST'])
def add_customer_route():
    data = request.form
    customer_id = add_customer(data['customerName'], data['address'], data['phone'], data['email'], data['password'])

    # Print the contents of the 'customers' list for debugging
    print("Customers:", customers)

    # Execute the C program logic here if needed
    c_program_command = 'chmod +x ./bank.exe'  # Replace with the actual command to execute your C program
    c_program_stdout, c_program_stderr = execute_c_program(c_program_command)

    message = "Record added successfully"
    
    # Redirect to the '/success' page
    return redirect(url_for('success_page', message=message, customerID=customer_id, c_program_stdout=c_program_stdout, c_program_stderr=c_program_stderr))

@app.route('/success')
def success_page():
    return render_template('success.html', message=request.args.get('message'), customerID=request.args.get('customerID'), c_program_stdout=request.args.get('c_program_stdout'), c_program_stderr=request.args.get('c_program_stderr'))

if __name__ == '__main__':
    app.run(debug=True)
