
function disable(ckType){
    var ckName = document.getElementsByName(ckType.name);
    var checked = document.getElementById(ckType.id);

    if (checked.checked) {
      for(var i=0; i < ckName.length; i++){

          if(!ckName[i].checked){
              ckName[i].disabled = true;
          }else{
              ckName[i].disabled = false;
          }
      } 
    }
    else {
      for(var i=0; i < ckName.length; i++){
        ckName[i].disabled = false;
      } 
    }    
}

var str = '';
var  results=new Array;

function getValue() {
  var checks = document.getElementsByClassName('checks');
  

  for ( i = 0; i < checks.length; i++) {
      if ( checks[i].checked === true ) {
          str += checks[i].value + "  ";
          results.push(checks[i].value);
      }
      
  }
  
  console.log(results);
  
  sessionStorage.setItem('thearray',JSON.stringify(results));
  window.loaction.href="preview.html";
  
  
  
}
var sessionstring = sessionStorage.getItem('thearray');
var page2array=JSON.parse(sessionstring);
console.log(page2array);
window.onload=function(){
document.getElementById("course1").innerHTML = page2array[0];
document.getElementById("course2").innerHTML = page2array[1];
document.getElementById("course3").innerHTML = page2array[2];
document.getElementById("course4").innerHTML = page2array[3];
document.getElementById("course5").innerHTML = page2array[4];
        }