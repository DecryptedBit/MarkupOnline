// var url = "/static/sample.pdf";

// var loadingTask = pdfjsLib.getDocument(url);
// loadingTask.promise.then(function(pdf) {
//     //
//     // Fetch the first page
//     //
//     pdf.getPage(1).then(function(page) {
//     var scale = 1.5;
//     var viewport = page.getViewport({ scale: scale, });
    
//     //
//     // Prepare canvas using PDF page dimensions
//     //
//     var canvas = document.getElementById('pdf-canvas');
//     var context = canvas.getContext('2d');
//     canvas.height = canvas.parentElement.clientHeight;
//     canvas.width = viewport.width;

//     //
//     // Render PDF page into canvas context
//     //
//     var renderContext = {
//         canvasContext: context,
//         viewport: viewport,
//     };
//     page.render(renderContext);
//     });
// });

"use strict";

if (!pdfjsLib.getDocument || !pdfjsViewer.PDFViewer) {
  alert("Please build the pdfjs-dist library using\n  `gulp dist-install`");
}

// The workerSrc property shall be specified.
//
pdfjsLib.GlobalWorkerOptions.workerSrc = "/static/node_modules/pdfjs-dist/build/pdf.worker.js";

// Some PDFs need external cmaps.
//
var CMAP_URL = "/static/node_modules/pdfjs-dist/cmaps/";
var CMAP_PACKED = true;

// var DEFAULT_URL = "/static/sample.pdf";
var DEFAULT_URL = "/static/sample.pdf";
var SEARCH_FOR = ""; // try 'Mozilla';

var container = document.getElementById("viewerContainer");

// (Optionally) enable hyperlinks within PDF files.
var pdfLinkService = new pdfjsViewer.PDFLinkService();

// (Optionally) enable find controller.
var pdfFindController = new pdfjsViewer.PDFFindController({
    linkService: pdfLinkService,
});

var pdfViewer = new pdfjsViewer.PDFViewer({
    container: container,
    linkService: pdfLinkService,
    findController: pdfFindController,
});
pdfLinkService.setViewer(pdfViewer);

document.addEventListener("pagesinit", function() {
    // We can use pdfViewer now, e.g. let's change default scale.
    pdfViewer.currentScaleValue = "page-width";

    // We can try searching for things.
    if (SEARCH_FOR) {
        pdfFindController.executeCommand("find", { query: SEARCH_FOR });
    }
});

// Loading document.
var loadingTask = pdfjsLib.getDocument({
    url: DEFAULT_URL,
    cMapUrl: CMAP_URL,
    cMapPacked: CMAP_PACKED,
});
loadingTask.promise.then(function(pdfDocument) {
    // Document loaded, specifying document for the viewer and
    // the (optional) linkService.
    pdfViewer.setDocument(pdfDocument);

    pdfLinkService.setDocument(pdfDocument, null);
});

