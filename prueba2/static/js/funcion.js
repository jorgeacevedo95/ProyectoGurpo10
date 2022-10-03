function validar_login(){
    let usuario= document.formLogin.usuario;
    let password=document.formLogin.password;

 
    let longitudPassword=password.value.length;

    if (longitudPassword==0 || longitudPassword<8) {
        alert("Ingrese una contraseña valida");
        password.focus();
        return false;   
    } 
}
function deslizar(){
    const contenidoDatosGestion=document.querySelector("#contenidoDatosGestion");
    contenidoDatosGestion.classList.add("deslizar");    
}
setTimeout(deslizar,1000);

function deslizarRegistro(){
    const contenidoDatosRegistro=document.querySelector("#contenidoDatosRegistro");
    const contenidoDatosGestion=document.querySelector("#contenidoDatosGestion");
    contenidoDatosRegistro.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");
    contenidoDatosGestion.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");

    contenidoDatosGestion.classList.toggle("deslizarizquierda");    
    contenidoDatosRegistro.classList.toggle("deslizar");
}

function deslizarGestionar(){
    const contenidoDatosRegistro=document.querySelector("#contenidoDatosRegistro");
    const contenidoDatosGestion=document.querySelector("#contenidoDatosGestion");
    contenidoDatosRegistro.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");
    contenidoDatosGestion.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");

    contenidoDatosGestion.classList.toggle("deslizar");    
    contenidoDatosRegistro.classList.toggle("deslizarDerecha");
}

function deslizarSA(){
    const contenidoDatosGestionSA=document.querySelector("#contenidoDatosGestionSA");
    contenidoDatosGestionSA.classList.add("deslizar");    
}
setTimeout(deslizarSA,1000);

function deslizarRegistroSA(){
    const contenidoDatosRegistroSA=document.querySelector("#contenidoDatosRegistroSA");
    const contenidoDatosGestionSA=document.querySelector("#contenidoDatosGestionSA");
    const contenidoDatosEliminarSA=document.querySelector("#contenidoDatosEliminarSA");
    contenidoDatosRegistroSA.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");
    contenidoDatosGestionSA.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");
    contenidoDatosEliminarSA.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");

    contenidoDatosGestionSA.classList.toggle("deslizarizquierda");    
    contenidoDatosRegistroSA.classList.toggle("deslizar");
    contenidoDatosEliminarSA.classList.toggle("deslizarDerecha");
}

function deslizarEliminarSA(){
    const contenidoDatosRegistroSA=document.querySelector("#contenidoDatosRegistroSA");
    const contenidoDatosGestionSA=document.querySelector("#contenidoDatosGestionSA");
    const contenidoDatosEliminarSA=document.querySelector("#contenidoDatosEliminarSA");
    contenidoDatosRegistroSA.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");
    contenidoDatosGestionSA.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");
    contenidoDatosEliminarSA.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");

    contenidoDatosEliminarSA.classList.toggle("deslizar");    
    contenidoDatosRegistroSA.classList.toggle("deslizarizquierda");
    contenidoDatosGestionSA.classList.toggle("deslizarizquierda");
}

function deslizarGestionarSA(){
    const contenidoDatosRegistroSA=document.querySelector("#contenidoDatosRegistroSA");
    const contenidoDatosGestionSA=document.querySelector("#contenidoDatosGestionSA");
    const contenidoDatosEliminarSA=document.querySelector("#contenidoDatosEliminarSA");
    contenidoDatosRegistroSA.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");
    contenidoDatosGestionSA.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");
    contenidoDatosEliminarSA.classList.remove("deslizar","deslizarizquierda", "deslizarDerecha");

    contenidoDatosGestionSA.classList.toggle("deslizar");    
    contenidoDatosRegistroSA.classList.toggle("deslizarDerecha");
    contenidoDatosEliminarSA.classList.toggle("deslizarDerecha");
}

