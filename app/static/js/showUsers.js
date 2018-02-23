$(function(){
	$('#btnShowUsers1').click(function(){
		
		$.ajax({
			url: '/ShowUsers',
			data: $('form').serialize(),
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
