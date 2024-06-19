
document.addEventListener('DOMContentLoaded', function(){
	var token=Cookies.get('token');
	if(token){
		//setSession(token);
	}
	$('#loginSubmit').click(()=>{
		const login=$('input[name=login]').val()
		const password=sha256($('input[name=password]').val());
		$.ajax({
			url: "token/",
			method: 'post',
			headers: {
				"Authorization":"Basic "+btoa(login + ":" + password),
				'X-CSRFToken': getCookie('csrftoken')
			},
			data: JSON.stringify({'login':login,'password':password})
		}).then(msg=>{
			msg=JSON.parse(msg)
			if(msg.id){
				Cookies.set('token',msg.token);
				document.location.href='/';
				//Cookies.set('ticket',msg.ticket,{expires: 1825});
				//setSession(msg.token);
			}
		}).fail(msg=>{
			console.log(msg)
			$('#loginError').removeClass('st-hidden')
		})
		return false;
	})
})