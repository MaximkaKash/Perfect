
 const big_box=document.getElementById("big_box")
 const autorization=document.getElementById("autorization")

 
 const button=document.getElementById("button")
 const back=document.getElementById("back")
 
 button.onclick=()=>{
     
big_box.style.display="none";
autorization.style.display="block";

 }

 back.onclick=()=>{
    
big_box.style.display="block";
autorization.style.display="none";

}


 

