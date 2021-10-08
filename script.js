var dis = new Array;
var mincout = 16;
var studentname="ss";
var idno = 77;


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
var lenpage2 = page2array.length;
var  coursearray =["course1","course2","course3","course4","course5","course6","course7","course8","course9","course10","course11","course12","course13","course14","course15","course16","course17","course18","course19","course20"];
window.onload=function(){
  for( var i = 0 ; i<= lenpage2; i++){
document.getElementById(coursearray[i]).innerHTML = page2array[i];
  }

console.log(results);
}
var jsresults={};
  jsresults.name=studentname;
  jsresults.id=idno;
  jsresults.course1=page2array[0];
  jsresults.course2=page2array[1];
  jsresults.course3=page2array[2];
  jsresults.course4=page2array[3];
  jsresults.course5=page2array[4];
  jsresults.course6=page2array[5];
  jsresults.course7=page2array[6];
  jsresults.course8=page2array[7];
  jsresults.course9=page2array[8];
  jsresults.course10=page2array[9];
  jsresults.course11=page2array[10];
  jsresults.course12=page2array[11];
  jsresults.course13=page2array[12];
  jsresults.course14=page2array[13];
  jsresults.course15=page2array[14];
  jsresults.course16=page2array[15];
  jsresults.course17=page2array[16];
  jsresults.course18=page2array[17];
  jsresults.course19=page2array[18];
  jsresults.course20=page2array[19];

const tosend=JSON.stringify(jsresults);
const xhr  = new XMLHttpRequest();
  
function submitdata(){
  console.log(jsresults);
console.log(tosend);
let xhr = new XMLHttpRequest();
               let url = "submit.php";
           
               // open a connection
               xhr.open("POST", url, true);
     
               // Set the request header i.e. which type of content you are sending
               xhr.setRequestHeader("Content-Type", "application/json");
     
               // Create a state change callback
               xhr.onreadystatechange = function () {
                   if (xhr.readyState === 4 && xhr.status === 200) {
     
                       // Print received data from server
                       result.innerHTML = this.responseText;
     
                   }
               };
     
               // Converting JSON data to string
               var data = JSON.stringify(jsresults);
     
               // Sending data with the request
               xhr.send(data);
           }



 


