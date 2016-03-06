$(document).ready(function(){
    var counter;
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function vote(photoID){
$.ajax({
	type:"POST",
	url:"/vote/",
	data:{"photo":photoID},
	success: function(result){
	$("#photo-vote-" + photoID).hide();
        $("#like-span-" + photoID).hide();
        $("#pin-span-" + photoID).after('<div style="color:white!important;position:relative;top:-30px;z-index:9;height:0!important;left:76%;font-weight:500;"><span></span></div>');
        $("#pin-span-" + photoID + "+" + "div").attr('id', "like-span-" + photoID);
         $("#like-span-" + photoID + ">" + "span").attr('id', "likespan-" + photoID);
        $("#likespan-" + photoID).text(result + " " + "likes");	
    },
	headers:{
	'X-CSRFToken' :csrftoken
	}
});
return false;

}
$(document).on('click',"button.vote",function(){

var photoID=parseInt(this.id.split("-")[2]);
console.log(photoID);

return vote(photoID);

})
                 

function addcomment(photoID,text){
$.ajax({
	type:"POST",
	url:"/addcomment/",
	data:{"photo":photoID,"text":text},
	success: function(){
   
	$("#commentphoto-ul-"+photoID).append('<li class="child"><a href="users/'+ userid + '">' + user + '</a>:</li>');
     //   counter=Math.round(Math.random() * 323234 + 5)
    //$("#like-p-" + photoID + ">" + "p").attr('id', "commentp" + counter);
        
   $("#commentphoto-ul-"+photoID + " " + "li").last().append(text);      
	},
	headers:{
	'X-CSRFToken' :csrftoken
	}
});
return false;

}
$(document).on('click',"a.addcomment",function(){
var photoID=parseInt(this.id.split("-")[2]);
console.log(photoID);
photomy=photoID+"";
    var text=$("#photocommentinput-"+photomy).val();
    console.log(text);
return addcomment(photoID,text);

})




function pin(photoID){
$.ajax({
	type:"POST",
	url:"/pin_photo/",
	data:{"photo":photoID},
	success: function(result){
	$("#photo-pin-" + photoID).hide();
        $("#pin-span-" + photoID).hide();
        $("#like-span-" + photoID).after('<div style="color:white!important;position:relative;top:-30px;z-index:9;height:0!important;left:7%; font-weight:500;"><span></span></div>');
        $("#like-span-" + photoID + "+" + "div").attr('id', "pinspan" + photoID);
        $("#pinspan" + photoID).text(result + " " + "pools");        
	
    },
	headers:{
	'X-CSRFToken' :csrftoken
	}
});
return false;

}
$(document).on('click',"button.pin",function(){

var photoID=parseInt(this.id.split("-")[2]);
console.log(photoID);

return pin(photoID);

})


});






