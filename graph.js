document.addEventListener('DOMContentLoaded', main, false);

function main() {
    var graphCanvas = document.getElementById("graph_canvas");
    var ctx = graphCanvas.getContext("2d");
    ctx.strokeStyle = '#373D3F';
    ctx.font = " bold 10px Helvetica";
    ctx.fillText("Preformance",120,10);
    ctx.fillText("Built quality",130,140);
    ctx.fillText("Camera",0,70);
    ctx.fillText("Price",270,70);
    ctx.lineWidth = 2;
    ctx.moveTo(150,12);
    ctx.lineTo(150,130);
    ctx.moveTo(40,67);
    ctx.lineTo(270,67);
    
    ctx.moveTo(70,67);
    ctx.lineTo(150,30);
    ctx.moveTo(150,30);
    ctx.lineTo(260,67);
    ctx.moveTo(260,67);
    ctx.lineTo(150,120);
    ctx.moveTo(150,120);
    ctx.lineTo(70,67);
    ctx.stroke();
}