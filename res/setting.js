function darkmodeMatch(){
	if(Cookies.get('dark')=='off'){
		$('html').className='light'
	}else if (Cookies.get('dark')=='auto') {
		if(!matchMedia('(prefers-color-scheme: dark)').matches){
			$('html').className='light'	
		}else{
			$('html').className=''	
		}
	}else{
		$('html').className=''
	}
}
function addMediaListener(){
	let media = window.matchMedia('(prefers-color-scheme: dark)');
	let callback = () => {
		darkmodeMatch()
	};
	if (typeof media.addEventListener === 'function') {
		media.addEventListener('change', callback);
	} else if (typeof media.addListener === 'function') {
		media.addListener(callback);
	}
}

window.onload=()=>{
	addMediaListener()
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
		$('*[name="'+el+'"][value="'+Cookies.get(el)+'"]').classList.add('ckd')
	})
	darkmodeMatch()
	
	$('.radiobox',1).forEach((ele)=>{
		ele.querySelectorAll('span').forEach((ele2)=>{
			ele2.addEventListener('click',(e)=>{
				if(ele2!=e.srcElement){return}
				ele.querySelectorAll('span').forEach((ele3)=>{
					ele3.classList.remove('ckd')
				})
				ele2.classList.add('ckd')
				Cookies.set($A(ele2,'name'),$A(ele2,'value'),{'max-age':'60000'})
				if($A(ele2,'name')=='dark'){
					darkmodeMatch()
				}
			})
		})
	})
	
}