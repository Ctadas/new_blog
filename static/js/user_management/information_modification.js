$('.form-group').on('mouseover','.img_upload',function(){
	var offsetParent  = $('.uplaod_show').position()
	var img_parent = $('.uplaod_show').offsetParent()
	var mask_html = '<div class="mask" style="top:'+offsetParent.top+';left:'+offsetParent.left+';"></div>'
	var tip_html = '<p class="img_text">点击上传头像</p>'
	img_parent.append(mask_html)
	img_parent.append(tip_html)
})
.on('mouseout','.img_upload',function(){
	$('.mask').remove()
	$('.img_text').remove()
})
.on('change','.img_upload',function(){
	console.log(window.webkitURL.createObjectURL(this.files[0]),12312)
	var uplaod_img_url = getObjectURL(this.files[0])
	$('.uplaod_show').attr('src',uplaod_img_url)
})

function getObjectURL(file) {
	var url = null ;
	if (window.createObjectURL!=undefined) { // basic
		url = window.createObjectURL(file) ;
	} else if (window.URL!=undefined) { // mozilla(firefox)
		url = window.URL.createObjectURL(file) ;
	} else if (window.webkitURL!=undefined) { // webkit or chrome
		url = window.webkitURL.createObjectURL(file) ;
	}
	return url ;
}
