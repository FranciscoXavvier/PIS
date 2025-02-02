function descargarInforme() {
  // Obtén los datos del informe de Power BI (puedes obtenerlos de una URL, una API, etc.)
  const informeData = obtenerInformeData();

  // Crea un objeto Blob a partir de los datos del informe
  const informeBlob = new Blob([informeData], { type: 'application/octet-stream' });

  // Utiliza FileSaver.js para descargar el informe como un archivo
  saveAs(informeBlob, 'informe_powerbi.pdf');
}
