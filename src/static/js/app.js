//(function (){
//   "use strict";
//   
//   // This function exists only for purpose of
//   // JS Hint Validation Demo. Will raise multiple
//   // errors on running 'bin/fab lint_js'. 
//
//   x = 100;
// 
//    
//})();

function userlogin(){
	var acc = document.getElementById('username').value;
	var pass = document.getElementById('password').value;
	var xmlHttp = null;
	var theUrl="authenticate/" + acc + "/" + pass
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

$(document).ready(function() {
    $("#test").submit(function(event){
    	username=$('#username').val()
    	password=$('#password').val()
         $.ajax({
              type:"POST",
              contentType:"application/json",
              url:"/authenticate",
              data: JSON.stringify({
                     "user_name": username, // from form
                     "passw": password                     }),
              success: function(result){
                if(result=="active")
                	var url="/tasks/" + username
                	location.href = url
              }
         });
         return false; //<---- move it here
    });

});
