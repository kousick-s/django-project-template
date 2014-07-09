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
                var url="/tasks/" + result
                location.href = url
              }
         });
         return false; //<---- move it here
    });

});

$(document).ready(function() {
    $("#addtask").submit(function(event){
    	tUid=$('#uid').val()
    	tTitle=$('#taskname').val()
    	tDesc=$('#taskdesc').val()
    	tStatus=$('#taskstatus').val()
    	tAccess=$('#taskaccess').val()
         $.ajax({
              type:"POST",
              contentType:"application/json",
              url:"/tasks/create/" + tUid,
              data: JSON.stringify({
                     "tTitle": tTitle, // from form
                     "tDesc": tDesc,
                     "tStatus":tStatus,
                     "tAccess":tAccess}),
              success: function(){
                var url="/tasks/" + tUid 
                location.href = url
              }
         });
         return false; //<---- move it here
    });

});
