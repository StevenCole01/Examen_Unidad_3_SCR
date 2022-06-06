var express = require("express");
var app = express();
var server = require("http").Server(app);
var io = require("socket.io")(server);

var joystick = 0;//Coordenada [x,y]
var joystickAnterior = 100;

app.use(express.static("public"));

io.on("connection", function (socket) {
  console.log("Alguien se ha conectado con Sockets");

  socket.on("python", function (data) {
    console.log(data);
    switch (data) {
      case 1://ARRIBA
        joystick = 1;
      break;
      case 2://DERECHA
        joystick = 2;
      break;      
      case 3://ABAJO
        joystick = 3;
      break;
      case 4://IZQUIERDA
        joystick = 4;
      break;
      case 5://Boton
        joystick = 5;
      break;
      default://Default
      break;
    } 
    if(joystickAnterior != joystick)
    {
      io.sockets.emit("joystick", joystick);
      joystickAnterior = joystick;
    }   
       
  });
  
});

server.listen(5000, function () {
  console.log("Servidor corriendo en http://localhost:5000");
});