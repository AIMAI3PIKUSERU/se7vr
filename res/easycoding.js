const log=console.log
function $(arg,arg2) {
	let els = document.querySelectorAll(arg)
	
	if (arg2) {
		return els
	}else if (els.length == 1) return els[0]
	else if(els.length==0) return undefined
	return els
}

function $A(ele, arg1, arg2) {
	if (arg2 == undefined) {
		return ele.getAttribute(arg1)
	} else {
		ele.setAttribute(arg1, arg2)
	}
}

function $C(arg) {
	return document.createElement(arg)
}