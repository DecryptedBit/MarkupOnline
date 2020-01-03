var url = "/static/sample.pdf";

var loadingTask = pdfjsLib.getDocument(url);
loadingTask.promise.then(function(pdf) {
    //
    // Fetch the first page
    //
    pdf.getPage(1).then(function(page) {
    var scale = 1.5;
    var viewport = page.getViewport({ scale: scale, });
    
    //
    // Prepare canvas using PDF page dimensions
    //
    var canvas = document.getElementById('pdf-canvas');
    var context = canvas.getContext('2d');
    canvas.height = canvas.parentElement.clientHeight;
    canvas.width = viewport.width;

    //
    // Render PDF page into canvas context
    //
    var renderContext = {
        canvasContext: context,
        viewport: viewport,
    };
    page.render(renderContext);
    });
});