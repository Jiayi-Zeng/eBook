// Generative the TOC
document.addEventListener('DOMContentLoaded', function () {
    var contentToc = document.getElementById('navbar-example3');
    var headings = document.querySelectorAll('.body h2, .body h3');

    headings.forEach(function (heading) {
        // Create a container <nav> element
        var navContainer = document.createElement('nav');
        navContainer.classList.add('nav', 'nav-pills', 'flex-column');

        // Create the TOC item <a> element
        var link = document.createElement('a');
        link.classList.add('nav-link');
        link.textContent = heading.textContent;
        link.href = '#' + heading.dataset.blockKey;

        // Append the TOC item to the container
        navContainer.appendChild(link);

        // Determine the indentation level based on the heading's tag (h2 or h3)
        var indentationLevel = heading.tagName === 'H2' ? 0 : 1;
        navContainer.style.marginLeft = indentationLevel * 20 + 'px';

        // Append the container to the TOC
        contentToc.appendChild(navContainer);

        
    });
});
