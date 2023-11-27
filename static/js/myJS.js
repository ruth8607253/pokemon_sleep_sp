$(function(){
	var ulul=$("#PIC ul")
	var	lili = ulul.append( ulul.html() ).children()
	var TT;
	
	$("#ICON li").eq(0).addClass("CC")

	function GOGO(){
		var NOW = ulul.position().left / -800;
		NOW+=1
		
		ulul.animate({left: NOW * -800}, 600, function(){ if(NOW == lili.length/2){ulul.css("left",0)}  })
		
		if(NOW==10){
			$("#ICON li").eq(0).addClass("CC").siblings().removeClass();
		}else{
			$("#ICON li").eq(NOW).addClass("CC").siblings().removeClass();
		}	
 	
		TT = setTimeout(GOGO,3000);
	}

	GOGO();  //啟動計時器ion

//===========================================================
	
	$("#PIC").hover(function(){ 
		clearTimeout(TT);
	},function(){
		TT = setTimeout(GOGO, 3000);
	});
	
//===========================================================
	
	$("#ICON li").click(function(){
		
		
		NOW = $(this).index()

		
		ulul.animate({left: NOW * -800}, 600, function(){ if(NOW == lili.length/2){ulul.css("left",0)}  })
		
	if(NOW==10){
		$("#ICON li").eq(0).addClass("CC").siblings().removeClass();
	}else{
		$("#ICON li").eq(NOW).addClass("CC").siblings().removeClass();
	}	
	
		
	})

	
});

