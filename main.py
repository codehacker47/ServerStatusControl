from flask import Flask, render_template, redirect, url_for, flash
import psutil
import subprocess

app = Flask(__name__)
app.secret_key = '12345' # Change this 

def get_disk_usage():
    usage = psutil.disk_usage('your_path') # Change this to your disk path. It could even be a RAID path like /dev/md0
    return usage

def restart_samba():
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', 'smbd'], check=True)
        return "Restarted Samba"
    except subprocess.CalledProcessError as e:
        return f"Error in the restart of Samba! {e}"

def get_sensors_info():
    try:
        result = subprocess.run(['sensors'], capture_output=True, text=True, check=True)
        output = result.stdout
        
        # Filter the output 
        disk_temperature = None
        for line in output.splitlines():
            if 'Sensor 1' in line:
                parts = line.split(':')
                if len(parts) > 1:
                    temp_value = parts[1].strip().split()[0]  # Get ONLY the temperature
                    disk_temperature = temp_value
        
        return disk_temperature
    except subprocess.CalledProcessError as e:
        return f"Error retrieving the temperatures! {e}"

@app.route('/')
def home():
    usage = get_disk_usage()
    return render_template('index.html', usage=usage)

@app.route('/restart_samba', methods=['POST'])
def restart():
    message = restart_samba()
    flash(message)
    return redirect(url_for('home'))

@app.route('/sensors', methods=['POST'])
def sensor_flash():
    disk_temp = get_sensors_info()
    if disk_temp:
        flash(f"Temperature of the disk: {disk_temp}")
    else:
        flash("Disk sensor not found or error in the process!")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
