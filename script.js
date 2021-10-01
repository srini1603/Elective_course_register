var dis = new Array;
var mincout = 16;

var  t1_course= new Array;
var  t2_course= new Array;
var  t3_course= new Array;
var  t4_course= new Array;

function disable(ck)
{
var term1 = document.getElementsByClassName('term1');
var term2 = document.getElementsByClassName('term2');
var term3 = document.getElementsByClassName('term3');
var term4 = document.getElementsByClassName('term4');
var ckid = document.getElementById(ck.id);
var ckname =document.getElementsByName(ck.name)
var limit =5;

var bol = dis.includes(ckname)

if(ckid.checked) {  
  
  for(var i=0; i < term1.length; i++){
    
  var total =0;
  for (var i = 0; i < term1.length; i++) {
        total += (term1[i].checked) ? 1 : 0;
        

    }
    if (total > limit) {
      console.log("You can select maximum of " + limit + " checkbox.");
      alert("You can select maximum of " + limit + " courses");
      ckid.checked = false;
      return false;
  }
 }
}

if(ckid.checked) {  
  for(var i=0; i < term2.length; i++){

  var total =0;
  for (var i = 0; i < term2.length; i++) {
        total += (term2[i].checked) ? 1 : 0;

    }
    if (total > limit) {
      console.log("You can select maximum of " + limit + " checkbox.");
      alert("You can select maximum of " + limit + " courses");
      ckid.checked = false;
      return false;
  }
 }
}

if(ckid.checked) {  
  for(var i=0; i < term3.length; i++){

  var total =0;
  for (var i = 0; i < term3.length; i++) {
        total += (term3[i].checked) ? 1 : 0;

    }
    if (total > limit) {
      console.log("You can select maximum of " + limit + " checkbox.");
      alert("You can select maximum of " + limit + " courses");
      ckid.checked = false;
      return false;
  }
 }
}

if(ckid.checked) {  
  for(var i=0; i < term4.length; i++){

  var total =0;
  for (var i = 0; i < term4.length; i++) {
        total += (term4[i].checked) ? 1 : 0;

    }
    if (total > limit) {
      console.log("You can select maximum of " + limit + " checkbox.");
      alert("You can select maximum of " + limit + " courses");
      ckid.checked = false;
      return false;
  }
 }
}

  for(var i=0; i < 1; i++)
  {

    if(bol){
      if(ckid.checked==true){
        alert('selected');
        ckid.checked=false;
        return false;
        }
      else{
        dis =dis.filter(e=> e !== ckname);
        }}
       else{

      if(ckid.checked==true){
        dis.push(ckname);
    }
      else{
        dis =dis.filter(e=> e !== ckname);
    }}

  }

console.log(dis);




}

 
  
var str = '';
var  results=new Array;

function getValue() {


  

  var checkboxes = document.querySelectorAll('input[type=checkbox]:checked');

  for (var i = 0; i < checkboxes.length; i++) {
    results.push(checkboxes[i].value);
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
document.getElementById("course6").innerHTML = page2array[5];
document.getElementById("course7").innerHTML = page2array[6];
document.getElementById("course8").innerHTML = page2array[7];
document.getElementById("course9").innerHTML = page2array[8];
document.getElementById("course10").innerHTML = page2array[9];
document.getElementById("course11").innerHTML = page2array[10];
document.getElementById("course12").innerHTML = page2array[11];
console.log(results);
        }