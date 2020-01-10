
let CM = CodeMirror(document.getElementById('code'), {
    lineNumbers: true,
    theme: "panda-syntax",
    mode: "markdown",
    viewportMargin: 0
});

function updateViewer() {
    const iframe = document.querySelector('.pdf-frame');
    iframe.src = iframe.src + "?_=" + new Date().getTime();
}

function compileMarkdown() {
    md = CM.getValue();
    
    let data = new FormData();
    data.append('json', JSON.stringify({
        markdown: md,
    }));

    fetch('/editor/compile', {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({markdown: md})
    })
    .then(function(res) { return res.json(); })
    .then(function(data) { setTimeout(updateViewer, 1000); })
}