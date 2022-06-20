const orders=document.getElementsByClassName('order');

const phones=document.getElementsByClassName('phone');
const input_phone=document.getElementById('input_phone');

const codes=document.getElementsByClassName('code');
const input_number=document.getElementById('input_number');

const names=document.getElementsByClassName('name');
const input_name=document.getElementById('input_name');



function renderList(){
	for(var i=0;i<orders.length;i++){
       
        if( phones[i].textContent.includes(input_phone.value) && codes[i].textContent.includes(input_number.value) && names[i].textContent.includes(input_name.value)) {

            orders[i].style.display="block";
        }
        else{
            orders[i].style.display="none";
                
                

        }
        

    }
}


input_phone.addEventListener('input',e=>renderList());
input_number.addEventListener('input',e=>renderList());
input_name.addEventListener('input',e=>renderList());





