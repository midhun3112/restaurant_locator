
function addRestaurantClick(isLoggedIn) {
	if(isLoggedIn){
		location.href='/restaurant/add'
	}else{
	location.href='/authentication/login'
	}
}

function loginClick() {
	alert("cc")
    location.href='/authentication/login'
}