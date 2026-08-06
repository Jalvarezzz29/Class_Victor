// --- BASE DE DATOS LOCAL MEMORY ---
let tablaUsuariosMemory = [
    { id: 1, nombre: "Admin Corporativo", email: "admin@myd.com", password_hash: "admin123", plan: "Premium", rol: "admin", estado_cuenta: "Activo" },
    { id: 2, nombre: "Samuel Mira", email: "samuel@myd.com", password_hash: "password123", plan: "Básico", rol: "user", estado_cuenta: "Activo" }
];

let listaTareasMemory = [];
let listaFinanzasMemory = [];
let sesionUsuario = null;

// --- INICIALIZACIÓN DE LA APLICACIÓN ---
document.addEventListener("DOMContentLoaded", () => {
    actualizarSelectUsuarios();
    
    // Bindear Eventos de Formularios
    document.getElementById("formLogin").addEventListener("submit", ejecutarLogin);
    document.getElementById("formRegistro").addEventListener("submit", ejecutarRegistro);
    document.getElementById("formTarea").addEventListener("submit", guardarTarea);
    document.getElementById("formFinanzas").addEventListener("submit", guardarFinanza);
    document.getElementById("formCambioPassword").addEventListener("submit", cambiarPasswordPerfil);
});

// --- FUNCIÓN GLOBAL: VER / OCULTAR CONTRASEÑA ---
function toggleVisibilidadPassword(inputId, boton) {
    const input = document.getElementById(inputId);
    if (input.type === "password") {
        input.type = "text";
        boton.innerText = "🙈";
        boton.classList.add("text-blue-400");
    } else {
        input.type = "password";
        boton.innerText = "👁️";
        boton.classList.remove("text-blue-400");
    }
}

// --- PROCESO: LOGIN CON CONTROL ESTRICTO DE ERRORES ---
function ejecutarLogin(e) {
    e.preventDefault();
    const id = parseInt(document.getElementById("loginSelect").value);
    const inputPass = document.getElementById("loginPassword").value;
    const usuarioEncontrado = tablaUsuariosMemory.find(u => u.id === id);

    // CONTROL DE ERROR DE CLAVE
    if (!usuarioEncontrado || usuarioEncontrado.password_hash !== inputPass) {
        pushNotificacion("❌", "Acceso Denegado", "La contraseña es incorrecta. Inténtalo de nuevo.", "error");
        
        // UX Mobile: Limpiar campo erróneo y forzar enfoque para reescritura inmediata
        const campoPassword = document.getElementById("loginPassword");
        campoPassword.value = "";
        campoPassword.focus();
        return;
    }

    // Ingreso correcto
    sesionUsuario = usuarioEncontrado;
    document.getElementById("authGate").classList.add("hidden");
    document.getElementById("appLayout").classList.remove("hidden");
    document.getElementById("loginPassword").value = ""; 
    
    document.getElementById("badgeUserRol").innerText = `${sesionUsuario.nombre} | ${sesionUsuario.plan}`;
    pushNotificacion("🔓", "Autenticado", `Bienvenido de nuevo a tu Suite.`, "success");
    
    actualizarMetricsDashboard();
    renderizarTareas();
}

// --- REGISTRO DE NUEVOS USUARIOS ---
function ejecutarRegistro(e) {
    e.preventDefault();
    const nombre = document.getElementById("regNombre").value;
    const email = document.getElementById("regEmail").value;
    const pass = document.getElementById("regPassword").value;
    const plan = document.getElementById("regPlan").value;

    const nuevoUsuario = {
        id: Date.now(),
        nombre,
        email,
        password_hash: pass,
        plan,
        rol: "user",
        estado_cuenta: "Activo"
    };

    tablaUsuariosMemory.push(nuevoUsuario);
    pushNotificacion("✨", "Cuenta Creada", "Tu cuenta se ha guardado localmente.", "success");
    actualizarSelectUsuarios();
    conmutarAuth(false);
    
    document.getElementById("regNombre").value = "";
    document.getElementById("regEmail").value = "";
    document.getElementById("regPassword").value = "";
}

// --- CAMBIAR MÓDULOS DE FORMA NATIVA (NAVEGACIÓN) ---
function cambiarModulo(moduloId) {
    document.querySelectorAll(".modulo-page").forEach(p => p.classList.add("hidden"));
    document.getElementById(moduloId).classList.remove("hidden");
    
    // Cambiar estados visuales de los botones en la Tab Bar
    document.querySelectorAll(".btn-nav").forEach(b => {
        b.classList.remove("text-blue-500");
        b.classList.add("text-slate-400");
    });
    event.currentTarget.classList.remove("text-slate-400");
    event.currentTarget.classList.add("text-blue-500");
}

// --- MÓDULO: CONTROL DE TAREAS ---
function guardarTarea(e) {
    e.preventDefault();
    const desc = document.getElementById("taskInput").value;
    const fecha = document.getElementById("taskDate").value;

    listaTareasMemory.push({ id: Date.now(), userId: sesionUsuario.id, desc, fecha, completada: false });
    document.getElementById("taskInput").value = "";
    
    pushNotificacion("📋", "Tarea Agregada", "Actividad guardada en tu cronograma.", "success");
    renderizarTareas();
    actualizarMetricsDashboard();
}

function renderizarTareas() {
    const caja = document.getElementById("listaTareas");
    caja.innerHTML = "";
    const misTareas = listaTareasMemory.filter(t => t.userId === sesionUsuario.id);

    if(misTareas.length === 0) {
        caja.innerHTML = `<p class="text-xs text-slate-500 p-4 text-center">No hay tareas programadas para hoy.</p>`;
        return;
    }

    misTareas.forEach(t => {
        const item = document.createElement("div");
        item.className = "flex justify-between items-center p-3 text-xs";
        item.innerHTML = `
            <div class="flex items-center space-x-2">
                <input type="checkbox" ${t.completada ? 'checked' : ''} onclick="alternarTarea(${t.id})" class="rounded bg-slate-900 border-slate-700 text-blue-500 h-4 w-4">
                <span class="${t.completada ? 'line-through text-slate-500' : 'text-white'}">${t.desc} (${t.fecha})</span>
            </div>
            <button onclick="eliminarTarea(${t.id})" class="text-rose-400 font-bold active:scale-95 px-2">✕</button>
        `;
        caja.appendChild(item);
    });
}

function alternarTarea(id) {
    const t = listaTareasMemory.find(x => x.id === id);
    if(t) t.completada = !t.completada;
    renderizarTareas();
    actualizarMetricsDashboard();
}

function eliminarTarea(id) {
    listaTareasMemory = listaTareasMemory.filter(x => x.id !== id);
    renderizarTareas();
    actualizarMetricsDashboard();
}

// --- MÓDULO: FINANZAS ---
function guardarFinanza(e) {
    e.preventDefault();
    const tipo = document.getElementById("finTipo").value;
    const monto = parseFloat(document.getElementById("finMonto").value);
    const concepto = document.getElementById("finConcepto").value;

    listaFinanzasMemory.push({ id: Date.now(), userId: sesionUsuario.id, tipo, monto, concepto });
    
    document.getElementById("finMonto").value = "";
    document.getElementById("finConcepto").value = "";
    
    pushNotificacion("💰", "Movimiento Registrado", "Balance general sincronizado.", "success");
    actualizarMetricsDashboard();
}

// --- CAMBIO DE CONTRASEÑA ---
function cambiarPasswordPerfil(e) {
    e.preventDefault();
    const actual = document.getElementById("pwdActual").value;
    const nueva = document.getElementById("pwdNueva").value;

    if (sesionUsuario.password_hash !== actual) {
        pushNotificacion("⚠️", "Error de Validación", "La clave actual no coincide.", "error");
        return;
    }

    sesionUsuario.password_hash = nueva;
    pushNotificacion("🔐", "Seguridad Actualizada", "Nueva credencial guardada con éxito.", "success");
    document.getElementById("pwdActual").value = "";
    document.getElementById("pwdNueva").value = "";
}

// --- ENGINE RECOLECTOR DE MÉTRICAS (DASHBOARD REACTIVO) ---
function actualizarMetricsDashboard() {
    const misTareas = listaTareasMemory.filter(t => t.userId === sesionUsuario.id);
    const misFinanzas = listaFinanzasMemory.filter(f => f.userId === sesionUsuario.id);

    // Calcular Productividad
    const completadas = misTareas.filter(t => t.completada).length;
    const ratioProd = misTareas.length > 0 ? Math.round((completadas / misTareas.length) * 100) : 0;
    
    document.getElementById("dashProdTxt").innerText = `${ratioProd}%`;
    document.getElementById("dashProdBar").style.width = `${ratioProd}%`;

    // Calcular Flujo de Dinero
    let balance = 0;
    misFinanzas.forEach(f => {
        if(f.tipo === "Ingreso") balance += f.monto;
        else balance -= f.monto;
    });

    document.getElementById("dashFinTxt").innerText = `COP $${balance.toLocaleString('es-CO')}`;
    document.getElementById("dashFinBar").style.width = balance > 0 ? "100%" : "30%";
    document.getElementById("dashFinBar").className = balance >= 0 ? "bg-emerald-500 h-full transition-all" : "bg-rose-500 h-full transition-all";
}

// --- UTILIDADES DE INTERFAZ MÓVIL ---
function actualizarSelectUsuarios() {
    const select = document.getElementById("loginSelect");
    select.innerHTML = "";
    tablaUsuariosMemory.forEach(u => {
        const opt = document.createElement("option");
        opt.value = u.id;
        opt.innerText = `${u.nombre} (${u.email})`;
        select.appendChild(opt);
    });
}

function conmutarAuth(mostrarRegistro) {
    if(mostrarRegistro) {
        document.getElementById("formLogin").classList.add("hidden");
        document.getElementById("formRegistro").classList.remove("hidden");
        document.getElementById("authTitle").innerText = "Unirse a MYD";
    } else {
        document.getElementById("formLogin").classList.remove("hidden");
        document.getElementById("formRegistro").classList.add("hidden");
        document.getElementById("authTitle").innerText = "Ingresar a MYD";
    }
}

function pushNotificacion(icono, titulo, desc, tipo) {
    const caja = document.getElementById("contenedorNotificaciones");
    const toast = document.createElement("div");
    
    const colorBg = tipo === "error" ? "bg-rose-950/95 border-rose-500/40" : "bg-slate-900/95 border-blue-500/40";
    
    toast.className = `p-3.5 rounded-xl border ${colorBg} flex items-start space-x-3 shadow-xl backdrop-blur-md transition-all duration-300 transform translate-y-2 opacity-0`;
    toast.innerHTML = `
        <div class="text-lg">${icono}</div>
        <div class="flex-1">
            <h4 class="text-xs font-black text-white leading-tight">${titulo}</h4>
            <p class="text-[10px] text-slate-300 mt-0.5 leading-snug">${desc}</p>
        </div>
    `;
    
    caja.appendChild(toast);
    setTimeout(() => { toast.classList.remove("translate-y-2", "opacity-0"); }, 50);
    setTimeout(() => {
        toast.classList.add("opacity-0", "translate-y-[-10px]");
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

function logout() {
    sesionUsuario = null;
    document.getElementById("appLayout").classList.add("hidden");
    document.getElementById("authGate").classList.remove("hidden");
}