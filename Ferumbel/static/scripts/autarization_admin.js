const check=document.getElementById('check');
const password=document.getElementById('password');

check.onclick=()=>{
if (password.type === "text"){
    password.type = "password";
}

else{
    password.type = "text"
}

}