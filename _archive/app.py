from flask import Flask, render_template
import tablib
import os
 
app = Flask (__name__)
dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'draft_proj_new_083023/OVR/2023_projections_20230830-193027.csv')) as f:
    dataset.csv = f.read()
 
@app.route("/")
def index():    
    return dataset.html    
 
if __name__ == "__main__":
    app.run(port=8080)