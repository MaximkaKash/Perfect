

const photo2=document.getElementById('photo2');
const other_filters=document.getElementById('other_filters');


var i=0;
var j="";



photo2.onclick=()=>{
    if ( i == 0){
        photo2.src = "../photos/arrow2.png";
        i = 1;
        other_filters.style.display="block";
    }
else{
    i=0;
    photo2.src = "../photos/arrow.png";
    other_filters.style.display="none";
}
       
        
}

const active_filter=document.getElementById('active_filter');
const filter_1=document.getElementById('filter_1');
const filter_2=document.getElementById('filter_2');

filter_1.onclick=()=>{

    j=filter_1.textContent;
    filter_1.textContent=active_filter.textContent;
    active_filter.textContent=j;

}

filter_2.onclick=()=>{

    j=filter_2.textContent;
    filter_2.textContent=active_filter.textContent;
    active_filter.textContent=j;

}






