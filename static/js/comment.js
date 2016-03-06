$(document).ready(function(){
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

function deletephoto(photoID){
$.ajax({
	type:"POST",
	url:"/deletephoto/",
	data:{"photo":photoID},
	success: function(){
	$("#photo-delete-" + photoID).hide();
	$("#photo-" + photoID).hide();
	},
	headers:{
	'X-CSRFToken' :csrftoken
	}
});
return false;

}
$(".delphoto").click(function(){

var photoID=parseInt(this.id.split("-")[2]);
console.log(photoID);

return deletephoto(photoID);

})
});