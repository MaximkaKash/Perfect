const sam=document.getElementById('sam');
const dos=document.getElementById('dos');
const adres=document.getElementById('adres');

sam.onclick=()=>{
    adres.style.display="none";

    sam.style.background="#F9F5FF";
   

    dos.style.background="#170631";
   
}


dos.onclick=()=>{
    adres.style.display="block";

    sam.style.backgroundColor="#F9F5FF";
    

    dos.style.backgroundColor="#170631";
    
}