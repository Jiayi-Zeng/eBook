// Generative the TOC
document.addEventListener('DOMContentLoaded', function () {
    var contentToc = document.getElementById('navbar-example3');
    var headings = document.querySelectorAll('.body h2, .body h3');

    // 遍历所有标题元素
    headings.forEach(function (heading) {
        // 获取标题文本
        var titleText = heading.textContent;

        // 创建标题的锚点ID，使用标题文本，去除空格并转为小写
        var titleId = titleText.trim().replace(/ /g, '_').toLowerCase();

        // 设置标题的锚点ID
        heading.id = titleId;

        // 创建内部链接
        // var link = document.createElement('h2');
        // link.href = '#' + titleId;
        // link.textContent = titleText;

        // // 替换标题元素为带有链接的元素
        // heading.parentNode.replaceChild(link, heading);
    });


    headings.forEach(function (heading) {
        // Create a container <nav> element
        var navContainer = document.createElement('nav');
        navContainer.classList.add('nav', 'nav-pills', 'flex-column');

        // Create the TOC item <a> element
        var link = document.createElement('a');
        link.classList.add('nav-link');
        link.textContent = heading.textContent;
        link.href = '#' + heading.id;

        // Append the TOC item to the container
        navContainer.appendChild(link);

        // Determine the indentation level based on the heading's tag (h2 or h3)
        var indentationLevel = heading.tagName === 'H2' ? 0 : 1;
        navContainer.style.marginLeft = indentationLevel * 20 + 'px';

        // Append the container to the TOC
        contentToc.appendChild(navContainer);


    });
});
