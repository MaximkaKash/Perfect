const min_header = document.getElementById('min_menu')
const burger = document.getElementById('burger')

const header_club = document.getElementById('header_club')
const menu_item = document.getElementById('menu_item')



function club_start() {
   

    burger.onclick=()=>{
        if(min_header.style.display=="none"){
            min_header.style.display="block";
    
        }
        else{
            min_header.style.display="none";
    
        }
    }

    header_club.onmouseover=()=>{
        
        menu_item.style.display="block";
        
    }

    header_club.onmouseout=()=>{
        
        menu_item.style.display="none";
        
    }

    menu_item.onmouseover=()=>{
        
        menu_item.style.display="block";
        
    }

    menu_item.onmouseout=()=>{
        
        menu_item.style.display="none";
        
    }
   
}





/*----------------------------------------------------------------------------------------------*/

club_start();


const find = document.getElementById('find')
const find_goods = document.getElementById('find_goods')
const not_find = document.getElementById('not_find')
const find_good=document.getElementsByClassName('find_good');



document.addEventListener( 'click', (e) => {
	const withinBoundaries = e.composedPath().includes(find_goods);
 
	if ( ! withinBoundaries ) {
		find_goods.style.display = 'none'; 
	}
})

let counter;
function renderList(){
    if (find.value===""){
        find_goods.style.display="none";
    }
    else{
        find_goods.style.display="block";
        counter=0
        for(var i=0;i<find_good.length;i++){
            if( find_good[i].textContent.includes(find.value) ) {
                counter++;
                find_good[i].style.display="block";
                find_goods.style.display="block";
            }
            else{
                find_good[i].style.display="none";
                    
                    
    
            }
        }
        if(counter===0){
            not_find.style.display="block"
        }
        else{
            not_find.style.display="none"
        }
    
    }
    
   
}


find.addEventListener('input',e=>renderList());


const photo_animate = document.getElementsByClassName('photo_animate')

  counter=0; 
    function anim(){
        
        
        for(var i=0;i<photo_animate.length;i++){
        photo_animate[i].style.display="none";
        }
        photo_animate[counter].style.display="block";
        
        counter++;
        if (counter==photo_animate.length){
            counter=0;
        }
        
        
        setTimeout(function(){anim();},5000);
        
    }

anim()




