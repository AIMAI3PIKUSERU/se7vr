function download(href,title){
	const a=$C('a')
	$A(a,'href',href)
	$A(a,'download',title)
	a.click()
	a.remove()
}
function redirect(href){
	const a=$C('a')
	$A(a,'href',href)
	a.click()
	a.remove()
}
function appendItem(){
	let listpath=$('#listpath').innerText.trim()
	let listtype=$('#listtype').innerText.trim().split('\n')
	$('#listname').innerText.trim().split('\n').forEach((el,ind)=>{
		if(!el.includes($('#filter').value)){return}
		let ele=$C('a')
		ele.href='/'+(listpath=='/'?'':listpath+'/')+el
		ele.innerText=el
		if(listtype[ind]=='1'){
			ele.className='list folder'
		}else{
			ele.className='list file'
		}
		//click	->	get-method(preview/download)
		ele.addEventListener('click',(e)=>{
			e.preventDefault()
			let ele2=$('*[name="method"].ckd')
			if($A(ele2,'value')=='preview'){
				redirect(e.srcElement.href)
			}else{
				if(e.srcElement.className.includes('folder')){
					redirect(e.srcElement.href)
					return
				}
				download(e.srcElement.href,e.srcElement.innerText)
			}
		})
		$('#body').appendChild(ele)
	})
}
window.addEventListener('load',()=>{
	appendItem(listpath,listtype)
	if(Cookies.get('align')=='right'){
		$('#body').className='align_right'
	}else if(Cookies.get('align')=='center'){
		$('#body').className='align_center'
	}else{
		$('#body').className=''
	}
	$('.buttonbox>input').addEventListener('keyup',()=>{
		$('#body').innerHTML=''
		appendItem()
	})
})