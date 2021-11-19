var dis = new Array;
var mincout = 16;
var studentname="D";
var idno = 3;
var maxcount =18;
var minicount = 16;


someJavaScriptVarTabAll = '{{indicourse}}';
console.log(someJavaScriptVarTabAll);



function disable(ck)
{
var term1 = document.getElementsByClassName('term1');
var term2 = document.getElementsByClassName('term2');
var term3 = document.getElementsByClassName('term3');
var term4 = document.getElementsByClassName('term4');
var ckid = document.getElementById(ck.id);
var ckname =document.getElementsByName(ck.name)
var term1limit =5;
var term2limit =5;
var term3limit =5;
var term4limit =5;

var bol = dis.includes(ckname)

if(ckid.checked) {  
  
  for(var i=0; i < term1.length; i++){
    
  var total =0;
  for (var i = 0; i < term1.length; i++) {
        total += (term1[i].checked) ? 1 : 0;
        

    }
    if (total > term1limit) {
      alert("max count reached");
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
    if (total > term2limit) {
      alert("max count reached");
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
    if (total > term3limit) {
      alert("max count reached");
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
    if (total > term4limit) {
      alert("max count reached");
      ckid.checked = false;
      return false;
  }
 }
}

  for(var i=0; i < 1; i++)
  {

    if(bol){
      if(ckid.checked==true){
        alert('This course is already selected');
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
var dislength=dis.length;
console.log(dislength);


}



  
var str = '';
var  results=new Array;


function getValue() {


  

  var checkboxes = document.querySelectorAll('input[type=checkbox]:checked');

  for (var i = 0; i < checkboxes.length; i++) {
    results.push(checkboxes[i].value);
  }
  console.log("results")
  console.log(results);
  
  sessionStorage.setItem('thearray',JSON.stringify(results));
  window.loaction.href="/preview";
  
  
  
}
var sessionstring = sessionStorage.getItem('thearray');
var page2array=JSON.parse(sessionstring);



console.log("page2")
console.log(page2array);
var lenpage2 = page2array.length;
var  coursearray =["course1","course2","course3","course4","course5","course6","course7","course8","course9","course10","course11","course12","course13","course14","course15","course16","course17","course18","course19","course20"];
window.onload=function(){
  for( var i = 0 ; i<= lenpage2-1; i++){
document.getElementById(coursearray[i]).innerHTML = page2array[i];
  }

console.log(results);
}
var temp =page2array.toString();
var jsresults={};
  jsresults.course1=page2array;
const tosend=JSON.stringify(jsresults);
const xhr  = new XMLHttpRequest();
var insert=new Array;
  
function submitdata(){
  console.log(temp);
  console.log(jsresults);
  alert("no more changes feasible once submitted");
console.log(tosend);
var b=document.getElementById('submit');
var checkboxes=document.querySelectorAll('input[type="checkbox"]:checked');
         
      
            if(lenpage2>=mincout && lenpage2<=maxcount){ //if 2 checkbox is checked only the submit button is visible

              swal({
                title: "did you selected 8 major courses?",
                        text: " Did you selected a minimum of 8 courses in your major / domain?",
                                  showCancelButton: true,
                                  buttons: ['Cancel!','Confirm!'],
                                  customClass:'swal-wide',
                                }).then(function(isConfirm){
                                                            if(isConfirm){
                                                                            swal({
                                                                                  title: "Are you sure to submit?",
                                                                                  text: "course will be submiited!",
                                                                                  icon: "warning",
                                                                                  buttons: ['Cancel!','Confirm!'],
                                                                                  dangerMode: true,
                                                                              
                                                                                  })
                                                                            .then(function(isConfirm) {
                                                                                                        if (isConfirm) {
                                                                                                                         swal({title: 'Submitted!',text: 'your courses are successfully submitted!',icon: 'success'})
                                                                                                                         .then(function() {
                                                                                                                                            // mention ur download file directory
                                                                                                                                          });
  
                                                               //do not touch this
  
                                b.disabled=false; //  submit button is visible
  
  fetch('/submit', { //fetching the data to  the server
  
    // Specify the method
    method: 'POST',
  
    // JSON
    headers: {
      'Content-Type': 'application/json'
    },
  
    // A JSON payload
    body: tosend
    
  }).then(function (response) { // At this point, Flask has printed our JSON
    return response.text();
  }).then(function (text) {
  
    console.log('POST response: ');
  
    // Should be 'OK' if everything was successful
    }
  );
  console.log("done");
  
  //do not touch this
  // print the course of student
  
  const invoice = this.document.getElementById("invoice");
  console.log(invoice);
  console.log(window);
  var opt = {
  margin: 1,
  filename: 'myselectedcourse.pdf',
  image: { type: 'jpeg', quality: 0.98 },
  html2canvas: { scale: 2 },
  jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
  };
  html2pdf().from(invoice).set(opt).save();
  
                                                                                                                        } 
                                                                                                        else {swal("Cancelled", ":)", "error");}
                                                                                                       });
                                                                                                    
                                                                          }
                                                            
                                                            });

      }

      else if(lenpage2<minicount){b.disabled=true;
        alert("minimum number is not selected");

      }

      else if(lenpage2>maxcount){b.disabled=true;
        alert("max count reached");

      }
      

        else{b.disabled=true;
            alert("invalid");}

}




 


