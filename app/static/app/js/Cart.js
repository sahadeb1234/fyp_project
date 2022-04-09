$(document).ready(function(){

    $(document).on('click',".add-wishlist",function(){
		var _pid=$(this).attr('data-product');
		console.log( _pid);
		var _vm=$(this);
		// Ajax
		$.ajax({
			url:"/add-wishlist",
			data:{
				product:_pid
			},
			dataType:'json',
			success:function(res){
				if(res.bool==true){
					_vm.addClass('disabled').removeClass('add-wishlist');
				}
			}
		});
		// EndAjax
	});
	// End

});



