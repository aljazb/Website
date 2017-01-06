document.addEventListener('DOMContentLoaded', main, false);

function main() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
            document.getElementById("left_camera_section").innerHTML += '<video id="viewfinder" width="640" height="480" autoplay></video>';
            document.getElementById("left_camera_section").innerHTML += '<a id="snap_photo">Snap Photo</a>';
            document.getElementById("camera_section").innerHTML += '<canvas id="camera_canvas" width="640" height="480"></canvas>';
        
            var video = document.getElementById('viewfinder');
            var canvas = document.getElementById('camera_canvas');
            var context = canvas.getContext('2d');
            var video = document.getElementById('viewfinder');
                
            video.src = window.URL.createObjectURL(stream);
            video.play();
            
            document.getElementById("snap_photo").addEventListener("click", function() {
            	context.drawImage(video, 0, 0, 640, 480);
            });
        });
    }
    
    
}