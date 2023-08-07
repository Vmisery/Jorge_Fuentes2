
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const campos = {
	nombres: false,
	ap: false,
	am: false,
	direccion: false,
    rut: false,
    email: false,
    phone: false
};

const expresiones = {
	nombres: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	email: /^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$/,
	phone: /^\+?\d{0,3}\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$/, 
    rut: /^(\d{1,3}(\.?\d{3})*)\-?([\dkK])$/,
    direccion: /^[a-zA-ZÁÉÍÓÚáéíóúñÑ-ÿ]+\s\d+$/
};

const validarCampo = (expresion, input, campo) => {
	const grupoCampo = document.getElementById(`grupo__${campo}`);
	if(grupoCampo){
		if(expresion.test(input.value)){
			grupoCampo.classList.remove('formulario__grupo-incorrecto');
			grupoCampo.classList.add('formulario__grupo-correcto');
			document.querySelector(`#grupo__${campo} i`).classList.add('fa-circle-check');
			document.querySelector(`#grupo__${campo} i`).classList.remove('fa-circle-xmark');
			document.querySelector(`#grupo__${campo} .formulario__input-error`)?.classList.remove('formulario__input-error-activo');
			campos[campo] = true;
		} else {
			grupoCampo.classList.add('formulario__grupo-incorrecto');
			grupoCampo.classList.remove('formulario__grupo-correcto');
			document.querySelector(`#grupo__${campo} i`).classList.add('fa-circle-xmark');
			document.querySelector(`#grupo__${campo} i`).classList.remove('fa-circle-check');
			document.querySelector(`#grupo__${campo} .formulario__input-error`)?.classList.add('formulario__input-error-activo');
			campos[campo] = false;
		}
	}
};


const validarFormulario = (e) =>{
    switch (e.target.name) {
        case "nombres": 
            validarCampo(expresiones.nombres, e.target, 'nombres')
        break;

        case "apellidopaterno": 
            validarCampo(expresiones.nombres, e.target, 'ap')
        break;

        case "apellidomaterno": 
            validarCampo(expresiones.nombres, e.target, 'am')
        break;

        case "direccion": 
            validarCampo(expresiones.direccion, e.target, 'direccion')
        break;

        case "rut": 
            validarCampo(expresiones.rut, e.target, 'rut')
        break;

        case "email": 
            validarCampo(expresiones.email, e.target, 'email')
        break;

        case "phone": 
            validarCampo(expresiones.phone, e.target, 'phone')
        break;
    }
};


inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
    }
);

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    if(campos.nombres && campos.ap && campos.am && campos.rut && campos.direccion && campos.email && campos.phone){
        formulario.reset();
        Object.entries(campos).forEach(([key, val]) => {
            campos[key] = false;
        });
        document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);
        terminos.checked = false;
        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        });
    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
    }});
    