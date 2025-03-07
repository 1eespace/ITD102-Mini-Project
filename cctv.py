from flask import Flask, render_template, Response, url_for, redirect
from PIL import ImageFont, ImageDraw, Image
import datetime
import cv2
import numpy as np

app = Flask(__name__)
# Specify is_capture and is_record, start_record as global variables
global is_capture, is_record, start_record            
# Retrieve the camera image and save it to the capture class
capture = cv2.VideoCapture(-1)  
# Set codecs to store recorded files                     
fourcc = cv2.VideoWriter_fourcc(*'XVID')            
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

font = ImageFont.truetype('fonts/SCDream6.otf', 20)
# Each variable is initially false (do not press the button)
is_record = False
is_capture = False
start_record = False                                    

def gen_frames():  
    global is_record, start_record, is_capture, video 
    # an infinite loop  
    while True:            
        # Current time received                        
        now = datetime.datetime.now()                     
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S') 
        nowDatetime_path = now.strftime('%Y-%m-%d %H_%M_%S')
        # Current video received
        ref, frame = capture.read() 

        # If the video was not well received (ref is false)
        if not ref:                     
            break                       
        else:
            frame = Image.fromarray(frame)    
            draw = ImageDraw.Draw(frame)    
            # xy is where the text starts, text is the string to output, font is the font, and fill is the color of the letter (blue, green, red)  
            draw.text(xy=(10, 15),  text="Smart Home CCTV "+nowDatetime, font=font, fill=(255, 255, 255))
            frame = np.array(frame)
            ref, buffer = cv2.imencode('.jpg', frame) 
            # Copy the current screen to frame1           
            frame1 = frame              
            frame = buffer.tobytes()
            # If you are not currently in the recording state and start_record is true (press the recording button)
            if start_record == True and is_record == False: 
                # Make it recorded 
                is_record = True            
                start_record = False        
                video = cv2.VideoWriter("record " + nowDatetime_path + ".avi", fourcc, 15, (frame1.shape[1], frame1.shape[0]))
            # If you press the recording button again while you're recording
            elif start_record and is_record == True:
                is_record = False       
                start_record = False
                video.release()         
            # If you press the capture button
            elif is_capture:       
                is_capture = False
                cv2.imwrite("capture " + nowDatetime_path + ".png", frame1)  
            # If it's currently recorded
            if is_record == True:                 
                # Save the current frame to a video
                video.write(frame1)
            # Pile up the picture files and wait for the call
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  

@app.route('/')
def index():
    global is_record
    # Show web pages in format
    return render_template('index.html', is_record=is_record)             

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/push_record')
def push_record():                   
    global start_record                 
    start_record = not start_record     
    return redirect(url_for('index'))

# Runs when the capture button is pressed
@app.route('/push_capture')
def push_capture(): 
    # Calling is_capture as a global variable                       
    global is_capture  
    # Makes is_capture true                 
    is_capture = True                   
    return redirect(url_for('index'))

# The portion to host a website and show it to an accessor
if __name__ == "__main__":  
    # Host is currently the internal IP of Raspberry Pi, and port is set arbitrarily
    app.run(host="0.0.0.0", port = "5000")
    
    


