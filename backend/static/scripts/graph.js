document.addEventListener('DOMContentLoaded', main, false);

function main() {
    var performance = document.getElementById("performance_stars").children.length;
    var build = document.getElementById("build_stars").children.length;
    var camera = document.getElementById("camera_stars").children.length;
    var price = document.getElementById("price_stars").children.length;
    
    var minY = 15;
    var maxY = 119;
    var maxX = 255;
    var minX = 45;
    var centX = 150;
    var centY = 67;
    var stepX = (maxX - centX) / 5.0;
    var stepY = (maxY - centY) / 5.0;
    
    var graphCanvas = document.getElementById("graph_canvas");
    var ctx = graphCanvas.getContext("2d");
    ctx.strokeStyle = '#373D3F';
    ctx.font = " bold 10px Helvetica";
    ctx.fillText("Performance",120,10);
    ctx.fillText("Built quality",130,134);
    ctx.fillText("Camera",0,70);
    ctx.fillText("Price",260,70);
    ctx.lineWidth = 2;
    ctx.moveTo(150,12);
    ctx.lineTo(150,124);
    ctx.moveTo(40,67);
    ctx.lineTo(260,67);
    
    ctx.moveTo(centX-camera*stepX, centY);
    ctx.lineTo(centX, centY-performance*stepY);
    ctx.moveTo(centX, centY-performance*stepY);
    ctx.lineTo(centX+price*stepX, centY);
    ctx.moveTo(centX+price*stepX, centY);
    ctx.lineTo(centX, centY+build*stepY);
    ctx.moveTo(centX, centY+build*stepY);
    ctx.lineTo(centX-camera*stepX, centY);
    ctx.stroke();
}