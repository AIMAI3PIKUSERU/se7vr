window.onload=()=>{
	let defaultMap={
		short:'a',
		align:'left',
		dark:'on',
		method:'preview',
	}
	Object.keys(defaultMap).forEach((el)=>{
		if(!Cookies.get(el)){
			Cookies.set(el,defaultMap[el],{'max-age':'60000'})
		}
		let ele=$('*[name="'+el+'"][value="'+Cookies.get(el)+'"]')
		if(ele){
			ele.classList.add('ckd')
		}
	})
	$('.radiobox',1).forEach((ele)=>{

		ele.querySelectorAll('span').forEach((ele2)=>{
			ele2.addEventListener('click',(e)=>{
				if(ele2!=e.srcElement){return}
				ele.querySelectorAll('span').forEach((ele3)=>{
					ele3.classList.remove('ckd')
				})
				ele2.classList.add('ckd')
				Cookies.set($A(ele2,'name'),$A(ele2,'value'),{'max-age':'60000'});
			})
		})
	})
}