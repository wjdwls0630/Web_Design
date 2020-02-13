var MaintextLink = {
  setColor: function(color) {
    var aList = document.querySelectorAll('#maintext a');
    for (i in aList) {
      aList[i].style.color = color;
    }
  }
}
var Body = {
  setColor: function(color) {
    document.querySelector('body').style.color = color;
  },
  setBackgroundcolor: function(color) {
    document.querySelector('body').style.backgroundColor = color;
  }
}

function nightDayhandler(self){
  if(self.value=="night"){
    Body.setColor("white")
    Body.setBackgroundcolor("black")
    self.value="day"
    MaintextLink.setColor("powderblue")
  }else{
    Body.setColor("black")
    Body.setBackgroundcolor("white")
    self.value="night"
    MaintextLink.setColor("black")
  }
}
