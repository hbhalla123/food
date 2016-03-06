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

function pin(photoID){
$.ajax({
	type:"POST",
	url:"/vote/",
	data:{"photo":photoID},
	success: function(result){
	$("#photo-vote-" + photoID).hide();
        $("#like-span-" + photoID).hide();
        $("#like-p-" + photoID).prepend('<span></span>');
        $("#like-p-" + photoID + ">" + "span").attr('id', "likespan" + photoID);
        $("#likespan" + photoID).text(result);
        
        
        
	
    },
	headers:{
	'X-CSRFToken' :csrftoken
	}
});
return false;

}
$("a.pin").click(function(){

var photoID=parseInt(this.id.split("-")[2]);
console.log(photoID);

return pin(photoID);

})


});






