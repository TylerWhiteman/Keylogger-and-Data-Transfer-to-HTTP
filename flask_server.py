from flask import Flask, request, render_template_string


# create Flask variable and empty list for key log data
app = Flask(__name__)
data_storage = []

#creates receive-data route using post method to send in the log data
@app.route('/receive-data', methods=['POST'])

# receive data function, gets recieved data in json format, adds data to data storage list, for log, return successful
def receive_data():
    data = request.json.get('data')
    data_storage.append(data)
    return "Data received", 200

#defult route, shows log title and log information
@app.route('/')
def index():
    return render_template_string('''
        <h1>Logger Data</h1>
        <h1>-------------------------------------- LOG -------------------------------------</h1>                          
        <ul>
        {% for data in data_storage %}
            <li><pre>{{ data }}</pre></li>
        {% endfor %}
        </ul>
    ''', data_storage=data_storage)

# run local server with local ip address on port 5000
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

