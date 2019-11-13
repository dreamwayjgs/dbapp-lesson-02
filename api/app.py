from flask import Flask, render_template, request
from apicall import hosp_list, pharm_list

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def index():            
    return render_template("index.html")


@app.route('/hosp')
def hosp():
    lat = request.args.get('lat', 33.450701)
    lng = request.args.get('lng', 126.570667)
    print(type(lat))
    host_list(lat, lng)
    return render_template("index.html")


if __name__ == ("__main__"):
    app.run(debug=True)