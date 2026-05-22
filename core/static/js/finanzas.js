function toggleMiembro() {
    const tipo = document.getElementById('tipo-select').value;
    const miembroGroup = document.getElementById('miembro-group');
    const miembroSelect = document.getElementById('miembro-select');
    const descripcionField = document.getElementById('descripcion-field');

    if (tipo === 'diezmo') {
        miembroGroup.style.display = 'block';
        miembroSelect.required = true;
    } else {
        miembroGroup.style.display = 'none';
        miembroSelect.required = false;
        miembroSelect.value = '';
    }

    if (tipo === 'gasto') {
        descripcionField.style.border = '2px solid #e74c3c';
        descripcionField.placeholder = 'Describe en qué se realizó el gasto *';
        descripcionField.required = true;
    } else {
        descripcionField.style.border = '';
        descripcionField.placeholder = '';
        descripcionField.required = false;
    }
}